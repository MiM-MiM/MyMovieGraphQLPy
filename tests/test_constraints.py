from __future__ import annotations

import inspect

import pytest

from MyMovieGraphQL import Constraints


def test_constraint_builders_can_be_invoked_with_defaults():
    funcs = [
        (name, func)
        for name, func in inspect.getmembers(Constraints, inspect.isfunction)
        if not name.startswith("_") and name != "beartype"
    ]

    for name, func in funcs:
        result = func()
        assert result is None or isinstance(result, dict), f"{name} returned {type(result)}"


def test_basic_constraint_builders_return_expected_shapes():
    assert Constraints.textSearchConstraint("matrix") == {"searchTerm": "matrix"}
    assert Constraints.titleTypeConstraint("MOVIE") == {"anyTitleTypeIds": ["MOVIE"]}
    assert Constraints.titleTypeConstraint("MOVIE", "TV") == {"excludeTitleTypeIds": ["TV"]}

    assert Constraints.withDataConstraint(["rating", "cast"], ["plot"]) == {
        "allDataAvailable": ["RATING", "CAST"],
        "noDataAvailable": ["PLOT"],
    }

    assert Constraints.birthDateConstraint("1990-01-01", "1999-12-31", "--06-19") == {
        "birthday": "--06-19",
        "birthDateRange": {"start": "1990-01-01", "end": "1999-12-31"},
    }

    with pytest.raises(ValueError, match="start date"):
        Constraints.birthDateConstraint("bad-date")


def test_constraint_helpers_return_expected_outputs():
    expected_outputs = {
        "alternateVersionMatchingConstraint": (
            {"alternateVersion": ["release"], "alternateVersionIncludeType": "any"},
            {"anyAlternateVersionTextTerms": ["release"]},
        ),
        "awardConstraint": (
            {"award": ["award-1"], "awardIncludeType": "any"},
            {"anyEventNominations": [{"eventId": "award-1"}]},
        ),
        "biographyConstraint": (
            {"biographyAuthor": ["Author Name"], "biographyText": "sample bio"},
            {"anyBiographyAuthors": ["Author Name"], "searchText": "sample bio"},
        ),
        "birthDateConstraint": (
            {
                "birthdayRangeStart": "1990-01-01",
                "birthdayRangeEnd": "1999-12-31",
                "birthday": "--06-19",
            },
            {
                "birthDateRange": {"end": "1999-12-31", "start": "1990-01-01"},
                "birthday": "--06-19",
            },
        ),
        "birthPlaceConstraint": (
            {"birthPlace": "Paris"},
            {"birthPlace": "Paris"},
        ),
        "certificateConstraint": (
            {
                "certificate": {"rating": "PG", "region": "US"},
                "certificateIncludeType": "any",
            },
            {"anyRegionCertificateRatings": [{"rating": "PG", "region": "US"}]},
        ),
        "characterConstraint": (
            {"character": ["Neo"], "creditedCharacters": True},
            {"anyCharacterNames": ["Neo"], "shouldLimitToCreditedNameIds": True},
        ),
        "colorationConstraint": (
            {"coloration": ["COLOR"], "colorationIncludeType": "any"},
            {"anyColorationTypes": ["COLOR"]},
        ),
        "crazyCreditMatchingConstraint": (
            {"crazyCredit": ["secret"], "crazyCreditIncludeType": "all"},
            {"allCrazyCreditTextTerms": ["secret"]},
        ),
        "creditedCompanyConstraint": (
            {
                "companyCategory": ["production"],
                "company": ["co-123"],
                "companyIncludeType": "any",
            },
            {"anyCompanyCategories": ["production"], "anyCompanyIds": ["co-123"]},
        ),
        "creditedNameConstraint": (
            {"creditedNameID": ["nm123"], "creditedNameIncludeType": "all"},
            {"allNameIds": ["nm123"]},
        ),
        "currentProductionStatusStageConstraint": (
            {"productionStageID": ["stage-1"], "productionStageIncludeType": "any"},
            {"anyProductionStageIds": ["stage-1"]},
        ),
        "deathDateConstraint": (
            {"deathDate": "2000-01-01", "deathDateEnd": "2000-12-31"},
            {"deathDateRange": {"end": "2000-12-31", "start": "2000-01-01"}},
        ),
        "deathPlaceConstraint": (
            {"deathPlace": "London"},
            {"deathPlace": "London"},
        ),
        "episodicConstraint": (
            {
                "seriesID": ["tt123"],
                "seriesIDType": "any",
                "season": ["1"],
                "episode": ["2"],
                "seasonEpisodeType": "any",
            },
            {
                "anySeriesIds": ["tt123"],
                "anySeasons": ["1"],
                "anyEpisodeNumbers": ["2"],
            },
        ),
        "explicitContentConstraint": (
            {"explicit": "INCLUDE_ADULT"},
            {"explicitContentFilter": "INCLUDE_ADULT"},
        ),
        "filmingLocationConstraint": (
            {"filmingLocation": ["Paris"], "filmingLocationType": "any"},
            {"anyLocations": ["Paris"]},
        ),
        "filmographyConstraint": (
            {
                "filmographyTitleID": ["tt456"],
                "filmographyTitleIDType": "all",
                "filmographyTitleIDExclude": ["tt789"],
            },
            {"allTitleIds": ["tt456"], "excludeTitleIds": ["tt789"]},
        ),
        "genderIdentityConstraint": (
            {"gender": ["female"], "genderType": "any"},
            {"anyGender": ["FEMALE"]},
        ),
        "genreConstraint": (
            {"genre": ["Action"], "genreType": "all", "genreMaxRelevant": 3},
            {"allGenreIds": ["Action"], "maxRelevantGenres": 3},
        ),
        "goofMatchingConstraint": (
            {"goof": ["mistake"], "goofType": "all"},
            {"allGoofTextTerms": ["mistake"]},
        ),
        "inTheatersConstraint": (
            {
                "theaterID": ["theater-1"],
                "theaterAttribute": ["IMAX"],
                "theaterStart": "2024-01-01",
                "theaterEnd": "2024-01-10",
                "theaterLocation": "10001",
                "theaterLocationLatLong": {"lat": 40.7, "long": -74.0},
                "theaterLocationRadius": 50,
                "theaterFavorite": True,
            },
            {
                "allTheaterAttributes": ["IMAX"],
                "anyCinemaIds": ["theater-1"],
                "dateTimeRange": {"end": "2024-01-10", "start": "2024-01-01"},
                "location": {
                    "latLong": {"lat": 40.7, "long": -74.0},
                    "postalCode": "10001",
                    "radiusInMeters": 50,
                },
                "myFavoriteTheaters": "ONLY_MY_FAVORITE",
            },
        ),
        "interestConstraint": (
            {"interestID": ["interest-1"], "interestType": "all"},
            None,
        ),
        "keywordConstraint": (
            {"keyword": ["space"], "keywordType": "all"},
            {"allKeywords": ["space"]},
        ),
        "languageConstraint": (
            {
                "language": ["English"],
                "languageType": "any",
                "languagePrimary": ["English"],
                "languagePrimaryType": "any",
                "silent": False,
            },
            {
                "anyLanguages": ["English"],
                "anyPrimaryLanguages": ["English"],
                "isSilent": False,
            },
        ),
        "listConstraint": (
            {
                "inList": ["list-1"],
                "inPredefinedList": ["class-1"],
                "notInList": ["list-2"],
                "notInPredefinedList": ["class-2"],
                "inListType": "any",
                "inPredefinedListType": "all",
            },
            {
                "inAnyList": ["list-1"],
                "inAllPredefinedList": {"classId": ["class-1"]},
                "notInAnyList": ["list-2"],
                "notInAnyPredefinedList": {"classId": ["class-2"]},
            },
        ),
        "myRatingConstraint": (
            {"myRatingType": "INCLUDE", "myRatingMin": 6, "myRatingMax": 9},
            {"filterType": "INCLUDE", "ratingRange": {"max": 9, "min": 6}},
        ),
        "originCountryConstraint": (
            {
                "originCountry": ["US"],
                "originCountryType": "all",
                "originPrimaryCountry": ["US"],
                "originPrimaryCountryType": "any",
            },
            {"allCountries": ["US"], "anyPrimaryCountries": ["US"]},
        ),
        "plotMatchingConstraint": (
            {
                "plotText": ["space travel"],
                "plotTextType": "all",
                "plotAuthor": ["author-1"],
            },
            {"allPlotTextTerms": ["space travel"], "anyPlotAuthors": ["author-1"]},
        ),
        "professionConstraint": (
            {
                "profession": ["actor"],
                "professionType": "any",
                "professionExclude": ["producer"],
            },
            {"anyProfessionIds": ["actor"], "excludeProfessionIds": ["producer"]},
        ),
        "professionCategoryConstraint": (
            {
                "professionCategory": ["acting"],
                "professionCategoryType": "any",
                "professionCategoryExclude": ["music"],
            },
            {
                "anyProfessionCategoryIds": ["acting"],
                "excludeProfessionCategoryIds": ["music"],
            },
        ),
        "quoteMatchingConstraint": (
            {"quote": ["hello"], "quoteType": "all"},
            {"allQuoteTextTerms": ["hello"]},
        ),
        "rankedTitleListConstraint": (
            {
                "rankedTitleMin": 1,
                "rankedTitleMax": 10,
                "rankedTitleListType": "TITLE_METER",
                "rankedTitleType": "all",
            },
            {
                "allRankedTitleLists": [
                    {
                        "rankRange": {"max": 10, "min": 1},
                        "rankedTitleListType": "TITLE_METER",
                    }
                ]
            },
        ),
        "releaseDateConstraint": (
            {"year": 2020, "yearEnd": 2021},
            {"releaseDateRange": {"end": "2021-12-31", "start": "2020-01-01"}},
        ),
        "runtimeConstraint": (
            {"runtimeMin": 90, "runtimeMax": 120},
            {"runtimeRangeMinutes": {"max": 120, "min": 90}},
        ),
        "singleUserRatingConstraint": (
            {
                "ratingUserID": "ur-1",
                "ratingUserRangeMin": 4,
                "ratingUserRangeMax": 8,
                "ratingUserType": "INCLUDE",
            },
            {
                "filterType": "INCLUDE",
                "ratingRange": {"max": 8, "min": 4},
                "userId": "ur-1",
            },
        ),
        "soundMixConstraint": (
            {"soundMix": ["Dolby Digital"], "soundMixExclude": ["Mono"]},
            {"anySoundMixTypes": ["Dolby Digital"], "excludeSoundMixTypes": ["Mono"]},
        ),
        "soundtrackMatchingConstraint": (
            {"soundtrackTerms": ["theme"], "soundtrackTermsType": "all"},
            {"allSoundtrackTextTerms": ["theme"]},
        ),
        "textSearchConstraint": (
            {"search": "matrix"},
            {"searchTerm": "matrix"},
        ),
        "titleCreditsConstraint": (
            {
                "creditCharacter": ["Neo"],
                "creditCategory": ["actor"],
                "creditJobCategory": ["lead"],
                "creditNameID": ["nm123"],
                "creditType": "all",
            },
            {
                "allCredits": [
                    {
                        "character": "Neo",
                        "creditCategory": "actor",
                        "jobCategory": "lead",
                        "nameId": "nm123",
                    }
                ]
            },
        ),
        "titleMeterConstraint": (
            {"meterMin": 1, "meterMax": 10, "meterType": "TITLE_METER"},
            {"rankRange": {"max": 10, "min": 1}, "titleMeterType": "TITLE_METER"},
        ),
        "titleTypeConstraint": (
            {"titleType": ["MOVIE"], "titleTypeExclude": ["TV"]},
            {"excludeTitleTypeIds": ["TV"]},
        ),
        "triviaMatchingConstraint": (
            {"triviaTerm": ["hidden detail"], "triviaTermType": "all"},
            {"allTriviaTextTerms": ["hidden detail"]},
        ),
        "userRatingsConstraint": (
            {
                "ratingMin": 7.5,
                "ratingMax": 9.5,
                "ratingCountMin": 100,
                "ratingCountMax": 500,
            },
            {
                "aggregateRatingRange": {"max": 9.5, "min": 7.5},
                "ratingsCountRange": {"max": 500, "min": 100},
            },
        ),
        "watchOptionsConstraint": (
            {
                "watchProviderID": ["provider-1"],
                "watchRegion": ["US"],
                "watchProviderIDExclude": ["provider-2"],
                "watchRegionExclude": ["CA"],
                "watchType": ["STREAMING"],
            },
            {
                "anyWatchProviderIds": ["provider-1"],
                "anyWatchRegions": ["US"],
                "excludeWatchProviderIds": ["provider-2"],
                "excludeWatchRegions": ["CA"],
                "hasWatchOptionTypes": ["STREAMING"],
            },
        ),
        "withDataConstraint": (
            {
                "withData": ["rating"],
                "withDataMissing": ["cast"],
                "withDataAny": ["plot"],
            },
            {
                "allDataAvailable": ["RATING"],
                "anyDataAvailable": ["PLOT"],
                "noDataAvailable": ["CAST"],
            },
        ),
    }

    all_function_names = {
        name
        for name, _ in inspect.getmembers(Constraints, inspect.isfunction)
        if not name.startswith("_") and name != "beartype"
    }
    assert set(expected_outputs) == all_function_names

    for name, _func in inspect.getmembers(Constraints, inspect.isfunction):
        if name.startswith("_") or name == "beartype":
            continue
        kwargs, expected = expected_outputs[name]
        assert getattr(Constraints, name)(**kwargs) == expected, name
