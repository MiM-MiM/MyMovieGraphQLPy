# General Information
MyMovieGraphQL is a Python3.10 implementation to fetch data from IMDb via their GraphQL interface.

## Features
- Get info by ID, only specific types can be queried.
  - To be listed.

## Planned Features
- Still a major WIP, no reason to list yet.

# Installation
MyMovieGraphQL is configured as a python module. It is suggested to create a [venv](https://docs.python.org/3/library/venv.html) first.

```bash
# Activate venv first if used.
# Navigate to cloned folder, `cd MyMovieGraphQLPy`
python3 -m pip install .
```

# Notes
The API alothough works publicly, is not documented for the public. The listed fields and arguments may not be complete. If you find one that should be listed please raise an issue with what it belongs to, even if you do not yet know any of the attributes or required arguments.

The types are typically named well to hint at what they may be/return.
- Pluarl names typically return a list in some way.
- Names ending in `Connection` indicate it is a graph `edges ... node` form.
- Types encased in brackets, `[]`, will typically have an attribute of the same name or made singular, indicates a list.
- `ENUM` types are in all caps, such as `DOMESTIC`, no quotes around them.
- Strings require doune quotes, `"`.
- Dates are always `yyyy-mm-dd` with possible timezone extension or are split in `int` types for `year`, `month`, and `day`.
- IDs that have a main type you may search/link by start with two characters, followed by 7 or 8 numbers.
- IDs that are not normally used for linking and are just types/values are typically lower case with underscores instead of spaces.
  - Each of these will also have a `text` form, being the normal human readible form.
- If something returns a `Title` or `Name` type, you should use the `Limited` version created.
  - This both avoids circular query generation, a recursion limit in `Python`.
- Complex queryies should be avoided, although possible, not suggested.
  - If a query is too complex it will time out and return a cloud error rather than a normal json encoded one.
- Errors are json encoded and may contain helpful hints to what you may have wanted.
  - Things will say `did you mean ...` and provide possible new keys. Example: if something has an `id` field and you pass `bad` it will suggest to use `id`.
  - The same applies to required arguments.
  - Arguments do not get much help besides expected type, which may indicate if it is an `ENUM`.

## Known, need help to implement
### Missing required arguments
#### Title
- `plotContributionLink`, `imageUploadLink`
  - Return `ContributionLink`
    - Has a `url`, assumed type is `str`
  - Missing requlred argument of type `ContributionContext`
  - Notes
    - I assume this requires authencation and will be considered private.
### Missing all attributes
#### Title
- `engagementStatistics`
  - Return `EngagementStatistics`
  - Unknown attributes on `EngagementStatistics`
- `meta`
  - Return `TitleMeta`
    - Has `restrictions` of type `TitleMetaRestrictions`
      - Unknown attributes for `TitleMetaRestrictions`

# Atrributions

All metadata fetched from the following providers is to be used and creditted following their respective TOS.

## Internet Movie Database (IMDb)

<center><a href="https://imdb.com/"><img src="images/imdb.svg" alt="IMDb Logo" title="IMDb" height="60"/></a></center>


Metadata provided by IMDb. Please consider [adding missing information](https://help.imdb.com/article/contribution/contribution-information/adding-new-data/G6BXD2JFDCCETUF4).

This interface is provided free of charge and is not intended to be used for commercial and/or for profit projects. If you wish to use this implementation for that, you must comply with IMDb's terms for gaining access for that type. [Getting Commercial/Paid API Access](https://developer.imdb.com/documentation/api-documentation/getting-access/?ref_=up_next)
