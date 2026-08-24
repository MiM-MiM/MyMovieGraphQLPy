from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

import orjson

from MyMovieGraphQL import GetByID


def _mask_scalar(
    value: Any,
    seen: dict[tuple[str, Any], Any],
    *,
    preserve: bool = False,
) -> Any:
    """Return a deterministic masked value for copy-safe fixture snapshots."""
    if value is None or preserve:
        return value

    key = (type(value).__name__, value)
    if key in seen:
        return seen[key]

    if isinstance(value, bool):
        masked = value
    elif isinstance(value, int):
        masked = int(hashlib.sha256(str(value).encode("utf-8")).hexdigest()[:8], 16)
    elif isinstance(value, float):
        masked = float(int(hashlib.sha256(str(value).encode("utf-8")).hexdigest()[:8], 16))
    elif isinstance(value, str):
        masked = f"MASKED_{hashlib.sha256(value.encode('utf-8')).hexdigest()[:12]}"
    else:
        masked = value

    seen[key] = masked
    return masked


def _mock_graphql_dict(
    value: Any,
    seen: dict[tuple[str, Any], Any] | None = None,
    *,
    preserve: bool = False,
):
    """Recursively replace real GraphQL content with deterministic masked values.

    ``__typename`` values remain unchanged, while repeated scalar values that
    match earlier at the same dict level are re-used so matching real values stay
    consistent in the mock without exposing the original source text.
    """
    if seen is None:
        seen = {}

    if isinstance(value, dict):
        result: dict[str, Any] = {}
        level_seen: dict[tuple[str, Any], Any] = {}
        for key, item in value.items():
            if key == "__typename":
                result[key] = item
                continue

            should_preserve = preserve or key in {
                "id",
                "cursor",
                "startCursor",
                "endCursor",
                "position",
                "total",
                "hasNextPage",
                "hasPreviousPage",
            }
            result[key] = _mock_graphql_dict(item, level_seen, preserve=should_preserve)
            if isinstance(item, (str, int, float, bool)) or item is None:
                level_seen[(type(item).__name__, item)] = _mask_scalar(
                    item,
                    level_seen,
                    preserve=should_preserve,
                )
        return result

    if isinstance(value, list):
        return [_mock_graphql_dict(item, seen, preserve=preserve) for item in value]

    if isinstance(value, (str, int, float, bool)) or value is None:
        return _mask_scalar(value, seen, preserve=preserve)

    return value


def save_fixture(obj, path: Path) -> None:
    path.write_bytes(orjson.dumps(_mock_graphql_dict(obj.to_dict()), option=orjson.OPT_INDENT_2))


def save_mocked_fixture(obj, path: Path) -> None:
    path.write_bytes(orjson.dumps(_mock_graphql_dict(obj.to_dict()), option=orjson.OPT_INDENT_2))


if __name__ == "__main__":
    movie = GetByID.getByID("tt22084616")
    base_path = Path(__file__).with_name("tt22084616.json")
    save_fixture(movie, base_path)

    first_update = movie.update("akas")
    if first_update is None:
        raise RuntimeError("The first 'akas' update returned no data.")

    first_update_path = Path(__file__).with_name("tt22084616_akas.json")
    save_fixture(movie, first_update_path)

    first_update_raw_path = Path(__file__).with_name("tt22084616_akas_raw.json")
    save_mocked_fixture(first_update, first_update_raw_path)

    second_update = movie.update("akas")
    if second_update is None:
        raise RuntimeError("The second 'akas' update returned no data.")

    second_update_path = Path(__file__).with_name("tt22084616_akas_page2.json")
    save_fixture(movie, second_update_path)

    second_update_raw_path = Path(__file__).with_name("tt22084616_akas_page2_raw.json")
    save_mocked_fixture(second_update, second_update_raw_path)

    print(f"Saved base fixture to {base_path}")
    print(f"Saved first full-object fixture to {first_update_path}")
    print(f"Saved first raw update fixture to {first_update_raw_path}")
    print(f"Saved second full-object fixture to {second_update_path}")
    print(f"Saved second raw update fixture to {second_update_raw_path}")
