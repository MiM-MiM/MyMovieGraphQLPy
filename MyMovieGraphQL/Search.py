from MyMovieGraphQL import Constraints, GraphQL

def sort(
        sortBy: str = "", # Changes per sort, an ENUM
        sortOrder: str = "DESC",
) -> dict | None:
    sort_by = {}
    sortOrder = sortOrder.upper()
    if sortBy and sortOrder:
        sort_by = {
            'sortBy': sortBy,
            'sortOrder': sortOrder,
        }
    return sort_by or None

def searchTitle(
        # kwargs not used that way it is more clear what is availiable and defaults are displayed easier.
        title: str = "",
        titleType: str | list = "",
        titleTypeExclude: str | list = "",
        year: int = 0,
        yearEnd: int = 0,
        dateStart: str = "",
        dateEnd: str = "",
        sortBy: str = "RELEASE_DATE", # AdvancedTitleSearchSortBy
        sortOrder: str = "DESC",
        limit: int = 25,
        offset: int = 0,
        pagnation: str = "",
        alternateVersion: str | list = "",
        alternateVersionIncludeType: str = "any", # any/all
        award: str | list = "",  # The award ID
        awardIncludeType: str = "any", # any/all/exclude
        certificate: dict | list = {},  # {rating: xxx, region: xxx}
        certificateIncludeType: str = "any", # any/exclude
        character: str | list = "",
        creditedCharacters: bool = True,  # Limit to only credited roles.
        coloration: str | list = "", # The ColorationType ENUM
        colorationIncludeType: str = "any", # any/exclude
        crazyCredit: str = "",
        crazyCreditIncludeType: str = "all", # any/all
        companyCategory: str | list = "",
        company: str | list = "",
        companyIncludeType: str = "any", # all/any/exclude
        creditedNameID: str | list = "",
        creditedNameIncludeType: str = "all", # any/all/exclude
        productionStageID: str | list = "",
        productionStageIncludeType: str = "any", # any/exclude
        seriesID: str | list = "", # Ther ID of the series to use
        seriesIDType: str = "any", # any/exclude # Limit to them matching.
        season: str | list = "", # The season numbers to use.
        episode: str | list = "", # The episode numbers to use.
        seasonEpisodeType: str = "any", # any/exclude # Limit to them matching.
        explicit: str = "INCLUDE_ADULT", # ExplicitContentFilter ENUM
        filmingLocation: str | list = "", # The filming location
        filmingLocationType: str = "any", # any/all
        genre: str | list = "", # The genre
        genreType: str = "all", # all/any/exclude
        genreMaxRelevant: int | None = None,
        goof: str | list = "", # the text to search for
        goofType: str = "all", # all/any
        theaterID: str | list = "", # The theater IDs
        theaterAttribute: str | list = "", # SearchTheaterAttribute ENUM.
        theaterStart: str = "", # ISO-8601 format
        theaterEnd: str = "", # The showtime dates, must have at least start
        theaterLocation: str = "", # The postal code 
        theaterLocationLatLong: dict = {}, # {lat: float, long: float}
        theaterLocationRadius: int = 50, # In meters
        theaterFavorite: bool = False, # Wehn true: MyFavoriteTheaterSearchFilter ENUM
        interestID: str | list = "",
        interestType: str = "all", # all/any/exclude
        keyword: str | list = "",
        keywordType: str = "all", # all/any/exclude
        language: str | list = "",
        languageType: str = "any", # all/any/exclude
        languagePrimary: str | list = "",
        languagePrimaryType: str = "any", # any/exclude
        silent: bool | None = None, # Silent
        inList: str | list = "",
        inPredefinedList: str | list = "", # ListClassId ENUM
        notInList: str | list = "", # always an any
        notInPredefinedList: str | list = "", # always an any
        inListType: str = "any", # all/any
        inPredefinedListType: str = "any", # all/any
        myRatingType: str = "INCLUDE", # MyRatingSearchFilterType ENUM
        myRatingMin: int | None = None,
        myRatingMax: int | None = None,
        originCountry: str | list = "",
        originCountryType: str = "all", # all/any/exclude
        originPrimaryCountry: str | list = "",
        originPrimaryCountryType: str = "any", # any/exclude
        plotText: str | list = "",
        plotTextType: str = "all", #all/any
        plotAuthor: str | list = "",
        quote: str | list = "",
        quoteType: str = "all", # all/any
        rankedTitleMin: int | None = None,
        rankedTitleMax: int | None = None,
        rankedTitleListType: str = "TITLE_METER", # RankedTitleListType ENUM
        rankedTitleType: str = "all", # all/exclude
        runtimeMin: int = 0, # In minutes
        runtimeMax: int = 0,
        ratingUserID: str = "",
        ratingUserRangeMin: int = 0,
        ratingUserRangeMax: int = 0,
        ratingUserType: str = "INCLUDE", # SingleUserRatingSearchFilterType ENUM
        soundMix: str | list = "",
        soundMixExclude: str | list = "",
        soundtrackTerms: str | list = "",
        soundtrackTermsType: str = "all", # all/any
        creditCharacter: str | list = "",
        creditCategory: str | list = "",
        creditJobCategory: str | list = "",
        creditNameID: str | list = "",
        creditType: str = "all",
        creditAdvanced: dict = {},
        meterMin: int = 0,
        meterMax: int = 0,
        meterType: str = "TITLE_METER", # TitleMeterType ENUM
        triviaTerm: str | list = "",
        triviaTermType: str = "all", # all/any
        ratingMin: float = 0.0,
        ratingMax: float = 0.0,
        ratingCountMin: int = 0,
        ratingCountMax: int = 0,
        watchProviderID: str | list = "",
        watchRegion: str | list = "",
        watchProviderIDExclude: str | list = "",
        watchRegionExclude: str | list = "",
        watchType: str | list = "", # SearchWatchOptionType ENUM
        withData: str | list = "",  # TitleDataType ENUMs
        withDataMissing: str | list = "",
        withDataAny: str | list = "",
) -> dict:
    if not isinstance(limit, int):
        raise TypeError(f"Limit must be an int, `{type(limit)}` given.")
    if not isinstance(offset, int):
        raise TypeError(f"Offset must be an int, `{type(offset)}` given.")
    if not isinstance(pagnation, str):
        raise TypeError(f"pagnation must be a string, `{type(pagnation)}` given.")
    if limit < 0:
        raise ValueError(f"Limit must be >= 0, `{limit}` passed")
    if offset < 0:
        raise ValueError(f"Offset must be >= 1, `{offset}` passed")
    # The dict could be generated with the query `generate_argument_dict` function
    # That could be used here, but the search function will cover them all,
    # it would only be extra steps.
    args = {
        "first": limit,
        "after": pagnation or None,
        "jumpToPosition": offset or None,
        "sort": sort(sortBy, sortOrder),
        "constraints": {
            # Not allowing experimental for this search.
            "experimental_boxOfficeEarningsConstraint": None,
            "experimental_occupationCreditConstraint": None,
            "experimental_professionCatagoryConstraint": None,
            "alternateVersionMatchingConstraint": Constraints.alternateVersionMatchingConstraint(alternateVersion, alternateVersionIncludeType),
            "awardConstraint": Constraints.awardConstraint(award, awardIncludeType),
            "certificateConstraint": Constraints.certificateConstraint(certificate, certificateIncludeType),
            "characterConstraint": Constraints.characterConstraint(character, creditedCharacters),
            "colorationConstraint": Constraints.colorationConstraint(coloration, colorationIncludeType),
            "crazyCreditMatchingConstraint": Constraints.crazyCreditMatchingConstraint(crazyCredit, crazyCreditIncludeType),
            "creditedCompanyConstraint": Constraints.creditedCompanyConstraint(companyCategory, company, companyIncludeType),
            "creditedNameConstraint": Constraints.creditedNameConstraint(creditedNameID, creditedNameIncludeType),
            "currentProductionStatusStageConstraint" : Constraints.currentProductionStatusStageConstraint(productionStageID, productionStageIncludeType),
            "episodicConstraint": Constraints.episodicConstraint(seriesID, seriesIDType, season, episode, seasonEpisodeType),
            "explicitContentConstraint": Constraints.explicitContentConstraint(explicit),
            "filmingLocationConstraint": Constraints.filmingLocationConstraint(filmingLocation, filmingLocationType),
            "genreConstraint": Constraints.genreConstraint(genre, genreType, genreMaxRelevant),
            "goofMatchingConstraint": Constraints.goofMatchingConstraint(goof, goofType),
            "inTheatersConstraint": Constraints.inTheatersConstraint(theaterID, theaterAttribute, theaterStart, theaterEnd, theaterLocation, theaterLocationLatLong, theaterLocationRadius, theaterFavorite),
            "interestConstraint": Constraints.interestConstraint(interestID, interestType),
            "keywordConstraint": Constraints.keywordConstraint(keyword, interestType),
            "languageConstraint": Constraints.languageConstraint(language, languageType, languagePrimary, languagePrimaryType, silent),
            "listConstraint": Constraints.listConstraint(inList, inPredefinedList, notInList, notInPredefinedList, inListType, inPredefinedListType),
            "myRatingConstraint": Constraints.myRatingConstraint(myRatingType, myRatingMin, myRatingMax),
            "originCountryConstraint": Constraints.originCountryConstraint(originCountry, originCountryType, originPrimaryCountry, originPrimaryCountryType),
            "plotMatchingConstraint": Constraints.plotMatchingConstraint(plotText, plotTextType, plotAuthor),
            "quoteMatchingConstraint": Constraints.quoteMatchingConstraint(quote, quoteType),
            "rankedTitleListConstraint": Constraints.rankedTitleListConstraint(rankedTitleMin, rankedTitleMax, rankedTitleListType, rankedTitleType),
            "releaseDateConstraint": Constraints.releaseDateConstraint(year, yearEnd, dateStart, dateEnd),
            "runtimeConstraint": Constraints.runtimeConstraint(runtimeMin, runtimeMax),
            "singleUserRatingConstraint": Constraints.singleUserRatingConstraint(ratingUserID, ratingUserRangeMin, ratingUserRangeMax, ratingUserType),
            "soundMixConstraint": Constraints.soundMixConstraint(soundMix, soundMixExclude),
            "soundtrackMatchingConstraint": Constraints.soundtrackMatchingConstraint(soundtrackTerms, soundtrackTermsType),
            "titleCreditsConstraint": Constraints.titleCreditsConstraint(creditCharacter, creditCategory, creditJobCategory, creditNameID, creditType, creditAdvanced),
            "titleMeterConstraint": Constraints.titleMeterConstraint(meterMin, meterMax, meterType),
            "titleTextConstraint": Constraints.textSearchConstraint(title),
            "titleTypeConstraint": Constraints.titleTypeConstraint(titleType, titleTypeExclude),
            "triviaMatchingConstraint": Constraints.triviaMatchingConstraint(triviaTerm, triviaTermType),
            "userRatingsConstraint": Constraints.userRatingsConstraint(ratingMin, ratingMax, ratingCountMin, ratingCountMax),
            "watchOptionsConstraint": Constraints.watchOptionsConstraint(watchProviderID, watchRegion, watchProviderIDExclude, watchRegionExclude, watchType),
            "withTitleDataConstraint": Constraints.withDataConstraint(withData, withDataMissing, withDataAny),
        }
    }
    return GraphQL.search('advancedTitleSearch', **args)

def searchName(
        name: str = "",
        sortBy: str = "BIRTH_DATE", # AdvancedNameSearchSortBy ENUM
        sortOrder: str = "DESC",
        limit: int = 25,
        offset: int = 0,
        pagnation: str = "",
        award: str | list = "",  # The award ID
        awardIncludeType: str = "any", # any/all/exclude
        biographyAuthor: str | list = "",
        biographyText: str = "",
        birthdayRangeStart: str = "",
        birthdayRangeEnd: str = "",
        birthday: str = "", # MonthDay ISO-8601 format '--06-19'
        birthPlace: str = "",
        deathDate: str = "", # If this is the only one provided it is exact day
        deathDateEnd: str = "",
        deathPlace: str = "",
        explicit: str = "INCLUDE_ADULT", # ExplicitContentFilter ENUM
        filmographyTitleID: str | list = "",
        filmographyTitleIDType: str = "all", # all/any/exclude
        filmographyTitleIDExclude: str | list = "", # If type is also exclude it will use this one.
        gender: str | list = "",
        genderType: str = "any", # any/exclude
        inList: str | list = "",
        inPredefinedList: str | list = "", # ListClassId ENUM
        notInList: str | list = "", # always an any
        notInPredefinedList: str | list = "", # always an any
        inListType: str = "any", # all/any
        inPredefinedListType: str = "any", # all/any
        # professionCategory example: amzn1.imdb.concept.profession_category.db674385-f70e-42b1-b4ef-910b8c64afa5
        # Seems to not work correctly, exclude returns results, even the one the ID came from.
        # Above example is one listed in nm0000115's
        professionCategory: str | list = "",
        professionCategoryType: str = "any",
        professionCategoryExclude: str | list = "", # If type is set to exclude this overrids the above.
        # profession example: amzn1.imdb.concept.profession.38160716-b702-4b4e-a737-1052cba53548
        # Seems to not work correctly, exclude returns results, even the one the ID came from.
        # Above example is one listed in nm0000115's
        profession: str | list = "",
        professionType: str = "any",
        professionExclude: str | list = "",
        quote: str | list = "",
        quoteType: str = "all", # all/any
        triviaTerm: str | list = "",
        triviaTermType: str = "all", # all/any
        withData: str | list = "",  # NameDataType ENUMs
        withDataMissing: str | list = "",
        withDataAny: str | list = "",
) -> dict:
    if not isinstance(limit, int):
        raise TypeError(f"Limit must be an int, `{type(limit)}` given.")
    if not isinstance(offset, int):
        raise TypeError(f"Offset must be an int, `{type(offset)}` given.")
    if not isinstance(pagnation, str):
        raise TypeError(f"pagnation must be a string, `{type(pagnation)}` given.")
    if limit < 0:
        raise ValueError(f"Limit must be >= 0, `{limit}` passed")
    if offset < 0:
        raise ValueError(f"Offset must be >= 1, `{offset}` passed")
    args = {
        "first": limit,
        "after": pagnation or None,
        "jumpToPosition": offset or None,
        "sort": sort(sortBy, sortOrder),
        "constraints": {
                "awardConstraint": Constraints.awardConstraint(award, awardIncludeType),
                "biographyConstraint": Constraints.biographyConstraint(biographyAuthor, biographyText),
                "birthDateConstraint": Constraints.birthDateConstraint(birthdayRangeStart, birthdayRangeEnd, birthday),
                "birthPlaceConstraint": Constraints.birthPlaceConstraint(birthPlace),
                "deathDateConstraint": Constraints.deathDateConstraint(deathDate, deathDateEnd),
                "deathPlaceConstraint": Constraints.deathPlaceConstraint(deathPlace),
                "explicitContentConstraint": Constraints.explicitContentConstraint(explicit),
                "filmographyConstraint": Constraints.filmographyConstraint(filmographyTitleID, filmographyTitleIDType, filmographyTitleIDExclude),
                "genderIdentityConstraint": Constraints.genderIdentityConstraint(gender, genderType),
                "listConstraint": Constraints.listConstraint(inList, inPredefinedList, notInList, notInPredefinedList, inListType, inPredefinedListType),
                "nameTextConstraint": Constraints.textSearchConstraint(name),
                "professionCategoryConstraint": Constraints.professionCategoryConstraint(professionCategory, professionCategoryType, professionCategoryExclude),
                "professionConstraint": Constraints.professionConstraint(profession, professionType, professionExclude),
                "quoteMatchingConstraint": Constraints.quoteMatchingConstraint(quote, quoteType),
                "triviaMatchingConstraint": Constraints.triviaMatchingConstraint(triviaTerm, triviaTermType),
                "withNameDataConstraint": Constraints.withDataConstraint(withData, withDataMissing, withDataAny),
            }
    }
    return GraphQL.search('advancedTitleSearch', **args)
