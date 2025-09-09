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
    python_requires='>=3.10',
    install_requires=[
        "beartype", # Type checking
        "langcodes", # Validate language codes
        "requests", # Make HTTP requests
    ],
    package_data={
        'MyMovieGraphQL': ['data/*.json'],  # Include the JSON files
    },
)
