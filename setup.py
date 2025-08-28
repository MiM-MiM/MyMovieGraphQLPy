import setuptools

DEV_PACKAGES = ["responses", "flake8", "pytest"]

setuptools.setup(
    name="MyMovieGraphQL",
    packages=["MyMovieGraphQL"],
    url="https://github.com/MiM-MiM/MyMovieGraphQLPy",
    version="1.0.0-rc1",
    description="Python3.10+ to fetch data from IMDb via the GraphQL API",
    author="MiM",
    keywords=["IMDb", "IMDbGraphQL", "GraphQL", "IMDbAPI", "API"],
    license="GNU General Public License v3.0",
    extras_require={
        "dev": DEV_PACKAGES,
    },
    install_requires=[
        'importlib-metadata; python_version>="3.10"',
        "langcodes",
        "requests",
    ],
    package_data={
        'MyMovieGraphQL': ['data/*.json'],  # Include the JSON files
    },
)
