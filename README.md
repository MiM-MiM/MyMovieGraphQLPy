# General Information
MyMovieGraphQL is a Python3.10 implementation to fetch data from IMDb via their GraphQL interface.

## Features
- Uses a `json` file created from introspecting the types.
- Creates a `limited` version that avoids cyclicle query generation
- Uses arguments in the query generation, allowing the same query to work for multiple variables, caching of the generated query to be added.
- `Name`. `Title`, and `Main` (multiple type) search have been abstracted.

## Planned Features
- Add more known types to the `getID`
- `str(obj)` logic to attempt and print what is expected based on possible keys and types.

# Installation
MyMovieGraphQL is configured as a python module. It is suggested to create a [venv](https://docs.python.org/3/library/venv.html) first.

## General Install
This will always use the latest versions of packages, may encounter bugs.
```bash
# Activate venv first if used.
# Navigate to cloned folder, `cd MyMovieGraphQLPy`
python3 -m pip install .
```

## Secure Install
This install uses the requirements.txt with hashes specified to ensure known good versions get installed.  If the `--require-hashes` argument is not passed it will not perform the hash check and can lead to compromised packages being installed.
```bash
# Activate venv first if used.
# Navigate to cloned folder, `cd MyMovieGraphQLPy`
python -m pip install -r requirements.txt --require-hashes
python -m pip install --no-deps .
```
See [Secure installs](https://pip.pypa.io/en/stable/topics/secure-installs/) for more information.

### Generate secure requirements.txt
Update the `requirements.in` file and run the `compile` command to fetch the latest hashes.
```bash
pip-compile --generate-hashes requirements.in
```

## Editable mode
Add `-e` after `install`.
```bash
python -m pip install -e .
# Or 
python -m pip install -e --no-deps .
```

# Notes
The API although works publicly, is not documented for the public. The listed fields and arguments may not be complete. If you find one that should be listed please raise an issue with what it belongs to, even if you do not yet know any of the attributes or required arguments.

The types are typically named well to hint at what they may be/return.
- Pluarl names typically return a list in some way.
- Names ending in `Connection` indicate it is a graph `edges ... node` form.
- Types encased in brackets, `[]`, will typically have an attribute of the same name or made singular, indicates a list.
- `ENUM` types are in all caps, such as `DOMESTIC`.
- Dates are always `yyyy-mm-dd` with possible timezone extension or are split in `int` types for `year`, `month`, and `day`.
- IDs that have a main type you may search/link by start with two characters, followed by 7 or 8 numbers.
- IDs that are not normally used for linking and are just types/values are typically lower case with underscores instead of spaces.
  - Each of these will also have a `text` form, being the normal human readible form.
- Complex queryies should be avoided, although possible, not suggested.
  - If a query is too complex it will time out and return a cloud error rather than a normal json encoded one.
- Errors are json encoded and may contain helpful hints to what you may have wanted.

## Known issues
All the API calls that require auth will fail.
The `x-` headers need set.

# Atrributions

All metadata fetched from the following providers is to be used and creditted following their respective TOS.

## Internet Movie Database (IMDb)

<center><a href="https://imdb.com/"><img src="images/imdb.svg" alt="IMDb Logo" title="IMDb" height="60"/></a></center>


Metadata provided by IMDb. Please consider [adding missing information](https://help.imdb.com/article/contribution/contribution-information/adding-new-data/G6BXD2JFDCCETUF4).

This interface is provided free of charge and is not intended to be used for commercial and/or for profit projects. If you wish to use this implementation for that, you must comply with IMDb's terms for gaining access for that type. [Getting Commercial/Paid API Access](https://developer.imdb.com/documentation/api-documentation/getting-access/?ref_=up_next)
