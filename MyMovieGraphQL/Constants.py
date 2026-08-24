import os

from orjson import OPT_INDENT_2

COUNTRY = os.environ.get("MYMOVIEGRAPHQL_COUNTRY", "US")
LANGUAGE = os.environ.get("MYMOVIEGRAPHQL_LANGUAGE", "en")
INDENT = os.environ.get("MYMOVIEGRAPHQL_INDENT", 1)
if isinstance(INDENT, str):
    try:
        INDENT = int(INDENT)
    except ValueError:
        INDENT = 1
INDENT = OPT_INDENT_2 if INDENT and INDENT > 0 else 0  # fmt: skip

API_URL = "https://caching.graphql.imdb.com/"
if "MYMOVIEGRAPHQL_LIVE" in os.environ:
    API_URL = "https://api.graphql.imdb.com/"
