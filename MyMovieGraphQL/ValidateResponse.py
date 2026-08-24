"""Standalone response validation helpers for MyMovieGraphQL payloads.

These helpers intentionally validate the raw GraphQL payload before it is
flattened into a ``MyMovie`` object. This preserves the original GraphQL field
prefixes (for example ``Title_id`` or ``Title_titleText``) and fails early when
an unexpected response shape arrives.
"""

from __future__ import annotations

from typing import Any

from beartype import beartype

from MyMovieGraphQL.logger import logger


class ResponseValidationError(ValueError):
    """Raised when a GraphQL response payload is malformed."""


@beartype
def validate_graphql_response(payload: dict[str, Any], *, expect_query: bool = True) -> dict[str, Any]:
    """Validate a GraphQL response payload at the call boundary.

    Args:
        payload: The raw JSON-decoded response object from requests.
        expect_query: Whether to require a top-level ``data.query`` shape.

    Returns:
        The validated ``payload["data"]["query"]`` dict when it is shape-correct.

    Raises:
        ResponseValidationError: If the payload is missing keys or has the wrong type.
    """
    data = payload.get("data")
    if not isinstance(data, dict):
        logger.debug(
            "GraphQL payload missing 'data' object; keys=%s",
            sorted(payload.keys()),
        )
        raise ResponseValidationError("GraphQL response missing 'data' object")

    if expect_query:
        query_data = data.get("query")
        if not isinstance(query_data, dict):
            logger.debug(
                "GraphQL payload missing 'data.query' object; data_keys=%s",
                sorted(data.keys()),
            )
            raise ResponseValidationError("GraphQL response missing 'data.query' object")
        logger.debug("Validated GraphQL payload with keys: %s", sorted(query_data.keys()))
        return query_data

    logger.debug("Validated GraphQL data object with keys: %s", sorted(data.keys()))
    return data


@beartype
def validate_my_movie_object(obj: dict[str, Any], *, field_name: str = "payload") -> dict[str, Any]:
    """Validate a MyMovie-compatible object before wrapping it."""
    logger.debug("Validating MyMovie-like object for %s", field_name)
    if not obj:
        logger.debug("MyMovie-like object for %s is empty", field_name)
        raise ResponseValidationError(f"{field_name} cannot be empty")
    if not isinstance(obj.get("__typename"), str):
        logger.debug(
            "MyMovie-like object for %s missing __typename; keys=%s",
            field_name,
            sorted(obj.keys()),
        )
        raise ResponseValidationError(f"{field_name} missing string '__typename' field")
    logger.debug(
        "Validated MyMovie-like object for %s: %s",
        field_name,
        obj.get("__typename"),
    )
    return obj


@beartype
def validate_connection_payload(obj: dict[str, Any], *, field_name: str = "connection") -> dict[str, Any]:
    """Validate that a connection-like payload has the common fields used by merge logic."""
    logger.debug("Validating connection payload for %s", field_name)
    validated = validate_my_movie_object(obj, field_name=field_name)
    if "edges" in validated:
        edges = validated["edges"]
        if not isinstance(edges, list):
            logger.debug(
                "Connection payload for %s has non-list edges; keys=%s",
                field_name,
                sorted(validated.keys()),
            )
            raise ResponseValidationError(f"{field_name} has 'edges' but it is not a list")
        for index, edge in enumerate(edges):
            if not isinstance(edge, dict):
                logger.debug(
                    "Connection payload for %s edge %s is not an object; type=%s",
                    field_name,
                    index,
                    type(edge).__name__,
                )
                raise ResponseValidationError(f"{field_name} edge at index {index} is not an object")
            node = edge.get("node")
            if node is not None and not isinstance(node, dict):
                logger.debug(
                    "Connection payload for %s edge %s node is not an object; type=%s",
                    field_name,
                    index,
                    type(node).__name__,
                )
                raise ResponseValidationError(f"{field_name} edge node at index {index} is not an object")
    logger.debug("Connection payload for %s validated successfully", field_name)
    return validated


@beartype
def validate_response_and_wrap(payload: dict[str, Any]) -> dict[str, Any]:
    """Validate the raw GraphQL response and then the wrapped object shape."""
    logger.debug(
        "Validating response and wrap path for payload with keys: %s",
        sorted(payload.keys()),
    )
    query_data = validate_graphql_response(payload)
    result = validate_my_movie_object(query_data, field_name="data.query")
    logger.debug(
        "Response and wrap validation succeeded for type: %s",
        result.get("__typename"),
    )
    return result
