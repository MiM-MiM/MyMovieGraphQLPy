"""Constraints helpers for GraphQL search constraints.

This module exposes a set of small functions, each of which builds and
returns a dictionary suitable for inclusion in a GraphQL "constraints"
argument. Functions return ``dict`` when they produce a constraint or
``None`` when no constraint should be applied.

Docstring style: Google style (``Args``, ``Returns``, ``Raises``).
"""

from typing import Any
import re
from beartype import beartype

# Each constraint should return a base search dict or None
# for that constraint with the given args used to fill it out.
# TODO: Add value validation, ENUMs should check against the `ENUM.json`

@beartype
def _getFromListIfExists(l: list, idx: int) -> Any | None:
    """Return the list element at ``idx`` or ``None`` if out of range.

    Args:
        l (list): The list to read from.
        idx (int): The index to retrieve.

    Returns:
        Any | None: The element at ``idx`` or ``None`` when the index is
        out of range.
    """
    try:
        return l[idx]
    except IndexError:
        return None

@beartype
def alternateVersionMatchingConstraint(
        alternateVersion: str | list[str] = "",
        alternateVersionIncludeType: str = "any", # any/all
) -> dict | None:
    """Build an alternate-version matching constraint.

    Args:
        alternateVersion (str | list[str]): Alternate version text(s) to
            match.
        alternateVersionIncludeType (str): One of ``'any'`` or ``'all'`` to
            indicate inclusion semantics.

    Returns:
        dict | None: Constraint dict or ``None`` when no constraint applies.
    """
    constraint = {}
    allowedTypes = ['any', 'all']
    alternateVersionIncludeType = alternateVersionIncludeType.lower()
    if alternateVersion and alternateVersionIncludeType in allowedTypes:
        if isinstance(alternateVersion, str):
            alternateVersion = [alternateVersion]
        constraintName = f"{alternateVersionIncludeType}AlternateVersionTextTerms"
        constraint[constraintName] = alternateVersion
    return constraint or None

@beartype
def awardConstraint(
        award: str | list[str] = "",  # The award ID
        awardIncludeType: str = "any", # any/all/exclude
) -> dict | None:
    """Build an award-based constraint.

    Args:
        award (str | list[str]): Award ID or list of award IDs.
        awardIncludeType (str): One of ``'any'``, ``'all'``, or ``'exclude'``.

    Returns:
        dict | None: Constraint dict or ``None`` when no constraint applies.
    """
    constraint = {}
    allowedTypes = ['any', 'all', 'exclude']
    awardIncludeType = awardIncludeType.lower()
    if award and awardIncludeType in allowedTypes:
        if isinstance(award, str):
            award = [award]
        constraintName = f"{awardIncludeType}EventNominations"
        awardFilter = [{"eventId": a} for a in award]
        constraint[constraintName] = awardFilter
    return constraint or None

@beartype
def biographyConstraint(
        biographyAuthor: str | list[str] = "",
        biographyText: str = "",
) -> dict | None:
    """Build a biography search constraint.

    Args:
        biographyAuthor (str | list[str]): Author name(s) to filter by.
        biographyText (str): Text to search for inside biographies.

    Returns:
        dict | None: Constraint dict or ``None`` when no constraint applies.
    """
    constraint = {}
    if biographyText:
        constraint["searchText"] = biographyText
    if biographyAuthor:
        if isinstance(biographyAuthor, str):
            biographyAuthor = [biographyAuthor]
        constraint["anyBiographyAuthors"] = biographyAuthor
    return constraint or None

@beartype
def birthDateConstraint(
        birthdayRangeStart: str = "",
        birthdayRangeEnd: str = "",
        birthday: str = "", # MonthDay ISO-8601 format '--06-19'
) -> dict | None:
    """Build a birth date constraint.

    Args:
        birthdayRangeStart (str): Range start date in ``YYYY-MM-DD`` format.
        birthdayRangeEnd (str): Range end date in ``YYYY-MM-DD`` format.
        birthday (str): Month-day in ``MM-DD`` or ``--MM-DD`` format.

    Returns:
        dict | None: Constraint dict or ``None`` when no constraint applies.

    Raises:
        ValueError: When date formats are invalid.
    """
    if birthdayRangeStart and not re.fullmatch(r'\d{4}-\d{2}-\d{2}', birthdayRangeStart):
        raise ValueError(f"The start date is not of the correct form, yy-mm-dd")
    if birthdayRangeEnd and not re.fullmatch(r'\d{4}-\d{2}-\d{2}', birthdayRangeEnd):
        raise ValueError(f"The end date is not of the correct form, yy-mm-dd")
    if birthday and not re.fullmatch(r'(--)?\d{2}-\d{2}', birthday):
        raise ValueError(f"The birthday is not of the correct form, mm-dd or --mm-dd")
    constraint = {}
    birthday = '--' + birthday.removeprefix('--')
    if birthday and len(birthday) == 7:
        constraint["birthday"] = birthday
    if (birthdayRangeStart or birthdayRangeEnd):
        constraint["birthDateRange"] = {
            "start": birthdayRangeStart or None,
            "end": birthdayRangeEnd or None,
        }
    return constraint or None

@beartype
def birthPlaceConstraint(
        birthPlace: str = "",
) -> dict | None:
    """Build a birthplace constraint.

    Args:
        birthPlace (str): Birthplace string to match.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    if birthPlace:
        constraint["birthPlace"] = birthPlace
    return constraint or None

@beartype
def certificateConstraint(
        certificate: dict | list = {},  # {rating: xxx, region: xxx}
        certificateIncludeType: str = "any", # any/exclude
) -> dict | None:
    """Build a certificate (rating/region) constraint.

    Args:
        certificate (dict | list): Certificate dict or list of dicts with
            keys ``rating`` and/or ``region``.
        certificateIncludeType (str): One of ``'any'`` or ``'exclude'``.

    Returns:
        dict | None: Constraint dict or ``None`` when no constraint applies.

    Raises:
        ValueError: If certificate dict contains unexpected keys.
        TypeError: If certificate values are not strings or None.
    """
    allowedDictKeys: set[str] = {"rating", "region"}
    if isinstance(certificate, dict):
        if any([key not in allowedDictKeys for key in certificate.keys()]):
            raise ValueError(f"Certificate contained more keys than allowed, {allowedDictKeys}.")
        for a in allowedDictKeys:
            if not isinstance(certificate.get(a), str | None):
                raise TypeError(f"Certificate must be strings for the keys: {allowedDictKeys}")
    constraint = {}
    allowedTypes = ['any', 'exclude']
    certificateIncludeType = certificateIncludeType.lower() 
    if certificate and certificateIncludeType in allowedTypes:
        if isinstance(certificate, dict):
            certificate = [certificate]
        constraintName = f"{certificateIncludeType}RegionCertificateRatings"
        constraint[constraintName] = certificate
    return constraint or None

@beartype
def characterConstraint(
        character: str | list[str] = "",
        creditedCharacters: bool = True,  # Limit to only credited roles.
) -> dict | None:
    """Build a character name constraint.

    Args:
        character (str | list[str]): Character name(s) to match.
        creditedCharacters (bool): Limit to credited roles when True.

    Returns:
        dict | None: Constraint dict or ``None`` when no constraint applies.
    """
    constraint = {}
    if character:
        if isinstance(character, str):
            character = [character]
        constraint["anyCharacterNames"] = character
        constraint["shouldLimitToCreditedNameIds"] = creditedCharacters
    return constraint or None

@beartype
def colorationConstraint(
        coloration: str | list[str] = "", # The ColorationType ENUM
        colorationIncludeType: str = "any", # any/exclude
) -> dict | None:
    """Build a coloration (color/black-and-white) constraint.

    Args:
        coloration (str | list[str]): Coloration type(s) to match.
        colorationIncludeType (str): One of ``'any'`` or ``'exclude'``.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    allowedTypes = ['any', 'exclude']
    colorationIncludeType = colorationIncludeType.lower()
    if coloration and colorationIncludeType in allowedTypes:
        if isinstance(coloration, str):
            coloration = [coloration]
        constraintName = f"{colorationIncludeType}ColorationTypes"
        constraint[constraintName] = coloration
    return constraint or None

@beartype
def crazyCreditMatchingConstraint(
        crazyCredit: str | list[str] = "",
        crazyCreditIncludeType: str = "all", # any/all
) -> dict | None:
    """Build a crazy-credit text matching constraint.

    Args:
        crazyCredit (str | list[str]): Text terms to match in crazy credits.
        crazyCreditIncludeType (str): One of ``'any'`` or ``'all'``.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    allowedTypes = ['any', 'all']
    crazyCreditIncludeType = crazyCreditIncludeType.lower() 
    if crazyCredit and crazyCreditIncludeType in allowedTypes:
        if isinstance(crazyCredit, str):
            crazyCredit = [crazyCredit]
        constraintName = f"{crazyCreditIncludeType}CrazyCreditTextTerms"
        constraint[constraintName] = crazyCredit
    return constraint or None

@beartype
def creditedCompanyConstraint(
        companyCategory: str | list[str] = "",
        company: str | list[str] = "",
        companyIncludeType: str = "any", # all/any/exclude
) -> dict | None:
    """Build a credited-company constraint.

    Args:
        companyCategory (str | list[str]): Company category or categories.
        company (str | list[str]): Company ID(s).
        companyIncludeType (str): One of ``'any'``, ``'all'``, or ``'exclude'``.

    Returns:
        dict | None: Constraint dict or ``None`` when no constraint applies.
    """
    constraint = {}
    allowedTypes = ["any", "all", "exclude"]
    companyIncludeType = companyIncludeType.lower()
    if companyIncludeType not in allowedTypes:
        company = ""
    if not company and not companyCategory:
        return None
    if companyCategory:
        if isinstance(companyCategory, str):
            companyCategory = [companyCategory]
        constraint["anyCompanyCategories"] = companyCategory
    if company:
        if isinstance(company, str):
            company = [company]
        constraintName = f"{companyIncludeType}CompanyIds"
        constraint[constraintName] = company
    return constraint or None

@beartype
def creditedNameConstraint(
        creditedNameID: str | list[str] = "",
        creditedNameIncludeType: str = "all", # any/all/exclude
) -> dict | None:
    """Build a constraint filtering credited name IDs.

    Args:
        creditedNameID (str | list[str]): Name ID(s) to include/exclude.
        creditedNameIncludeType (str): One of ``'any'``, ``'all'``, or
            ``'exclude'``.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    allowedTypes = ["any", "all", "exclude"]
    creditedNameIncludeType = creditedNameIncludeType.lower()
    if creditedNameID and creditedNameIncludeType in allowedTypes:
        if isinstance(creditedNameID, str):
            creditedNameID = [creditedNameID]
        constraintName = f"{creditedNameIncludeType}NameIds"
        constraint[constraintName] = creditedNameID
    return constraint or None

@beartype
def currentProductionStatusStageConstraint(
        productionStageID: str | list[str] = "",
        productionStageIncludeType: str = "any", # any/exclude
) -> dict | None:
    """Build a production-stage constraint.

    Args:
        productionStageID (str | list[str]): Production stage ID(s).
        productionStageIncludeType (str): One of ``'any'`` or ``'exclude'``.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    allowedTypes = ["any", "exclude"]
    productionStageIncludeType = productionStageIncludeType.lower()
    if productionStageID and productionStageIncludeType in allowedTypes:
        if isinstance(productionStageID, str):
            productionStageID = [productionStageID]
        constraintName = f"{productionStageIncludeType}ProductionStageIds"
        constraint[constraintName] = productionStageID
    return constraint or None

@beartype
def deathDateConstraint(
        deathDate: str = "", # The start day or exact day.
        deathDateEnd: str = "", # If both given it is a range.
) -> dict | None:
    """Build a death date constraint.

    Args:
        deathDate (str): Start or exact date in ``YYYY-MM-DD`` format.
        deathDateEnd (str): End date when defining a range.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.

    Raises:
        ValueError: When date formats are invalid.
    """
    if deathDate and not re.fullmatch(r'\d{4}-\d{2}-\d{2}', deathDate):
        raise ValueError(f"The death date is not of the correct form, yy-mm-dd")
    if deathDateEnd and not re.fullmatch(r'\d{4}-\d{2}-\d{2}', deathDateEnd):
        raise ValueError(f"The death date end is not of the correct form, yy-mm-dd")
    constraint = {}
    if deathDate or deathDateEnd:
        constraint["deathDateRange"] = {
            "start": deathDate or None,
            "end": deathDateEnd or deathDate or None,
        }
    return constraint or None

@beartype
def deathPlaceConstraint(
        deathPlace: str = "",
) -> dict | None:
    """Build a death-place constraint.

    Args:
        deathPlace (str): Death place string to match.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    if deathPlace:
        constraint["deathPlace"] = deathPlace
    return constraint or None

@beartype
def episodicConstraint(
        seriesID: str | list[str] = "", # Ther ID of the series to use
        seriesIDType: str = "any", # any/exclude # Limit to them matching.
        season: str | list[str] = "", # The season numbers to use.
        episode: str | list[str] = "", # The episode numbers to use.
        seasonEpisodeType: str = "any", # any/exclude # Limit to them matching.
) -> dict | None:
    """Build an episodic (series/season/episode) constraint.

    Args:
        seriesID (str | list[str]): Series ID(s) to filter by.
        seriesIDType (str): One of ``'any'`` or ``'exclude'``.
        season (str | list[str]): Season number(s).
        episode (str | list[str]): Episode number(s).
        seasonEpisodeType (str): One of ``'any'`` or ``'exclude'``.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    seasonEpisodeType = seasonEpisodeType.lower()
    seriesIDType = seriesIDType.lower()
    allowedTypes = ["any", "exclude"]
    if seriesID and seriesIDType in allowedTypes:
        if isinstance(seriesID, str):
            seriesID = [seriesID]
        constraintName = f"{seasonEpisodeType}SeriesIds"
        constraint[constraintName] = seriesID
    if (season or episode) and seasonEpisodeType in allowedTypes:
        if season:
            if isinstance(season, str):
                season = [season]
            constraintName = f"{seasonEpisodeType}Seasons"
            constraint[constraintName] = season
        if episode:
            if isinstance(episode, str):
                episode = [episode]
            constraintName = f"{seasonEpisodeType}EpisodeNumbers"
            constraint[constraintName] = episode
    return constraint or None

@beartype
def explicitContentConstraint(
        explicit: str = "INCLUDE_ADULT", # ExplicitContentFilter ENUM
) -> dict | None:
    """Build an explicit-content constraint (adult inclusion/exclusion).

    Args:
        explicit (str): One of ``'INCLUDE_ADULT'``, ``'EXCLUDE_ADULT'``, or
            ``'ONLY_ADULT'``.

    Returns:
        dict | None: Constraint dict or ``None`` when input is invalid.
    """
    constraint = {}
    explicit = explicit.upper()
    explicit = explicit.removesuffix("_ADULT") + "_ADULT"
    allowedTypes = ["EXCLUDE_ADULT", "INCLUDE_ADULT", "ONLY_ADULT"]
    if explicit in allowedTypes:
        constraint["explicitContentFilter"] = explicit
    return constraint or None

@beartype
def filmingLocationConstraint(
        filmingLocation: str | list[str] = "", # The filming location
        filmingLocationType: str = "any", # any/all
) -> dict | None:
    """Build a filming-location constraint.

    Args:
        filmingLocation (str | list[str]): Location(s) to match.
        filmingLocationType (str): One of ``'any'`` or ``'all'``.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    allowedTypes = ["any", "all"]
    filmingLocationType = filmingLocationType.lower()
    if filmingLocation and filmingLocationType in allowedTypes:
        if isinstance(filmingLocation, str):
                filmingLocation = [filmingLocation]
        constraintName = f"{filmingLocationType}Locations"
        constraint[constraintName] = filmingLocation
    return constraint or None

@beartype
def filmographyConstraint(
        filmographyTitleID: str | list[str] = "",
        filmographyTitleIDType: str = "all", # all/any/exclude
        filmographyTitleIDExclude: str | list[str] = "", # If type is also exclude it will use this one.
) -> dict | None:
    """Build a filmography-based constraint for name searches.

    Args:
        filmographyTitleID (str | list[str]): Title ID(s) to match in
            filmographies.
        filmographyTitleIDType (str): One of ``'all'``, ``'any'``, or
            ``'exclude'``.
        filmographyTitleIDExclude (str | list[str]): IDs to explicitly exclude.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    allowedTypes = ["any", "all", "exclude"]
    filmographyTitleIDType = filmographyTitleIDType.lower()
    if filmographyTitleID and filmographyTitleIDType in allowedTypes:
        if isinstance(filmographyTitleID, str):
            filmographyTitleID = [filmographyTitleID]
        constraintName = f"{filmographyTitleIDType}TitleIds"
        constraint[constraintName] = filmographyTitleID
    if filmographyTitleIDExclude:
        if isinstance(filmographyTitleIDExclude, str):
            filmographyTitleIDExclude = [filmographyTitleIDExclude]
        constraint["excludeTitleIds"] = filmographyTitleIDExclude
    return constraint or None

@beartype
def genderIdentityConstraint(
        gender: str | list[str] = "",
        genderType: str = "any",
) -> dict | None:
    """Build a gender constraint.

    Args:
        gender (str | list[str]): Gender value(s) to filter by.
        genderType (str): One of ``'any'`` or ``'exclude'``.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    genderType = genderType.lower()
    allowedTypes = ["any", "exclude"]
    if gender and genderType in allowedTypes:
        if isinstance(gender, str):
            gender = [gender]
        gender = [g.upper() for g in gender]
        constraintName = f"{genderType}Gender"
        constraint[constraintName] = gender
    return constraint or None

@beartype
def genreConstraint(
        genre: str | list[str] = "", # The genre
        genreType: str = "all", # all/any/exclude
        genreMaxRelevant: int | None = None,
) -> dict | None:
    """Build a genre constraint.

    Args:
        genre (str | list[str]): Genre(s) to match.
        genreType (str): One of ``'all'``, ``'any'``, or ``'exclude'``.
        genreMaxRelevant (int | None): Optional maximum relevant genres.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    allowedTypes = ["any", "all", "exclude"]
    genreType = genreType.lower()
    if genre and genreType in allowedTypes:
        if isinstance(genre, str):
            genre = [genre]
        constraintName = f"{genreType}GenreIds"
        constraint[constraintName] = genre
        if genreMaxRelevant is not None:
            constraint["maxRelevantGenres"] = genreMaxRelevant
    return constraint or None

@beartype
def goofMatchingConstraint(
        goof: str | list[str] = "", # the text to search for
        goofType: str = "all", # all/any
) -> dict | None:
    """Build a goof text matching constraint.

    Args:
        goof (str | list[str]): Text terms to search for.
        goofType (str): Either ``'all'`` or ``'any'``.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    allowedTypes = ["any", "all"]
    goofType = goofType.lower()
    if goof and goofType in allowedTypes:
        if isinstance(goof, str):
            goof = [goof]
        constraintName = f"{goofType}GoofTextTerms"
        constraint[constraintName] = goof
    return constraint or None

@beartype
def inTheatersConstraint(
        theaterID: str | list[str] = "", # The theater IDs
        theaterAttribute: str | list[str] = "", # SearchTheaterAttribute ENUM.
        theaterStart: str = "", # ISO-8601 format
        theaterEnd: str = "", # The showtime dates, must have at least start
        theaterLocation: str = "", # The postal code 
        theaterLocationLatLong: dict[str, float] = {}, # {lat: float, long: float}
        theaterLocationRadius: int = 50, # In meters, default 50m
        theaterFavorite: bool = False, # Wehn true: MyFavoriteTheaterSearchFilter ENUM
) -> dict | None:
    """Build an in-theaters (showtime) constraint.

    Args:
        theaterID (str | list[str]): Theater ID(s) to include.
        theaterAttribute (str | list[str]): Theater attributes to filter.
        theaterStart (str): Start date in ``YYYY-MM-DD`` format.
        theaterEnd (str): End date in ``YYYY-MM-DD`` format.
        theaterLocation (str): Postal code for location filtering.
        theaterLocationLatLong (dict[str, float]): Latitude/longitude dict
            with ``lat`` and ``long`` keys.
        theaterLocationRadius (int): Radius in meters for lat/long filtering.
        theaterFavorite (bool): When True, only favorite theaters are used.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.

    Raises:
        ValueError: For invalid date formats or inconsistent location args.
    """
    if theaterEnd and not theaterStart:
        raise ValueError(f"You must have a start if you have an end date.")
    allowedDictKeys: set[str] = {"lat", "long"}
    if isinstance(theaterLocationLatLong, dict):
        if any([key not in allowedDictKeys for key in theaterLocationLatLong.keys()]):
            raise ValueError(f"Certificate contained more keys than allowed, {allowedDictKeys}.")
    if theaterStart and not re.fullmatch(r'\d{4}-\d{2}-\d{2}', theaterStart):
        raise ValueError(f"The start date is not of the correct form, yy-mm-dd")
    if theaterEnd and not re.fullmatch(r'\d{4}-\d{2}-\d{2}', theaterEnd):
        raise ValueError(f"The end date is not of the correct form, yy-mm-dd")
    lat = theaterLocationLatLong.get("lat")
    long = theaterLocationLatLong.get("long")
    if (bool(lat) ^ bool(long)):
        raise ValueError(f"Either both latitude and longitude are passed or none.")
    if theaterLocationRadius < 1:
        raise ValueError(f"The radius must be a positive integer {theaterLocationRadius}")
    constraint = {}
    if theaterID:
        if isinstance(theaterID, str):
            theaterID = [theaterID]
        constraint["anyCinemaIds"] = theaterID
    if theaterAttribute:
        if isinstance(theaterAttribute, str):
            theaterAttribute = [theaterAttribute]
        constraint["allTheaterAttributes"] = theaterAttribute
    if theaterStart:
        constraint["dateTimeRange"] = {
            'start': theaterStart,
            'end': theaterEnd or None
        }
    if theaterLocationLatLong or theaterLocation:
        constraint["location"] = {
            "postalCode": theaterLocation or None,
            "latLong": theaterLocationLatLong or None,
            "radiusInMeters": theaterLocationRadius or None,
        }
    if theaterFavorite:
        constraint["myFavoriteTheaters"] = "ONLY_MY_FAVORITE"
    return constraint or None

@beartype
def interestConstraint(
        interestID: str | list[str] = "",
        interestType: str = "all", # all/any/exclude
) -> dict | None:
    """Build an interest-category constraint.

    Args:
        interestID (str | list[str]): Interest ID(s) to filter by.
        interestType (str): One of ``'any'``, ``'all'``, or ``'exclude'``.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    allowedTypes = ['any', 'all', 'exclude']
    interestType = interestType.lower() 
    if interestID and interestType in allowedTypes:
        if isinstance(interestID, str):
            interestID = [interestID]
            constraintName = f"{interestType}InterestIds"
            constraint[constraintName] = interestID
    return constraint or None

@beartype
def keywordConstraint(
        keyword: str | list[str] = "",
        keywordType: str = "all", # all/any/exclude
) -> dict | None:
    """Build a keyword constraint.

    Args:
        keyword (str | list[str]): Keyword(s) to match.
        keywordType (str): One of ``'all'``, ``'any'``, or ``'exclude'``.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    allowedTypes = ['any', 'all', 'exclude']
    keywordType = keywordType.lower()
    if keyword and keywordType in allowedTypes:
        if isinstance(keyword, str):
            keyword = [keyword]
        constraintName = f"{keywordType}Keywords"
        constraint[constraintName] = keyword
    return constraint or None

@beartype
def languageConstraint(
        language: str | list[str] = "",
        languageType: str = "any", # all/any/exclude
        languagePrimary: str | list[str] = "",
        languagePrimaryType: str = "any", # any/exclude
        silent: bool | None = None, # Silent
) -> dict | None:
    """Build language-related constraints.

    Args:
        language (str | list[str]): Language(s) to match.
        languageType (str): One of ``'any'``, ``'all'``, or ``'exclude'``.
        languagePrimary (str | list[str]): Primary language(s) to match.
        languagePrimaryType (str): One of ``'any'`` or ``'exclude'``.
        silent (bool | None): When provided, filter for silent films.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    languageType = languageType.lower() 
    languagePrimaryType = languagePrimaryType.lower() 
    allowedTypes = ['any', 'all', 'exclude']
    if language and languageType in allowedTypes:
        if isinstance(language, str):
            language = [language]
        constraintName = f"{languageType}Languages"
        constraint[constraintName] = language
    allowedTypes = ['any', 'exclude']
    if languagePrimary and languagePrimaryType in allowedTypes:
        if isinstance(languagePrimary, str):
            languagePrimary = [languagePrimary]
        constraintName = f"{languagePrimaryType}PrimaryLanguages"
        constraint[constraintName] = languagePrimary
    if silent is not None:
        constraint["isSilent"] = silent
    return constraint or None

@beartype
def listConstraint(
        inList: str | list[str] = "",
        inPredefinedList: str | list[str] = "", # ListClassId ENUM
        notInList: str | list[str] = "", # always an any
        notInPredefinedList: str | list[str] = "", # always an any
        inListType: str = "any", # all/any
        inPredefinedListType: str = "any", # all/any
) -> dict | None:
    """Build list membership constraints.

    Args:
        inList (str | list[str]): User lists to include.
        inPredefinedList (str | list[str]): Predefined list class IDs.
        notInList (str | list[str]): Lists to exclude.
        notInPredefinedList (str | list[str]): Predefined lists to exclude.
        inListType (str): ``'any'`` or ``'all'`` semantics for in-list.
        inPredefinedListType (str): ``'any'`` or ``'all'`` for predefined lists.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    inListType = inListType.capitalize() 
    inPredefinedListType = inPredefinedListType.capitalize() 
    allowedTypes = ['Any', 'All']
    s = 's' if inPredefinedListType == 'Any' else ''
    if inList and inListType in allowedTypes:
        if isinstance(inList, str):
            inList = [inList]
        constraintName = f"in{inListType}List{s}"
        constraint[constraintName] = inList
    if inPredefinedList and inPredefinedListType in allowedTypes:
        if isinstance(inPredefinedList, str):
            inPredefinedList = [inPredefinedList]
        constraintName = f"in{inPredefinedListType}PredefinedList{s}"
        constraint[constraintName] = {
            "classId": inPredefinedList
        }
    if notInList:
        if isinstance(notInList, str):
            notInList = [notInList]
        constraint["notInAnyList"] = notInList
    if notInPredefinedList:
        if isinstance(notInPredefinedList, str):
            notInPredefinedList = [notInPredefinedList]
        constraint["notInAnyPredefinedList"] = {
            "classId": notInPredefinedList
        }
    return constraint or None

@beartype
def myRatingConstraint(
        myRatingType: str = "INCLUDE", # MyRatingSearchFilterType ENUM
        myRatingMin: int | None = None,
        myRatingMax: int | None = None,
):
    """Build a personal-rating range constraint.

    Args:
        myRatingType (str): Filter type such as ``'INCLUDE'``.
        myRatingMin (int | None): Minimum personal rating.
        myRatingMax (int | None): Maximum personal rating.

    Returns:
        dict | None: Constraint dict or ``None`` when no rating range provided.

    Raises:
        ValueError: When ``myRatingMin`` is greater than ``myRatingMax``.
    """
    if myRatingMin is not None and myRatingMax is not None and myRatingMin > myRatingMax:
        # Cannot use the float(min or 'inf') style here, if one is 0, it results in inf.
        raise ValueError(f"The min cannot be larger than the mad, min:{myRatingMin} > max:{myRatingMax}")
    constraint = {}
    if myRatingMin is not None or myRatingMax is not None:
        constraint = {
            "filterType": myRatingType,
            "ratingRange": {
                "min": myRatingMin,
                "max": myRatingMax,
            }
        }
    return constraint or None

@beartype
def originCountryConstraint(
        originCountry: str | list[str] = "",
        originCountryType: str = "all", # all/any/exclude
        originPrimaryCountry: str | list[str] = "",
        originPrimaryCountryType: str = "any", # any/exclude
):
    """Build origin country constraints for titles.

    Args:
        originCountry (str | list[str]): Origin country IDs or names.
        originCountryType (str): One of ``'all'``, ``'any'``, or ``'exclude'``.
        originPrimaryCountry (str | list[str]): Primary country(s) to match.
        originPrimaryCountryType (str): One of ``'any'`` or ``'exclude'``.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    allowedTypes = ['all', 'any', 'exclude']
    if originCountry and originCountryType in allowedTypes:
        if isinstance(originCountry, str):
            originCountry = [originCountry]
        constraintName = f"{originCountryType}Countries"
        constraint[constraintName] = originCountry
    allowedTypes = ['any', 'exclude']
    if originPrimaryCountry and originPrimaryCountryType in allowedTypes:
        if isinstance(originPrimaryCountry, str):
            originPrimaryCountry = [originPrimaryCountry]
        constraintName = f"{originPrimaryCountryType}PrimaryCountries"
        constraint[constraintName] = originPrimaryCountry
    return constraint or None

@beartype
def plotMatchingConstraint(
        plotText: str | list[str] = "",
        plotTextType: str = "all", #all/any
        plotAuthor: str | list[str] = "",
) -> dict | None:
    """Build a plot-text matching constraint.

    Args:
        plotText (str | list[str]): Text to search in plot descriptions.
        plotTextType (str): Either ``'all'`` or ``'any'``.
        plotAuthor (str | list[str]): Author(s) of plot entries to filter.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    allowedTypes = ['all', 'any']
    plotTextType = plotTextType.lower()
    if plotText and plotTextType in allowedTypes:
        if isinstance(plotText, str):
            plotText = [plotText]
        constraintName = f"{plotTextType}PlotTextTerms"
        constraint[constraintName] = plotText
    if plotAuthor:
        if isinstance(plotAuthor, str):
            plotAuthor = [plotAuthor]
        constraint["anyPlotAuthors"] = plotAuthor
    return constraint or None

@beartype
def professionConstraint(
        profession: str | list[str] = "",
        professionType: str = "any",
        professionExclude: str | list[str] = "", # If type is set to exclude this overrids the above.
) -> dict | None:
    """Build a profession-based constraint for name searches.

    Args:
        profession (str | list[str]): Profession ID(s) to include.
        professionType (str): One of ``'all'``, ``'any'``, or ``'exclude'``.
        professionExclude (str | list[str]): Profession IDs to exclude.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    allowedTypes = ["all", "any", "exclude"]
    professionType = professionType.lower()
    if profession and professionType in allowedTypes:
        if isinstance(profession, str):
            profession = [profession]
        constraintName = f"{professionType}ProfessionIds"
        constraint[constraintName] = profession
    if professionExclude:
        if isinstance(professionExclude, str):
            profession = [professionExclude]
        constraint["excludeProfessionIds"] = professionExclude
    return constraint or None

@beartype
def professionCategoryConstraint(
        professionCategory: str | list[str] = "",
        professionCategoryType: str = "any",
        professionCategoryExclude: str | list[str] = "", # If type is set to exclude this overrids the above.
) -> dict | None:
    """Build a profession-category constraint.

    Args:
        professionCategory (str | list[str]): Profession category IDs.
        professionCategoryType (str): One of ``'all'``, ``'any'``, or
            ``'exclude'``.
        professionCategoryExclude (str | list[str]): Categories to exclude.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    allowedTypes = ["all", "any", "exclude"]
    professionCategoryType = professionCategoryType.lower()
    if professionCategory and professionCategoryType in allowedTypes:
        if isinstance(professionCategory, str):
            professionCategory = [professionCategory]
        constraintName = f"{professionCategoryType}ProfessionCategoryIds"
        constraint[constraintName] = professionCategory
    if professionCategoryExclude:
        if isinstance(professionCategoryExclude, str):
            professionCategoryExclude = [professionCategoryExclude]
        constraint["excludeProfessionCategoryIds"] = professionCategoryExclude
    return constraint or None

@beartype
def quoteMatchingConstraint(
        quote: str | list[str] = "",
        quoteType: str = "all", # all/any
) -> dict | None:
    """Build a quote-text matching constraint.

    Args:
        quote (str | list[str]): Quote text terms to match.
        quoteType (str): Either ``'all'`` or ``'any'``.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    allowedTypes = ['all', 'any']
    quoteType = quoteType.lower()
    if quote and quoteType in allowedTypes:
        if isinstance(quote, str):
            quote = [quote]
        constraintName = f"{quoteType}QuoteTextTerms"
        constraint[constraintName] = quote
    return constraint or None

@beartype
def rankedTitleListConstraint(
        rankedTitleMin: int | None = None,
        rankedTitleMax: int | None = None,
        rankedTitleListType: str = "TITLE_METER", # RankedTitleListType ENUM
        rankedTitleType: str = "all", # all/exclude
) -> dict | None:
    """Build a ranked-title list constraint.

    Args:
        rankedTitleMin (int | None): Minimum rank value.
        rankedTitleMax (int | None): Maximum rank value.
        rankedTitleListType (str): Ranked list type identifier.
        rankedTitleType (str): Either ``'all'`` or ``'any'``.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.

    Raises:
        ValueError: When min is greater than max.
    """
    if rankedTitleMin is not None and rankedTitleMax is not None and rankedTitleMin > rankedTitleMax:
        raise ValueError(f"The min cannot be larger than the ma, min:{rankedTitleMin} > max:{rankedTitleMax}")
    # This can have a list of ranges, out of scope for basic search.
    constraint = {}
    allowedTypes = ['all', 'any']
    rankedTitleType = rankedTitleType.lower()
    if (rankedTitleMin or rankedTitleMax) and rankedTitleListType and rankedTitleType in allowedTypes:
        constraintName = f"{rankedTitleType}RankedTitleLists"
        constraint[constraintName] = [
            {
                'rankRange': {
                    'min': rankedTitleMin,
                    'max': rankedTitleMax,
                },
                'rankedTitleListType': rankedTitleListType,
            }
        ]
    return constraint or None

@beartype
def releaseDateConstraint(
        year: int = 0,
        yearEnd: int = 0,
        dateStart: str = "", # yyyy-mm-dd
        dateEnd: str = "", # yyyy-mm-dd
) -> dict | None:
    """Build a release-date range constraint.

    Args:
        year (int): Single year to search (expands to start/end of year).
        yearEnd (int): End year when specifying a year range.
        dateStart (str): Start date in ``YYYY-MM-DD`` format.
        dateEnd (str): End date in ``YYYY-MM-DD`` format.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.

    Raises:
        ValueError: When incompatible or invalid date arguments are given.
    """
    if year and dateStart:
        raise ValueError(f"You can only pass a start date or a year, not both.")
    if yearEnd and dateEnd:
        raise ValueError(f"You can only pass a end date or a year, not both.")
    if dateStart and not re.fullmatch(r'\d{4}-\d{2}-\d{2}', dateStart):
        raise ValueError(f"The start date is not of the correct form, yy-mm-dd")
    if dateEnd and not re.fullmatch(r'\d{4}-\d{2}-\d{2}', dateEnd):
        raise ValueError(f"The end date is not of the correct form, yy-mm-dd")
    # If you only give a year, do start and end of that year.
    # Otherwise you can specify yearEnd or more exact dates.
    constraint = {}
    if year and not dateStart and not dateEnd and not yearEnd:
        dateStart = f"{year:04d}-01-01"
        dateEnd = f"{year:04d}-12-31"
    if year and not dateStart:
        dateStart = f"{year:04d}-01-01"
    if yearEnd and not dateEnd:
        dateEnd = f"{yearEnd:04d}-12-31"
    if dateStart or dateEnd:
        constraint["releaseDateRange"] = {
            'start': dateStart or None,
            'end': dateEnd or None,
        }
    return constraint or None

@beartype
def runtimeConstraint(
        runtimeMin: int = 0, # In minutes
        runtimeMax: int = 0,
) -> dict | None:
    """Build a runtime range constraint (in minutes).

    Args:
        runtimeMin (int): Minimum runtime in minutes.
        runtimeMax (int): Maximum runtime in minutes.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.

    Raises:
        ValueError: For invalid ranges or negative runtimes.
    """
    if runtimeMax and runtimeMin and runtimeMin > runtimeMax:
        raise ValueError(f"The min cannot be larger than the max, min:{runtimeMin} > max:{runtimeMax}.")
    if runtimeMin < 0 or runtimeMax < 0:
        raise ValueError(f"The runtimes cannot be negative, min:{runtimeMin} and max:{runtimeMax}")
    constraint = {}
    if runtimeMin or runtimeMax:
        constraint['runtimeRangeMinutes'] = {
            'min': runtimeMin or None,
            'max': runtimeMax or None,
        }
    return constraint or None

@beartype
def singleUserRatingConstraint(
        ratingUserID: str = "",
        ratingUserRangeMin: int = 0,
        ratingUserRangeMax: int = 0,
        ratingUserType: str = "INCLUDE", # SingleUserRatingSearchFilterType ENUM
) -> dict | None:
    """Build a single-user rating constraint.

    Args:
        ratingUserID (str): User ID whose ratings to filter by.
        ratingUserRangeMin (int): Minimum rating value (0-10).
        ratingUserRangeMax (int): Maximum rating value (0-10).
        ratingUserType (str): Filter type such as ``'INCLUDE'``.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.

    Raises:
        ValueError: For invalid ranges or out-of-bounds rating values.
    """
    if ratingUserRangeMin and ratingUserRangeMax and ratingUserRangeMin > ratingUserRangeMax:
        raise ValueError(f"The min cannot be larger than the max, min:{ratingUserRangeMin} > max:{ratingUserRangeMax}.")
    if ratingUserRangeMin < 0 or ratingUserRangeMax < 0:
        raise ValueError(f"The ratings cannot be negative, min:{ratingUserRangeMin} and max:{ratingUserRangeMax}")
    if ratingUserRangeMin > 10 or ratingUserRangeMax > 10:
        raise ValueError(f"The ratings cannot be above 10, min:{ratingUserRangeMin} and max:{ratingUserRangeMax}")
    constraint = {}
    if ratingUserID and ratingUserType and (ratingUserRangeMin or ratingUserRangeMax):
        constraint = {
            'filterType': ratingUserType,
            'ratingRange': {
                'min': ratingUserRangeMin or None,
                'max': ratingUserRangeMax or None,
            },
            'userId': ratingUserID,
        }
    return constraint or None

@beartype
def soundMixConstraint(
        soundMix: str | list[str] = "",
        soundMixExclude: str | list[str] = "",
) -> dict | None:
    """Build a sound-mix inclusion/exclusion constraint.

    Args:
        soundMix (str | list[str]): Sound mix types to include.
        soundMixExclude (str | list[str]): Sound mix types to exclude.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    anySoundMixTypes = []
    excludeSoundMixTypes = []
    if soundMix:
        anySoundMixTypes = [soundMix] if isinstance(soundMix, str) else soundMix
    if soundMixExclude:
        excludeSoundMixTypes = [soundMixExclude] if isinstance(soundMixExclude, str) else soundMixExclude
    if anySoundMixTypes or excludeSoundMixTypes:
        constraint = {
            'anySoundMixTypes': anySoundMixTypes or None,
            'excludeSoundMixTypes': excludeSoundMixTypes or None
        }
    return constraint or None

@beartype
def soundtrackMatchingConstraint(
        soundtrackTerms: str | list[str] = "",
        soundtrackTermsType: str = "all", # all/any
) -> dict | None:
    """Build a soundtrack-text matching constraint.

    Args:
        soundtrackTerms (str | list[str]): Text terms to search in soundtrack
            metadata.
        soundtrackTermsType (str): Either ``'all'`` or ``'any'``.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    allowedTypes = ['all', 'any']
    soundtrackTermsType = soundtrackTermsType.lower()
    if soundtrackTerms and soundtrackTermsType in allowedTypes:
        if isinstance(soundtrackTerms, str):
            soundtrackTerms = [soundtrackTerms]
        constraintName = f"{soundtrackTermsType}SoundtrackTextTerms"
        constraint[constraintName] = soundtrackTerms
    return constraint or None

@beartype
def textSearchConstraint(
        search: str = "",
) -> dict | None:
    """Build a simple text-search constraint.

    Args:
        search (str): Text to use as a search term.

    Returns:
        dict | None: ``{'searchTerm': search}`` or ``None`` when empty.
    """
    constraint = {}
    if search:
        constraint = {
            'searchTerm': search
        }
    return constraint or None

@beartype
def titleCreditsConstraint(
        creditCharacter: str | list[str] = "",
        creditCategory: str | list[str] = "",
        creditJobCategory: str | list[str] = "",
        creditNameID: str | list[str] = "",
        creditType: str = "all",
        creditAdvanced: dict = {},
) -> dict | None:
    """Build constraints for title credit filters.

    Args:
        creditCharacter (str | list[str]): Character name(s) for credit filters.
        creditCategory (str | list[str]): Credit category(ies).
        creditJobCategory (str | list[str]): Job category(ies).
        creditNameID (str | list[str]): Name ID(s) to filter by.
        creditType (str): Either ``'all'`` or ``'any'``.
        creditAdvanced (dict): Advanced/custom credit specification (overrides
            simple arguments when provided).

    Returns:
        dict | None: Constraint dict or ``None`` when empty or invalid.
    """
    # TODO: Validate the creditAdvanced keys/values, this is not a general use arg.
    constraint = {}
    allowedTypes = ['all', 'any']
    creditType = creditType.lower()
    constraintName = f"{creditType}Credits"
    if creditAdvanced:
        # Useful if someone wants to include and exclude.
        constraint = creditAdvanced
    elif (creditCharacter or creditCategory or creditJobCategory or creditJobCategory or creditNameID) and creditType in allowedTypes:
        creditOptions = [creditCharacter, creditCategory, creditJobCategory, creditJobCategory, creditNameID]
        if all(isinstance(x, str) for x in creditOptions):
            # All strings, single character
            constraint[constraintName] = [
                {
                    "character": creditCharacter or None,
                    "creditCategory": creditCategory or None,
                    "jobCategory": creditJobCategory or None,
                    "nameId": creditNameID or None,
                }
            ]
        elif any(isinstance(x, list) for x in creditOptions):
            # all lists, must be same lengths or empty
            maxLength = 0
            constraint[constraintName] = []
            for x in creditOptions:
                if not isinstance(x, list):
                    continue
                if len(x) == 0:
                    continue
                if maxLength == 0:
                    maxLength = len(x)
                if len(x) != maxLength:
                    return None
            if maxLength == 0:
                return None
            # Allow to find if someone directed multiple films and similar.
            if creditCharacter and isinstance(creditCharacter, str):
                creditCharacter = [creditCharacter]*maxLength
            if creditCategory and isinstance(creditCategory, str):
                creditCategory = [creditCategory]*maxLength
            if creditJobCategory and isinstance(creditJobCategory, str):
                creditJobCategory = [creditJobCategory]*maxLength
            if creditNameID and isinstance(creditNameID, str):
                creditNameID = [creditNameID]*maxLength

            constraint[constraintName] = []
            for i in range(0, maxLength):
                constraint[constraintName].append(
                    {
                        "character": _getFromListIfExists(creditCharacter, i), # pyright: ignore[reportArgumentType]
                        "creditCategory": _getFromListIfExists(creditCategory, i), # pyright: ignore[reportArgumentType]
                        "jobCategory": _getFromListIfExists(creditJobCategory, i), # pyright: ignore[reportArgumentType]
                        "nameId": _getFromListIfExists(creditNameID, i), # pyright: ignore[reportArgumentType]
                    }
                )
    return constraint or None

@beartype
def titleMeterConstraint(
        meterMin: int = 0,
        meterMax: int = 0,
        meterType: str = "TITLE_METER", # TitleMeterType ENUM
) -> dict | None:
    """Build a title-meter ranking range constraint.

    Args:
        meterMin (int): Minimum meter rank.
        meterMax (int): Maximum meter rank.
        meterType (str): Meter type identifier (e.g. ``'TITLE_METER'``).

    Returns:
        dict | None: Constraint dict or ``None`` when empty.

    Raises:
        ValueError: For invalid ranges or negative values.
    """
    if meterMin and meterMax and meterMin > meterMax:
        raise ValueError(f"The min cannot be bigger than the max, min:{meterMin} > max:{meterMax}")
    if meterMin < 0 or meterMax < 0:
        raise ValueError(f"The min and max must be positive, min:{meterMin} and max:{meterMax}")
    constraint = {}
    meterType = meterType.upper().removesuffix("_METER") + "_METER"
    if meterMin or meterMax:
        constraint = {
            'rankRange': {
                'min': meterMin or None,
                'max': meterMax or None,
            },
            'titleMeterType': meterType
        }
    return constraint or None

@beartype
def titleTypeConstraint(
        titleType: str | list[str] = "",
        titleTypeExclude: str | list[str] = "",
) -> dict | None:
    """Build a title-type inclusion/exclusion constraint.

    Args:
        titleType (str | list[str]): Title type IDs to include.
        titleTypeExclude (str | list[str]): Title type IDs to exclude.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    if titleType:
        if isinstance(titleType, str):
            titleType = [titleType]
        constraint = {
            'anyTitleTypeIds': titleType
        }
    if titleTypeExclude:
        if isinstance(titleTypeExclude, str):
            titleTypeExclude = [titleTypeExclude]
        constraint = {
            'excludeTitleTypeIds': titleTypeExclude
        }
    return constraint or None

@beartype
def triviaMatchingConstraint(
        triviaTerm: str | list[str] = "",
        triviaTermType: str = "all", # all/any
) -> dict | None:
    """Build a trivia-text matching constraint.

    Args:
        triviaTerm (str | list[str]): Trivia text terms to match.
        triviaTermType (str): Either ``'all'`` or ``'any'``.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    triviaTermType = triviaTermType.lower()
    allowedTypes = ['all', 'any']
    if triviaTerm and triviaTermType in allowedTypes:
        if isinstance(triviaTerm, str):
            triviaTerm = [triviaTerm]
        constraintName = f"{triviaTermType}TriviaTextTerms"
        constraint[constraintName] = triviaTerm
    return constraint or None

@beartype
def userRatingsConstraint(
        ratingMin: float = 0.0,
        ratingMax: float = 0.0,
        ratingCountMin: int = 0,
        ratingCountMax: int = 0,
) -> dict | None:
    """Build aggregate user-rating and rating-count constraints.

    Args:
        ratingMin (float): Minimum aggregate rating.
        ratingMax (float): Maximum aggregate rating.
        ratingCountMin (int): Minimum rating count.
        ratingCountMax (int): Maximum rating count.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    if (ratingMin or ratingMax):
        constraint["aggregateRatingRange"] = {
            'min': ratingMin or None,
            'max': ratingMax or None,
        }
    if (ratingMin or ratingMax):
        constraint["ratingsCountRange"] = {
            'min': ratingCountMin or None,
            'max': ratingCountMax or None,
        }
    return constraint or None

@beartype
def watchOptionsConstraint(
        watchProviderID: str | list[str] = "",
        watchRegion: str | list[str] = "",
        watchProviderIDExclude: str | list[str] = "",
        watchRegionExclude: str | list[str] = "",
        watchType: str | list[str] = "", # SearchWatchOptionType ENUM
) -> dict | None:
    """Build watch-provider and region constraints.

    Args:
        watchProviderID (str | list[str]): Provider ID(s) to include.
        watchRegion (str | list[str]): Region(s) to include.
        watchProviderIDExclude (str | list[str]): Provider IDs to exclude.
        watchRegionExclude (str | list[str]): Regions to exclude.
        watchType (str | list[str]): Watch option types to require.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    if watchProviderID:
        if isinstance(watchProviderID, str):
            watchProviderID = [watchProviderID]
        constraint["anyWatchProviderIds"] = watchProviderID
    if watchRegion:
        if isinstance(watchRegion, str):
            watchRegion = [watchRegion]
        constraint["anyWatchRegions"] = watchRegion
    if watchProviderIDExclude:
        if isinstance(watchProviderIDExclude, str):
            watchProviderIDExclude = [watchProviderIDExclude]
        constraint["excludeWatchProviderIds"] = watchProviderIDExclude
    if watchRegionExclude:
        if isinstance(watchRegionExclude, str):
            watchRegionExclude = [watchRegionExclude]
        constraint["excludeWatchRegions"] = watchRegionExclude
    if watchType:
        # Does not need any other args, can filter only on types.
        if isinstance(watchType, str):
            watchType = [watchType]
        constraint["hasWatchOptionTypes"] = watchType
    return constraint or None

@beartype
def withDataConstraint(
        withData: str | list[str] = "",  # respective (DataType)DataType ENUMs
        withDataMissing: str | list[str] = "",
        withDataAny: str | list[str] = "",
) -> dict | None:
    """Build constraints that require or forbid specific data availability.

    Args:
        withData (str | list[str]): Data types that must be available.
        withDataMissing (str | list[str]): Data types that must be missing.
        withDataAny (str | list[str]): Any of these data types may be available.

    Returns:
        dict | None: Constraint dict or ``None`` when empty.
    """
    constraint = {}
    if withData:
        if isinstance(withData, str):
            withData = [withData]
        withData = [td.upper() for td in withData]
        constraint["allDataAvailable"] = withData
    if withDataMissing:
        if isinstance(withDataMissing, str):
            withDataMissing = [withDataMissing]
        withDataMissing = [td.upper() for td in withDataMissing]
        constraint["noDataAvailable"] = withDataMissing
    if withDataAny:
        if isinstance(withDataAny, str):
            withDataAny = [withDataAny]
        withDataAny = [td.upper() for td in withDataAny]
        constraint["anyDataAvailable"] = withDataAny
    return constraint or None
