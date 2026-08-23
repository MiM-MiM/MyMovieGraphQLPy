import setuptools

DEV_PACKAGES = [
    "responses",
    "flake8",
    "pytest",
    "sphinx",
    "sphinx-rtd-theme",
    "sphinx-autodoc-typehints",
]

setuptools.setup(
    name="MyMovieGraphQL",
    packages=["MyMovieGraphQL"],
    url="https://github.com/MiM-MiM/MyMovieGraphQLPy",
    project_urls={
        "Homepage": "https://github.com/MiM-MiM/MyMovieGraphQLPy",
        "Source": "https://github.com/MiM-MiM/MyMovieGraphQLPy",
        "Tracker": "https://github.com/MiM-MiM/MyMovieGraphQLPy/issues",
        "Documentation": "https://github.com/MiM-MiM/MyMovieGraphQLPy/wiki",
    },
    version="1.1.0",
    description="Python3.10+ to fetch data from IMDb via the GraphQL API",
    author="MiM-MiM",
    author_email="69122723+MiM-MiM@users.noreply.github.com",
    maintainer="MiM-MiM",
    maintainer_email="69122723+MiM-MiM@users.noreply.github.com",
    keywords=["IMDb", "IMDbGraphQL", "GraphQL", "IMDbAPI", "API"],
    license="GNU General Public License v3.0",
    extras_require={
        "dev": DEV_PACKAGES,
    },
    python_requires=">=3.10",
    install_requires=[
        "beartype",  # Type checking
        "langcodes",  # Validate language codes
        "requests",  # Make HTTP requests
        "orjson",  # Faster json decoding.
    ],
    package_data={
        "MyMovieGraphQL": ["data/*.json"],  # Include the JSON files
    },
)
