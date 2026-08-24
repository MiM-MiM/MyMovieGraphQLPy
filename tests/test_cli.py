from __future__ import annotations

import ast
import io
import json
import logging
import runpy
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

CLI_PATH = Path(__file__).resolve().parents[1] / "MyMovieGraphQL" / "__main__.py"


class FakeStdin:
    def __init__(self, payload: str):
        self.buffer = io.BytesIO(payload.encode("utf-8"))


class DummyResult:
    def __init__(self, payload):
        self.payload = payload

    def to_dict(self):
        return self.payload


def run_cli(argv, stdin_payload: str | None = None, *, patch_search=None):
    old_argv = sys.argv[:]
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.argv = argv
    stdout = io.StringIO()
    stderr = io.StringIO()
    sys.stdout = stdout
    sys.stderr = stderr
    if stdin_payload is not None:
        sys.stdin = FakeStdin(stdin_payload)
    else:
        sys.stdin = old_stdin

    patched = {}
    try:
        if patch_search is not None:
            patched["search"] = patch("MyMovieGraphQL.Search.search", return_value=patch_search)
            patched["search"].start()
        try:
            result = runpy.run_path(str(CLI_PATH), run_name="__main__")
        except SystemExit as exc:
            result = exc.code
        return result, stdout.getvalue(), stderr.getvalue()
    finally:
        for patcher in patched.values():
            patcher.stop()
        sys.argv = old_argv
        sys.stdin = old_stdin
        sys.stdout = old_stdout
        sys.stderr = old_stderr


def test_cli_help_and_invalid_selection():
    exit_code, output, _ = run_cli(["prog"])
    assert exit_code == 0
    assert "MyMovieGraphQL" in output
    assert "help" in output.lower()

    with pytest.raises(ValueError, match="Invalid selection"):
        run_cli(["prog", "unknown-command"])


def test_cli_valid_search_arguments_and_output():
    result = DummyResult({"__typename": "Title", "id": "tt0000001", "titleText": "Example"})
    _, output, _ = run_cli(
        ["prog", "search", "Example", "limit=2", "year=2024", "includeAdult=false"],
        patch_search=result,
    )

    assert '"id": "tt0000001"' in output
    assert "Example" in output

    cli_tree = ast.parse(CLI_PATH.read_text(encoding="utf-8"))
    search_fn = next(node for node in cli_tree.body if isinstance(node, ast.FunctionDef) and node.name == "search")
    assert search_fn.returns is not None
    assert ast.unparse(search_fn.returns) == "MyMovie"


def test_cli_name_and_title_variants_parse_expected_arguments():
    result = DummyResult({"__typename": "Title", "id": "tt0000001", "titleText": "Example"})
    for argv in (
        ["prog", "namesearch", "Example Name", "limit=5"],
        ["prog", "titlesearch", "Example Title", "limit=7"],
    ):
        with (
            patch("MyMovieGraphQL.Search.searchName", return_value=result),
            patch("MyMovieGraphQL.Search.searchTitle", return_value=result),
        ):
            run_cli(argv)

    cli_tree = ast.parse(CLI_PATH.read_text(encoding="utf-8"))
    name_fn = next(node for node in cli_tree.body if isinstance(node, ast.FunctionDef) and node.name == "nameSearch")
    title_fn = next(node for node in cli_tree.body if isinstance(node, ast.FunctionDef) and node.name == "titleSearch")
    # fmt: off
    assert (ast.unparse(name_fn.returns) == "MyMovie")  # pyright: ignore[reportArgumentType]
    assert (ast.unparse(title_fn.returns) == "MyMovie")  # pyright: ignore[reportArgumentType]
    # fmt: on


def test_cli_get_by_id_valid_and_invalid_arguments():
    result = DummyResult({"__typename": "Title", "id": "tt0000001", "titleText": "Example"})

    with patch("MyMovieGraphQL.GetByID.getByID", return_value=result):
        _, output, _ = run_cli(["prog", "getbyid", "tt0000001"])
    assert '"id": "tt0000001"' in output

    with pytest.raises(RuntimeError, match="requires exactly one additional argument"):
        run_cli(["prog", "getbyid"])

    with patch(
        "MyMovieGraphQL.GetByID.getByID",
        side_effect=ValueError("Unknown ID format: bad"),
    ):
        with pytest.raises(ValueError, match="Unknown ID format"):
            run_cli(["prog", "getbyid", "bad"])


def test_cli_applies_env_log_level_to_handler(monkeypatch):
    import MyMovieGraphQL.logger as pkg_logger

    old_level = pkg_logger.logger.level
    old_handler_level = pkg_logger.logger_sh.level
    monkeypatch.setenv("MYMOVIEGRAPHQL_LOGLEVEL", "DEBUG")
    # The env setting happens upon import, need to manually update it.
    import os

    pkg_logger.set_log_level(os.environ.get("MYMOVIEGRAPHQL_LOGLEVEL", "INFO"))
    try:
        run_cli(["prog", "help"])
        assert pkg_logger.logger.level == logging.DEBUG
        assert pkg_logger.logger_sh.level == logging.DEBUG
    finally:
        # Set them individuall in case they were different.
        pkg_logger.logger.setLevel(old_level)
        pkg_logger.logger_sh.setLevel(old_handler_level)


def test_cli_update_valid_and_invalid_arguments():
    payload = {"__typename": "Title", "id": "tt0000001", "titleText": "Example"}
    _, output, _ = run_cli(["prog", "update", "akas"], json.dumps(payload))
    assert '"titleText": "Example"' in output

    with pytest.raises(RuntimeError, match="requires at least one additional argument"):
        run_cli(["prog", "update"])

    with pytest.raises(ValueError, match="does not contain a type and id"):
        run_cli(["prog", "update", "akas"], "{}")


def test_cli_type_contract_and_expected_io_shape():
    cli_tree = ast.parse(CLI_PATH.read_text(encoding="utf-8"))
    defs = {node.name: node for node in cli_tree.body if isinstance(node, ast.FunctionDef)}

    for name in ["getByID", "search", "nameSearch", "titleSearch", "update"]:
        assert defs[name].returns is not None
        # fmt: off
        assert (ast.unparse(defs[name].returns) == "MyMovie")  # pyright: ignore[reportArgumentType]
        # fmt: on

    get_args_fn = defs["get_args"]
    # fmt: off
    assert (ast.unparse(get_args_fn.args.args[0].annotation) == "FunctionType")  # pyright: ignore[reportArgumentType]
    # fmt: on
