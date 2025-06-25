"""Notes:
Names starting with "_" are private and require authencation.
Names starting with "*" fragments `... on TypeHere {{ selectiosn }}`

Some entries will cause circular references, using pre-defined minimal data instead.
These can be updated later for more information.
i.e.
 - Name: NameLimited # Remove most, keeping basic info
 - Title: TitleLimited # Remove most, keeping basic info
 - Image: ImageLimited # Remove names, can be updated later
"""

EngagementStatistics = {}
ProductionStatusHistoryRestriction = {}
TitleMetaRestrictions = {}
TitleFullCredits = {}
AggregateRatingsBreakdown = {}

Title = {
    "id": str,  # tt____
    "canonicalUrl": str,  # The URL
    "titleText": "TitleText",
    "titleType": "TitleType",
    "originalTitleText": "TitleText",
    "releaseYear": "ReleaseYear",
    "releaseDate": "ReleaseDate",
    "countriesOfOrigin": "CountriesOfOrigin",
    "runtime": "Runtime",
    "runtimes": "Runtime.edges",
    "canRate": "CanRate",
    "productionStatus": "ProductionStatusDetails",
    "canHaveEpisodes": bool,
    "certificate": "Certificate",
    "certificates": "Certificate.edges",
    "ratingsSummary": "RatingsSummary",
    "images": "Image.edges",
    "primaryImage": "ImageLimited",
    "videos": "TitleRelatedVideos",
    "primaryVideos": "Video.edges",
    "externalLinks": "ExternalLink.edges",
    "metacritic": "Metacritic",
    "series": "Series",
    "keywords": "TitleKeyword.edges",
    "genres": "Genres",
    "plot": "Plot",
    "plots": "Plot.edges",
    "credits": "Credit.edges",
    "episodeCredits": "CreditV2.edges",
    "meterRanking": "TitleMeterRanking",
    "principalCredits": "PrincipalCreditsForCategory",
    "principalCreditsV2": "PrincipalCreditsForGrouping",
    "episodes": "Episodes.manual",
    "certificates": "Certificate.edges",
    "parentsGuide": "ParentsGuide",
    "nominations": "Nomination.edges",
    "soundtrack": "Soundtrack.edges",
    "alternateVersions": "AlternateVersion.edges",
    "technicalSpecifications": "TechnicalSpecifications",
    "rankedLifetimeGross": "RankedLifetimeBoxOfficeGross",
    "openingWeekendGross": "OpeningWeekendGross",
    "lifetimeGross": "BoxOfficeGross",
    "productionBudget": "ProductionBudget",
    "prestigiousAwardSummary": "PrestigiousAwardSummary",
    "awardNominations": "AwardNomination.edges",
    "crazyCredits": "CrazyCredit.edges",
    "trivia": "Trivia",
    "videoStrip": "Video.edges",
    "crazyCredits": "CrazyCredit.edges",
    "reviews": "Review",
    "companyCredits": "CompanyCredit.edges",
    "faqs": "Faq",
    "productionDates": "ProductionDates.edges",
    "featuredReviews": "Review.edges",
    "filmingDates": "FilmingDates.edges",
    "filmingLocations": "FilmingLocation.edges",
    "moreLikeThisTitles": "TitleLimited.edges",
    "goofs": "Goof.edges",
    "quotes": "TitleQuote.edges",
    "connections": "TitleConnection.edges",
    "alexaTopQuestions": "AlexaQuestion.edges",
    "spokenLanguages": "SpokenLanguages",
    "contributionQuestions": "Question",
    "meta": "TitleMeta",
    ##################################################
    # disabled until I can figure out a required argument
    # "plotContributionLink": "ContributionLink", # contributionContext
    # "plotContributionLink": "ContributionLink", # contributionContext
    # "imageUploadLink": "ContributionLink", # contributionContext
    # "cinemaShowtimesByScreeningType": "TitleCinemaShowtimesByScreeningType.edges" # TitleCinemaShowtimesFilter
    ##################################################
    # disabled until I can figure out some attributes
    # "engagementStatistics": "EngagementStatistics",
    # "fullCredits": "TitleFullCredits",
    # "aggregateRatingsBreakdown": "AggregateRatingsBreakdown",
    ##################################################
}

TitleCinemaShowtimesByScreeningType = {}

TitleMeta = {
    "canonicalId": str,  # Same as id
    # "restrictions": "TitleMetaRestrictions",
}

NameMeta = {
    "canonicalId": str,  # Same as id
}

TitleConnection = {"text": str}

SpokenLanguages = {
    "language": "DisplayableLanguage",
}

Question = {
    "questionId": str,  # ??? maybe
    "questionText": "Markdown",
}
AlexaQuestion = {
    "question": "Markdown",
    "answer": "Markdown",
}

TitleQuote = {
    "id": str,  # qt____
    "language": "DisplayableLanguage",
}

Goof = {
    "id": str,  # gf____
    "text": "Markdown",
}

FilmingLocation = {
    "id": str,  # lc____
    "location": str,
    "text": str,
    "language": "DisplayableLanguage",
}

FilmingDates = {
    "startDate": dict,  # {day, month, year}
    "endDate": dict,
}

ProductionDates = {
    "startDate": "DisplayableDate",
    "endDate": "DisplayableDate",
}

Faq = {"id": str, "question": "Markdown"}  # fq____

Company = {
    "id": str,  # co____
    "companyText": "CompanyText",
    "companyTypes": "CompanyType",
}

CompanyText = {"text": str}

CompanyType = {
    "id": str,
    "text": str,
}

CompanyCredit = {"title": "TitleLimited"}

CrazyCredit = {
    "id": str,  # ???
    "text": "Markdown",
}

Trivia = {"id": str, "text": "Markdown"}  # tr____

CrazyCredit = {
    "id": str,  # ???
    "text": "Markdown",
}

Series = {"series": "TitleLimited"}

TitleLimited = (
    {  # define a limited scope Title to be used to avoid circlular generation
        "id": str,  # tt____
        "canonicalUrl": str,  # The URL
        "titleType": "TitleType",
        "releaseYear": "ReleaseYear",
        "titleText": "TitleText",
        "originalTitleText": "TitleText",
    }
)

TitleType = {
    "id": str,  # movie/tv/etc
    "text": str,
    "language": "DisplayableLanguage",
}

Name = {
    "id": str,  # nm____
    "canonicalUrl": str,  # The URL
    "creditCategories": "NameCreditCategoryWithCredits",
    "credits": "CreditAttribute.edges",
    "trademarks": "Trademark.edges",
    "bio": "NameBio",
    "akas": "NameAka.edges",
    "news": "News.edges",
    "images": "Image.edges",
    "age": "AgeDetails",
    "_isClaimed": bool,
    "knownForV2": "KnownForV2",
    "knownFor": "NameKnownFor",
    "spouses": "NameSpouse",
    "height": "NameHeight",
    "relations": "NameRelations.edges",
    "birthDate": "DisplayableDate",  # yyyy-mm-dd
    "nameText": "NameText",
    "birthName": "BirthName",
    "birth": "NameBirth",
    "deathStatus": str,
    "deathLocation": "DisplayableLocation",
    "death": "NameDeath",
    "meta": "NameMeta",
}

NameLimited = {
    "id": str,  # nm____
    "canonicalUrl": str,  # The URL
    "bio": "NameBio",
    "akas": "NameAka.edges",
    "height": "NameHeight",
    "birthDate": "DisplayableDate",  # yyyy-mm-dd
    "nameText": "NameText",
    "birthName": "BirthName",
    "birth": "NameBirth",
    "deathStatus": str,
    "deathLocation": "DisplayableLocation",
    "death": "NameDeath",
}

AwardDetails = {
    "id": str,  # aw____
    "year": int,
    "category": "AwardCategory",
}

AwardNomination = {
    "id": str,  # an____
    "isWinner": bool,
    "forSongTitles": str,  # Maybe, can't fine one that returns
    "winningRank": int,
    "award": "AwardDetails",
    "category": "AwardCategory",
    "forEpisodes": "TitleLimited",
    "notes": "Markdown",
    "winAnnouncementDate": "DisplayableDate",
    "awardedEntities": "AwardedEntities",
}

NominationEvent = {
    "id": str,  # ev____
    "name": "NominationEventName",
    "location": "DisplayableLocation",
    "awards": "NominationAward",
    "akas": "NominationEventAka",
}

ImageLimited = {
    "id": str,  # rm____
    "type": str,
    "width": int,
    "height": int,
    "url": str,
    "languages": "DisplayableLanguage",
}

Image = {
    "id": str,  # rm____
    "names": "NameLimited",
    "type": str,
    "width": int,
    "height": int,
    "url": str,
    "languages": "DisplayableLanguage",
}

NameRelations = {
    "id": str,  # rs____
    "relationName": "RelationName",
}

News = {
    "id": str,  # ni____
    "date": str,  # yyyy-mm-dd'T'hh:mm:ssZ
    "image": "ImageLimited",
}

NominationAward = {
    "id": str,  # aw____
    "text": str,
}

Runtime = {
    "id": str,  # rt____
    "seconds": int,
    "displayableProperty": "DisplayableTitleRuntimeProperty",
    "attributes": "DisplayableAttribute",
    "country": "DisplayableCountry",
}


Soundtrack = {
    "id": str,  # sn____
    "comments": "Markdown",
    "amazonMusicProducts": "AmazonMusicProduct",
}

Video = {
    "id": str,  # vi____
    "name": "LocalizedString",
    "description": "LocalizedString",
}

Coloration = {"id": str, "text": str, "attributes": "DisplayableAttribute"}

DisplayableDate = {"date": str}

CountryOfOrigin = {
    "id": str,  # The country code, i.e. US
    "text": str,
    "language": "DisplayableLanguage",
}

CreditAttribute = {
    "id": str,
    "text": str,
    "language": "DisplayableLanguage",
    "*SeriesCreditAttribute": "SeriesCreditAttribute",
}

SeriesCreditAttribute = {
    "id": str,
    "total": int,
    "text": str,
    "language": "DisplayableLanguage",
}

CreditCategory = {
    "id": str,
    "text": str,
    "language": "DisplayableLanguage",
}

DisplayableAttribute = {
    "id": str,
    "text": str,
}

DisplayableCountry = {"id": str, "text": str}

DisplayableLanguage = {
    "id": str,  # two-letter language code, i.e. en
    "text": str,
}

ExternalLink = {
    "id": str,  # amzn#.imdb.item.####
    "url": str,
}

Genre = {
    "id": str,
    "text": str,
    "language": "DisplayableLanguage",
}

ParentsGuideCategory = {
    "id": str,
    "text": str,
    "language": "DisplayableLanguage",
}

ProductionStage = {
    "id": str,
    "text": str,
}

SeverityLevel = {
    "id": str,
    "text": str,
}

SoundMix = {"id": str, "attributes": "DisplayableAttribute"}

Status = {
    "id": str,  # underscore lowercase name
    "text": str,  # Human name
}

TitleKeyword = {
    "id": str,
    "text": str,
}

TopRanking = {
    "id": str,  # topRated:tt###:language_country
    "rank": int,
    "text": "LocalizedText",
}

AgeDetails = {
    "id": str,  # Seems to be some b64 encoded binary data.
}

AlternateVersion = {
    "text": "Markdown",
}

AmazonMusicProduct = {
    "amazonId": "AmazonStandardId",
    "artists": "AmazonMusicProductArtist",
    "format": "AmazonMusicProductFormat",
    "productTitle": "AmazonMusicProductTitle",
}

AmazonMusicProductArtist = {
    "artistName": "AmazonMusicProductArtistName",
}

AmazonMusicProductArtistName = {"text": str, "language": "DisplayableLanguage"}

AmazonMusicProductFormat = {
    "text": str,
    "language": "DisplayableLanguage",
}

AmazonMusicProductTitle = {
    "text": str,
    "language": "DisplayableLanguage",
}

AmazonStandardId = {
    "asin": str,
}

AspectRatio = {"aspectRatio": str, "attributes": "DisplayableAttribute"}

AspectRatios = {"items": "AspectRatio"}

AwardCategory = {"text": str}

AwardedEntities = {"*AwardedNames": "AwardedNames", "*AwardedTitles": "AwardedTitles"}

AwardedNames = {"names": "NameLimited"}

AwardedTitles = {
    "titles": "TitleLimited",
}

BirthName = {"text": str}

BoxOfficeGross = {
    "total": "Money",
}

Camera = {"camera": str, "attributes": "DisplayableAttribute"}

Cameras = {"items": "Camera"}

CanRate = {
    "isRatable": bool,
}

Certificate = {
    "rating": str,  # the rating, i.e. PG-13
    "country": "DisplayableCountry",
}

Certificates = {
    "rating": str,
    "country": "DisplayableCountry",
}

Colorations = {"items": "Coloration"}

ContributionLink = {
    "url": str,
}

CountriesOfOrigin = {"countries": "CountryOfOrigin"}

Credit = {
    "title": "TitleLimited",
    "attributes": "CreditAttribute",
    "category": "CreditCategory",
    "name": "NameLimited",
}

KnownForV2 = {"credits": "CreditV2"}

CreditV2 = {
    "title": "TitleLimited",
    "name": "NameLimited",
    "creditedRoles": "CreditedRole.edges",
}

CreditedRole = {
    "text": str,
    "category": "CreditCategory",
}

DeathCause = {
    "text": str,
}

DisplayableLocation = {
    "text": str,
}

DisplayableTitleRuntimeProperty = {
    "value": "Markdown",
    "language": "DisplayableLanguage",
}

Episodes = {
    "episodes": "TitleLimited.edges",
    "seasons": "EpisodesSeason",
}

EpisodesSeason = {
    "number": int,
}

FilmLength = {
    "filmLength": str,
    "numReels": int,
    "countries": "DisplayableCountry",
    "attributes": "DisplayableAttribute",
}

FilmLengths = {"items": "FilmLength"}

Genres = {"genres": "Genre"}

Laboratories = {"items": "Laboratory"}

Laboratory = {"laboratory": str, "attributes": "DisplayableAttribute"}

LengthMeasurement = {
    "unit": str,
    "value": float,
}

LocalizedText = {
    "language": str,  # language code with country, i.e. en-US
}

LocalizedString = {
    "language": str,
    "value": str,
}

Location = {
    "text": str,
}

Markdown = {"plainText": str}

Metacritic = {
    "reviews": "MetacriticReview.edges",
}

MetacriticReview = {
    "reviewer": str,
    "url": str,
    "score": int,
    "site": str,
}

Money = {
    "currency": str,
    "amount": int,
}

NameAka = {
    "text": str,
}

NameBio = {"language": "DisplayableLanguage", "text": "Markdown"}

NameBirth = {
    "date": str,  # yyyy-mm-dd
    "location": "Location",
}

NameCreditCategoryWithCredits = {"category": "CreditCategory"}

NameDeath = {"date": str, "cause": "DeathCause", "location": "Location"}  # yyyy-mm-dd

NameHeight = {"measurement": "LengthMeasurement"}

NameKnownFor = {
    "title": "TitleLimited",
    "credit": "Credit",
}

NameSpouse = {"name": "NameLimited"}

NameText = {
    "text": str,
}

NegativeFormat = {"negativeFormat": str, "attributes": "DisplayableAttribute"}

NegativeFormats = {"items": "NegativeFormat"}

Nomination = {"award": "NominationAward"}

NominationEventAka = {
    "name": "NominationEventName",
}

NominationEventName = {
    "text": str,
    "language": "DisplayableLanguage",
}

OpeningWeekendGross = {
    "gross": "BoxOfficeGross",
    "theaterCount": int,
    "weekendStartDate": str,  # yyyy-mm-dd
    "weekendEndDate": str,  # yyyy-mm-dd
}

ParentsGuide = {
    "categories": "ParentsGuideCategorySummary",
    "guideItems": "ParentsGuideItem.edges",
}

ParentsGuideCategorySummary = {
    "severity": "SeverityLevel",
    "category": "ParentsGuideCategory",
    "guideItems": "ParentsGuideItem.edges",
}

ParentsGuideItem = {"isSpoiler": bool, "text": "Markdown"}

Plot = {
    "plotText": "Markdown",
    "language": "DisplayableLanguage",
    "plotType": str,
}

PrestigiousAwardSummary = {
    "wins": int,
    "nominations": int,
    "award": "AwardDetails",
}

PrincipalCreditsForCategory = {"category": "CreditCategory", "credits": "Credit"}

PrincipalCreditsForGrouping = {
    "credits": "CreditV2",
}

PrintedFormat = {"printedFormat": str, "attributes": "DisplayableAttribute"}

PrintedFormats = {"items": "PrintedFormat"}

Process = {"process": str, "attributes": "DisplayableAttribute"}

Processes = {"items": "Process"}

ProductionBudget = {
    "budget": "Money",
}

ProductionStage = {
    "id": str,
    "text": str,
}

ProductionStatusDetails = {
    "currentProductionStage": "ProductionStage",
    "productionStatusHistory": "ProductionStatusHistory",
    # Disabled until it is found out some attributes
    # "restriction": "ProductionStatusHistoryRestriction",
}

ProductionStatusHistory = {
    "status": "Status",
    "date": str,  # yyyy-mm-dd
}

RankedLifetimeBoxOfficeGross = {
    "total": "Money",
    "rank": int,
}

RatingsSummary = {
    "aggregateRating": float,
    "voteCount": int,
    "topRanking": "TopRanking",
}

RelationName = {"name": "NameLimited"}

ReleaseDate = {
    "day": int,
    "month": int,
    "year": int,
    "country": "DisplayableCountry",
}

ReleaseYear = {"year": int}

Review = {
    "id": str,  # rw____
    "language": str,
    "text": "ReviewText",
    "title": "TitleLimited",
    "authorRating": int,  # ??? maybe not an int
    "author": "UserProfile",
    "submissionDate": str,  # yyyy-mm-dd
    "helpfulness": "ReviewHelpfulness",
}

ReviewHelpfulness = {
    "upVotes": int,
    "downVotes": int,
}

User = {
    "fullName": str,
    "profile": "UserProfile",
}

UserProfile = {
    "bio": "UserProfileBio",
    "username": "UserProfileUsername",
}

UserProfileUsername = {"text": str}

UserProfileBio = {"text": "Markdown"}

ReviewText = {"text": "Markdown"}

SoundMixes = {"items": "SoundMix"}

TechnicalSpecifications = {
    "aspectRatios": "AspectRatios",
    "cameras": "Cameras",
    "colorations": "Colorations",
    "laboratories": "Laboratories",
    "negativeFormats": "NegativeFormats",
    "printedFormats": "PrintedFormats",
    "processes": "Processes",
    "soundMixes": "SoundMixes",
    "filmLengths": "FilmLengths",
}

TitleMeterRanking = {"meterType": str}

TitleRelatedVideos = {"total": int}

TitleText = {
    "text": str,
    "language": "DisplayableLanguage",
    "isOriginalTitle": bool,
}

Trademark = {"text": "Markdown"}
