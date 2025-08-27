from typing import Any
import re
# Each constraint should return a base search dict or none
# for that constraint with the given args used to fill it out.
# TODO: Add type checking
# TODO: Add value validation, ENUMs should check agaist the `ENUM.json``

def _getFromListIfExists(l: list, idx: int) -> Any | None:
    if not isinstance(l, list):
        raise TypeError(f"getFromList requires a list, '{type(l)}' given.")
    try:
        return l[idx]
    except IndexError:
        return None


def alternateVersionMatchingConstraint(
        alternateVersion: str | list[str] = "",
        alternateVersionIncludeType: str = "any", # any/all
) -> dict | None:
    if not isinstance(alternateVersion, str | list):
        raise TypeError(f"alternateVersion must be a string or list, `{type(alternateVersion)}` given.")
    if not isinstance(alternateVersionIncludeType, str):
        raise TypeError(f"pagnation must be a string, `{type(alternateVersionIncludeType)}` given.")
    
    constraint = {}
    allowedTypes = ['any', 'all']
    alternateVersionIncludeType = alternateVersionIncludeType.lower()
    if alternateVersion and alternateVersionIncludeType in allowedTypes:
        if isinstance(alternateVersion, str):
            alternateVersion = [alternateVersion]
        constraintName = f"{alternateVersionIncludeType}AlternateVersionTextTerms"
        constraint[constraintName] = alternateVersion
    return constraint or None

def awardConstraint(
        award: str | list[str] = "",  # The award ID
        awardIncludeType: str = "any", # any/all/exclude
) -> dict | None:
    if not isinstance(award, str | list):
        raise TypeError(f"The award must be a string or list of strings, '{type(award)}' given.")
    if isinstance(award, list) and not all([isinstance(attrib, str) for attrib in award]):
        raise TypeError(f"award is a list containing a non-string.")
    if not isinstance(awardIncludeType, str):
        raise TypeError(f"The type must be a string, '{type(awardIncludeType)}' given.")
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

def biographyConstraint(
        biographyAuthor: str | list[str] = "",
        biographyText: str = "",
) -> dict | None:
    if not isinstance(biographyAuthor, str | list):
        raise TypeError(f"The biographyAuthor must be a string or list of strings, '{type(biographyAuthor)}' given.")
    if isinstance(biographyAuthor, list) and not all([isinstance(attrib, str) for attrib in biographyAuthor]):
        raise TypeError(f"biographyAuthor is a list containing a non-string.")
    if not isinstance(biographyText, str):
        raise TypeError(f"The type must be a string, '{type(biographyText)}' given.")
    constraint = {}
    if biographyText:
        constraint["searchText"] = biographyText
    if biographyAuthor:
        if isinstance(biographyAuthor, str):
            biographyAuthor = [biographyAuthor]
        constraint["anyBiographyAuthors"] = biographyAuthor
    return constraint or None

def birthDateConstraint(
        birthdayRangeStart: str = "",
        birthdayRangeEnd: str = "",
        birthday: str = "", # MonthDay ISO-8601 format '--06-19'
) -> dict | None:
    if not isinstance(birthdayRangeStart, str):
        raise TypeError(f"The start must be a string, '{type(birthdayRangeStart)}' given.")
    if not isinstance(birthdayRangeEnd, str):
        raise TypeError(f"The end must be a string, '{type(birthdayRangeEnd)}' given.")
    if not isinstance(birthday, str):
        raise TypeError(f"The birthday must be a string, '{type(birthday)}' given.")
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

def birthPlaceConstraint(
        birthPlace: str = "",
) -> dict | None:
    if not isinstance(birthPlace, str):
        raise TypeError(f"The birt place must be a string, '{type(birthPlace)}' given.")
    constraint = {}
    if birthPlace:
        constraint["birthPlace"] = birthPlace
    return constraint or None

def certificateConstraint(
        certificate: dict | list = {},  # {rating: xxx, region: xxx}
        certificateIncludeType: str = "any", # any/exclude
) -> dict | None:
    if not isinstance(certificate, str | dict):
        raise TypeError(f"The certificate must be a string or dict, '{type(certificate)}' given.")
    if not isinstance(certificateIncludeType, str):
        raise TypeError(f"The certificate type must be a string, '{type(certificateIncludeType)}' given.")
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

def characterConstraint(
        character: str | list[str] = "",
        creditedCharacters: bool = True,  # Limit to only credited roles.
) -> dict | None:
    if not isinstance(character, str | list):
        raise TypeError(f"The character must be a string or list of strings, '{type(character)}' given.")
    if isinstance(character, list) and not all([isinstance(attrib, str) for attrib in character]):
        raise TypeError(f"character is a list containing a non-string.")
    if not isinstance(creditedCharacters, bool):
        raise TypeError(f"The credited character flag must be a bool, '{type(creditedCharacters)}' given.")
    constraint = {}
    if character:
        if isinstance(character, str):
            character = [character]
        constraint["anyCharacterNames"] = character
        constraint["shouldLimitToCreditedNameIds"] = creditedCharacters
    return constraint or None

def colorationConstraint(
        coloration: str | list[str] = "", # The ColorationType ENUM
        colorationIncludeType: str = "any", # any/exclude
) -> dict | None:
    if not isinstance(coloration, str | list):
        raise TypeError(f"The coloration must be a string or list of strings, '{type(coloration)}' given.")
    if isinstance(coloration, list) and not all([isinstance(attrib, str) for attrib in coloration]):
        raise TypeError(f"coloration is a list containing a non-string.")
    if not isinstance(colorationIncludeType, str):
        raise TypeError(f"The type must be a string, '{type(colorationIncludeType)}' given.")
    constraint = {}
    allowedTypes = ['any', 'exclude']
    colorationIncludeType = colorationIncludeType.lower()
    if coloration and colorationIncludeType in allowedTypes:
        if isinstance(coloration, str):
            coloration = [coloration]
        constraintName = f"{colorationIncludeType}ColorationTypes"
        constraint[constraintName] = coloration
    return constraint or None

def crazyCreditMatchingConstraint(
        crazyCredit: str | list[str] = "",
        crazyCreditIncludeType: str = "all", # any/all
) -> dict | None:
    if not isinstance(crazyCredit, str | list):
        raise TypeError(f"The crazy credit must be a string or list of strings, '{type(crazyCredit)}' given.")
    if isinstance(crazyCredit, list) and not all([isinstance(attrib, str) for attrib in crazyCredit]):
        raise TypeError(f"crazy credit is a list containing a non-string.")
    if not isinstance(crazyCreditIncludeType, str):
        raise TypeError(f"The type must be a string, '{type(crazyCreditIncludeType)}' given.")
    constraint = {}
    allowedTypes = ['any', 'all']
    crazyCreditIncludeType = crazyCreditIncludeType.lower() 
    if crazyCredit and crazyCreditIncludeType in allowedTypes:
        if isinstance(crazyCredit, str):
            crazyCredit = [crazyCredit]
        constraintName = f"{crazyCreditIncludeType}CrazyCreditTextTerms"
        constraint[constraintName] = crazyCredit
    return constraint or None

def creditedCompanyConstraint(
        companyCategory: str | list[str] = "",
        company: str | list[str] = "",
        companyIncludeType: str = "any", # all/any/exclude
) -> dict | None:
    if not isinstance(companyCategory, str | list):
        raise TypeError(f"The company category must be a string or list of strings, '{type(companyCategory)}' given.")
    if isinstance(companyCategory, list) and not all([isinstance(attrib, str) for attrib in companyCategory]):
        raise TypeError(f"company category is a list containing a non-string.")
    if not isinstance(company, str | list):
        raise TypeError(f"The company must be a string or list of strings, '{type(company)}' given.")
    if isinstance(company, list) and not all([isinstance(attrib, str) for attrib in company]):
        raise TypeError(f"company is a list containing a non-string.")
    if not isinstance(companyIncludeType, str):
        raise TypeError(f"The type must be a string, '{type(companyIncludeType)}' given.")
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

def creditedNameConstraint(
        creditedNameID: str | list[str] = "",
        creditedNameIncludeType: str = "all", # any/all/exclude
) -> dict | None:
    if not isinstance(creditedNameID, str | list):
        raise TypeError(f"The credited name must be a string or list of strings, '{type(creditedNameID)}' given.")
    if isinstance(creditedNameID, list) and not all([isinstance(attrib, str) for attrib in creditedNameID]):
        raise TypeError(f"credited name is a list containing a non-string.")
    if not isinstance(creditedNameIncludeType, str):
        raise TypeError(f"The type must be a string, '{type(creditedNameIncludeType)}' given.")
    constraint = {}
    allowedTypes = ["any", "all", "exclude"]
    creditedNameIncludeType = creditedNameIncludeType.lower()
    if creditedNameID and creditedNameIncludeType in allowedTypes:
        if isinstance(creditedNameID, str):
            creditedNameID = [creditedNameID]
        constraintName = f"{creditedNameIncludeType}NameIds"
        constraint[constraintName] = creditedNameID
    return constraint or None

def currentProductionStatusStageConstraint(
        productionStageID: str | list[str] = "",
        productionStageIncludeType: str = "any", # any/exclude
) -> dict | None:
    if not isinstance(productionStageID, str | list):
        raise TypeError(f"The credited name must be a string or list of strings, '{type(productionStageID)}' given.")
    if isinstance(productionStageID, list) and not all([isinstance(attrib, str) for attrib in productionStageID]):
        raise TypeError(f"credited name is a list containing a non-string.")
    if not isinstance(productionStageIncludeType, str):
        raise TypeError(f"The type must be a string, '{type(productionStageIncludeType)}' given.")
    constraint = {}
    allowedTypes = ["any", "exclude"]
    productionStageIncludeType = productionStageIncludeType.lower()
    if productionStageID and productionStageIncludeType in allowedTypes:
        if isinstance(productionStageID, str):
            productionStageID = [productionStageID]
        constraintName = f"{productionStageIncludeType}ProductionStageIds"
        constraint[constraintName] = productionStageID
    return constraint or None

def deathDateConstraint(
        deathDate: str = "", # The start day or exact day.
        deathDateEnd: str = "", # If both given it is a range.
) -> dict | None:
    if not isinstance(deathDate, str):
        raise TypeError(f"The death date must be a string, '{type(deathDate)}' given.")
    if not isinstance(deathDateEnd, str):
        raise TypeError(f"The death date end must be a string, '{type(deathDateEnd)}' given.")
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

def deathPlaceConstraint(
        deathPlace: str = "",
) -> dict | None:
    if not isinstance(deathPlace, str):
        raise TypeError(f"The death place must be a string, '{type(deathPlace)}' given.")
    constraint = {}
    if deathPlace:
        constraint["deathPlace"] = deathPlace
    return constraint or None

def episodicConstraint(
        seriesID: str | list[str] = "", # Ther ID of the series to use
        seriesIDType: str = "any", # any/exclude # Limit to them matching.
        season: str | list[str] = "", # The season numbers to use.
        episode: str | list[str] = "", # The episode numbers to use.
        seasonEpisodeType: str = "any", # any/exclude # Limit to them matching.
) -> dict | None:
    if not isinstance(seriesID, str | list):
        raise TypeError(f"The series ID must be a string or list of strings, '{type(seriesID)}' given.")
    if isinstance(seriesID, list) and not all([isinstance(attrib, str) for attrib in seriesID]):
        raise TypeError(f"Series ID is a list containing a non-string.")
    if not isinstance(season, str | list):
        raise TypeError(f"The season must be a string or list of strings, '{type(season)}' given.")
    if isinstance(season, list) and not all([isinstance(attrib, str) for attrib in season]):
        raise TypeError(f"Seeason is a list containing a non-string.")
    if not isinstance(episode, str | list):
        raise TypeError(f"The episode must be a string or list of strings, '{type(episode)}' given.")
    if isinstance(episode, list) and not all([isinstance(attrib, str) for attrib in episode]):
        raise TypeError(f"Episode is a list containing a non-string.")
    if not isinstance(seriesIDType, str):
        raise TypeError(f"The series type must be a string, '{type(seriesIDType)}' given.")
    if not isinstance(seasonEpisodeType, str):
        raise TypeError(f"The episode type must be a string, '{type(seasonEpisodeType)}' given.")
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

def explicitContentConstraint(
        explicit: str = "INCLUDE_ADULT", # ExplicitContentFilter ENUM
) -> dict | None:
    if not isinstance(explicit, str):
        raise TypeError(f"The explicit filter must be a string, '{type(explicit)}' given.")
    constraint = {}
    explicit = explicit.upper()
    explicit = explicit.removesuffix("_ADULT") + "_ADULT"
    allowedTypes = ["EXCLUDE_ADULT", "INCLUDE_ADULT", "ONLY_ADULT"]
    if explicit in allowedTypes:
        constraint["explicitContentFilter"] = explicit
    return constraint or None

def filmingLocationConstraint(
        filmingLocation: str | list[str] = "", # The filming location
        filmingLocationType: str = "any", # any/all
) -> dict | None:
    if not isinstance(filmingLocation, str | list):
        raise TypeError(f"The location must be a string or list of strings, '{type(filmingLocation)}' given.")
    if isinstance(filmingLocation, list) and not all([isinstance(attrib, str) for attrib in filmingLocation]):
        raise TypeError(f"Location is a list containing a non-string.")
    if not isinstance(filmingLocationType, str):
        raise TypeError(f"The type must be a string, '{type(filmingLocationType)}' given.")
    constraint = {}
    allowedTypes = ["any", "all"]
    filmingLocationType = filmingLocationType.lower()
    if filmingLocation and filmingLocationType in allowedTypes:
        if isinstance(filmingLocation, str):
                filmingLocation = [filmingLocation]
        constraintName = f"{filmingLocationType}Locations"
        constraint[constraintName] = filmingLocation
    return constraint or None

def filmographyConstraint(
        filmographyTitleID: str | list[str] = "",
        filmographyTitleIDType: str = "all", # all/any/exclude
        filmographyTitleIDExclude: str | list[str] = "", # If type is also exclude it will use this one.
) -> dict | None:
    if not isinstance(filmographyTitleID, str | list):
        raise TypeError(f"The title ID must be a string or list of strings, '{type(filmographyTitleID)}' given.")
    if isinstance(filmographyTitleID, list) and not all([isinstance(attrib, str) for attrib in filmographyTitleID]):
        raise TypeError(f"Title ID is a list containing a non-string.")
    if not isinstance(filmographyTitleIDType, str):
        raise TypeError(f"The type must be a string, '{type(filmographyTitleIDType)}' given.")
    if not isinstance(filmographyTitleIDExclude, str | list):
        raise TypeError(f"The title ID (exclude) must be a string or list of strings, '{type(filmographyTitleIDExclude)}' given.")
    if isinstance(filmographyTitleIDExclude, list) and not all([isinstance(attrib, str) for attrib in filmographyTitleIDExclude]):
        raise TypeError(f"Title ID (exclude) is a list containing a non-string.")
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

def genderIdentityConstraint(
        gender: str | list[str] = "",
        genderType: str = "any",
) -> dict | None:
    if not isinstance(gender, str | list):
        raise TypeError(f"The gender must be a string or list of strings, '{type(gender)}' given.")
    if isinstance(gender, list) and not all([isinstance(attrib, str) for attrib in gender]):
        raise TypeError(f"Gender is a list containing a non-string.")
    if not isinstance(genderType, str):
        raise TypeError(f"The type must be a string, '{type(genderType)}' given.")
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

def genreConstraint(
        genre: str | list[str] = "", # The genre
        genreType: str = "all", # all/any/exclude
        genreMaxRelevant: int | None = None,
) -> dict | None:
    if not isinstance(genre, str | list):
        raise TypeError(f"The genre must be a string or list of strings, '{type(genre)}' given.")
    if isinstance(genre, list) and not all([isinstance(attrib, str) for attrib in genre]):
        raise TypeError(f"genre is a list containing a non-string.")
    if not isinstance(genreType, str):
        raise TypeError(f"The type must be a string, '{type(genreType)}' given.")
    if not isinstance(genreMaxRelevant, int | None):
        raise TypeError(f"The max relevant must be an int or None, '{type(genreMaxRelevant)}' given.")
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

def goofMatchingConstraint(
        goof: str | list[str] = "", # the text to search for
        goofType: str = "all", # all/any
) -> dict | None:
    if not isinstance(goof, str | list):
        raise TypeError(f"The goof must be a string or list of strings, '{type(goof)}' given.")
    if isinstance(goof, list) and not all([isinstance(attrib, str) for attrib in goof]):
        raise TypeError(f"goof is a list containing a non-string.")
    if not isinstance(goofType, str):
        raise TypeError(f"The type must be a string, '{type(goofType)}' given.")
    constraint = {}
    allowedTypes = ["any", "all"]
    goofType = goofType.lower()
    if goof and goofType in allowedTypes:
        if isinstance(goof, str):
            goof = [goof]
        constraintName = f"{goofType}GoofTextTerms"
        constraint[constraintName] = goof
    return constraint or None

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
    if not isinstance(theaterID, str | list):
        raise TypeError(f"The theater ID must be a string or list of strings, '{type(theaterID)}' given.")
    if isinstance(theaterID, list) and not all([isinstance(attrib, str) for attrib in theaterID]):
        raise TypeError(f"Theater ID is a list containing a non-string.")
    if not isinstance(theaterStart, str):
        raise TypeError(f"The start must be a string (ISO-8601 date), '{type(theaterStart)}' given.")
    if not isinstance(theaterEnd, str):
        raise TypeError(f"The end must be a string (ISO-8601 date), '{type(theaterEnd)}' given.")
    if theaterEnd and not theaterStart:
        raise ValueError(f"You must have a start if you have an end date.")
    allowedDictKeys: set[str] = {"lat", "long"}
    if not isinstance(theaterLocationLatLong, dict):
        raise TypeError(f"The latitude and longitude must be a dict containing {allowedDictKeys} as floats, '{type(theaterLocationLatLong)}' given.")
    if isinstance(theaterLocationLatLong, dict):
        if any([key not in allowedDictKeys for key in theaterLocationLatLong.keys()]):
            raise ValueError(f"Certificate contained more keys than allowed, {allowedDictKeys}.")
        for a in allowedDictKeys:
            if not isinstance(theaterLocationLatLong.get(a), float | None):
                raise TypeError(f"Latitude and Longitude must be floats for the keys: {allowedDictKeys}")
    if theaterStart and not re.fullmatch(r'\d{4}-\d{2}-\d{2}', theaterStart):
        raise ValueError(f"The start date is not of the correct form, yy-mm-dd")
    if theaterEnd and not re.fullmatch(r'\d{4}-\d{2}-\d{2}', theaterEnd):
        raise ValueError(f"The end date is not of the correct form, yy-mm-dd")
    lat = theaterLocationLatLong.get("lat")
    long = theaterLocationLatLong.get("long")
    if (bool(lat) ^ bool(long)):
        raise ValueError(f"Either both latitude and longitude are passed or none.")
    if not isinstance(theaterLocation, str):
        raise TypeError(f"The location must be a string (postal code), '{type(theaterLocation)}' given.")
    if not isinstance(theaterLocationRadius, int):
        raise TypeError(f"The radius must be an int (in meters), '{type(theaterLocationRadius)}' given.")
    if theaterLocationRadius < 1:
        raise ValueError(f"The radius must be a positive integer {theaterLocationRadius}")
    if not isinstance(theaterFavorite, bool):
        raise TypeError(f"The favorite flag must be a bool, '{type(theaterFavorite)}' given.")
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

def interestConstraint(
        interestID: str | list[str] = "",
        interestType: str = "all", # all/any/exclude
) -> dict | None:
    if not isinstance(interestID, str | list):
        raise TypeError(f"The interest ID must be a string or list of strings, '{type(interestID)}' given.")
    if isinstance(interestID, list) and not all([isinstance(attrib, str) for attrib in interestID]):
        raise TypeError(f"interest ID is a list containing a non-string.")
    if not isinstance(interestType, str):
        raise TypeError(f"The type must be a string, '{type(interestType)}' given.")
    constraint = {}
    allowedTypes = ['any', 'all', 'exclude']
    interestType = interestType.lower() 
    if interestID and interestType in allowedTypes:
        if isinstance(interestID, str):
            interestID = [interestID]
            constraintName = f"{interestType}InterestIds"
            constraint[constraintName] = interestID
    return constraint or None

def keywordConstraint(
        keyword: str | list[str] = "",
        keywordType: str = "all", # all/any/exclude
) -> dict | None:
    if not isinstance(keyword, str | list):
        raise TypeError(f"The keyword must be a string or list of strings, '{type(keyword)}' given.")
    if isinstance(keyword, list) and not all([isinstance(attrib, str) for attrib in keyword]):
        raise TypeError(f"keyword is a list containing a non-string.")
    if not isinstance(keywordType, str):
        raise TypeError(f"The type must be a string, '{type(keywordType)}' given.")
    constraint = {}
    allowedTypes = ['any', 'all', 'exclude']
    keywordType = keywordType.lower()
    if keyword and keywordType in allowedTypes:
        if isinstance(keyword, str):
            keyword = [keyword]
        constraintName = f"{keywordType}Keywords"
        constraint[constraintName] = keyword
    return constraint or None

def languageConstraint(
        language: str | list[str] = "",
        languageType: str = "any", # all/any/exclude
        languagePrimary: str | list[str] = "",
        languagePrimaryType: str = "any", # any/exclude
        silent: bool | None = None, # Silent
) -> dict | None:
    if not isinstance(language, str | list):
        raise TypeError(f"The language must be a string or list of strings, '{type(language)}' given.")
    if isinstance(language, list) and not all([isinstance(attrib, str) for attrib in language]):
        raise TypeError(f"language is a list containing a non-string.")
    if not isinstance(languageType, str):
        raise TypeError(f"The type must be a string, '{type(languageType)}' given.")
    if not isinstance(languagePrimary, str | list):
        raise TypeError(f"The primary language must be a string or list of strings, '{type(languagePrimary)}' given.")
    if isinstance(languagePrimary, list) and not all([isinstance(attrib, str) for attrib in languagePrimary]):
        raise TypeError(f"Primary language is a list containing a non-string.")
    if not isinstance(languagePrimaryType, str):
        raise TypeError(f"The primary type must be a string, '{type(languagePrimaryType)}' given.")
    if not isinstance(silent, bool | None):
        raise TypeError(f"The silent flag must be a bool or None, '{type(silent)}' given.")
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

def listConstraint(
        inList: str | list[str] = "",
        inPredefinedList: str | list[str] = "", # ListClassId ENUM
        notInList: str | list[str] = "", # always an any
        notInPredefinedList: str | list[str] = "", # always an any
        inListType: str = "any", # all/any
        inPredefinedListType: str = "any", # all/any
) -> dict | None:
    if not isinstance(inList, str | list):
        raise TypeError(f"The list must be a string or list of strings, '{type(inList)}' given.")
    if isinstance(inList, list) and not all([isinstance(attrib, str) for attrib in inList]):
        raise TypeError(f"list is a list containing a non-string.")
    if not isinstance(inListType, str):
        raise TypeError(f"The type must be a string, '{type(inListType)}' given.")
    if not isinstance(inPredefinedList, str | list):
        raise TypeError(f"The pre-defined list must be a string or list of strings, '{type(inPredefinedList)}' given.")
    if isinstance(inPredefinedList, list) and not all([isinstance(attrib, str) for attrib in inPredefinedList]):
        raise TypeError(f"Pre-defined list is a list containing a non-string.")
    if not isinstance(inPredefinedListType, str):
        raise TypeError(f"The pre-defined list type must be a string, '{type(inPredefinedListType)}' given.")
    if not isinstance(notInPredefinedList, str | list):
        raise TypeError(f"The pre-defined (not in) list must be a string or list of strings, '{type(notInPredefinedList)}' given.")
    if isinstance(notInPredefinedList, list) and not all([isinstance(attrib, str) for attrib in notInPredefinedList]):
        raise TypeError(f"Pre-defined list (not in) is a list containing a non-string.")
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

def myRatingConstraint(
        myRatingType: str = "INCLUDE", # MyRatingSearchFilterType ENUM
        myRatingMin: int | None = None,
        myRatingMax: int | None = None,
):
    if not isinstance(myRatingType, str):
        raise TypeError(f"The type must be a string, '{type(myRatingType)}' given.")
    if not isinstance(myRatingMin, int | None):
        raise TypeError(f"The min must be an int (or None), '{type(myRatingMin)}' given.")
    if not isinstance(myRatingMax, int | None):
        raise TypeError(f"The min must be an int (or None), '{type(myRatingMax)}' given.")
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

def originCountryConstraint(
        originCountry: str | list[str] = "",
        originCountryType: str = "all", # all/any/exclude
        originPrimaryCountry: str | list[str] = "",
        originPrimaryCountryType: str = "any", # any/exclude
):
    if not isinstance(originCountry, str | list):
        raise TypeError(f"The country must be a string or list of strings, '{type(originCountry)}' given.")
    if isinstance(originCountry, list) and not all([isinstance(attrib, str) for attrib in originCountry]):
        raise TypeError(f"country is a list containing a non-string.")
    if not isinstance(originCountryType, str):
        raise TypeError(f"The type must be a string, '{type(originCountryType)}' given.")
    if not isinstance(originPrimaryCountry, str | list):
        raise TypeError(f"The primary country must be a string or list of strings, '{type(originPrimaryCountry)}' given.")
    if isinstance(originPrimaryCountry, list) and not all([isinstance(attrib, str) for attrib in originPrimaryCountry]):
        raise TypeError(f"Primary country is a list containing a non-string.")
    if not isinstance(originPrimaryCountryType, str):
        raise TypeError(f"The primary type must be a string, '{type(originPrimaryCountryType)}' given.")
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

def plotMatchingConstraint(
        plotText: str | list[str] = "",
        plotTextType: str = "all", #all/any
        plotAuthor: str | list[str] = "",
) -> dict | None:
    if not isinstance(plotText, str | list):
        raise TypeError(f"The plot must be a string or list of strings, '{type(plotText)}' given.")
    if isinstance(plotText, list) and not all([isinstance(attrib, str) for attrib in plotText]):
        raise TypeError(f"Plot is a list containing a non-string.")
    if not isinstance(plotTextType, str):
        raise TypeError(f"The type must be a string, '{type(plotTextType)}' given.")
    if not isinstance(plotAuthor, str | list):
        raise TypeError(f"The plot author must be a string or list of strings, '{type(plotAuthor)}' given.")
    if isinstance(plotAuthor, list) and not all([isinstance(attrib, str) for attrib in plotAuthor]):
        raise TypeError(f"Plot author is a list containing a non-string.")
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

def professionConstraint(
        profession: str | list[str] = "",
        professionType: str = "any",
        professionExclude: str | list[str] = "", # If type is set to exclude this overrids the above.
) -> dict | None:
    if not isinstance(profession, str | list):
        raise TypeError(f"The profession must be a string or list of strings, '{type(profession)}' given.")
    if isinstance(profession, list) and not all([isinstance(attrib, str) for attrib in profession]):
        raise TypeError(f"profession is a list containing a non-string.")
    if not isinstance(professionType, str):
        raise TypeError(f"The type must be a string, '{type(professionType)}' given.")
    if not isinstance(professionExclude, str | list):
        raise TypeError(f"The profession exclude must be a string or list of strings, '{type(professionExclude)}' given.")
    if isinstance(professionExclude, list) and not all([isinstance(attrib, str) for attrib in professionExclude]):
        raise TypeError(f"profession exclude is a list containing a non-string.")
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

def professionCategoryConstraint(
        professionCategory: str | list[str] = "",
        professionCategoryType: str = "any",
        professionCategoryExclude: str | list[str] = "", # If type is set to exclude this overrids the above.
) -> dict | None:
    if not isinstance(professionCategory, str | list):
        raise TypeError(f"The profession category must be a string or list of strings, '{type(professionCategory)}' given.")
    if isinstance(professionCategory, list) and not all([isinstance(attrib, str) for attrib in professionCategory]):
        raise TypeError(f"profession category is a list containing a non-string.")
    if not isinstance(professionCategoryType, str):
        raise TypeError(f"The type must be a string, '{type(professionCategoryType)}' given.")
    if not isinstance(professionCategoryExclude, str | list):
        raise TypeError(f"The profession category must be a string or list of strings, '{type(professionCategoryExclude)}' given.")
    if isinstance(professionCategoryExclude, list) and not all([isinstance(attrib, str) for attrib in professionCategoryExclude]):
        raise TypeError(f"profession exclude category is a list containing a non-string.")
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

def quoteMatchingConstraint(
        quote: str | list[str] = "",
        quoteType: str = "all", # all/any
) -> dict | None:
    if not isinstance(quote, str | list):
        raise TypeError(f"The quote must be a string or list of strings, '{type(quote)}' given.")
    if isinstance(quote, list) and not all([isinstance(attrib, str) for attrib in quote]):
        raise TypeError(f"quote is a list containing a non-string.")
    if not isinstance(quoteType, str):
        raise TypeError(f"The type must be a string, '{type(quoteType)}' given.")
    constraint = {}
    allowedTypes = ['all', 'any']
    quoteType = quoteType.lower()
    if quote and quoteType in allowedTypes:
        if isinstance(quote, str):
            quote = [quote]
        constraintName = f"{quoteType}QuoteTextTerms"
        constraint[constraintName] = quote
    return constraint or None

def rankedTitleListConstraint(
        rankedTitleMin: int | None = None,
        rankedTitleMax: int | None = None,
        rankedTitleListType: str = "TITLE_METER", # RankedTitleListType ENUM
        rankedTitleType: str = "all", # all/exclude
) -> dict | None:
    if not isinstance(rankedTitleMin, int | None):
        raise TypeError(f"The min must be an int or None, '{type(rankedTitleMin)}' given.")
    if not isinstance(rankedTitleMax, int | None):
        raise TypeError(f"The max must be an int or None, '{type(rankedTitleMax)}' given.")
    if not isinstance(rankedTitleListType, str):
        raise TypeError(f"The list type must be a string, '{type(rankedTitleListType)}' given.")
    if not isinstance(rankedTitleType, str):
        raise TypeError(f"The type must be a string, '{type(rankedTitleType)}' given.")
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

def releaseDateConstraint(
        year: int = 0,
        yearEnd: int = 0,
        dateStart: str = "", # yyyy-mm-dd
        dateEnd: str = "", # yyyy-mm-dd
) -> dict | None:
    if not isinstance(year, int):
        raise TypeError(f"The year must be an int, '{type(year)}' given.")
    if not isinstance(yearEnd, int):
        raise TypeError(f"The end year must be an int, '{type(yearEnd)}' given.")
    if not isinstance(dateStart, str):
        raise TypeError(f"The start date type must be a string, '{type(dateStart)}' given.")
    if not isinstance(dateEnd, str):
        raise TypeError(f"The end date type must be a string, '{type(dateEnd)}' given.")
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

def runtimeConstraint(
        runtimeMin: int = 0, # In minutes
        runtimeMax: int = 0,
) -> dict | None:
    if not isinstance(runtimeMin, int):
        raise TypeError(f"The min must be an int, '{type(year)}' given.")
    if not isinstance(runtimeMax, int):
        raise TypeError(f"The max must be an int, '{type(year)}' given.")
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

def singleUserRatingConstraint(
        ratingUserID: str = "",
        ratingUserRangeMin: int = 0,
        ratingUserRangeMax: int = 0,
        ratingUserType: str = "INCLUDE", # SingleUserRatingSearchFilterType ENUM
) -> dict | None:
    if not isinstance(ratingUserID, str):
        raise TypeError(f"The user ID must be a string, '{type(ratingUserID)}' given.")
    if not isinstance(ratingUserType, str):
        raise TypeError(f"The type must be a string, '{type(ratingUserType)}' given.")
    if not isinstance(ratingUserRangeMin, int):
        raise TypeError(f"The min must be an int, '{type(ratingUserRangeMin)}' given.")
    if not isinstance(ratingUserRangeMax, int):
        raise TypeError(f"The max must be an int, '{type(ratingUserRangeMax)}' given.")
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

def soundMixConstraint(
        soundMix: str | list[str] = "",
        soundMixExclude: str | list[str] = "",
) -> dict | None:
    if not isinstance(soundMix, str | list):
        raise TypeError(f"The sound mix must be a string or list of strings, '{type(soundMix)}' given.")
    if isinstance(soundMix, list) and not all([isinstance(attrib, str) for attrib in soundMix]):
        raise TypeError(f"Sound mix is a list containing a non-string.")
    if not isinstance(soundMixExclude, str | list):
        raise TypeError(f"The sound mix (exclude) must be a string or list of strings, '{type(soundMixExclude)}' given.")
    if isinstance(soundMixExclude, list) and not all([isinstance(attrib, str) for attrib in soundMixExclude]):
        raise TypeError(f"Sound mix (exclude) is a list containing a non-string.")
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

def soundtrackMatchingConstraint(
        soundtrackTerms: str | list[str] = "",
        soundtrackTermsType: str = "all", # all/any
) -> dict | None:
    if not isinstance(soundtrackTerms, str | list):
        raise TypeError(f"The sound track terms must be a string or list of strings, '{type(soundtrackTerms)}' given.")
    if isinstance(soundtrackTerms, list) and not all([isinstance(attrib, str) for attrib in soundtrackTerms]):
        raise TypeError(f"Sound track terms is a list containing a non-string.")
    if not isinstance(soundtrackTermsType, str):
        raise TypeError(f"The type must be a string, '{type(soundtrackTermsType)}' given.")
    constraint = {}
    allowedTypes = ['all', 'any']
    soundtrackTermsType = soundtrackTermsType.lower()
    if soundtrackTerms and soundtrackTermsType in allowedTypes:
        if isinstance(soundtrackTerms, str):
            soundtrackTerms = [soundtrackTerms]
        constraintName = f"{soundtrackTermsType}SoundtrackTextTerms"
        constraint[constraintName] = soundtrackTerms
    return constraint or None

def textSearchConstraint(
        search: str = "",
) -> dict | None:
    if not isinstance(search, str):
        raise TypeError(f"The search must be a string, '{type(search)}' given.")
    constraint = {}
    if search:
        constraint = {
            'searchTerm': search
        }
    return constraint or None

def titleCreditsConstraint(
        creditCharacter: str | list[str] = "",
        creditCategory: str | list[str] = "",
        creditJobCategory: str | list[str] = "",
        creditNameID: str | list[str] = "",
        creditType: str = "all",
        creditAdvanced: dict = {},
) -> dict | None:
    if not isinstance(creditCharacter, str | list):
        raise TypeError(f"The character must be a string or list of strings, '{type(creditCharacter)}' given.")
    if isinstance(creditCharacter, list) and not all([isinstance(attrib, str) for attrib in creditCharacter]):
        raise TypeError(f"character is a list containing a non-string.")
    if not isinstance(creditCategory, str | list):
        raise TypeError(f"The credit category must be a string or list of strings, '{type(creditCategory)}' given.")
    if isinstance(creditCategory, list) and not all([isinstance(attrib, str) for attrib in creditCategory]):
        raise TypeError(f"credit category is a list containing a non-string.")
    if not isinstance(creditJobCategory, str | list):
        raise TypeError(f"The credit job category must be a string or list of strings, '{type(creditJobCategory)}' given.")
    if isinstance(creditJobCategory, list) and not all([isinstance(attrib, str) for attrib in creditJobCategory]):
        raise TypeError(f"credit job category is a list containing a non-string.")
    if not isinstance(creditNameID, str | list):
        raise TypeError(f"The name ID must be a string or list of strings, '{type(creditNameID)}' given.")
    if isinstance(creditNameID, list) and not all([isinstance(attrib, str) for attrib in creditNameID]):
        raise TypeError(f"Name ID is a list containing a non-string.")
    if not isinstance(creditType, str):
        raise TypeError(f"The type must be a string, '{type(creditType)}' given.")
    # TODO: Validate the keys/values, this is not a general use arg.
    if not isinstance(creditAdvanced, dict):
        raise TypeError(f"The advanced credit filter must be a dict, '{type(creditAdvanced)}' given.")
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

def titleMeterConstraint(
        meterMin: int = 0,
        meterMax: int = 0,
        meterType: str = "TITLE_METER", # TitleMeterType ENUM
) -> dict | None:
    if not isinstance(meterMin, int):
        raise TypeError(f"The min must be an int, '{type(meterMin)}' given.")
    if not isinstance(meterMax, int):
        raise TypeError(f"The max must be an int, '{type(meterMax)}' given.")
    if not isinstance(meterType, str):
        raise TypeError(f"The type must be a string, '{type(meterType)}' given.")
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

def titleTypeConstraint(
        titleType: str | list[str] = "",
        titleTypeExclude: str | list[str] = "",
) -> dict | None:
    if not isinstance(titleType, str | list):
        raise TypeError(f"The type must be a string or list of strings, '{type(titleType)}' given.")
    if isinstance(titleType, list) and not all([isinstance(attrib, str) for attrib in titleType]):
        raise TypeError(f"Type is a list containing a non-string.")
    if not isinstance(titleTypeExclude, str | list):
        raise TypeError(f"The exclude type must be a string or list of strings, '{type(titleTypeExclude)}' given.")
    if isinstance(titleTypeExclude, list) and not all([isinstance(attrib, str) for attrib in titleTypeExclude]):
        raise TypeError(f"Exclude type is a list containing a non-string.")
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

def triviaMatchingConstraint(
        triviaTerm: str | list[str] = "",
        triviaTermType: str = "all", # all/any
) -> dict | None:
    if not isinstance(triviaTerm, str | list):
        raise TypeError(f"The trivia term must be a string or list of strings, '{type(triviaTerm)}' given.")
    if isinstance(triviaTerm, list) and not all([isinstance(attrib, str) for attrib in triviaTerm]):
        raise TypeError(f"Trivia term is a list containing a non-string.")
    if not isinstance(triviaTermType, str):
        raise TypeError(f"The type must be a string, '{type(triviaTermType)}' given.")
    constraint = {}
    triviaTermType = triviaTermType.lower()
    allowedTypes = ['all', 'any']
    if triviaTerm and triviaTermType in allowedTypes:
        if isinstance(triviaTerm, str):
            triviaTerm = [triviaTerm]
        constraintName = f"{triviaTermType}TriviaTextTerms"
        constraint[constraintName] = triviaTerm
    return constraint or None

def userRatingsConstraint(
        ratingMin: float = 0.0,
        ratingMax: float = 0.0,
        ratingCountMin: int = 0,
        ratingCountMax: int = 0,
) -> dict | None:
    if not isinstance(ratingMin, float):
        raise TypeError(f"The min must be a float, '{type(ratingMin)}' given.")
    if not isinstance(ratingMax, float):
        raise TypeError(f"The max must be a float, '{type(ratingMax)}' given.")
    if not isinstance(ratingCountMin, int):
        raise TypeError(f"The rating count min must be an int, '{type(ratingCountMin)}' given.")
    if not isinstance(ratingCountMax, int):
        raise TypeError(f"The rating count max must be an int, '{type(ratingMax)}' given.")
    if ratingMin and ratingMax and ratingMin > ratingMax:
        raise TypeError(f"The min cannot be larger than the max, min:{ratingMin} > max:{ratingMax}")
    if ratingMin < 0 or ratingMax < 0:
        raise TypeError(f"The min and max must be positive, min:{ratingMin} and max:{ratingMax}")
    if ratingMin > 10 or ratingMax > 10:
        raise TypeError(f"The min and max can be at most 10, min:{ratingMin} and max:{ratingMax}")
    if ratingCountMin and ratingCountMax and ratingCountMin > ratingCountMax:
        raise TypeError(f"The rating count min cannot be larger than the max, min:{ratingCountMin} > max:{ratingCountMax}")
    if ratingCountMin < 0 or ratingCountMax < 0:
        raise TypeError(f"The rating count min and max must be positive, min:{ratingCountMin} and max:{ratingCountMax}")
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

def watchOptionsConstraint(
        watchProviderID: str | list[str] = "",
        watchRegion: str | list[str] = "",
        watchProviderIDExclude: str | list[str] = "",
        watchRegionExclude: str | list[str] = "",
        watchType: str | list[str] = "", # SearchWatchOptionType ENUM
) -> dict | None:
    if not isinstance(watchProviderID, str | list):
        raise TypeError(f"The provider ID must be a string or list of strings, '{type(watchProviderID)}' given.")
    if isinstance(watchProviderID, list) and not all([isinstance(attrib, str) for attrib in watchProviderID]):
        raise TypeError(f"Provider ID is a list containing a non-string.")
    if not isinstance(watchRegion, str | list):
        raise TypeError(f"The region must be a string or list of strings, '{type(watchRegion)}' given.")
    if isinstance(watchRegion, list) and not all([isinstance(attrib, str) for attrib in watchRegion]):
        raise TypeError(f"Region is a list containing a non-string.")
    if not isinstance(watchProviderIDExclude, str | list):
        raise TypeError(f"The provider exclude must be a string or list of strings, '{type(watchProviderIDExclude)}' given.")
    if isinstance(watchProviderIDExclude, list) and not all([isinstance(attrib, str) for attrib in watchProviderIDExclude]):
        raise TypeError(f"Provider exclude is a list containing a non-string.")
    if not isinstance(watchRegionExclude, str | list):
        raise TypeError(f"The region exclude must be a string or list of strings, '{type(watchRegionExclude)}' given.")
    if isinstance(watchRegionExclude, list) and not all([isinstance(attrib, str) for attrib in watchRegionExclude]):
        raise TypeError(f"Region exclude is a list containing a non-string.")
    if not isinstance(watchType, str | list):
        raise TypeError(f"The watch type must be a string or list of strings, '{type(watchType)}' given.")
    if isinstance(watchType, list) and not all([isinstance(attrib, str) for attrib in watchType]):
        raise TypeError(f"Watch type is a list containing a non-string.")
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

def withDataConstraint(
        withData: str | list[str] = "",  # respective (DataType)DataType ENUMs
        withDataMissing: str | list[str] = "",
        withDataAny: str | list[str] = "",
) -> dict | None:
    if not isinstance(withData, str | list):
        raise TypeError(f"The with data must be a string or list of strings, '{type(withData)}' given.")
    if isinstance(withData, list) and not all([isinstance(attrib, str) for attrib in withData]):
        raise TypeError(f"With data is a list containing a non-string.")
    if not isinstance(withDataMissing, str | list):
        raise TypeError(f"The missing data must be a string or list of strings, '{type(withDataMissing)}' given.")
    if isinstance(withDataMissing, list) and not all([isinstance(attrib, str) for attrib in withDataMissing]):
        raise TypeError(f"Missing data is a list containing a non-string.")
    if not isinstance(withDataAny, str | list):
        raise TypeError(f"The any data must be a string or list of strings, '{type(withDataAny)}' given.")
    if isinstance(withDataAny, list) and not all([isinstance(attrib, str) for attrib in withDataAny]):
        raise TypeError(f"Any data is a list containing a non-string.")
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
