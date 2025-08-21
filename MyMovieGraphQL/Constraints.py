from typing import Any
# Each constraint should return a base search dict or none
# for that constraint with the given args used to fill it out.
# TODO: Add type checking
# TODO: Add value validation, ENUMs should check agaist the `ENUM.json``

def _getFromListIfExists(l: list, idx: int) -> Any | None:
    try:
        return l[idx]
    except IndexError:
        return None


def alternateVersionMatchingConstraint(
        alternateVersion: str | list = "",
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
        award: str | list = "",  # The award ID
        awardIncludeType: str = "any", # any/all/exclude
) -> dict | None:
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
        biographyAuthor: str | list = "",
        biographyText: str = "",
) -> dict | None:
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
    constraint = {}
    if birthPlace:
        constraint["birthPlace"] = birthPlace
    return constraint or None

def certificateConstraint(
        certificate: dict | list = "",  # {rating: xxx, region: xxx}
        certificateIncludeType: str = "any", # any/exclude
) -> dict | None:
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
        character: str | list = "",
        creditedCharacters: bool = True,  # Limit to only credited roles.
) -> dict | None:
    constraint = {}
    if character:
        if isinstance(character, str):
            character = [character]
        constraint["anyCharacterNames"] = character
        constraint["shouldLimitToCreditedNameIds"] = creditedCharacters
    return constraint or None

def colorationConstraint(
        coloration: str | list = "", # The ColorationType ENUM
        colorationIncludeType: str = "any", # any/exclude
) -> dict | None:
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
        crazyCredit: str = "",
        crazyCreditIncludeType: str = "all", # any/all
) -> dict | None:
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
        companyCategory: str | list = "",
        company: str | list = "",
        companyIncludeType: str = "any", # all/any/exclude
) -> dict | None:
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
        creditedNameID: str | list = "",
        creditedNameIncludeType: str = "all", # any/all/exclude
) -> dict | None:
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
        productionStageID: str | list = "",
        productionStageIncludeType: str = "any", # any/exclude
) -> dict | None:
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
    constraint = {}
    if deathPlace:
        constraint["deathPlace"] = deathPlace
    return constraint or None

def episodicConstraint(
        seriesID: str | list = "", # Ther ID of the series to use
        seriesIDType: str = "any", # any/exclude # Limit to them matching.
        season: str | list = "", # The season numbers to use.
        episode: str | list = "", # The episode numbers to use.
        seasonEpisodeType: str = "any", # any/exclude # Limit to them matching.
) -> dict | None:
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
) -> str | None:
    constraint = {}
    explicit = explicit.upper()
    explicit = explicit.removesuffix("_ADULT") + "_ADULT"
    allowedTypes = ["EXCLUDE_ADULT", "INCLUDE_ADULT", "ONLY_ADULT"]
    if explicit in allowedTypes:
        constraint["explicitContentFilter"] = explicit
    return constraint or None

def filmingLocationConstraint(
        filmingLocation: str | list = "", # The filming location
        filmingLocationType: str = "any", # any/all
) -> dict | None:
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
        filmographyTitleID: str | list = "",
        filmographyTitleIDType: str = "all", # all/any/exclude
        filmographyTitleIDExclude: str | list = "", # If type is also exclude it will use this one.
) -> dict | None:
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
        gender: str | list = "",
        genderType: str = "any",
) -> dict | None:
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
        genre: str | list = "", # The genre
        genreType: str = "all", # all/any/exclude
        genreMaxRelevant: int | None = None,
) -> dict | None:
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
        goof: str | list = "", # the text to search for
        goofType: str = "all", # all/any
) -> dict | None:
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
        theaterID: str | list = "", # The theater IDs
        theaterAttribute: str | list = "", # SearchTheaterAttribute ENUM.
        theaterStart: str = "", # ISO-8601 format
        theaterEnd: str = "", # The showtime dates, must have at least start
        theaterLocation: str = "", # The postal code 
        theaterLocationLatLong: dict = {}, # {lat: float, long: float}
        theaterLocationRadius: int = 50, # In meters, default 50m
        theaterFavorite: bool = False, # Wehn true: MyFavoriteTheaterSearchFilter ENUM
) -> dict | None:
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
            "postalCode": postalCode or None,
            "latLong": theaterLocationLatLong or None,
            "radiusInMeters": radiusInMeters or None,
        }
    if theaterFavorite:
        constraint["myFavoriteTheaters"] = "ONLY_MY_FAVORITE"
    return constraint or None

def interestConstraint(
        interestID: str | list = "",
        interestType: str = "all", # all/any/exclude
) -> dict | None:
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
        keyword: str | list = "",
        keywordType: str = "all", # all/any/exclude
) -> dict | None:
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
        language: str | list = "",
        languageType: str = "any", # all/any/exclude
        languagePrimary: str | list = "",
        languagePrimaryType: str = "any", # any/exclude
        silent: bool | None = None, # Silent
) -> dict | None:
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
        inList: str | list = "",
        inPredefinedList: str | list = "", # ListClassId ENUM
        notInList: str | list = "", # always an any
        notInPredefinedList: str | list = "", # always an any
        inListType: str = "any", # all/any
        inPredefinedListType: str = "any", # all/any
) -> dict | None:
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
        originCountry: str | list = "",
        originCountryType: str = "all", # all/any/exclude
        originPrimaryCountry: str | list = "",
        originPrimaryCountryType: str = "any", # any/exclude
):
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
        plotText: str | list = "",
        plotTextType: str = "all", #all/any
        plotAuthor: str | list = "",
) -> dict | None:
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
        profession: str | list = "",
        professionType: str = "any",
        professionExclude: str | list = "", # If type is set to exclude this overrids the above.
) -> dict | None:
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
        professionCategory: str | list = "",
        professionCategoryType: str = "any",
        professionCategoryExclude: str | list = "", # If type is set to exclude this overrids the above.
) -> dict | None:
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
        quote: str | list = "",
        quoteType: str = "all", # all/any
) -> dict | None:
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
        soundMix: str | list = "",
        soundMixExclude: str | list = "",
) -> dict or None:
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
        soundtrackTerms: str | list = "",
        soundtrackTermsType: str = "all", # all/any
) -> dict | None:
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
    constraint = {}
    if search:
        constraint = {
            'searchTerm': search
        }
    return constraint or None

def titleCreditsConstraint(
        creditCharacter: str | list = "",
        creditCategory: str | list = "",
        creditJobCategory: str | list = "",
        creditNameID: str | list = "",
        creditType: str | list = "all",
        creditAdvanced: dict = {},
) -> dict | None:
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
                        "character": _getFromListIfExists(creditCharacter, i),
                        "creditCategory": _getFromListIfExists(creditCategory, i),
                        "jobCategory": _getFromListIfExists(creditJobCategory, i),
                        "nameId": _getFromListIfExists(creditNameID, i),
                    }
                )
    return constraint or None

def titleMeterConstraint(
        meterMin: int = 0,
        meterMax: int = 0,
        meterType: str = "TITLE_METER", # TitleMeterType ENUM
) -> dict | None:
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
        titleType: str | list = "",
        titleTypeExclude: str | list = "",
) -> dict | None:
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
        triviaTerm: str | list = "",
        triviaTermType: str = "all", # all/any
) -> dict | None:
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
        watchProviderID: str | list = "",
        watchRegion: str | list = "",
        watchProviderIDExclude: str | list = "",
        watchRegionExclude: str | list = "",
        watchType: str | list = "", # SearchWatchOptionType ENUM
) -> dict | None:
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
        withData: str | list = "",  # respective (DataType)DataType ENUMs
        withDataMissing: str | list = "",
        withDataAny: str | list = "",
) -> dict | None:
    constraint = {}
    if withData:
        if isinstance(titleData, str):
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
