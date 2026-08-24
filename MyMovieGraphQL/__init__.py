import os

from . import GraphQL
from .Constants import COUNTRY, LANGUAGE
from .logger import set_log_level

"""MyMovieGraphQL package initializer.

This package provides a small helper layer on top of the IMDb GraphQL
endpoints. Import the submodules (``GraphQL``, ``Search``, ``GetByID``,
``MyMovie``, etc.) to access the public API.
"""

set_log_level(os.environ.get("MYMOVIEGRAPHQL_LOGLEVEL", "INFO"))
GraphQL.setLocalCountryLanguage(country=COUNTRY, language=LANGUAGE)
