TitleLimited ={
    "id": str,  # tt____
    "canonicalUrl": str,  # The URL
    "titleType": "TitleType",
    "releaseYear": "ReleaseYear",
    "titleText": "TitleText",
    "originalTitleText": "TitleText",
}

NameLimited = {
    "id": str,  # nm____
    "canonicalUrl": str,  # The URL
    "bio": "NameBio",
    "akas": "NameAkaConnection",
    "height": "NameHeight",
    "birthDate": "DisplayableDate",  # yyyy-mm-dd
    "nameText": "NameText",
    "birthName": "BirthName",
    "birth": "NameBirth",
    "death": "NameDeath",  # (Not Null)
   "deathCause": "DisplayableNameDeathCause",
   "deathDate": "DisplayableDate",
   "deathLocation": "DisplayableLocation",
   "deathStatus": str, # (ENUM)
}

ImageLimited = {
    "id": str,  # rm____
    "type": str,
    "width": int,
    "height": int,
    "url": str,
    "languages": "DisplayableLanguage",
}

VideoLimited = {
    "contentType": "VideoContentType",
   "createdDate": str,
   "description": "LocalizedString",
   "id": str,  # (Not Null)
   "runtime": "VideoRuntime",
}

NominationLimited = {
   "forEpisodes": "TitleLimited",  # (Not Null)
   "forSongTitles": "DisplayableSongTitle",  # (Not Null)
   "id": str,  # (Not Null)
   "isWinner": bool,
   "notes": "Markdown",
   "winAnnouncementDate": "DisplayableDate",
   "winningRank": int,
}

NominationAwardLimited = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

Language = {
    "language": str
}

"""--------------- AccountDataDialogOutput --------------"""
AccountDataDialogOutput = {
   "prompt": "LocalizedMarkdown",  # (Not Null)
   "redirectionPrompt": "AccountDataDialogRedirectionPrompt",
   "supportMessage": "LocalizedMarkdown",  # (Not Null)
}

"""--------- AccountDataDialogRedirectionPrompt ---------"""
AccountDataDialogRedirectionPrompt = {
   "action": "RedirectLink",  # (Not Null)
   "message": "LocalizedMarkdown",  # (Not Null)
}

"""
------------------------ ActionLink ------------------------
Generic type for an action link which has a url and
optionally associated label (localized text)
------------------------------------------------------------
"""
ActionLink = {
   "label": "CallToActionText",
   "url": str,  # (Not Null)
}

"""------------------- AdCreativeInfo -------------------"""
AdCreativeInfo = {
   "hasAutoplay": bool,  # (Not Null)
   "isEligibleFor3pAd": bool,  # (Not Null)
   "isPremium": bool,  # (Not Null)
   "shouldFitToWidth": bool,  # (Not Null)
   "size": "CreativeSize",  # (Not Null)
   "slotMarkup": str,  # (Not Null)
}

"""
------------------- AdditionalCreditItem -------------------
This is an unverified Resume credit, which Pro customers can
create for display on   their pro name page. These credits
are not vetted and are accepted as is.
------------------------------------------------------------
"""
AdditionalCreditItem = {
   "category": "LocalizedString",  # (Not Null)
   "details": "LocalizedString",  # (Not Null)
   "id": str,  # (Not Null)
   "job": "LocalizedString",  # (Not Null)
   "title": "LocalizedString",  # (Not Null)
}

"""---------------- AdditionalResumeInfo ----------------"""
AdditionalResumeInfo = {
   "details": "LocalizedString",
   "id": str,  # (Not Null)
   "title": "LocalizedString",
}

"""
------------------- AdLayoutConfiguration ------------------
An entry to the ad layout slot configuration map containing
an ad layout type and a list of supported slots and their
configurations.
------------------------------------------------------------
"""
AdLayoutConfiguration = {
   "adLayoutType": str,  # (Not Null)
   "adSlotConfigs": "AdSlotConfiguration",  # (Not Null)
}

"""----------------------- AdSlot -----------------------"""
AdSlot = {
   "adFeedbackUrl": str,
   "creativeInfo": "AdCreativeInfo",  # (Not Null)
   "name": str,  # (Not Null)
}

"""
-------------------- AdSlotConfiguration -------------------
The configuration for an ad slot.
------------------------------------------------------------
"""
AdSlotConfiguration = {
   "apsConfig": "ApsConfiguration",
   "name": str,  # (Not Null)
   "size": "CreativeSize",  # (Not Null)
}

"""-------------- AdvancedNameSearchResult --------------"""
AdvancedNameSearchResult = {
   "name": "NameLimited",  # (Not Null)
}

"""-------------- AdvancedTitleSearchResult -------------"""
AdvancedTitleSearchResult = {
   "title": "TitleLimited",  # (Not Null)
}

"""--------------------- AgeDetails ---------------------"""
AgeDetails = {
   "displayableProperty": "DisplayableNameAgeDetailsProperty",  # (Not Null)
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
   "value": int,  # (Not Null)
}

"""
-------------------------- Agency --------------------------
An agency that represents a name
------------------------------------------------------------
"""
Agency = {
   "agents": "Agent",  #
   "company": "Company",  # (Not Null)
}

"""
--------------------------- Agent --------------------------
An employee of a company who represents a name in some
capacity
------------------------------------------------------------
"""
Agent = {
   "branch": "CompanyBranch",
   "company": "Company",  # (Not Null)
   "employeeContact": "CompanyContactDetails",
   "id": str,  # (Not Null)
   "isPrimaryAgent": bool,  # (Not Null)
   "jobTitle": "LocalizedString",
   "name": "NameLimited",  # (Not Null)
   "occupation": "OccupationValue",
   "relationshipType": "RepresentationRelationshipType",  # (Not Null)
}

"""------------------- AgePlayingRange ------------------"""
AgePlayingRange = {
   "from": int,  # (Not Null)
   "to": int,  # (Not Null)
}

"""-------------- AggregateRatingsBreakdown -------------"""
AggregateRatingsBreakdown = {
   "histogram": "Histogram",
   "isCollapsed": bool,  # (Not Null)
   "ratingsSummaryByCountry": "RatingsSummaryByCountry",  # (Not Null)
   "ratingsSummaryByDemographics": "DemographicRatings",  # (Not Null)
}

"""
---------------------------- Aka ---------------------------
Aka details
------------------------------------------------------------
"""
Aka = {
   "attributes": "DisplayableAttribute",  # (Not Null)
   "country": "DisplayableCountry",
   "displayableProperty": "DisplayableTitleAkaProperty",  # (Not Null)
   "language": "DisplayableLanguage",
   "text": str,  # (Not Null)
}

"""
----------------------- AlexaQuestion ----------------------
An Alexa question.
------------------------------------------------------------
"""
AlexaQuestion = {
   "answer": "Markdown",  # (Not Null)
   "attributeId": str,  # (Not Null)
   "question": "Markdown",  # (Not Null)
}

"""
--------------------- AlternateVersion ---------------------
Alternate version details
------------------------------------------------------------
"""
AlternateVersion = {
   "displayableArticle": "DisplayableArticle",  # (Not Null)
   "text": "Markdown",  # (Not Null)
}

"""----------------- AmazonMusicProduct -----------------"""
AmazonMusicProduct = {
   "amazonId": "AmazonStandardId",  # (Not Null)
   "artists": "AmazonMusicProductArtist",  # (Not Null)
   "format": "AmazonMusicProductFormat",  # (Not Null)
   "image": "ImageLimited",
   "productTitle": "AmazonMusicProductTitle",  # (Not Null)
}

"""-------------- AmazonMusicProductArtist --------------"""
AmazonMusicProductArtist = {
   "artistName": "AmazonMusicProductArtistName",  # (Not Null)
}

"""------------ AmazonMusicProductArtistName ------------"""
AmazonMusicProductArtistName = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""-------------- AmazonMusicProductFormat --------------"""
AmazonMusicProductFormat = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""--------------- AmazonMusicProductTitle --------------"""
AmazonMusicProductTitle = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""------------------ AmazonStandardId ------------------"""
AmazonStandardId = {
   "asin": str,  # (Not Null)
   "obfuscatedMarketplaceId": str,  # (Not Null)
   "region": str,  # (Not Null)
}

"""-------------------- AnswerOption --------------------"""
AnswerOption = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""
--------------------- AppAdsInfoOutput ---------------------
Contains the eligibility status for apps to serve 3p ads and
configuration map for slots on each mobile app page.
------------------------------------------------------------
"""
AppAdsInfoOutput = {
   "adLayoutSlotConfig": "AdLayoutConfiguration",  # (Not Null)
   "thirdPartyAdsEligibility": bool,  # (Not Null)
}

"""
--------------------- ApsConfiguration ---------------------
The configuration of APS placements for an individual IMDb
ad slot.
------------------------------------------------------------
"""
ApsConfiguration = {
   "apsSlot": "ApsSlot",  # (Not Null)
   "apsSlotAdRefresh": "ApsSlot",
}

"""
-------------------------- ApsSlot -------------------------
The APS slot level information needed for 3p ad requests.
------------------------------------------------------------
"""
ApsSlot = {
   "apsSlotId": str,  # (Not Null)
   "apsSlotName": str,  # (Not Null)
}

"""
------------------------ AspectRatio -----------------------
An aspect ratio, along with any attributes. For example, the
aspect ratio for the IMAX and IMAX3D versions might be
2.35:1.
------------------------------------------------------------
"""
AspectRatio = {
   "aspectRatio": str,  # (Not Null)
   "attributes": "DisplayableAttribute",  # (Not Null)
   "displayableProperty": "DisplayableTechnicalSpecificationProperty",  # (Not Null)
}

"""
----------------------- AspectRatios -----------------------
Aspect ratios for this title.
------------------------------------------------------------
"""
AspectRatios = {
   "items": "AspectRatio",  # (Not Null)
   "restriction": "TechnicalSpecificationsRestriction",
   "total": int,  # (Not Null)
}

"""----------- AuthProviderDeprecationMessage -----------"""
AuthProviderDeprecationMessage = {
   "message": "LocalizedMarkdown",  # (Not Null)
   "urls": "AuthProviderDeprecationUrl",  # (Not Null)
}

"""------------- AuthProviderDeprecationUrl -------------"""
AuthProviderDeprecationUrl = {
   "label": "AuthProviderDeprecationUrlLabel",  # (Not Null)
   "value": str,  # (Not Null)
}

"""----------- AuthProviderDeprecationUrlLabel ----------"""
AuthProviderDeprecationUrlLabel = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""----------------- AuthProviderStatus -----------------"""
AuthProviderStatus = {
   "provider": str,  # (Not Null)
   "providerLinkingURL": str,
}

"""-------------------- AwardCategory -------------------"""
AwardCategory = {
   "text": str,
}

"""-------------------- AwardDetails --------------------"""
AwardDetails = {
   #"awardNominationCategories": "AwardNominationsWithCategoryConnection",
   "eventEdition": "EventEdition",  # (Not Null)
   "id": str,  # (Not Null)
   "text": str,  # (Not Null)
}

AwardDetailsLimited = {
   "id": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""------------------- AwardNomination ------------------"""
AwardNomination = {
   "award": "AwardDetails",  # (Not Null)
   "category": "AwardCategory",
   "forEpisodes": "TitleLimited",  # (Not Null)
   "forSongTitles": str,  # (Not Null)
   "id": str,  # (Not Null)
   "isWinner": bool,  # (Not Null)
   "notes": "Markdown",
   "winAnnouncementDate": "DisplayableDate",
   "winningRank": int,
}

"""------------ AwardNominationsWithCategory ------------"""
AwardNominationsWithCategory = {
   "awardNominations": "AwardNominationConnection",
   "category": "AwardCategory",
}

"""--------------------- AwardsEvent --------------------"""
AwardsEvent = {
   "editions": "EventEditionLimitedConnection",
   "id": str,  # (Not Null)
   "location": "DisplayableLocation",
   "text": str,  # (Not Null)
   "trivia": "Markdown",  # (Not Null)
   "urls": "EventUrl",  # (Not Null)
}

"""
--------------------------- Badge --------------------------
Badge represents an achievement that can be earned by
customers
------------------------------------------------------------
"""
Badge = {
   "description": "LocalizedMarkdown",  # (Not Null)
   "id": str,  # (Not Null)
   "image": "MediaServiceImage",  # (Not Null)
   "subtitle": "CommonLocalizedDisplayableConcept",
   "title": "CommonLocalizedDisplayableConcept",  # (Not Null)
}

"""
---------------------- BadgeGuideEntry ---------------------
BadgeGuideEntry is a help page description for directions on
how to achieve one or many badges. e.g. All Oscars badge
awarding criteria is represented as the Oscars
BadgeGuideEntry
------------------------------------------------------------
"""
BadgeGuideEntry = {
   "description": "LocalizedMarkdown",  # (Not Null)
   "image": "MediaServiceImage",  # (Not Null)
   "subtitle": "CommonLocalizedDisplayableConcept",
   "title": "CommonLocalizedDisplayableConcept",  # (Not Null)
}

"""----------------------- Banner -----------------------"""
Banner = {
   "attributionUrl": str,  # (Not Null)
   "height": int,  # (Not Null)
   "imageUrl": str,  # (Not Null)
   "url": str,  # (Not Null)
   "width": int,  # (Not Null)
}

"""---------------------- BirthName ---------------------"""
BirthName = {
   "displayableProperty": "DisplayableBirthNameProperty",  # (Not Null)
   "text": str,  # (Not Null)
}

"""---------------------- BlogLink ----------------------"""
BlogLink = {
   "label": str,
   "url": str,  # (Not Null)
}

"""
--------------------- BoxOfficeAreaType --------------------
Displayable BoxOfficeArea type. See sections 'Area Rollups
and Special Areas' and 'Individual Areas' at
https://developer.imdb.com/documentation/bulk-data-
documentation/data-dictionary/box-office.
------------------------------------------------------------
"""
BoxOfficeAreaType = {
   "code": str,  # (Not Null)
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""------------------- BoxOfficeGross -------------------"""
BoxOfficeGross = {
   "total": "Money",  # (Not Null)
}

"""
--------------------- BoxOfficeRelease ---------------------
BoxOfficeRelease: a program of content designed to be
consumed in a single session that is exhibited in a specific
Box Office Area in a continuous period of time. Most
releases consist of a single film shown during a limited run
in a cinema, but other cases refer to more than one title.
For example a double-bill (two full-length movies shown
back-to-back with a single ticket) or the "Oscar Shorts"
program (theatrically exhibited collection of multiple films
back to back with a single ticket).
------------------------------------------------------------
"""
BoxOfficeRelease = {
   "titles": "TitleLimited",  # (Not Null)
   "weeksRunning": int,
}

"""---------------- BoxOfficeWeekendChart ---------------"""
BoxOfficeWeekendChart = {
   "entries": "ChartEntry",  # (Not Null)
   "weekendEndDate": str,  # (Not Null)
   "weekendStartDate": str,  # (Not Null)
}

"""-------------------- CallToAction --------------------"""
CallToAction = {
   "landingPagePro": "LinkCallToAction",
   "nameBanner": "MarkdownSlotCallToAction",
   "nameClaimPageForFree": "SectionCallToAction",
   "nameDiscoverMoreInsights": "LinkCallToAction",
   "nameImagesReels": "LinkCallToAction",
   "nameProUpsell": "MultiLinkCallToAction",
   "nameViewStarMeter": "LinkCallToAction",
   "navbarProFlyout": "ImageAndLinkCallToAction",
   "titleProUpsell": "LinkCallToAction",
}

"""
--------------------- CallToActionImage --------------------
Generic type for an image resource which has height, url,
width, and optional caption for accessibility
------------------------------------------------------------
"""
CallToActionImage = {
   "caption": "LocalizedMarkdown",
   "height": int,  # (Not Null)
   "url": str,  # (Not Null)
   "width": int,  # (Not Null)
}

"""
--------------------- CallToActionText ---------------------
Generic type for a localized text which has an ID or token,
associated display text, and the language of the display
text
------------------------------------------------------------
"""
CallToActionText = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""
-------------------------- Camera --------------------------
A camera (or lens), along with any attributes. For example,
a wide angle lens used for outdoor shots.
------------------------------------------------------------
"""
Camera = {
   "attributes": "DisplayableAttribute",  # (Not Null)
   "camera": str,  # (Not Null)
   "displayableProperty": "DisplayableTechnicalSpecificationProperty",  # (Not Null)
}

"""
-------------------------- Cameras -------------------------
Cameras for this title.
------------------------------------------------------------
"""
Cameras = {
   "items": "Camera",  # (Not Null)
   "restriction": "TechnicalSpecificationsRestriction",
   "total": int,  # (Not Null)
}

"""----------------------- CanRate ----------------------"""
CanRate = {
   "isRatable": bool,  # (Not Null)
}

"""--------------- CategorizedWatchOptions --------------"""
CategorizedWatchOptions = {
   "categoryName": "LocalizedString",  # (Not Null)
   "watchOptions": "WatchOption",  # (Not Null)
}

"""------------- CategorizedWatchOptionsList ------------"""
CategorizedWatchOptionsList = {
   "categorizedWatchOptionsList": "CategorizedWatchOptions",  # (Not Null)
}

"""--------------------- Certificate --------------------"""
Certificate = {
   "attributes": "DisplayableAttribute",  # (Not Null)
   "country": "DisplayableCountry",  # (Not Null)
   "id": str,  # (Not Null)
   "rating": str,  # (Not Null)
   "ratingReason": str,
   "ratingsBody": "RatingsBody",
   "ratingsBodyCertificateId": str,
}

"""-------- ChangeLoginSecurityRedirectURLOutput --------"""
ChangeLoginSecurityRedirectURLOutput = {
   "redirectURL": str,  # (Not Null)
}

"""
------------------------- Character ------------------------
Character details.
------------------------------------------------------------
"""
Character = {
   "id": str,
   "language": "DisplayableLanguage",
   "name": str,  # (Not Null)
}

"""--------------------- ChartEntry ---------------------"""
ChartEntry = {
   "title": "TitleLimited",  # (Not Null)
   "weekendGross": "BoxOfficeGross",  # (Not Null)
}

"""
-------------------------- Cinema --------------------------
Cinema type Extends external type.
------------------------------------------------------------
"""
Cinema = {
   "accessibility": "CinemaAccessibility",
   "contactDetails": "CinemaContactDetails",
   "distanceToCinema": "DistanceToCinema",
   "id": str,  # (Not Null)
   "location": "CinemaLocation",
   "name": "CinemaName",
}

"""
-------------------- CinemaAccessibility -------------------
Accessibility information for a cinema.
------------------------------------------------------------
"""
CinemaAccessibility = {
   "audioAccessibility": "CinemaAudioAccessibility",
   "wheelchairAccessibility": "CinemaWheelchairAccessibility",
}

"""
----------------- CinemaAudioAccessibility -----------------
Audio accessibility information for a cinema.
------------------------------------------------------------
"""
CinemaAudioAccessibility = {
   "hasHearingDevices": bool,
}

"""
------------------- CinemaContactDetails -------------------
Contact details for a cinema.
------------------------------------------------------------
"""
CinemaContactDetails = {
   "phoneNumber": str,
}

"""
---------------------- CinemaLocation ----------------------
Location data of a cinema.
------------------------------------------------------------
"""
CinemaLocation = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""
------------------------ CinemaName ------------------------
The name of a cinema.
------------------------------------------------------------
"""
CinemaName = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""
--------------- CinemaWheelchairAccessibility --------------
Wheelchair accessibility information for a cinema.
------------------------------------------------------------
"""
CinemaWheelchairAccessibility = {
   "hasWheelchairAccess": bool,
}

"""--------------------- ClaimedName --------------------"""
ClaimedName = {
   "name": "NameLimited",
   "status": str,  # (Not Null)
}

"""
------------------------ Coloration ------------------------
A coloration, along with any attributes. For example, we
could have a color picture that used technicolor, with black
and white flashback scenes.
------------------------------------------------------------
"""
Coloration = {
   "attributes": "DisplayableAttribute",  # (Not Null)
   "conceptId": str,  # (Not Null)
   "displayableProperty": "DisplayableTechnicalSpecificationProperty",  # (Not Null)
   "id": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""
------------------------ Colorations -----------------------
Colorations for this title.
------------------------------------------------------------
"""
Colorations = {
   "items": "Coloration",  # (Not Null)
   "restriction": "TechnicalSpecificationsRestriction",
   "total": int,  # (Not Null)
}

"""
------------- CommonLocalizedDisplayableConcept ------------
Implementation of the LocalizedDisplayableConcept interface.
See LocalizedDisplayableConcept docs
------------------------------------------------------------
"""
CommonLocalizedDisplayableConcept = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""----------------------- Company ----------------------"""
Company = {
   "acronyms": "CompanyAcronymConnection",
   "affiliations": "CompanyAffiliationConnection",
   "bio": "CompanyBio",
   "branches": "CompanyBranchConnection",
   "clients": "CompanyClientConnection",
   "companyText": "CompanyText",
   "companyTypes": "CompanyType",  # (Not Null)
   "country": "LocalizedDisplayableCountry",
   "experimental_branches": "Experimental_CompanyBranchConnection",
   "experimental_clients": "Experimental_CompanyClientConnection",
   "id": str,  # (Not Null)
   "images": "ImageConnection",
   "keyStaff": "CompanyKeyStaffConnection",
   "knownForClients": "CompanyKnownForClientConnection",
   "knownForTitles": "CompanyKnownForTitleConnection",
   "managedData": "ManagedCompanyData",
   "meterRank": "CompanyMeterRanking",
   "meterRankingHistory": "CompanyMeterRankingHistory",
   "primaryImage": "ImageLimited",
}

"""
---------------------- CompanyAcronym ----------------------
An acronym of a company
------------------------------------------------------------
"""
CompanyAcronym = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""
-------------------- CompanyAffiliation --------------------
The affiliated company
------------------------------------------------------------
"""
CompanyAffiliation = {
   "company": "Company",  # (Not Null)
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""--------------------- CompanyBio ---------------------"""
CompanyBio = {
   "displayableArticle": "DisplayableArticle",  # (Not Null)
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": "Markdown",  # (Not Null)
}

"""-------------------- CompanyBranch -------------------"""
CompanyBranch = {
   "directContact": "CompanyContactDetails",
   "id": str,  # (Not Null)
   "name": "LocalizedString",
}

"""-------------------- CompanyClient -------------------"""
CompanyClient = {
   "agents": "Agent",  #
   "client": "NameLimited",  # (Not Null)
   "id": str,  # (Not Null)
}

"""---------------- CompanyContactDetails ---------------"""
CompanyContactDetails = {
   "emailAddress": str,
   "faxNumber": "LocalizedString",
   "phoneNumbers": "LocalizedString",  # (Not Null)
   "physicalAddress": "Location",
   "website": "WebsiteLink",
}

"""-------------------- CompanyCredit -------------------"""
CompanyCredit = {
   "attributes": "DisplayableAttribute",  # (Not Null)
   "category": "CompanyCreditCategory",  # (Not Null)
   "company": "Company",  # (Not Null)
   "countries": "DisplayableCountry",  # (Not Null)
   "displayableProperty": "DisplayableTitleCompanyCreditProperty",  # (Not Null)
   "distributionFormats": "DistributionFormat",  # (Not Null)
   "title": "TitleLimited",  # (Not Null)
   "yearsInvolved": "YearRange",
}

"""
------------------- CompanyCreditCategory ------------------
The category for the company credit, e.g. sales,
distribution etc.
------------------------------------------------------------
"""
CompanyCreditCategory = {
   "id": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""------- CompanyCreditCategoryWithCompanyCredits ------"""
CompanyCreditCategoryWithCompanyCredits = {
   "category": "CompanyCreditCategory",
   "companyCredits": "CompanyCreditConnection",
   "restriction": "CompanyCreditRestriction",
}

"""
----------------- CompanyCreditRestriction -----------------
Information about restrictions applied to Company Credits
------------------------------------------------------------
"""
CompanyCreditRestriction = {
   "explanations": "RestrictionExplanation",  # (Not Null)
   "reasons": str,  # (Not Null)
   "restrictionReason": str,  # (Not Null)
   "unrestrictedTotal": int,
}

"""
----------------- CompanyEmployeeOccupation ----------------
The occupation the client held while employed by the company
------------------------------------------------------------
"""
CompanyEmployeeOccupation = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""
------------------- CompanyEmployeeTitle -------------------
The title a company employee held while working for a
company
------------------------------------------------------------
"""
CompanyEmployeeTitle = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""
--------------------- CompanyEmployment --------------------
The employment relationship a staff member has with a
company
------------------------------------------------------------
"""
CompanyEmployment = {
   "branch": "EmployeeBranchName",
   "occupation": "CompanyEmployeeOccupation",  # (Not Null)
   "title": "CompanyEmployeeTitle",  # (Not Null)
}

"""
------------------------ CompanyJob ------------------------
The job for a company credit that has detail beyond the job
category, free form text
------------------------------------------------------------
"""
CompanyJob = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""
---------------------- CompanyKeyStaff ---------------------
A key staff memeber of a company
------------------------------------------------------------
"""
CompanyKeyStaff = {
   "name": "NameLimited",  # (Not Null)
   "summary": "CompanyKeyStaffSummary",  # (Not Null)
}

"""
------------------ CompanyKeyStaffSummary ------------------
A summary of the relationship a company has a the key staff
member
------------------------------------------------------------
"""
CompanyKeyStaffSummary = {
   "employment": "CompanyEmployment",  # (Not Null)
}

"""
------------------- CompanyKnownForClient ------------------
A known for client for a company
------------------------------------------------------------
"""
CompanyKnownForClient = {
   "name": "NameLimited",  # (Not Null)
   "summary": "CompanyKnownForClientSummary",  # (Not Null)
}

"""
--------------- CompanyKnownForClientSummary ---------------
A summary of the relationship the company has with the
client it is known for
------------------------------------------------------------
"""
CompanyKnownForClientSummary = {
   "representation": "CompanyRepresentationCategory",  # (Not Null)
   "representationCategories": "CompanyRepresentationCategories",  # (Not Null)
}

"""
--------------- CompanyKnownForCreditCategory --------------
The job category for a company credit
------------------------------------------------------------
"""
CompanyKnownForCreditCategory = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""
-------------------- CompanyKnownForJob --------------------
The job a company did on a particular known for
------------------------------------------------------------
"""
CompanyKnownForJob = {
   "category": "CompanyKnownForCreditCategory",  # (Not Null)
   "job": "CompanyJob",
}

"""
------------------- CompanyKnownForTitle -------------------
A Known for title for a company
------------------------------------------------------------
"""
CompanyKnownForTitle = {
   "summary": "CompanyKnownForTitleSummary",  # (Not Null)
   "title": "TitleLimited",  # (Not Null)
}

"""
---------------- CompanyKnownForTitleSummary ---------------
A summary of the relationship a company has with a title it
is known for
------------------------------------------------------------
"""
CompanyKnownForTitleSummary = {
   "countries": "DisplayableCountry",  # (Not Null)
   "jobs": "CompanyKnownForJob",  # (Not Null)
   "yearRange": "YearRange",
}

"""------------------- CompanyMetadata ------------------"""
CompanyMetadata = {
   "companyCreditCategories": "CompanyCreditCategory",  # (Not Null)
}

"""----------------- CompanyMeterRanking ----------------"""
CompanyMeterRanking = {
   "currentRank": int,  # (Not Null)
   "rankChange": "MeterRankChange",
}

"""------------- CompanyMeterRankingHistory -------------"""
CompanyMeterRankingHistory = {
   "bestRank": "MeterRankingHistoryEntry",
   "ranks": "MeterRankingHistoryEntry",  # (Not Null)
   "restriction": "MeterRestriction",
}

"""
-------------- CompanyRepresentationCategories -------------
A breakdown of a type of representative that represents this
client
------------------------------------------------------------
"""
CompanyRepresentationCategories = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
   "total": int,  # (Not Null)
}

"""
--------------- CompanyRepresentationCategory --------------
The type of client representation a company performed for a
client
------------------------------------------------------------
"""
CompanyRepresentationCategory = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""--------------------- CompanyText --------------------"""
CompanyText = {
   "text": str,  # (Not Null)
}

"""
------------------------ CompanyType -----------------------
The type of a company
------------------------------------------------------------
"""
CompanyType = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""---------- ConnectionCategoryWithConnections ---------"""
ConnectionCategoryWithConnections = {
   "category": "TitleConnectionCategory",  # (Not Null)
   "connections": "TitleConnectionConnection",
}

"""----------------------- Consent ----------------------"""
Consent = {
    "consentOperation": str,
    "consentType": str,
    "expirationDate": str,
}

"""------------------- ContentWarnings ------------------"""
ContentWarnings = {
   "isPrimarilyAdultActor": bool,  # (Not Null)
}

"""
--------------------- ContributionLink ---------------------
Contains the URL for contributing to this data type. Is a
type for extendability.
------------------------------------------------------------
"""
ContributionLink = {
   "url": str,  # (Not Null)
}

"""
----------------- ContributionQuestionsLink ----------------
Contains the URL for contributing via Answers. Is a type for
extendability.
------------------------------------------------------------
"""
ContributionQuestionsLink = {
   "url": str,  # (Not Null)
}

"""--------------------- Contributor --------------------"""
Contributor = {
   "id": str,  # (Not Null)
   "user": "UserProfile",
}

"""--------------- ContributorLeaderboard ---------------"""
ContributorLeaderboard = {
   "description": "LocalizedString",
   "id": str,  # (Not Null)
   "isFinalized": bool,  # (Not Null)
   "lastUpdated": str,  # (Not Null)
   "leaderboardUrl": str,  # (Not Null)
   "month": int,
   "period": "ContributorLeaderboardPeriodType",  # (Not Null)
   "rankings": "ContributorRankingsConnection",  # (Not Null)
   "title": "LocalizedString",  # (Not Null)
   "totalApprovedItems": int,  # (Not Null)
   "totalContributors": int,  # (Not Null)
   "year": int,
}

"""---------- ContributorLeaderboardPeriodType ----------"""
ContributorLeaderboardPeriodType = {
   "id": str,  # (Not Null)
}

"""------------- ContributorLeaderboardRank -------------"""
ContributorLeaderboardRank = {
   "leaderboard": "ContributorLeaderboard",  # (Not Null)
   "ranking": "ContributorRank",  # (Not Null)
}

"""--------------- ContributorLeaderboards --------------"""
ContributorLeaderboards = {
   "all": "ContributorLeaderboardConnection",  # (Not Null)
   "allTime": "ContributorLeaderboard",
   "month": "ContributorLeaderboard",
   "months": "ContributorLeaderboardConnection",  # (Not Null)
   "year": "ContributorLeaderboard",
   "years": "ContributorLeaderboardConnection",  # (Not Null)
}

"""------------------- ContributorRank ------------------"""
ContributorRank = {
   "approvedItems": int,  # (Not Null)
   "approvedItemsDelta": int,
   "contributor": "Contributor",
   "id": str,  # (Not Null)
   "rank": int,  # (Not Null)
   "rankDelta": int,
}

"""------------------ CountriesOfOrigin -----------------"""
CountriesOfOrigin = {
   "countries": "CountryOfOrigin",  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
}

"""-------------- CountryAttributeMetadata --------------"""
CountryAttributeMetadata = {
   "limit": int,
   "validValues": "LocalizedDisplayableCountry",  # (Not Null)
}

"""------------------- CountryOfOrigin ------------------"""
CountryOfOrigin = {
   "displayableProperty": "DisplayableTitleCountryOfOriginProperty",  # (Not Null)
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""
------------------------ CrazyCredit -----------------------
Crazy credit details
------------------------------------------------------------
"""
CrazyCredit = {
   "displayableArticle": "DisplayableArticle",  # (Not Null)
   "id": str,  # (Not Null)
   "interestScore": "InterestScore",  # (Not Null)
   "text": "Markdown",  # (Not Null)
}

"""----------- CreateAccountRedirectURLOutput -----------"""
CreateAccountRedirectURLOutput = {
   "redirectURL": str,  # (Not Null)
}

"""-------------------- CreativeSize --------------------"""
CreativeSize = {
   "height": int,  # (Not Null)
   "width": int,  # (Not Null)
}

"""
-------------------------- Credit -------------------------
Credit details. Open question: do we want
to add a persistent ID for credits?
Without this we require a nameID, titleID 
and Category to uniquely identify it.
------------------------------------------------------------
"""
Credit = {
    "category": "CreditCategory",
    "name": "NameLimited",
    "title": "TitleLimited",
}

"""------------------- CreditAttribute ------------------"""
CreditAttribute = {
    "id": str,
    "text": str,
    "language": "DisplayableLanguage",
    "*SeriesCreditAttribute": "SeriesCreditAttribute",
}

"""------------------- CreditCategory -------------------"""
CreditCategory = {
   "categoryId": str,
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""---------------- CreditCategorySummary ---------------"""
CreditCategorySummary = {
   "category": "CreditCategory",  # (Not Null)
   "total": int,  # (Not Null)
}

"""-------------------- CreditedRole --------------------"""
CreditedRole = {
   "attributes": "CreditAttribute",  # (Not Null)
   "category": "CreditCategory",  # (Not Null)
   "characters": "CharacterConnection",
   "episodeCredits": "CreditV2LimitedConnection",
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",
   "text": str,
}

"""---------------- CreditedWithNameItem ----------------"""
CreditedWithName = {
   "name": "NameLimited",  # (Not Null)
}

"""
---------------------- CreditGrouping ----------------------
Credits are assigned to exactly one category, but may be
displayed in different groupings to better represent talent
contributions. These groupings provide flexible presentation
of credits that may differ from their strict categorical
classification.
------------------------------------------------------------
"""
CreditGrouping = {
   "groupingId": str,  # (Not Null)
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""----------------- CreditGroupingNode -----------------"""
CreditGroupingNode = {
   "credits": "CreditV2LimitedConnection",
   "grouping": "CreditGrouping",  # (Not Null)
   "hierarchy": "CreditHierarchy",
}

"""
---------------------- CreditHierarchy ---------------------
Captures details of the hierarchy of credits, for credit
groups that support a hierarchy. Two examples where this
exists today: * Writer
(https://help.imdb.com/article/contribution/filmography-
credits/writers/GPLAT3NTCGA67A6R#)   * This category
supports a three-level hierarchy. The levels are named
"WriterFamily", "WriterTeam", and "WriterTeamMember".   *
Documentation below shows examples of this hierarchy * Cast
(https://help.imdb.com/article/contribution/filmography-
credits/how-are-cast-credits-ordered-why-don-t-the-main-
stars-appear-at-the-top-of-the-cast/G39K5N4YYV2QJ4GR)   *
These credits are vended as a collection of ordered credits,
followed by a collection of unordered credits.     Our
hierarchy here is therefore one level deep, with up to two
expected levelKeys at that level.   * Concretely we would
see a hierarchy of the form:      [Root]       /\      /  \
A    B        # CastGrouping    /|    /|\   / |   / | \  C
D  E  F  G    # CastMember   * In this example, C and D
would be cast members with an order number associated with
them. E, F, G would have no    associated order, and so are
in the second CastGrouping.
------------------------------------------------------------
"""
CreditHierarchy = {
   "levelDetails": "CreditHierarchyLevelDetail",  # (Not Null)
   "levels": str,  # (Not Null)
}

"""
------------------- CreditHierarchyDetail ------------------
Captures an individual CreditV2's position within a credit
group's hierarchy. This type captures the position within a
single level of the hierarchy. An array of these can
identify a credit's unique position within a multi-level
hierarchy. Values are zero-indexed. For example, for the
Writer credit group (with levels "WriterFamily",
"WriterTeam", "WriterTeamMember"), and hierarchy of shape:
[Root]       |       A          # WriterFamily      / \
/   \    B     C       # WriterTeam   /|    /|\  / |   / | \
D  E  F  G  H    # WriterTeamMember  Node "F" would have
values: `[    { "level": "WriterFamily", "position": 0 },
{ "level": "WriterTeam", "position": 1 },    { "level":
"WriterTeamMember", "position": 0 }  ]`
------------------------------------------------------------
"""
CreditHierarchyDetail = {
   "level": str,  # (Not Null)
   "position": int,  # (Not Null)
}

"""------------- CreditHierarchyLevelDetail -------------"""
CreditHierarchyLevelDetail = {
   "childCount": int,  # (Not Null)
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "levelsKey": str,
   "text": "Markdown",  # (Not Null)
}

"""
--------------------- CreditRestriction --------------------
Information about restrictions applied to Credits
------------------------------------------------------------
"""
CreditRestriction = {
   "explanations": "RestrictionExplanation",  # (Not Null)
   "reasons": str,  # (Not Null)
   "restrictionReason": str,  # (Not Null)
   "unrestrictedTotal": int,
}

"""-------------- CreditsCompletenessStatus -------------"""
CreditsCompletenessStatus = {
   "id": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""------------------ CreditsOrderedBy ------------------"""
CreditsOrderedBy = {
   "id": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""
------------------------- CreditV2 -------------------------
Details of a credit for a name on a title. Distinct from
Company Credits or Crazy Credits. Successor to Credit type.
Denotes the role(s) a person had on a title. Fields within
this record may be aggregations or summaries of work done,
depending on how the data was requested.  When requesting
credits for a series, roles performed on the episodes of
that series are rolled up to the series level. Each rolled-
up role comes with its own listing of the episodes that the
role was performed on. If the attributes of a role are not
shared across all episodes, we drop that detail. * Example:
Kaley Cuoco (nm0192505) was credited as Kaley Cuoco-Sweeting
for some but not all episodes of The Big Bang Theory
(tt0898266). When viewing credits at the series level, this
attribute is dropped. The attribute is still present at an
episode level.  Characters and CreditedRoles for a series
are ordered by most recent value first. This ensures a
person's most recent contribution to a title (and so the
work they are most likely to demonstrate their skillset) is
shown first. This also helps to highlight the roles that
users are likely to be exploring, particularly for long-
running shows where acting roles change over time (for
example, Saturday Night Live). Note that the ordering of
these fields differs when using name.knownForV2 (see its
documentation for details).  Appearance credits (such as
acting and self-appearances) are contributed to IMDb's
catalog as a single credit per title. * Example: Ryan
Reynolds (nm0005351) plays Deadpool and Nicepool in Deadpool
& Wolverine (tt6263850). This is different to crew credits,
where a single person can have many roles on a title, even
within a single credit category. * Example: Hugh Wilson
(nm0933505) is both screenplay and story writer for Down
Periscope (tt0116130), and these are captured in the catalog
as separate credits.  The CreditV2 shape maintains this
distinction. For appearance credits, the individual roles
played can be accessed individually from the
`CreditV2.creditedRoles.characters` field.  When a person
performs different appearance roles across episodes in a TV
series, we maintain this cast-specific difference in data
shape. All appearance work is aggregated into a single
CreditV2 entry, with a single `creditedRoles.text` value
that includes up to 100 roles, and all roles available in
the `characters` field. * Example: Kaley Cuoco (nm0192505)
plays two different roles across episodes in The Big Bang
Theory (tt0898266). This is vended at the series level as a
single credit with one `creditedRoles.text` ("Penny/Penny
Hofstatder") and two character values (["Penny", "Penny
Hofstatder"]). Character names are ordered by their
frequency across episodes, then by which occurs first in
release order.
------------------------------------------------------------
"""
CreditV2 = {
   "creditedRoles": "CreditedRoleConnection",
   "episodeCredits": "CreditV2LimitedConnection",
   "hierarchyDetails": "CreditHierarchyDetail",  # (Not Null)
   "id": str,  # (Not Null)
   "name": "NameLimited",  # (Not Null)
   "title": "TitleLimited",  # (Not Null)
}

CreditV2Limited = {
   "hierarchyDetails": "CreditHierarchyDetail",  # (Not Null)
   "id": str,  # (Not Null)
   "name": "NameLimited",  # (Not Null)
   "title": "TitleLimited",  # (Not Null)
}

"""
-------------------- CroppingParameters --------------------
Parameters used to define how an image should be cropped
------------------------------------------------------------
"""
CroppingParameters = {
   "height": int,  # (Not Null)
   "width": int,  # (Not Null)
   "xOffset": int,  # (Not Null)
   "yOffset": int,  # (Not Null)
}

"""
------------------- CustomFeaturedImages -------------------
Featured images that customer selected manually
------------------------------------------------------------
"""
CustomFeaturedImages = {
   "images": "ImageLimited",  # (Not Null)
   "isAdminEdited": bool,  # (Not Null)
   "isAdminNotificationSeen": bool,  # (Not Null)
   "isBlocked": bool,  # (Not Null)
   "isPublished": bool,  # (Not Null)
   "isReset": bool,  # (Not Null)
   "lastEdited": str,
   "lastEditedByAdmin": str,
}

"""
---------------------- CustomKnownFor ----------------------
Known for titles that customer selected manually
------------------------------------------------------------
"""
CustomKnownFor = {
   "isAdminEdited": bool,  # (Not Null)
   "isAdminNotificationSeen": bool,  # (Not Null)
   "isBlocked": bool,  # (Not Null)
   "isPublished": bool,  # (Not Null)
   "isReset": bool,  # (Not Null)
   "lastEdited": str,
   "lastEditedByAdmin": str,
   "titles": "TitleLimited",  # (Not Null)
}

"""
-------------------- CustomPrimaryImage --------------------
Primary image that the name owner had edited
------------------------------------------------------------
"""
CustomPrimaryImage = {
   "imageEditParameters": "ImageEditParameters",
   "originalImage": "ImageLimited",  # (Not Null)
}

"""
---------------------- DateComponents ----------------------
A type to represent dates that cannot be represented in ISO
8601 format, e.g. missing year in 23 March.
------------------------------------------------------------
"""
DateComponents = {
   "day": int,
   "isApproximate": bool,  # (Not Null)
   "isBCE": bool,  # (Not Null)
   "month": int,
   "partialYear": str,
   "year": int,
}

"""--------------------- DeathCause ---------------------"""
DeathCause = {
    "id": str,  # (Not NULL)
    "language": "DisplayableLanguage",  # (Not NULL)
    "text": str,
}

"""---------------- DeletionDialogOutput ----------------"""
DeletionDialogOutput = {
   "deletionPrompt": "LocalizedMarkdown",  # (Not Null)
   "redirectionPrompt": "DeletionDialogRedirectionPrompt",
   "requestId": str,
}

"""----------- DeletionDialogRedirectionPrompt ----------"""
DeletionDialogRedirectionPrompt = {
   "action": "RedirectLink",  # (Not Null)
   "message": "LocalizedMarkdown",  # (Not Null)
}

"""--------------------- Demographic --------------------"""
Demographic = {
   "age": str,
   "country": str,
   "displayText": "LocalizedString",  # (Not Null)
   "gender": str,
   "userCategory": str,
}

"""
----------------- DemographicDataComponent -----------------
A single component of a demographic data value
------------------------------------------------------------
"""
DemographicDataComponent = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""
-------------------- DemographicDataItem -------------------
A single demographic data item
------------------------------------------------------------
"""
DemographicDataItem = {
   "selfVerified": "SelfVerified",  # (Not Null)
   "type": "DemographicDataType",  # (Not Null)
   "value": "DemographicDataValue",  # (Not Null)
}

"""
-------------------- DemographicDataType -------------------
A single demographic data type
------------------------------------------------------------
"""
DemographicDataType = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
   "value": str,  # (Not Null)
}

"""
------------------- DemographicDataValue -------------------
A single demographic data value
------------------------------------------------------------
"""
DemographicDataValue = {
   "components": "DemographicDataComponent",  # (Not Null)
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""----------------- DemographicRatings -----------------"""
DemographicRatings = {
   "aggregate": float,
   "demographic": "Demographic",  # (Not Null)
   "voteCount": int,  # (Not Null)
}

"""---------------- DirectContactDetails ----------------"""
DirectContactDetails = {
   "emailAddress": str,
   "faxNumber": "LocalizedString",
   "phoneNumbers": "LocalizedString",  # (Not Null)
   "website": "WebsiteLink",
}

"""------------------- Disambiguation -------------------"""
Disambiguation = {
   "number": int,  # (Not Null)
   "text": str,  # (Not Null)
}

"""
-------------------- DisplayableArticle --------------------
Generic type for a display-ready article representation of
the parent type
------------------------------------------------------------
"""
DisplayableArticle = {
   "body": "Markdown",
   "footer": "Markdown",
   "header": "Markdown",
}

"""
------------------- DisplayableAttribute -------------------
Generic type for a concept which has display text and an
optional ID
------------------------------------------------------------
"""
DisplayableAttribute = {
   "id": str,
   "text": str,  # (Not Null)
}

"""------------ DisplayableBirthNameProperty ------------"""
DisplayableBirthNameProperty = {
   "value": "Markdown",  # (Not Null)
}

"""
-------------------- DisplayableCountry --------------------
Type for the display of a country
------------------------------------------------------------
"""
DisplayableCountry = {
   "id": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""------------------- DisplayableDate ------------------"""
DisplayableDate = {
   "date": str,
   "dateComponents": "DateComponents",
   "displayableProperty": "DisplayableDateProperty",  # (Not Null)
}

"""--------------- DisplayableDateProperty --------------"""
DisplayableDateProperty = {
   "language": "DisplayableLanguage",  # (Not Null)
   "value": "Markdown",  # (Not Null)
}

"""---------------- DisplayableDateRange ----------------"""
DisplayableDateRange = {
   "endDate": "DisplayableDate",
   "startDate": "DisplayableDate",
}

"""-------------- DisplayableEpisodeNumber --------------"""
DisplayableEpisodeNumber = {
   "displayableSeason": "LocalizedDisplayableSeason",  # (Not Null)
   "episodeNumber": "LocalizedDisplayableEpisodeNumber",  # (Not Null)
}

"""----------- DisplayableExternalLinkProperty ----------"""
DisplayableExternalLinkProperty = {
   "value": "Markdown",  # (Not Null)
}

"""----------------- DisplayableLanguage ----------------"""
DisplayableLanguage = {
   "id": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""----------------- DisplayableLocation ----------------"""
DisplayableLocation = {
   "displayableProperty": "DisplayableLocationProperty",  # (Not Null)
   "text": str,
}

"""------------- DisplayableLocationProperty ------------"""
DisplayableLocationProperty = {
   "language": "DisplayableLanguage",  # (Not Null)
   "value": "Markdown",  # (Not Null)
}

"""---------- DisplayableNameAgeDetailsProperty ---------"""
DisplayableNameAgeDetailsProperty = {
   "value": "Markdown",  # (Not Null)
}

"""
---------------- DisplayableNameAkaProperty ----------------
Name AKA as a Displayable Property
------------------------------------------------------------
"""
DisplayableNameAkaProperty = {
   "value": "Markdown",  # (Not Null)
}

"""-------------- DisplayableNameDeathCause -------------"""
DisplayableNameDeathCause = {
   "displayableProperty": "DisplayableNameDeathCauseProperty",  # (Not Null)
   "text": str,
}

"""---------- DisplayableNameDeathCauseProperty ---------"""
DisplayableNameDeathCauseProperty = {
   "language": "DisplayableLanguage",  # (Not Null)
   "value": "Markdown",  # (Not Null)
}

"""------------ DisplayableNameHeightProperty -----------"""
DisplayableNameHeightProperty = {
   "language": "DisplayableLanguage",  # (Not Null)
   "value": "Markdown",  # (Not Null)
}

"""---------- DisplayableNameOtherWorkProperty ----------"""
DisplayableNameOtherWorkProperty = {
   "qualifiersInMarkdownList": "Markdown",  # (Not Null)
   "value": "Markdown",  # (Not Null)
}

"""------------ DisplayableNameSpouseProperty -----------"""
DisplayableNameSpouseProperty = {
   "language": "DisplayableLanguage",  # (Not Null)
   "qualifiersInMarkdownList": "Markdown",  # (Not Null)
   "value": "Markdown",  # (Not Null)
}

"""------------- DisplayableNickNameProperty ------------"""
DisplayableNickNameProperty = {
   "value": "Markdown",  # (Not Null)
}

"""---------------- DisplayableProfession ---------------"""
DisplayableProfession = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""------------ DisplayableProfessionCategory -----------"""
DisplayableProfessionCategory = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""---------- DisplayableProfessionDescription ----------"""
DisplayableProfessionDescription = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""------------------ DisplayablePrompt -----------------"""
DisplayablePrompt = {
   "constId": str,  # (Not Null)
   "display": bool,  # (Not Null)
   "promptType": str,  # (Not Null)
}

"""----------- DisplayableRelationNameProperty ----------"""
DisplayableRelationNameProperty = {
   "value": "Markdown",  # (Not Null)
}

"""-------------- DisplayableSalaryProperty -------------"""
DisplayableSalaryProperty = {
   "key": "Markdown",  # (Not Null)
   "value": "Markdown",  # (Not Null)
}

"""---------------- DisplayableSongTitle ----------------"""
DisplayableSongTitle = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""------------- DisplayableSpouseTimeRange -------------"""
DisplayableSpouseTimeRange = {
   "displayableProperty": "DisplayableSpouseTimeRangeProperty",  # (Not Null)
   "fromDate": "DisplayableDate",
   "toDate": "DisplayableDate",
}

"""--------- DisplayableSpouseTimeRangeProperty ---------"""
DisplayableSpouseTimeRangeProperty = {
   "language": "DisplayableLanguage",  # (Not Null)
   "value": "Markdown",  # (Not Null)
}

"""- DisplayableTechnicalSpecificationLocalizedProperty -"""
DisplayableTechnicalSpecificationLocalizedProperty = {
   "language": "DisplayableLanguage",  # (Not Null)
   "qualifiersInMarkdownList": "Markdown",  # (Not Null)
   "value": "Markdown",  # (Not Null)
}

"""------ DisplayableTechnicalSpecificationProperty -----"""
DisplayableTechnicalSpecificationProperty = {
   "qualifiersInMarkdownList": "Markdown",  # (Not Null)
   "value": "Markdown",  # (Not Null)
}

"""------------- DisplayableTitleAkaProperty ------------"""
DisplayableTitleAkaProperty = {
   "key": "Markdown",  # (Not Null)
   "language": "DisplayableLanguage",
   "qualifiersInMarkdownList": "Markdown",  # (Not Null)
   "value": "Markdown",  # (Not Null)
}

"""
----------- DisplayableTitleCompanyCreditProperty ----------
Company credit displayable property
------------------------------------------------------------
"""
DisplayableTitleCompanyCreditProperty = {
   "qualifiersInMarkdownList": "Markdown",  # (Not Null)
   "value": "Markdown",  # (Not Null)
}

"""------- DisplayableTitleCountryOfOriginProperty ------"""
DisplayableTitleCountryOfOriginProperty = {
   "language": "DisplayableLanguage",  # (Not Null)
   "value": "Markdown",  # (Not Null)
}

"""
---------- DisplayableTitleFilmingLocationProperty ---------
Filming location displayable property
------------------------------------------------------------
"""
DisplayableTitleFilmingLocationProperty = {
   "language": "DisplayableLanguage",
   "qualifiersInMarkdownList": "Markdown",  # (Not Null)
   "value": "Markdown",  # (Not Null)
}

"""
--------------- DisplayableTitleGenreProperty --------------
Genre displayable property
------------------------------------------------------------
"""
DisplayableTitleGenreProperty = {
   "language": "DisplayableLanguage",  # (Not Null)
   "value": "Markdown",  # (Not Null)
}

"""--------- DisplayableTitleReleaseDateProperty --------"""
DisplayableTitleReleaseDateProperty = {
   "key": "Markdown",  # (Not Null)
   "qualifiersInMarkdownList": "Markdown",  # (Not Null)
   "value": "Markdown",  # (Not Null)
}

"""----------- DisplayableTitleRuntimeProperty ----------"""
DisplayableTitleRuntimeProperty = {
   "language": "DisplayableLanguage",  # (Not Null)
   "qualifiersInMarkdownList": "Markdown",  # (Not Null)
   "value": "Markdown",  # (Not Null)
}

"""------- DisplayableTitleSpokenLanguageProperty -------"""
DisplayableTitleSpokenLanguageProperty = {
   "language": "DisplayableLanguage",  # (Not Null)
   "value": "Markdown",  # (Not Null)
}

"""
-------------- DisplayableTitleTaglineProperty -------------
Tagline displayable property
------------------------------------------------------------
"""
DisplayableTitleTaglineProperty = {
   "value": "Markdown",  # (Not Null)
}

"""------------ DisplayableTitleTypeProperty ------------"""
DisplayableTitleTypeProperty = {
   "value": "Markdown",  # (Not Null)
}

"""-------------------- DisplayLabels -------------------"""
DisplayLabels = {
   "primaryLabel": str,  # (Not Null)
   "secondaryLabel": str,
}

"""
--------------------- DistanceToCinema ---------------------
The distance from a requested location to a cinema.
------------------------------------------------------------
"""
DistanceToCinema = {
   "distanceInMeters": int,  # (Not Null)
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""
-------------------- DistributionFormat --------------------
The distribution format of a title
------------------------------------------------------------
"""
DistributionFormat = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

Employment = {
    "branch": "CompanyBranch",
    "company": "Company",
    "employeeContact": "CompanyContactDetails",
    "id": str,  # (Not Null)
    "jobTitle": "LocalizedString",
    "name": "NameLimited",  # (Not Null)
    "occupation": "OccupationValue",
}

"""----------------- EmployeeBranchName -----------------"""
EmployeeBranchName = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""---------------- EngagementStatistics ----------------"""
EngagementStatistics = {
   "followerStatistics": "FollowerStatistics",
   "watchlistStatistics": "WatchlistStatistics",
}

"""---------- EpisodeNumberDisplayableProperty ----------"""
EpisodeNumberDisplayableProperty = {
   "value": "Markdown",  # (Not Null)
}

"""---------------------- Episodes ----------------------"""
Episodes = {
   "displayableSeasons": "LocalizedDisplayableSeasonConnection",
   "displayableYears": "LocalizedDisplayableEpisodeYearConnection",
   "episodes": "EpisodeConnection",
   "isOngoing": bool,
}

"""---------------------- Episode -----------------------"""
Episode = TitleLimited

"""
----------------------- EventEdition -----------------------
The instance of an event that took place in a specific year
------------------------------------------------------------
"""
EventEdition = {
   "awards": "AwardDetailsLimitedConnection",
   "event": "AwardsEvent",  # (Not Null)
   "id": str,  # (Not Null)
   "instanceWithinYear": int,  # (Not Null)
   "trivia": "Markdown",  # (Not Null)
   "year": int,  # (Not Null)
}

EventEditionLimited = {
   "id": str,  # (Not Null)
   "instanceWithinYear": int,  # (Not Null)
   "trivia": "Markdown",  # (Not Null)
   "year": int,  # (Not Null)
}

"""
--------------------- EventEditionAward --------------------
Data for a combination of Event Edition and Award.
------------------------------------------------------------
"""
EventEditionAward = {
   "awardName": str,  # (Not Null)
   "id": str,  # (Not Null)
   "winners": "AwardNomination",  # (Not Null)
}

"""------------------ EventLiveResults ------------------"""
EventLiveResults = {
   "displayDescription": "LocalizedString",
   "displayTitle": "LocalizedString",  # (Not Null)
   "eventEditionAward": "EventEditionAward",  # (Not Null)
   "eventId": str,  # (Not Null)
   "eventPageUrl": str,
   "noWinnersBlurb": "LocalizedString",  # (Not Null)
}

"""-------------------- EventMetadata -------------------"""
EventMetadata = {
   "event": "AwardsEvent",
   "events": "AwardsEventConnection",
}

"""---------------------- EventUrl ----------------------"""
EventUrl = {
   "category": "EventUrlCategory",  # (Not Null)
   "url": str,  # (Not Null)
}

"""------------------ EventUrlCategory ------------------"""
EventUrlCategory = {
   "categoryId": str,  # (Not Null)
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""---------- Experimental_AdditionalCreditItem ---------"""
Experimental_AdditionalCreditItem = {
   "category": "LocalizedString",  # (Not Null)
   "details": "LocalizedString",  # (Not Null)
   "id": str,  # (Not Null)
   "job": "LocalizedString",  # (Not Null)
   "title": "LocalizedString",  # (Not Null)
}

"""---------- Experimental_AdditionalResumeInfo ---------"""
Experimental_AdditionalResumeInfo = {
   "details": "LocalizedString",
   "id": str,  # (Not Null)
   "title": "LocalizedString",
}

"""
---------------- Experimental_AdProductType ----------------
Product type information for an ad
------------------------------------------------------------
"""
Experimental_AdProductType = {
   "grade": str,  # (Not Null)
   "name": str,  # (Not Null)
   "symbol": str,  # (Not Null)
}

"""
-------------------- Experimental_Agency -------------------
@experimental Experimental: DO NOT USE"  An agency that
represents a name
------------------------------------------------------------
"""
Experimental_Agency = {
   "company": "Company",  # (Not Null)
   "experimental_agents": "Experimental_Agent",  #
}

"""
-------------------- Experimental_Agent --------------------
@experimental Experimental: DO NOT USE"  An employee of a
company who represents a name in some capacity
------------------------------------------------------------
"""
Experimental_Agent = {
   "branch": "Experimental_CompanyBranch",
   "company": "Company",  # (Not Null)
   "experimental_employeeContact": "Experimental_CompanyContactDetails",
   "id": str,  # (Not Null)
   "isPrimaryAgent": bool,  # (Not Null)
   "jobTitle": "LocalizedString",
   "name": "NameLimited",  # (Not Null)
   "occupation": "OccupationValue",
   "relationshipType": "Experimental_RepresentationRelationshipType",  # (Not Null)
}

"""
----------------- Experimental_ApsSlotInfo -----------------
Information about an APS slot for Amazon Publisher Services
integration
------------------------------------------------------------
"""
Experimental_ApsSlotInfo = {
   "apsSlotId": str,  # (Not Null)
   "apsSlotName": str,  # (Not Null)
   "apsSlotParams": "Experimental_ApsSlotParam",  # (Not Null)
   "slotName": str,  # (Not Null)
}

"""
----------------- Experimental_ApsSlotParam ----------------
Key-value pair for APS slot parameters
------------------------------------------------------------
"""
Experimental_ApsSlotParam = {
   "key": str,  # (Not Null)
   "value": str,  # (Not Null)
}

"""
---------------- Experimental_CompanyBranch ----------------
@experimental Experimental: DO NOT USE
------------------------------------------------------------
"""
Experimental_CompanyBranch = {
   "experimental_directContact": "Experimental_CompanyContactDetails",
   "id": str,  # (Not Null)
   "name": "LocalizedString",
}

"""------------- Experimental_CompanyClient -------------"""
Experimental_CompanyClient = {
   "client": "NameLimited",  # (Not Null)
   "experimental_agents": "Experimental_Agent",  #
   "id": str,  # (Not Null)
}

"""
------------ Experimental_CompanyContactDetails ------------
@experimental Experimental: DO NOT USE
------------------------------------------------------------
"""
Experimental_CompanyContactDetails = {
   "emailAddress": str,
   "faxNumber": "LocalizedString",
   "phoneNumbers": "LocalizedString",  # (Not Null)
   "physicalAddress": "Location",
   "website": "WebsiteLink",
}

"""---------- Experimental_DirectContactDetails ---------"""
Experimental_DirectContactDetails = {
   "emailAddress": str,
   "faxNumber": "LocalizedString",
   "phoneNumbers": "LocalizedString",  # (Not Null)
   "website": "WebsiteLink",
}

"""
-------------- Experimental_NameRepresentation -------------
@experimental Experimental: DO NOT USE
------------------------------------------------------------
"""
Experimental_NameRepresentation = {
   "client": "NameLimited",  # (Not Null)
   "experimental_agency": "Experimental_Agency",
   "id": str,  # (Not Null)
   "independentRepresentative": "NameLimited",
   "relationshipType": "Experimental_RepresentationRelationshipType",  # (Not Null)
}

"""--------- Experimental_NotificationPreference --------"""
Experimental_NotificationPreference = {
   "interested": bool,  # (Not Null)
   "type": "Experimental_NotificationPreferenceType",  # (Not Null)
}

"""
---------- Experimental_NotificationPreferenceType ---------
Preference type for a tracked page
------------------------------------------------------------
"""
Experimental_NotificationPreferenceType = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""
-------------- Experimental_PersonalEmployment -------------
@experimental Experimental: DO NOT USE
------------------------------------------------------------
"""
Experimental_PersonalEmployment = {
   "branch": "Experimental_CompanyBranch",
   "company": "Company",  # (Not Null)
   "experimental_employeeContact": "Experimental_CompanyContactDetails",
   "id": str,  # (Not Null)
   "jobTitle": "LocalizedString",
   "name": "NameLimited",  # (Not Null)
   "occupation": "OccupationValue",
}

"""
---------------- Experimental_PlaidOverride ----------------
Key-value pair for plaid overrides
------------------------------------------------------------
"""
Experimental_PlaidOverride = {
   "key": str,  # (Not Null)
   "value": str,  # (Not Null)
}

"""
-------- Experimental_RepresentationRelationshipType -------
@experimental Experimental: DO NOT USE
------------------------------------------------------------
"""
Experimental_RepresentationRelationshipType = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "relationshipTypeId": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""----------------- Experimental_Resume ----------------"""
Experimental_Resume = {
   "experimental_additionalAwards": "Experimental_SelfVerifiedAwardConnection",
   "experimental_additionalCreditCategories": "Experimental_ResumeAdditionalCreditsCategories",
   "experimental_additionalCredits": "Experimental_AdditionalCreditItemConnection",
   "experimental_additionalResumeInfo": "Experimental_AdditionalResumeInfoConnection",
   "experimental_education": "Experimental_SelfVerifiedEducationConnection",
   "experimental_performerProfile": "Experimental_ResumeDataItem",  # (Not Null)
   "experimental_personalDetails": "Experimental_ResumeDataItem",  # (Not Null)
   "experimental_professionalBackground": "Experimental_ResumeDataItem",  # (Not Null)
   "experimental_references": "Experimental_SelfVerifiedReferenceConnection",
   "experimental_skills": "Experimental_ResumeDataItem",  # (Not Null)
   "experimental_training": "Experimental_SelfVerifiedTrainingConnection",
}

"""--- Experimental_ResumeAdditionalCreditsCategories ---"""
Experimental_ResumeAdditionalCreditsCategories = {
   "categories": "Experimental_ResumeAdditionalCreditsCategory",  # (Not Null)
   "total": int,  # (Not Null)
}

"""---- Experimental_ResumeAdditionalCreditsCategory ----"""
Experimental_ResumeAdditionalCreditsCategory = {
   "credits": "Experimental_AdditionalCreditItem",  # (Not Null)
   "id": str,  # (Not Null)
   "title": "LocalizedString",  # (Not Null)
   "total": int,  # (Not Null)
}

"""------------- Experimental_ResumeDataItem ------------"""
Experimental_ResumeDataItem = {
   "label": "LocalizedString",  # (Not Null)
   "values": "LocalizedString",  # (Not Null)
}

"""----------- Experimental_SelfVerifiedAward -----------"""
Experimental_SelfVerifiedAward = {
   "awardTitle": "LocalizedString",
   "details": "LocalizedString",
   "event": "LocalizedString",
   "id": str,  # (Not Null)
   "year": int,
}

"""--------- Experimental_SelfVerifiedEducation ---------"""
Experimental_SelfVerifiedEducation = {
   "degree": "LocalizedString",
   "details": "LocalizedString",
   "id": str,  # (Not Null)
   "location": "LocalizedString",
   "school": "LocalizedString",
   "year": int,
}

"""--------- Experimental_SelfVerifiedReference ---------"""
Experimental_SelfVerifiedReference = {
   "contact": str,
   "id": str,  # (Not Null)
   "name": "LocalizedString",
   "relationship": "LocalizedString",
}

"""---------- Experimental_SelfVerifiedTraining ---------"""
Experimental_SelfVerifiedTraining = {
   "details": "LocalizedString",
   "id": str,  # (Not Null)
   "instructor": "LocalizedString",
   "location": "LocalizedString",
   "school": "LocalizedString",
   "training": "LocalizedString",
   "year": int,
}

"""------ Experimental_TrackNotificationPreferences -----"""
Experimental_TrackNotificationPreferences = {
   "isTracking": bool,  # (Not Null)
   "notificationPreferences": "Experimental_NotificationPreference",  # (Not Null)
}

"""
-------------- Experimental_WebAdCreativeInfo --------------
AdCreativeInfo with additional web/responsive fields. Can be
merge into single definition when finalizing webAdsConfig
------------------------------------------------------------
"""
Experimental_WebAdCreativeInfo = {
   "aaxAdType": str,
   "adProductType": "Experimental_AdProductType",
   "creativeId": str,
   "hasAutoplay": bool,  # (Not Null)
   "isEligibleFor3pAd": bool,  # (Not Null)
   "isPremium": bool,  # (Not Null)
   "plaidOverrides": "Experimental_PlaidOverride",  # (Not Null)
   "responsiveResizingDisabledRange": str,
   "shouldFitToWidth": bool,  # (Not Null)
   "size": "CreativeSize",  # (Not Null)
   "slotMarkup": str,  # (Not Null)
}

"""
-------------- Experimental_WebAdFetchingInfo --------------
Information needed to fetch ads client-side
------------------------------------------------------------
"""
Experimental_WebAdFetchingInfo = {
   "endpoint": str,  # (Not Null)
   "params": str,
   "query": str,  # (Not Null)
}

"""
-------------- Experimental_WebAdsConfigOutput -------------
Output from the webAdsConfig operation containing all
information needed to request ads
------------------------------------------------------------
"""
Experimental_WebAdsConfigOutput = {
   "adFetchingInfo": "Experimental_WebAdFetchingInfo",  # (Not Null)
   "adRefreshEnabled": bool,  # (Not Null)
   "apsSlotInfoMap": "Experimental_ApsSlotInfo",  # (Not Null)
   "hasPremiumAd": bool,  # (Not Null)
   "headerMarkup": str,  # (Not Null)
   "plaidOverrides": "Experimental_PlaidOverride",  # (Not Null)
   "responsiveSlotSizes": "Experimental_WebResponsiveSlotSize",  # (Not Null)
   "slots": "Experimental_WebAdSlot",  # (Not Null)
   "slotsEnabled": bool,  # (Not Null)
}

"""
------------------ Experimental_WebAdSlot ------------------
AdSlot with additional web fields. Can be merged back into
single AdSlot definition when finalizing webAdsConfig
------------------------------------------------------------
"""
Experimental_WebAdSlot = {
   "abpAcceptable": bool,  # (Not Null)
   "adFeedbackUrl": str,
   "creativeInfo": "Experimental_WebAdCreativeInfo",  # (Not Null)
   "name": str,  # (Not Null)
}

"""
----------------- Experimental_WebAdsOutput ----------------
Output for the webAds query.
------------------------------------------------------------
"""
Experimental_WebAdsOutput = {
   "hasPremiumAd": bool,  # (Not Null)
   "plaidOverrides": "Experimental_PlaidOverride",  # (Not Null)
   "responsiveResizingDisabledSlots": "Experimental_WebResponsiveResizingDisabledSlot",  # (Not Null)
   "slots": "Experimental_WebAdSlot",  # (Not Null)
}

"""
--- Experimental_WebResponsiveResizingDisabledBreakpoint ---
Viewport breakpoint with disabled flag.
------------------------------------------------------------
"""
Experimental_WebResponsiveResizingDisabledBreakpoint = {
   "breakpoint": int,  # (Not Null)
   "disabled": bool,  # (Not Null)
}

"""
------ Experimental_WebResponsiveResizingDisabledSlot ------
Slot with responsive resizing disabled.
------------------------------------------------------------
"""
Experimental_WebResponsiveResizingDisabledSlot = {
   "breakpoints": "Experimental_WebResponsiveResizingDisabledBreakpoint",  # (Not Null)
   "name": str,  # (Not Null)
}

"""
------------ Experimental_WebResponsiveSlotSize ------------
Mapping between slot names and their size configurations for
different viewport breakpoints
------------------------------------------------------------
"""
Experimental_WebResponsiveSlotSize = {
   "breakpoints": "Experimental_WebViewportBreakpointSlotSize",  # (Not Null)
   "slotName": str,  # (Not Null)
}

"""
-------- Experimental_WebViewportBreakpointSlotSize --------
Viewport breakpoint configuration for responsive ad sizing
------------------------------------------------------------
"""
Experimental_WebViewportBreakpointSlotSize = {
   "breakpoint": str,  # (Not Null)
   "slotSize": "CreativeSize",  # (Not Null)
}

"""
-------------------- ExperimentalCredit --------------------
Experimental Field: DO NOT USE. Credit details.
Open question: do we want to add a persistent ID
for credits? Without this we require a
nameID, titleID and Category to uniquely identify it.
------------------------------------------------------------
"""
ExperimentalCredit = {
    "category": "CreditCategory",  # (Not Null)
    "name": "NameLimited",  # (Not Null)
    "title": "TitleLimited",  # (Not Null)
}

"""------ ExperimentalNameCreditCategoryWithCredits -----"""
ExperimentalNameCreditCategoryWithCredits = {
   "category": "CreditCategory",  # (Not Null)
   "credits": "ExperimentalCreditConnection",
}

"""
----------------------- ExternalLink -----------------------
External link details
------------------------------------------------------------
"""
ExternalLink = {
   "displayableProperty": "DisplayableExternalLinkProperty",  # (Not Null)
   "externalLinkCategory": "ExternalLinkCategory",  # (Not Null)
   "externalLinkLanguages": "DisplayableLanguage",  # (Not Null)
   "externalLinkRegion": "DisplayableCountry",
   "id": str,  # (Not Null)
   "label": str,
   "labelLanguage": "DisplayableLanguage",
   "url": str,  # (Not Null)
}

"""
------------------- ExternalLinkCategory -------------------
External link type
------------------------------------------------------------
"""
ExternalLinkCategory = {
   "id": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""-------- ExternalLinkCategoryWithExternalLinks -------"""
ExternalLinkCategoryWithExternalLinks = {
   "category": "ExternalLinkCategory",
   "externalLinks": "ExternalLinkConnection",
   "restriction": "ExternalLinkRestriction",
}

"""
------- ExternalLinkCategoryWithFeaturedExternalLinks ------
Group of external links from a single featured category
------------------------------------------------------------
"""
ExternalLinkCategoryWithFeaturedExternalLinks = {
   "externalLinks": "ExternalLink",  # (Not Null)
   "featuredCategory": "ExternalLinkCategory",  # (Not Null)
}

"""
------------------ ExternalLinkRestriction -----------------
Information about restrictions applied to external links
------------------------------------------------------------
"""
ExternalLinkRestriction = {
   "explanations": "RestrictionExplanation",  # (Not Null)
   "reasons": str,  # (Not Null)
   "restrictionReason": str,  # (Not Null)
   "unrestrictedTotal": int,
}

"""
---------------------------- Faq ---------------------------
Faq details
------------------------------------------------------------
"""
Faq = {
   "answer": "Markdown",
   "id": str,  # (Not Null)
   "isSpoiler": bool,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "question": "Markdown",  # (Not Null)
}

"""-------------------- FeatureAccess -------------------"""
FeatureAccess = {
   "proAppFunctionality": bool,  # (Not Null)
}

"""-------------------- FeedbackGiven -------------------"""
FeedbackGiven = {
   "hasGivenFeedback": bool,  # (Not Null)
}

"""-------------------- FileMetadata --------------------"""
FileMetadata = {
   "accountDataURL": str,  # (Not Null)
   "creationDate": str,  # (Not Null)
   "expirationDate": str,  # (Not Null)
   "name": str,  # (Not Null)
   "sizeLabel": "LocalizedString",  # (Not Null)
}

"""-------------------- FilmingDates --------------------"""
FilmingDates = {
   "dateRange": "DisplayableDateRange",
}

"""
---------------------- FilmingLocation ---------------------
Filming location details
------------------------------------------------------------
"""
FilmingLocation = {
   "attributes": "DisplayableAttribute",  # (Not Null)
   "displayableProperty": "DisplayableTitleFilmingLocationProperty",  # (Not Null)
   "id": str,  # (Not Null)
   "interestScore": "InterestScore",  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "location": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""
---------------- FilmingLocationRestriction ----------------
Information about restrictions applied to filming locations
------------------------------------------------------------
"""
FilmingLocationRestriction = {
   "explanations": "RestrictionExplanation",  # (Not Null)
   "reasons": str,  # (Not Null)
   "restrictionReason": str,  # (Not Null)
   "unrestrictedTotal": int,
}

"""
------------------------ FilmLength ------------------------
A film length or number of reels, or both, along with some
flags and any attributes. For example, we could have a film
that used 3447 meters of film using 8.5 reels in the US and
Canada.
------------------------------------------------------------
"""
FilmLength = {
   "attributes": "DisplayableAttribute",  # (Not Null)
   "countries": "DisplayableCountry",  # (Not Null)
   "displayableProperty": "DisplayableTechnicalSpecificationLocalizedProperty",  # (Not Null)
   "filmLength": float,
   "isSplitReel": bool,  # (Not Null)
   "numReels": float,
}

"""
------------------------ FilmLengths -----------------------
Film lengths for this title.
------------------------------------------------------------
"""
FilmLengths = {
   "items": "FilmLength",  # (Not Null)
   "restriction": "TechnicalSpecificationsRestriction",
   "total": int,  # (Not Null)
}

"""----------------- FollowerStatistics -----------------"""
FollowerStatistics = {
   "displayableCount": "LocalizedDisplayableCount",  # (Not Null)
   "totalCount": int,  # (Not Null)
}

"""----------- ForgotPasswordRedirectURLOutput ----------"""
ForgotPasswordRedirectURLOutput = {
   "redirectURL": str,  # (Not Null)
}

"""------------------- GenderIdentity -------------------"""
GenderIdentity = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

Genre = {
    "displayableProperty": "DisplayableTitleGenreProperty",
    "id": str,
    "language": "DisplayableLanguage",
    "relevanceRanking": int,
    "subgenres": "TitleKeyword",
    "text": str,
}

"""------------------------ Genre -----------------------"""
Genres = {
    "genres": "Genre",
}

"""---------------------- GenreItem ---------------------"""
GenreItem = {
   "displayableProperty": "DisplayableTitleGenreProperty",  # (Not Null)
   "genreId": str,  # (Not Null)
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""-------------------- GenreSummary --------------------"""
GenreSummary = {
   "genre": "GenreItem",  # (Not Null)
   "total": int,  # (Not Null)
}

"""
----------------- GetLatestUIWorkflowOutput ----------------
Defines the output response type for the getLatestUIWorkflow
query.
------------------------------------------------------------
"""
GetLatestUIWorkflowOutput = {
   "workflow": "UIWorkflow",
}

"""
--------------------------- Goof ---------------------------
Details of a single goof
------------------------------------------------------------
"""
Goof = {
   "category": "GoofCategory",  # (Not Null)
   "displayableArticle": "DisplayableArticle",  # (Not Null)
   "id": str,  # (Not Null)
   "interestScore": "InterestScore",  # (Not Null)
   "isSpoiler": bool,  # (Not Null)
   "text": "Markdown",  # (Not Null)
}

"""
----------------------- GoofCategory -----------------------
A category of goofs describing the nature of a subset of
goofs, e.g. 'Continuity'
------------------------------------------------------------
"""
GoofCategory = {
   "id": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""---------------- GoofCategoryWithGoofs ---------------"""
GoofCategoryWithGoofs = {
   "category": "GoofCategory",  # (Not Null)
   "goofs": "GoofConnection",
}

"""------------------ GranularDirective -----------------"""
GranularDirective = {
   "allow": bool,  # (Not Null)
   "id": str,  # (Not Null)
}

"""
------------ GuildAffiliationVerificationStatus ------------
The guild affiliation that includes the Company and
verification status
------------------------------------------------------------
"""
GuildAffiliationVerificationStatus = {
   "company": "Company",  # (Not Null)
   "isVerifiedByGuild": bool,  # (Not Null)
}

"""
------------- GuildAffiliationVisibilityStatus -------------
The visibility configured for a specific guild affiliation
company for a name
------------------------------------------------------------
"""
GuildAffiliationVisibilityStatus = {
   "company": "Company",  # (Not Null)
   "visibility": str,  # (Not Null)
}

"""---------------- GuildMembershipDetail ---------------"""
GuildMembershipDetail = {
   "company": "Company",  # (Not Null)
   "membershipId": str,  # (Not Null)
}

"""
------------------------ GuildStatus -----------------------
Additional metadata describing guild status
------------------------------------------------------------
"""
GuildStatus = {
   "isActraApprentice": bool,
   "isNonUnion": bool,
   "isSagEligible": bool,
}

"""
------------------------- HelpLink -------------------------
Defines a link to a help article. Clients can show a
relevant help icon such as a question mark, based on its
type.
------------------------------------------------------------
"""
HelpLink = {
   "label": "LocalizedString",  # (Not Null)
   "url": str,  # (Not Null)
}

"""---------------------- Histogram ---------------------"""
Histogram = {
   "demographic": "Demographic",  # (Not Null)
   "histogramValues": "HistogramValues",  # (Not Null)
}

"""------------------- HistogramValues ------------------"""
HistogramValues = {
   "rating": int,  # (Not Null)
   "voteCount": int,  # (Not Null)
}

"""
--------------------------- Image --------------------------
Image type Extends external type.
------------------------------------------------------------
"""
Image = {
   "caption": "Markdown",
   "copyright": str,
   "_correctionLink": "ContributionLink",
   "countries": "DisplayableCountry",  # (Not Null)
   "createdBy": str,
   "createdOn": "DisplayableDate",
   "height": int,
   "id": str,  # (Not Null)
   "languages": "DisplayableLanguage",  # (Not Null)
   "names": "NameLimited",  # (Not Null)
   "_reportingLink": "ContributionLink",
   "source": "Source",
   "titles": "TitleLimited",  # (Not Null)
   "type": str,
   "url": str,
   "width": int,
}

"""-------------- ImageAndLinkCallToAction --------------"""
ImageAndLinkCallToAction = {
   "action": "ActionLink",  # (Not Null)
   "backgroundImage": "CallToActionImage",
   "resultId": int,  # (Not Null)
}

"""----------------- ImageEditParameters ----------------"""
ImageEditParameters = {
   "cropBox": "CroppingParameters",
   "rotation": float,
}

"""--------------------- ImageFacets --------------------"""
ImageFacets = {
   "galleries": "ImageGalleryConnection",
   "names": "NameLimitedConnection",
   "titles": "TitleLimitedConnection",
   "types": "ImageTypeFacet",  # (Not Null)
}

"""-------------------- ImageGallery --------------------"""
ImageGallery = {
   "galleryText": str,
   "id": str,  # (Not Null)
   "images": "ImageConnection",
}

"""
--------------------- ImageRestriction ---------------------
Information about restrictions applied to images
------------------------------------------------------------
"""
ImageRestriction = {
   "explanations": "RestrictionExplanation",  # (Not Null)
   "reasons": str,  # (Not Null)
   "restrictionReason": str,  # (Not Null)
   "unrestrictedTotal": int,
}

"""
------------------------- ImageType ------------------------
An ImageType provides meta information describing the type
of a given image, such as whether it is a Poster or a photo
from an Event. It includes a localized display label as well
as a canonical non-localized imageTypeID, that can be used
as input to image filter APIs.
------------------------------------------------------------
"""
ImageType = {
   "id": str,  # (Not Null)
   "imageTypeId": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""
---------------------- ImageTypeFacet ----------------------
Provides information on how many images in a gallery match
the specified image type
------------------------------------------------------------
"""
ImageTypeFacet = {
   "total": int,  # (Not Null)
   "type": "ImageType",  # (Not Null)
}

"""----------------- ImageTypeWithImages ----------------"""
ImageTypeWithImages = {
   "images": "ImageTypesConnection",
   "imageType": "ImageType",  # (Not Null)
}

"""
------------------------- Interest -------------------------
Interest type Extends external type.
------------------------------------------------------------
"""
Interest = {
   "category": "InterestCategory",
   "description": "LocalizedMarkdown",
   "engagementStatistics": "EngagementStatistics",
   "id": str,  # (Not Null)
   "primaryImage": "ImageLimited",
   "primaryText": "InterestText",
   "score": "InterestImportanceScore",
   "secondaryText": "InterestText",
   "similarInterests": "InterestConnection",
   "visibilityLevel": str,
}

"""------------------ InterestCategory ------------------"""
InterestCategory = {
   "id": str,  # (Not Null)
   "interests": "InterestConnection",
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""--------------- InterestImportanceScore --------------"""
InterestImportanceScore = {
   "currentScore": int,  # (Not Null)
}

"""
----------------------- InterestScore ----------------------
Votes from users about whether an item is interesting.
------------------------------------------------------------
"""
InterestScore = {
   "usersInterested": int,  # (Not Null)
   "usersVoted": int,  # (Not Null)
}

"""-------------------- InterestText --------------------"""
InterestText = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""------------------- IsElementInList ------------------"""
IsElementInList = {
   "isElementInList": bool,  # (Not Null)
   "itemElementId": str,  # (Not Null)
   "itemIds": str,  # (Not Null)
}

"""----------------------- Keyword ----------------------"""
Keyword = {
   "category": "KeywordCategory",
   "id": str,  # (Not Null)
   "text": "KeywordText",
   "titles": "TitleLimitedConnection",
}

"""
---------------------- KeywordCategory ---------------------
Keyword Category details
------------------------------------------------------------
"""
KeywordCategory = {
   "id": str,  # (Not Null)
}

"""------------------- KeywordMetadata ------------------"""
KeywordMetadata = {
   "keywordCategories": "KeywordCategory",  # (Not Null)
}

"""
------------------------ KeywordText -----------------------
The keyword itself. Can contain lower case characters and
punctuation, but no uppercase characters or spaces.
------------------------------------------------------------
"""
KeywordText = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""--------------------- KnownForV2 ---------------------"""
KnownForV2 = {
   "credits": "CreditV2",  # (Not Null)
   "restriction": "NameKnownForRestriction",
}

"""
----------------------- Laboratories -----------------------
Laboratories for this title.
------------------------------------------------------------
"""
Laboratories = {
   "items": "Laboratory",  # (Not Null)
   "restriction": "TechnicalSpecificationsRestriction",
   "total": int,  # (Not Null)
}

"""
------------------------ Laboratory ------------------------
A lab used for a film, along with some flags and any
attributes. For example, we could have a lab named ILM,
which was credited as Industrial Light & Magic, and used for
developing specific sequences.
------------------------------------------------------------
"""
Laboratory = {
   "attributes": "DisplayableAttribute",  # (Not Null)
   "creditedAs": str,
   "displayableProperty": "DisplayableTechnicalSpecificationProperty",  # (Not Null)
   "isUncredited": bool,  # (Not Null)
   "laboratory": str,  # (Not Null)
}

"""------------------ LengthMeasurement -----------------"""
LengthMeasurement = {
   "unit": str,
   "value": float,
}

"""------------------ LinkCallToAction ------------------"""
LinkCallToAction = {
   "action": "ActionLink",  # (Not Null)
   "resultId": int,  # (Not Null)
}

"""----------------- LinkedAuthProvider -----------------"""
LinkedAuthProvider = {
   "deprecationMessage": "AuthProviderDeprecationMessage",
   "type": str,  # (Not Null)
}

"""
--------------------------- List ---------------------------
List Type Entity for federation. Other implementing services
can extend using field 'id'. Non key fields are all marked
as optional since this is a federation entity.
------------------------------------------------------------
"""
List = {
   "areElementsInList": "IsElementInList",  # (Not Null)
   "author": "UserProfile",
   "createdDate": str,
   "description": "ListDescription",
   "id": str,  # (Not Null)
   "isElementInList": bool,
   "isPredefined": bool,
   "items": "ListConnection",
   "lastModifiedDate": str,
   "listClass": "ListClass",
   "listInteractionCounts": "ListInteractionCounts",  # (Not Null)
   "listType": "ListType",
   "name": "ListName",
   "nameListItemSearch": "SearchFacetConnection",
   "primaryImage": "ListPrimaryImage",
   "titleListItemSearch": "ListItemSearchNodeConnection",
   "visibility": "ListVisibility",
}

"""---------------------- ListClass ---------------------"""
ListClass = {
   "id": str,  # (Not Null)
   "name": "ListClassName",
}

"""
----------------------- ListClassName ----------------------
The type of list Ex: Watchlist, check ins list
------------------------------------------------------------
"""
ListClassName = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""
---------------------- ListDescription ---------------------
Markdown text
------------------------------------------------------------
"""
ListDescription = {
   "originalText": "Markdown",  # (Not Null)
}

"""
---------------- ListFieldAttributeMetadata ----------------
Attribute Metadata for List Fields
------------------------------------------------------------
"""
ListFieldAttributeMetadata = {
   "listDescription": "ListTextFieldMetadata",  # (Not Null)
   "listItemDescription": "ListTextFieldMetadata",  # (Not Null)
   "listName": "ListTextFieldMetadata",  # (Not Null)
}

"""---------------- ListInteractionCounts ---------------"""
ListInteractionCounts = {
   "clicks": int,  # (Not Null)
   "listId": str,  # (Not Null)
   "timeRange": str,  # (Not Null)
   "views": int,  # (Not Null)
}

"""-------------------- ListItemNode --------------------"""
ListItemNode = {
   "absolutePosition": int,
   "createdDate": str,
   "description": "ListDescription",
   "itemId": str,
   "lastModifiedDate": str,
   # "listItem": "ListItem",  # TODO: this is a union type, need to handle unknown type
}

"""----------------- ListItemSearchNode -----------------"""
ListItemSearchNode = {
   "absolutePosition": int,  # (Not Null)
   "createdDate": str,
   "description": "ListDescription",
   "itemId": str,  # (Not Null)
   "lastModifiedDate": str,
}

"""
------------------------- ListName -------------------------
String Text
------------------------------------------------------------
"""
ListName = {
   "originalText": str,  # (Not Null)
}

"""------------------ ListPrimaryImage ------------------"""
ListPrimaryImage = {
   "image": "ImageLimited",  # (Not Null)
}

"""
------------------- ListTextFieldMetadata ------------------
Attribute Metadata for a List Text Field
------------------------------------------------------------
"""
ListTextFieldMetadata = {
   "maxCharacters": int,  # (Not Null)
}

"""---------------------- ListType ----------------------"""
ListType = {
   "id": str,  # (Not Null, ENUM)
}

"""------------------- ListVisibility -------------------"""
ListVisibility = {
   "id": str, # (ENUM),
   "name": "ListVisibilityName",
}

"""----------------- ListVisibilityName -----------------"""
ListVisibilityName = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""-------------- LocalizedDisplayableCount -------------"""
LocalizedDisplayableCount = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""
---------------- LocalizedDisplayableCountry ---------------
Generic type for a localized country, which has an ID or
token, associated display text, and the language of the
display text
------------------------------------------------------------
"""
LocalizedDisplayableCountry = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""---------- LocalizedDisplayableEpisodeNumber ---------"""
LocalizedDisplayableEpisodeNumber = {
   "displayableProperty": "EpisodeNumberDisplayableProperty",  # (Not Null)
   "episodeNumber": str,  # (Not Null)
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""----------- LocalizedDisplayableEpisodeYear ----------"""
LocalizedDisplayableEpisodeYear = {
   "displayableProperty": "YearDisplayableProperty",  # (Not Null)
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
   "year": str,  # (Not Null)
}

"""------------- LocalizedDisplayableSeason -------------"""
LocalizedDisplayableSeason = {
   "displayableProperty": "SeasonValueDisplayableProperty",  # (Not Null)
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "season": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""
--------------------- LocalizedMarkdown --------------------
An object composed of a displayable localized markdown along
with the language it is in.  The language is determined by
localization headers sent by the client, if the chosen
language is available. Otherwise an `en-US` string will
likely be returned by default.  More information on the
x-imdb-user-country and x-imdb-user-language headers at
https://w.amazon.com/bin/view/IMDb/Zuko/Headers/
------------------------------------------------------------
"""
LocalizedMarkdown = {
   "language": str,  # (Not Null)
   "value": "Markdown",  # (Not Null)
}

"""
---------------------- LocalizedString ---------------------
An object composed of a displayable localized string along
with the language it is in.  The language is determined by
localization headers sent by the client, if the chosen
language is available. Otherwise an `en-US` string will
likely be returned by default.  More information on the
x-imdb-user-country and x-imdb-user-language headers at
https://w.amazon.com/bin/view/IMDb/Zuko/Headers/
------------------------------------------------------------
"""
LocalizedString = {
   "language": str,  # (Not Null)
   "value": str,  # (Not Null)
}

"""---------------------- Location ----------------------"""
Location = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""--------------- LogoutRedirectURLOutput --------------"""
LogoutRedirectURLOutput = {
   "redirectURL": str,  # (Not Null)
}

"""------------------- MainSearchNode -------------------"""
MainSearchNode = {
   # "entity": "MainSearchEntity",  # (Not Null) # TODO: this is a union type, need to handle unknown type
   "id": str,  # (Not Null)
}

"""
----------------------- ManagedClient ----------------------
Client managed by a customer
------------------------------------------------------------
"""
ManagedClient = {
   "client": "NameLimited",  # (Not Null)
   "status": str,  # (Not Null)
}

"""
-------------------- ManagedCompanyData --------------------
Data that company managers control, defined here since it is
shared with multple files
------------------------------------------------------------
"""
ManagedCompanyData = {
   "knownFor": "ManagedCompanyKnownForGroup",
}

"""
-------------- ManagedCompanyKeyStaffCategory --------------
Company key staff that includes meta data needed to support
managers. Intended for consumption by managers.
------------------------------------------------------------
"""
ManagedCompanyKeyStaffCategory = {
   "staff": "CompanyKeyStaffConnection",  # (Not Null)
   "status": str,  # (Not Null, ENUM)
}

"""
---------------- ManagedCompanyKeyStaffGroup ---------------
Company key staff that company managers control
------------------------------------------------------------
"""
ManagedCompanyKeyStaffGroup = {
   "automatic": "ManagedCompanyKeyStaffCategory",  # (Not Null)
   "automaticHistory": "ManagedCompanyKeyStaffHistory",  # (Not Null)
   "custom": "ManagedCompanyKeyStaffCategory",  # (Not Null)
   "customHistory": "ManagedCompanyKeyStaffHistory",  # (Not Null)
   "sourcePreference": str,  # (Not Null, ENUM)
}

"""
--------------- ManagedCompanyKeyStaffHistory --------------
Company key staff history
------------------------------------------------------------
"""
ManagedCompanyKeyStaffHistory = {
   "keyStaffHistory": "ManagedCompanyKeyStaffHistoryConnection",  # (Not Null)
}

"""
----------- ManagedCompanyKnownForClientCategory -----------
Company known for client that includes meta data needed to
support managers. Intended for consumption by managers.
------------------------------------------------------------
"""
ManagedCompanyKnownForClientCategory = {
   "clients": "CompanyKnownForClientConnection",  # (Not Null)
   "status": str,  # (Not Null, ENUM)
}

"""
------------- ManagedCompanyKnownForClientGroup ------------
Company known for client that company managers control
------------------------------------------------------------
"""
ManagedCompanyKnownForClientGroup = {
   "automatic": "ManagedCompanyKnownForClientCategory",  # (Not Null)
   "automaticHistory": "ManagedCompanyKnownForClientHistory",  # (Not Null)
   "custom": "ManagedCompanyKnownForClientCategory",  # (Not Null)
   "customHistory": "ManagedCompanyKnownForClientHistory",  # (Not Null)
   "sourcePreference": str,  # (Not Null)
}

"""
------------ ManagedCompanyKnownForClientHistory -----------
Company known for client history
------------------------------------------------------------
"""
ManagedCompanyKnownForClientHistory = {
   "clientHistory": "ManagedCompanyKnownForClientHistoryConnection",  # (Not Null)
}

"""
------------ ManagedCompanyKnownForClientVersion -----------
A version snapshot of company known for client for
consumption by IMDb admins
------------------------------------------------------------
"""
ManagedCompanyKnownForClientVersion = {
   "clients": "CompanyKnownForClientConnection",  # (Not Null)
   "createdDate": str,  # (Not Null)
   "modifiedBy": "ModifiedBy",
   "status": str,  # (Not Null, ENUM)
   "versionNumber": int,  # (Not Null)
}

"""
---------------- ManagedCompanyKnownForGroup ---------------
Company known for that company managers control
------------------------------------------------------------
"""
ManagedCompanyKnownForGroup = {
   "keyStaff": "ManagedCompanyKeyStaffGroup",  # (Not Null)
   "knownForClient": "ManagedCompanyKnownForClientGroup",  # (Not Null)
   "knownForTitle": "ManagedCompanyKnownForTitleGroup",  # (Not Null)
}

"""
----------- ManagedCompanyKnownForKeyStaffVersion ----------
A version snapshot of company key staff for consumption by
IMDb admins
------------------------------------------------------------
"""
ManagedCompanyKnownForKeyStaffVersion = {
   "createdDate": str,  # (Not Null)
   "modifiedBy": "ModifiedBy",
   "staff": "CompanyKeyStaffConnection",  # (Not Null)
   "status": str,  # (Not Null)
   "versionNumber": int,  # (Not Null)
}

"""
------------ ManagedCompanyKnownForTitleCategory -----------
Company known for title that includes meta data needed to
support managers. Intended for consumption by managers.
------------------------------------------------------------
"""
ManagedCompanyKnownForTitleCategory = {
   "status": str,  # (Not Null)
   "titles": "CompanyKnownForTitleConnection",  # (Not Null)
}

"""
------------- ManagedCompanyKnownForTitleGroup -------------
Company known for title that company managers control
------------------------------------------------------------
"""
ManagedCompanyKnownForTitleGroup = {
   "automatic": "ManagedCompanyKnownForTitleCategory",  # (Not Null)
   "automaticHistory": "ManagedCompanyKnownForTitleHistory",  # (Not Null)
   "custom": "ManagedCompanyKnownForTitleCategory",  # (Not Null)
   "customHistory": "ManagedCompanyKnownForTitleHistory",  # (Not Null)
   "sourcePreference": str,  # (Not Null)
}

"""
------------ ManagedCompanyKnownForTitleHistory ------------
Company known for title history
------------------------------------------------------------
"""
ManagedCompanyKnownForTitleHistory = {
   "titleHistory": "ManagedCompanyKnownForTitleHistoryConnection",  # (Not Null)
}

"""
------------ ManagedCompanyKnownForTitleVersion ------------
A version snapshot of company known for title for
consumption by IMDb admins
------------------------------------------------------------
"""
ManagedCompanyKnownForTitleVersion = {
   "createdDate": str,  # (Not Null)
   "modifiedBy": "ModifiedBy",
   "status": str,  # (Not Null)
   "titles": "CompanyKnownForTitleConnection",  # (Not Null)
   "versionNumber": int,  # (Not Null)
}

"""
------------------ ManagingRepresentative ------------------
Representative that manages a customer
------------------------------------------------------------
"""
ManagingRepresentative = {
   "manager": "NameLimited",  # (Not Null)
   "status": str,  # (Not Null, ENUM)
}

"""
------------------------- Markdown -------------------------
Markdown type Extends external type.
------------------------------------------------------------
"""
Markdown = {
   "expandedMarkdown": str,  # (Not Null)
   "markdown": str,  # (Not Null)
   "plaidHtml": str,
   "plainText": str,
}

MarkdownEntity = {
    "markdown": "Markdown"
}

"""-------------- MarkdownSlotCallToAction --------------"""
MarkdownSlotCallToAction = {
   "markdown": "LocalizedMarkdown",
   "resultId": int,  # (Not Null)
}

"""
--------------------- MediaServiceImage --------------------
A generic implementation of the ImageObject
------------------------------------------------------------
"""
MediaServiceImage = {
   "accessibilityText": "CommonLocalizedDisplayableConcept",
   "fileType": str, # (ENUM)
   "height": int,
   "url": str,
   "width": int,
}

"""--------------------- Metacritic ---------------------"""
Metacritic = {
   "metascore": "Metascore",  # (Not Null)
   "reviews": "MetacriticReviewConnection",
   "url": str,
}

"""------------------ MetacriticReview ------------------"""
MetacriticReview = {
   "quote": "LocalizedString",
   "reviewer": str,
   "score": int,  # (Not Null)
   "site": str,
   "url": str,
}

"""---------------------- Metascore ---------------------"""
Metascore = {
   "reviewCount": int,  # (Not Null)
   "score": int,  # (Not Null)
}

"""
------------------------ MeterEvent ------------------------
Event that should be noted with meter
------------------------------------------------------------
"""
MeterEvent = {
   "title": "TitleLimited",
   "type": "LocalizedString",
}

"""------------------- MeterRankChange ------------------"""
MeterRankChange = {
   "changeDirection": str,  # (Not Null, ENUM)
   "difference": int,  # (Not Null)
}

"""-------------- MeterRankingHistoryEntry --------------"""
MeterRankingHistoryEntry = {
   "date": str,
   "events": "MeterEvent",  # (Not Null)
   "rank": int,  # (Not Null)
}

"""
--------------------- MeterRestriction ---------------------
Restriction information applied to Meter. By default,
restriction will be based on IMDbPro entitlements.
------------------------------------------------------------
"""
MeterRestriction = {
   "explanations": "RestrictionExplanation",  # (Not Null)
   "reasons": str,  # (Not Null)
   "restrictionReason": str,  # (Not Null)
}

"""----------------- MigrationTestOutput ----------------"""
MigrationTestOutput = {
   "result": str,
}

"""
------------------------ ModifiedBy ------------------------
The customer that modified the known for category and their
role for consumption by IMDb admins
------------------------------------------------------------
"""
ModifiedBy = {
   "role": str,  # (Not Null, ENUM)
}

"""------------------------ Money -----------------------"""
Money = {
   "amount": float,  # (Not Null)
   "currency": str,  # (Not Null)
}

"""
------------------- MultiLinkCallToAction ------------------
This is a multi-link CallToAction that may contain two
action lists: abbreviatedActions and standardActions. The
client will decide which action list to use when displaying
the actions. For example, the client may choose to display
the abbreviatedActions on devices with small screens, while
using standardActions on devices with larger screens. A
responsive solution may utilize both action lists.
------------------------------------------------------------
"""
MultiLinkCallToAction = {
   "abbreviatedActions": "NamedActionLink",  # (Not Null)
   "resultId": int,  # (Not Null)
   "standardActions": "NamedActionLink",  # (Not Null)
}

"""
--------------------------- Name ---------------------------
Name type Extends external type.
------------------------------------------------------------
"""
Name = {
   "age": "AgeDetails",
   "akas": "NameAkaConnection",
   "alexaTopQuestions": "AlexaQuestionConnection",
   "autoSelectedProfessions": "NameProfession",  # (Not Null)
   "awardNominations": "AwardNominationConnection",
   "bio": "NameBio",
   "bios": "NameBiosConnection",
   "birthDate": "DisplayableDate",
   "birthLocation": "DisplayableLocation",
   "birthName": "BirthName",
   "canonicalUrl": str,
   "clients": "NameRepresentationConnection",
   "contentWarnings": "ContentWarnings",
   "creditCategories": "NameCreditCategoryWithCredits",  # (Not Null)
   "creditedWithNames": "CreditedWithNamesConnection",
   "creditGroupings": "CreditGroupingConnection",
   "credits": "CreditConnection",
   "creditSummary": "NameCreditSummary",
   "creditsV2": "CreditV2LimitedConnection",
   "currentProfessions": "NameProfession",  # (Not Null)
   "death": "NameDeath",  # (Not Null)
   "deathCause": "DisplayableNameDeathCause",
   "deathDate": "DisplayableDate",
   "deathLocation": "DisplayableLocation",
   "deathStatus": str, # (ENUM)
   "demographicData": "DemographicDataItem",  # (Not Null)
   "directContact": "DirectContactDetails",
   "disambiguator": "Disambiguation",
   "employment": "EmploymentConnection",
   "engagementStatistics": "EngagementStatistics",
   "episodeCredits": "CreditV2LimitedConnection",
   "experimental_clients": "Experimental_NameRepresentationConnection",
   "experimental_creditCategories": "ExperimentalNameCreditCategoryWithCredits",  # (Not Null)
   "experimental_credits": "ExperimentalCreditConnection",
   "experimental_directContact": "Experimental_DirectContactDetails",
   "experimental_employment": "Experimental_PersonalEmploymentConnection",
   "experimental_representation": "Experimental_NameRepresentationConnection",
   "experimental_resume": "Experimental_Resume",
   "experimental_trackNotificationPreferences": "Experimental_TrackNotificationPreferences",
   "externalLinkCategories": "ExternalLinkCategoryWithExternalLinks",  # (Not Null)
   "externalLinks": "ExternalLinkConnection",
   "featuredExternalLinkCategories": "ExternalLinkCategoryWithFeaturedExternalLinks",  # (Not Null)
   "featuredPolls": "PollsConnection",
   "height": "NameHeight",
   "id": str,  # (Not Null)
   "images": "ImageConnection",
   "imageTypes": "ImageTypeWithImages",  # (Not Null)
   "_imageUploadLink": "ContributionLink",
   "isClaimed": bool,
   "knownFor": "NameKnownForConnection",
   "knownForV2": "KnownForV2",
   "managedData": "NameManagedData",
   "meta": "NameMeta",
   "meterRank": "NameMeterRanking",
   "meterRankingHistory": "NameMeterRankingHistory",
   "moreLikeThisNames": "NameLimitedConnection",
   "nameText": "NameText",
   "news": "NewsConnection",
   "nickNames": "NickName",  # (Not Null)
   "nominations": "NominationLimitedConnection",
   "otherWorks": "NameOtherWorkConnection",
   "prestigiousAwardSummary": "PrestigiousAwardSummary",
   "primaryImage": "ImageLimited",
   "primaryProfessions": "PrimaryProfession",  # (Not Null)
   "primaryVideos": "VideoConnection",
   "professions": "NameProfession",  # (Not Null)
   "publicityCategories": "PublicityCategoryWithListings",  # (Not Null)
   "publicityListings": "PublicityListingCategoryConnection",
   "quotes": "NameQuoteConnection",
   "recentlyViewedStatistics": "RecentlyViewedStatistics",
   "relatedLists": "ListConnection",
   "relations": "NameRelationsConnection",
   "representation": "NameRepresentationConnection",
   "resume": "Resume",
   "searchIndexing": "NameSearchIndexing",
   "selfVerifiedData": "SelfVerifiedNameData",
   "sharedNames": "SharedNamesResult",
   "sharedNamesSummary": "SharedNamesSummary",
   "sharedTitles": "SharedTitlesConnection",
   "spouses": "NameSpouse",  # (Not Null)
   "titleSalaries": "SalaryConnection",
   "trackNotificationPreferences": "TrackNotificationPreferences",
   "trademarks": "TrademarkConnection",
   "trivia": "NameTriviaConnection",
   "userSelectedProfessions": "NameProfession",  # (Not Null)
   "vanityUrl": "VanityUrl",
   "videos": "VideoConnection",
   "videoTypes": "VideoTypeWithVideos",  # (Not Null)
}

"""
-------------------------- NameAka -------------------------
Aka details
------------------------------------------------------------
"""
NameAka = {
   "displayableProperty": "DisplayableNameAkaProperty",  # (Not Null)
   "text": str,  # (Not Null)
}

"""----------------------- NameBio ----------------------"""
NameBio = {
   "author": "Markdown",
   "category": "NameBioCategory",
   "displayableArticle": "DisplayableArticle",
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": "Markdown",  # (Not Null)
}

"""
---------------------- NameBioCategory ---------------------
A category of person's bio describing the type of bio, e.g.
'auto-generated', 'mini-bio'
------------------------------------------------------------
"""
NameBioCategory = {
   "id": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""---------------------- NameBirth ---------------------"""
NameBirth = {
    "date": str,
    "location": "Location",
}

"""---------------- NameChartRankingsNode ---------------"""
NameChartRankingsNode = {
   "item": "NameLimited",  # (Not Null)
   "rank": int,  # (Not Null)
}

"""----------------- NameCreditCategory -----------------"""
NameCreditCategory = {
   "id": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""------------ NameCreditCategoryWithCredits -----------"""
NameCreditCategoryWithCredits = {
   "category": "CreditCategory",  # (Not Null)
   "credits": "CreditConnection",
}

"""
--------------------- NameCreditSummary --------------------
Summary of the name credits.
------------------------------------------------------------
"""
NameCreditSummary = {
   "categories": "CreditCategorySummary",  # (Not Null)
   "genres": "GenreSummary",  # (Not Null)
   "titleTypeCategories": "TitleTypeCategorySummary",  # (Not Null)
   "titleTypes": "TitleTypeSummary",  # (Not Null)
   "totalCredits": "TotalCredits",
}

"""---------------------- NameDeath --------------------"""
NameDeath = {
    "cause": "DeathCause",
    "date": str,
    "location": "Location",
}

"""
---------------------- NamedActionLink ---------------------
Generic type for an action link which has a unique name,
url, and optionally associated label (localized text)
------------------------------------------------------------
"""
NamedActionLink = {
   "actionName": int,  # (Not Null)
   "label": "CallToActionText",
   "url": str,  # (Not Null)
}

"""
------------------ NameDisplayPreferences ------------------
Page display preferences (e.g. whether to hide awards,
biography, etc.)
------------------------------------------------------------
"""
NameDisplayPreferences = {
   "akas": str,  # (Not Null)
   "awards": str,  # (Not Null)
   "biography": str,  # (Not Null)
   "height": str,  # (Not Null)
}

"""--------------------- NameHeight ---------------------"""
NameHeight = {
   "displayableProperty": "DisplayableNameHeightProperty",  # (Not Null)
   "measurement": "LengthMeasurement",  # (Not Null)
}

"""-------------------- NameKnownFor --------------------"""
NameKnownFor = {
   "credit": "Credit",  # (Not Null)
   "title": "TitleLimited",  # (Not Null)
}

"""
------------------ NameKnownForRestriction -----------------
Restriction information applied to KnownFor
------------------------------------------------------------
"""
NameKnownForRestriction = {
   "explanations": "RestrictionExplanation",  # (Not Null)
   "reasons": str,  # (Not Null)
   "restrictionReason": str,  # (Not Null)
   "unrestrictedTotal": int,
}

"""
---------------------- NameManagedData ---------------------
Name data that provides additional context exclusively for
name owner or authorized managers
------------------------------------------------------------
"""
NameManagedData = {
   "automaticFeaturedImages": "ImageLimited",  # (Not Null)
   "automaticKnownFor": "TitleLimited",  # (Not Null)
   "customFeaturedImages": "CustomFeaturedImages",
   "customKnownFor": "CustomKnownFor",
   "customPrimaryImage": "CustomPrimaryImage",
   "displayPreferences": "NameDisplayPreferences",
   "latestPrimaryImage": "ImageLimited",
   "managedClients": "ManagedClient",  # (Not Null)
   "managingRepresentatives": "ManagingRepresentative",  # (Not Null)
}

"""
----------- NameManagingPermissionRequestResponse ----------
A request sent from a rep to a client to ask for managing
permission Notes: it is the return type of a query field
------------------------------------------------------------
"""
NameManagingPermissionRequestResponse = {
   "isValid": bool,  # (Not Null)
   "requester": "NameLimited",  # (Not Null)
   "target": "NameLimited",  # (Not Null)
}

"""---------------------- NameMeta ----------------------"""
NameMeta = {
   "canonicalId": str,  # (Not Null)
   "publicationStatus": str,  # (Not Null)
}

"""-------------------- NameMetadata --------------------"""
NameMetadata = {
   "nameCreditCategories": "NameCreditCategory",  # (Not Null)
}

"""------------------ NameMeterRanking ------------------"""
NameMeterRanking = {
   "currentRank": int,  # (Not Null)
   "rankChange": "MeterRankChange",
}

"""--------------- NameMeterRankingHistory --------------"""
NameMeterRankingHistory = {
   "bestRank": "MeterRankingHistoryEntry",
   "ranks": "MeterRankingHistoryEntry",  # (Not Null)
   "restriction": "MeterRestriction",
}

"""-------------------- NameOtherWork -------------------"""
NameOtherWork = {
   "category": "NameOtherWorkCategory",
   "displayableProperty": "DisplayableNameOtherWorkProperty",  # (Not Null)
   "fromDate": str,
   "id": str,  # (Not Null)
   "text": "Markdown",  # (Not Null)
   "toDate": str,
}

"""---------------- NameOtherWorkCategory ---------------"""
NameOtherWorkCategory = {
   "id": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""---------------- NamePersonalLocation ----------------"""
NamePersonalLocation = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "latitude": str,  # (Not Null)
   "longitude": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""------------ NamePersonalLocationMetadata ------------"""
NamePersonalLocationMetadata = {
   "limit": int,  # (Not Null)
   "validValues": "NamePersonalLocation",  # (Not Null)
}

"""---------------- NamePersonalLocations ---------------"""
NamePersonalLocations = {
   "locations": "NamePersonalLocation",  # (Not Null)
   "total": int,  # (Not Null)
}

"""
---------------------- NameProfession ----------------------
A NameProfession is a type of work that someone wants to be
known for doing on an ongoing basis. For example a ôMakeup
Artistö.  All fields are marked as nullable in case of
invalid graphlet cross-link - in practice these should never
be null.
------------------------------------------------------------
"""
NameProfession = {
   "id": str,  # (Not Null)
   "isCustomerSelectable": bool,
   "profession": "DisplayableProfession",
   "professionCategory": "ProfessionCategory",
   "shortDescription": "DisplayableProfessionDescription",
}

"""---------------------- NameQuote ---------------------"""
NameQuote = {
   "displayableArticle": "DisplayableArticle",
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",
   "text": "Markdown",  # (Not Null)
}

"""----------------- NameRecommendation -----------------"""
NameRecommendation = {
   "explanation": "LocalizedMarkdown",  # (Not Null)
   "name": "NameLimited",  # (Not Null)
}

"""----------------- NameRecommendations ----------------"""
NameRecommendations = {
   "names": "NameRecommendationConnection",
   "refTag": str,  # (Not Null)
}

"""-------------------- NameRelation --------------------"""
NameRelation = {
   "birthDate": "DisplayableDate",
   "genderIdentity": "GenderIdentity",
   "id": str,  # (Not Null)
   "relationName": "RelationName",
   "relationshipType": "NameRelationType",  # (Not Null)
}

"""------------------ NameRelationType ------------------"""
NameRelationType = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""----------------- NameRepresentation -----------------"""
NameRepresentation = {
   "agency": "Agency",
   "client": "NameLimited",  # (Not Null)
   "id": str,  # (Not Null)
   "independentRepresentative": "NameLimited",
   "relationshipType": "RepresentationRelationshipType",  # (Not Null)
}

"""----------------- NameSearchIndexing -----------------"""
NameSearchIndexing = {
   "disableIndexing": bool,  # (Not Null)
}

"""--------------------- NameSpouse ---------------------"""
NameSpouse = {
   "attributes": "SpouseAttributes",  # (Not Null)
   "current": bool,  # (Not Null)
   "displayableProperty": "DisplayableNameSpouseProperty",  # (Not Null)
   "spouse": "SpouseName",
   "timeRange": "DisplayableSpouseTimeRange",
}

"""---------------------- NameText ----------------------"""
NameText = {
   "text": str,  # (Not Null)
}

"""
------------------- NameToTitleAttachment ------------------
Details about an attachment event, i.e. when a name is
attached to a title
------------------------------------------------------------
"""
NameToTitleAttachment = {
   "attachmentTime": str,  # (Not Null)
   "characterList": str,  # (Not Null)
   "creditCategories": "CreditCategory",  # (Not Null)
   "id": str,  # (Not Null)
   "name": "NameLimited",  # (Not Null)
   "title": "TitleLimited",  # (Not Null)
}

"""--------------------- NameTrivia ---------------------"""
NameTrivia = {
   "date": str,
   "displayableArticle": "DisplayableArticle",
   "id": str,  # (Not Null)
   "interestScore": "InterestScore",  # (Not Null)
   "text": "Markdown",  # (Not Null)
}

"""--------------------- NameWeight ---------------------"""
NameWeight = {
   "unit": str,  # (Not Null)
   "value": float,  # (Not Null)
}

"""
---------------------- NegativeFormat ----------------------
A negative format, along with any attributes. For example,
we could have 70MM film that was used for the IMAX and
IMAX3D versions.
------------------------------------------------------------
"""
NegativeFormat = {
   "attributes": "DisplayableAttribute",  # (Not Null)
   "displayableProperty": "DisplayableTechnicalSpecificationProperty",  # (Not Null)
   "negativeFormat": str,  # (Not Null)
}

"""
---------------------- NegativeFormats ---------------------
Negative formats for this title.
------------------------------------------------------------
"""
NegativeFormats = {
   "items": "NegativeFormat",  # (Not Null)
   "restriction": "TechnicalSpecificationsRestriction",
   "total": int,  # (Not Null)
}

"""
--------------------------- News ---------------------------
News details
------------------------------------------------------------
"""
News = {
   "articleTitle": "Markdown",  # (Not Null)
   "byline": str,
   "date": str,  # (Not Null)
   "externalUrl": str,
   "id": str,  # (Not Null)
   "image": "ImageLimited",
   "language": "DisplayableLanguage",
   "similarNewsItems": "News",  # (Not Null)
   "source": "NewsSource",  # (Not Null)
   "text": "Markdown",  # (Not Null)
}

"""
------------------- NewsCategoryMetadata -------------------
Additional metadata about NewsCategory enum values
------------------------------------------------------------
"""
NewsCategoryMetadata = {
   "category": str,  # (Not Null)
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""---------------------- NewsLink ----------------------"""
NewsLink = {
   "label": str,
   "url": str,  # (Not Null)
}

"""
----------------------- NewsPageInfo -----------------------
Page info of news articles.
------------------------------------------------------------
"""
NewsPageInfo = {
   "endCursor": str,
   "hasNextPage": bool,  # (Not Null)
}

"""------------------- NewsRestriction ------------------"""
NewsRestriction = {
   "explanations": "RestrictionExplanation",  # (Not Null)
   "reasons": str,  # (Not Null)
   "restrictionReason": str,  # (Not Null)
   "unrestrictedTotal": int,
}

"""
------------------------ NewsSource ------------------------
A news source
------------------------------------------------------------
"""
NewsSource = {
   "description": str,
   "homepage": "NewsLink",
   "icon": "NewsSourceIconImage",
   "id": str,  # (Not Null)
   "trustedSource": bool,  # (Not Null)
}

"""----------------- NewsSourceIconImage ----------------"""
NewsSourceIconImage = {
   "height": int,
   "url": str,
   "width": int,
}

"""---------------------- NickName ----------------------"""
NickName = {
   "displayableProperty": "DisplayableNickNameProperty",  # (Not Null)
   "text": str,  # (Not Null)
}

"""--------------------- Nomination ---------------------"""
Nomination = {
   "award": "NominationAwardLimited",
   "category": "AwardCategory",
   "event": "NominationEvent",
   "eventEdition": "NominationEventEdition",
   "forEpisodes": "TitleLimited",  # (Not Null)
   "forSongTitles": "DisplayableSongTitle",  # (Not Null)
   "id": str,  # (Not Null)
   "isWinner": bool,
   "notes": "Markdown",
   "winAnnouncementDate": "DisplayableDate",
   "winningRank": int,
}

"""------------------- NominationAward ------------------"""
NominationAward = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "nominationCategories": "NominationsWithCategoryConnection",
   "text": str,  # (Not Null)
}

"""------------------- NominationEvent ------------------"""
NominationEvent = {
   "akas": "NominationEventAka",  # (Not Null)
   "awards": "NominationAwardLimited",  # (Not Null)
   "editions": "NominationEventEdition",  # (Not Null)
   "id": str,  # (Not Null)
   "location": "DisplayableLocation",
   "name": "NominationEventName",  # (Not Null)
   "trivia": "Markdown",  # (Not Null)
   "urls": "EventUrl",  # (Not Null)
}

"""----------------- NominationEventAka -----------------"""
NominationEventAka = {
   "endYear": int,
   "name": "NominationEventName",  # (Not Null)
   "startYear": int,
}

"""--------------- NominationEventEdition ---------------"""
NominationEventEdition = {
   "awards": "NominationAwardLimited",  # (Not Null)
   "dateRange": "DisplayableDateRange",
   "event": "NominationEvent",  # (Not Null)
   "id": str,  # (Not Null)
   "instanceWithinYear": int,  # (Not Null)
   "trivia": "Markdown",  # (Not Null)
   "year": int,  # (Not Null)
}

"""----------------- NominationEventName ----------------"""
NominationEventName = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""--------------- NominationsWithCategory --------------"""
NominationsWithCategory = {
   "category": "AwardCategory",
   "nominations": "NominationLimitedConnection",
}

"""------------------- OccupationValue ------------------"""
OccupationValue = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""----------------- OpeningWeekendGross ----------------"""
OpeningWeekendGross = {
   "boxOfficeAreaType": "BoxOfficeAreaType",  # (Not Null)
   "gross": "BoxOfficeGross",  # (Not Null)
   "theaterCount": int,
   "weekendEndDate": str,  # (Not Null)
   "weekendStartDate": str,
}

"""---------------------- PageInfo ----------------------"""
PageInfo = {
   "endCursor": str,
   "hasNextPage": bool,  # (Not Null)
   "hasPreviousPage": bool,  # (Not Null)
   "startCursor": str,
}

"""------------------- PaginatedTitles ------------------"""
PaginatedTitles = {
   "paginationToken": str,
   "titles": "TitleLimited",  # (Not Null)
}

"""------------------- PaginatedVideos ------------------"""
PaginatedVideos = {
   "paginationToken": str,
   "videos": "Video",  # (Not Null)
}

"""
----------------------- ParentsGuide -----------------------
Parents guides for a given title
------------------------------------------------------------
"""
ParentsGuide = {
   "categories": "ParentsGuideCategorySummary",  # (Not Null)
   "guideItems": "ParentsGuideConnection",
}

"""
------------------- ParentsGuideCategory -------------------
Parents guide category details
------------------------------------------------------------
"""
ParentsGuideCategory = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""
---------------- ParentsGuideCategorySummary ---------------
Parents guide severity summary
------------------------------------------------------------
"""
ParentsGuideCategorySummary = {
   "category": "ParentsGuideCategory",  # (Not Null)
   "guideItems": "ParentsGuideConnection",
   "severity": "SeverityLevel",
   "severityBreakdown": "SeverityLevel",  # (Not Null)
   "totalSeverityVotes": int,  # (Not Null)
}

"""------------------ ParentsGuideItem ------------------"""
ParentsGuideItem = {
   "category": "ParentsGuideCategory",  # (Not Null)
   "_correctionLink": "ContributionLink",
   "id": str,  # (Not Null)
   "isSpoiler": bool,  # (Not Null)
   "_reportingLink": "ContributionLink",
   "text": "Markdown",  # (Not Null)
   "title": "TitleLimited",
}

"""---------------- PersonalDetailsOutput ---------------"""
PersonalDetailsOutput = {
   "countryOfResidence": str,
   "dateOfBirth": str,
   "gender": str,
}

"""----------------- PersonalEmployment -----------------"""
PersonalEmployment = {
   "branch": "CompanyBranch",
   "company": "Company",  # (Not Null)
   "employeeContact": "CompanyContactDetails",
   "id": str,  # (Not Null)
   "jobTitle": "LocalizedString",
   "name": "NameLimited",  # (Not Null)
   "occupation": "OccupationValue",
}

"""
------------------------ PlaybackURL -----------------------
Represents a single URL that can be used for video playback.
Contains the mime type and definition of content behind the
URL.
------------------------------------------------------------
"""
PlaybackURL = {
   "displayName": "LocalizedString",  # (Not Null)
   "url": str,  # (Not Null)
   "videoDefinition": str,  # (Not Null)
   "videoMimeType": str,  # (Not Null)
}

"""------------------------ Plot ------------------------"""
Plot = {
   "author": str,
   "_correctionLink": "ContributionLink",
   "id": str,  # (Not Null)
   "isSpoiler": bool,
   "language": "DisplayableLanguage",
   "plotText": "Markdown",
   "plotType": str,
   "_reportingLink": "ContributionLink",
   "restriction": "PlotRestriction",
   "title": "TitleLimited",
}

"""
---------------------- PlotRestriction ---------------------
Information about restrictions applied to plot
------------------------------------------------------------
"""
PlotRestriction = {
   "explanations": "RestrictionExplanation",  # (Not Null)
   "reasons": str,  # (Not Null)
   "restrictionReason": str,  # (Not Null)
}

"""------------------------ Poll ------------------------"""
Poll = {
   "answers": "PollAnswersConnection",  # (Not Null)
   "author": "UserProfile",  # (Not Null)
   "createdFromListId": str,  # (Not Null)
   "currentCustomerVote": "PollVote",
   "description": "Markdown",
   "id": str,  # (Not Null)
   "isClosed": bool,  # (Not Null)
   "primaryImage": "PollPrimaryImage",
   "question": "PollQuestion",  # (Not Null)
   "recentVotes": "PollVoteConnection",
   "relatedPolls": "PollsConnection",
   "totalVotes": int,  # (Not Null)
   "type": str,  # (Not Null)
}

"""
--------------------- PollAdminActivity --------------------
Entity type to represent a poll admin activity on the poll.
------------------------------------------------------------
"""
PollAdminActivity = {
   "action": str,  # (Not Null)
   "actionTime": str,  # (Not Null)
   "admin": "UserProfile",  # (Not Null)
   "poll": "Poll",  # (Not Null)
}

"""--------------------- PollAnswer ---------------------"""
PollAnswer = {
   "answerIndex": int,  # (Not Null)
   "description": "Markdown",
   #"item": "AnswerItem",  # (Not Null) # TODO: This is a union, need to handle it properly
   "votePercentage": float,  # (Not Null)
   "votes": int,  # (Not Null)
}

"""------------------ PollPrimaryImage ------------------"""
PollPrimaryImage = {
   "image": "ImageLimited",  # (Not Null)
}

"""-------------------- PollQuestion --------------------"""
PollQuestion = {
   "originalText": "Markdown",  # (Not Null)
}

"""
------------------------- PollVote -------------------------
Entity type to represent a vote on the poll.
------------------------------------------------------------
"""
PollVote = {
   # "answer": "AnswerItem",  # (Not Null) # TODO: This is a union, need to handle it properly
   "answerIndex": int,  # (Not Null)
   "poll": "Poll",  # (Not Null)
   "user": "UserProfile",  # (Not Null)
   "voteTime": str,  # (Not Null)
}

"""--------------- PrestigiousAwardSummary --------------"""
PrestigiousAwardSummary = {
   "awardNomination": "AwardNomination",  # (Not Null)
   "nominations": int,  # (Not Null)
   "wins": int,  # (Not Null)
}

"""------------------ PrimaryProfession -----------------"""
PrimaryProfession = {
   "category": "CreditCategory",  # (Not Null)
   "profession": "Profession",
}

"""----------------- PrimaryWatchOption -----------------"""
PrimaryWatchOption = {
   "additionalWatchOptionsCount": int,
   "watchOption": "WatchOption",  # (Not Null)
}

"""------------- PrincipalCreditsForCategory ------------"""
PrincipalCreditsForCategory = {
   "category": "CreditCategory",  # (Not Null)
   "credits": "Credit",  # (Not Null)
   "restriction": "CreditRestriction",
   "totalCredits": int,  # (Not Null)
}

"""------------- PrincipalCreditsForGrouping ------------"""
PrincipalCreditsForGrouping = {
   "credits": "CreditV2",  # (Not Null)
   "grouping": "CreditGrouping",  # (Not Null)
   "restriction": "CreditRestriction",
   "totalCredits": int,  # (Not Null)
}

"""
----------------------- PrintedFormat ----------------------
A printed format, along with any attributes. For example,
the BluRay version is 1080p.
------------------------------------------------------------
"""
PrintedFormat = {
   "attributes": "DisplayableAttribute",  # (Not Null)
   "displayableProperty": "DisplayableTechnicalSpecificationProperty",  # (Not Null)
   "printedFormat": str,  # (Not Null)
}

"""
---------------------- PrintedFormats ----------------------
Printed formats for this title.
------------------------------------------------------------
"""
PrintedFormats = {
   "items": "PrintedFormat",  # (Not Null)
   "restriction": "TechnicalSpecificationsRestriction",
   "total": int,  # (Not Null)
}

"""------------------ PrivacyDirectives -----------------"""
PrivacyDirectives = {
   "avlTcfString": str,
   "crossUseString": str,
   "directivesCookie": str,  # (Not Null)
   "expirationDate": str,  # (Not Null)
   "gvlTcfString": str,
   "purposes": "GranularDirective",  # (Not Null)
   "vendors": "GranularDirective",  # (Not Null)
}

"""--------------- PrivacyDirectivesOutput --------------"""
PrivacyDirectivesOutput = {
   "directives": "PrivacyDirectives",
}

"""-------------------- PrivacyPrompt -------------------"""
PrivacyPrompt = {
   "acceptButtonLabel": "PrivacyPromptText",  # (Not Null)
   "customizeButtonLabel": "PrivacyPromptText",
   "customizeUrl": str,  # (Not Null)
   "id": str,  # (Not Null)
   "promptMarkdown": "LocalizedMarkdown",  # (Not Null)
   "rejectButtonLabel": "PrivacyPromptText",  # (Not Null)
   "showPromptOnPageLoad": bool,  # (Not Null)
}

"""----------------- PrivacyPromptOutput ----------------"""
PrivacyPromptOutput = {
   "expirationDate": str,  # (Not Null)
   "privacyPrompt": "PrivacyPrompt",
}

"""------------------ PrivacyPromptText -----------------"""
PrivacyPromptText = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""
-------------------------- Process -------------------------
A process used for the film, along with any attributes. For
example, CinemaScope may have been used for the IMAX and
IMAX3D versions.
------------------------------------------------------------
"""
Process = {
   "attributes": "DisplayableAttribute",  # (Not Null)
   "displayableProperty": "DisplayableTechnicalSpecificationProperty",  # (Not Null)
   "process": str,  # (Not Null)
}

"""
------------------------- Processes ------------------------
Processes for this title.
------------------------------------------------------------
"""
Processes = {
   "items": "Process",  # (Not Null)
   "restriction": "TechnicalSpecificationsRestriction",
   "total": int,  # (Not Null)
}

"""
------------------ ProductionAnnouncement ------------------
Official announcements related to a title
------------------------------------------------------------
"""
ProductionAnnouncement = {
   "comment": "ProductionAnnouncementComment",
   "date": str,  # (Not Null)
}

"""
--------------- ProductionAnnouncementComment --------------
Additional information relating to a title's announcement
(e.g. a press release link)
------------------------------------------------------------
"""
ProductionAnnouncementComment = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""------------------ ProductionBudget ------------------"""
ProductionBudget = {
   "budget": "Money",  # (Not Null)
}

"""------------------- ProductionDate -------------------"""
ProductionDate = {
   "attributes": "DisplayableAttribute",  # (Not Null)
   "endDate": "DisplayableDate",
   "startDate": "DisplayableDate",
}

"""------------------- ProductionStage ------------------"""
ProductionStage = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""------------------ ProductionStatus ------------------"""
ProductionStatus = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""--------------- ProductionStatusDetails --------------"""
ProductionStatusDetails = {
   "announcements": "ProductionAnnouncement",  # (Not Null)
   "currentProductionStage": "ProductionStage",  # (Not Null)
   "productionStatusHistory": "ProductionStatusHistory",  #
   "restriction": "ProductionStatusHistoryRestriction",
}

"""--------------- ProductionStatusHistory --------------"""
ProductionStatusHistory = {
   "comment": "ProductionStatusHistoryComment",
   "date": str,  # (Not Null)
   "stage": "ProductionStage",  # (Not Null)
   "status": "ProductionStatus",  # (Not Null)
}

"""----------- ProductionStatusHistoryComment -----------"""
ProductionStatusHistoryComment = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""
------------ ProductionStatusHistoryRestriction ------------
Information about restrictions applied to production status
------------------------------------------------------------
"""
ProductionStatusHistoryRestriction = {
   "explanations": "RestrictionExplanation",  # (Not Null)
   "reasons": str,  # (Not Null)
   "restrictionReason": str,  # (Not Null)
   "unrestrictedTotal": int,
}

"""--------------------- Profession ---------------------"""
Profession = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""
-------------------- ProfessionCategory --------------------
Each NameProfession belongs to a ProfessionCategory. For
example, the Makeup Artist profession belongs to the ôMakeup
Departmentö ProfessionCategory.  All fields are marked as
nullable in case of invalid graphlet cross-link - in
practice these should never be null.
------------------------------------------------------------
"""
ProfessionCategory = {
   "id": str,  # (Not Null)
   "linkedCreditCategory": "CreditCategory",
   "listOrder": int,
   "text": "DisplayableProfessionCategory",
   "traits": str,  # (Not Null)
}

"""
---------------------- ProfessionCount ---------------------
Maps a number to a profession
------------------------------------------------------------
"""
ProfessionCount = {
   "profession": "NameProfession",  # (Not Null)
   "totalCount": int,  # (Not Null)
}

"""--------------- ProfessionCountsSummary --------------"""
ProfessionCountsSummary = {
   "displayableCounts": "LocalizedString",  # (Not Null)
   "professionCounts": "ProfessionCount",  # (Not Null)
}

"""------------------- PromotedVideoAd ------------------"""
PromotedVideoAd = {
   "adFeedbackUrl": str,
   "id": str,  # (Not Null)
   "thirdPartyTrackers": "ThirdPartyTrackers",  # (Not Null)
   "video": "Video",  # (Not Null)
}

"""
------------------------- ProStatus ------------------------
ProStatus: contains related pro subscription information.
Note: the Pro subscription status is published via Pro
subscription service, and may be out of sync with the
customer's actual subscription
------------------------------------------------------------
"""
ProStatus = {
   "hasSubscription": bool,
}

"""------------ PublicityCategoryWithListings -----------"""
PublicityCategoryWithListings = {
   "category": "PublicityListingCategory",  # (Not Null)
   "publicityListings": "PublicityListingCategoryConnection",
}

"""
----------------- PublicityListingCategory -----------------
A category of publicity listings describing the nature of a
subset of listings, e.g. 'Article'
------------------------------------------------------------
"""
PublicityListingCategory = {
   "id": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""
--------------- PushNotificationUserSettings ---------------
Push notification metadata for an authenticated user.
------------------------------------------------------------
"""
PushNotificationUserSettings = {
   "pushNotificationUserId": str,  # (Not Null)
}

"""--------------------- QueryStubs ---------------------"""
QueryStubs = {
   "matrix": "TitleLimited",
}

"""---------------------- Question ----------------------"""
Question = {
   "answerOptions": "AnswerOption",  # (Not Null)
   "answerType": str,  # (Not Null)
   "contributionLink": "ContributionQuestionsLink",  # (Not Null)
   "dataType": str,  # (Not Null)
   # "entity": "Entity",  # (Not Null) # TODO: This is a union, need to handle it properly
   "entityId": str,  # (Not Null)
   "questionId": str,  # (Not Null)
   "questionText": "Markdown",  # (Not Null)
}

"""--------------------- RankChange ---------------------"""
RankChange = {
   "changeDirection": str,  # (Not Null)
   "difference": int,  # (Not Null)
}

"""
--------------- RankedLifetimeBoxOfficeGross ---------------
The lifetime gross for the title within the relevant area.
------------------------------------------------------------
"""
RankedLifetimeBoxOfficeGross = {
   "boxOfficeAreaType": "BoxOfficeAreaType",  # (Not Null)
   "rank": int,
   "total": "Money",  # (Not Null)
}

"""----------------------- Rating -----------------------"""
Rating = {
   "date": str,  # (Not Null)
   "value": int,  # (Not Null)
}

"""--------------------- RatingsBody --------------------"""
RatingsBody = {
   "id": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""------------------- RatingsPrivacy -------------------"""
RatingsPrivacy = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "setting": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""-------------------- RatingsResult -------------------"""
RatingsResult = {
   "title": "TitleLimited",  # (Not Null)
   "userRating": "Rating",
}

"""------------------- RatingsSummary -------------------"""
RatingsSummary = {
   "aggregateRating": float,
   "notificationText": "LocalizedMarkdown",
   "topRanking": "TopRanking",
   "voteCount": int,  # (Not Null)
}

"""--------------- RatingsSummaryByCountry --------------"""
RatingsSummaryByCountry = {
   "aggregate": float,  # (Not Null)
   "country": str,  # (Not Null)
   "displayText": "LocalizedString",  # (Not Null)
   "voteCount": int,  # (Not Null)
}

"""
------------------------- Reaction -------------------------
Defines the base Reaction type, holding a description and ID
------------------------------------------------------------
"""
Reaction = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "reactionId": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""
--------------------- ReactionsSummary ---------------------
Defines list of Reaction Summary Groups
------------------------------------------------------------
"""
ReactionsSummary = {
   "reactionSummaryGroups": "ReactionSummaryGroup",  # (Not Null)
}

"""
---------------------- ReactionSummary ---------------------
Holds a reaction and its current count
------------------------------------------------------------
"""
ReactionSummary = {
   "count": int,  # (Not Null)
   "displayCount": "LocalizedString",  # (Not Null)
   "reaction": "Reaction",  # (Not Null)
}

"""
------------------- ReactionSummaryGroup -------------------
Defines a group of reactions
------------------------------------------------------------
"""
ReactionSummaryGroup = {
   "aggregateCount": int,  # (Not Null)
   "displayCount": "LocalizedString",  # (Not Null)
   "groupId": str,  # (Not Null)
   "reactionSummaries": "ReactionSummary",  # (Not Null)
   "selectionType": str,  # (Not Null)
}

"""
----------------- RecentlyViewedStatistics -----------------
Recent page view statistics for a given Pro claimed name
page, including a more detailed breakdown if available
------------------------------------------------------------
"""
RecentlyViewedStatistics = {
   "professionCountsSummary": "ProfessionCountsSummary",
   "uniquePageViewCount": int,  # (Not Null)
}

"""-------------- RecommendationExplanation -------------"""
RecommendationExplanation = {
   "title": "TitleLimited",  # (Not Null)
}

"""-------------------- RedirectLink --------------------"""
RedirectLink = {
   "label": "LocalizedString",  # (Not Null)
   "url": str,  # (Not Null)
}

"""----------------------- RefTag -----------------------"""
RefTag = {
   "ep13nReftag": str,
}

"""
------------------------ RelatedNews -----------------------
Details of news items related to a particular article
------------------------------------------------------------
"""
RelatedNews = {
   # "entity": "NewsEntity",  # (Not Null) # TODO: This is a union, need to handle it properly
   "items": "News",  # (Not Null)
}

"""-------------------- RelationName --------------------"""
RelationName = {
   "displayableProperty": "DisplayableRelationNameProperty",  # (Not Null)
   "name": "NameLimited",
   "nameText": str,
}

"""--------------------- ReleaseDate --------------------"""
ReleaseDate = {
   "attributes": "DisplayableAttribute",  # (Not Null)
   "country": "LocalizedDisplayableCountry",
   "day": int,
   "displayableProperty": "DisplayableTitleReleaseDateProperty",  # (Not Null)
   "month": int,
   "restriction": "ReleaseDateRestriction",
   "year": int,
}

"""--------------------- ReleaseYear --------------------"""
ReleaseYear = {
    "year": int,
}

"""
------------------ ReleaseDateRestriction ------------------
Information about restrictions applied to release date
------------------------------------------------------------
"""
ReleaseDateRestriction = {
   "explanations": "RestrictionExplanation",  # (Not Null)
   "reasons": str,  # (Not Null)
   "restrictionReason": str,  # (Not Null)
}

"""----------- RepresentationRelationshipType -----------"""
RepresentationRelationshipType = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "relationshipTypeId": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""
------------------ RestrictionExplanation ------------------
Restriction explanations
------------------------------------------------------------
"""
RestrictionExplanation = {
   "id": str,  # (Not Null)
   "reason": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""
-------------------------- Resume --------------------------
All fields under this type are considered self-verified.
This means that we accept the Pro customer's submission for
their own name page at face value and display it on their
page without any guarantees of its validity.
------------------------------------------------------------
"""
Resume = {
   "additionalAwards": "SelfVerifiedAwardConnection",
   "additionalCreditCategories": "ResumeAdditionalCreditsCategories",
   "additionalResumeInfo": "AdditionalResumeInfoConnection",
   "education": "SelfVerifiedEducationConnection",
   "performerProfile": "ResumeDataItem",  # (Not Null)
   "personalDetails": "ResumeDataItem",  # (Not Null)
   "professionalBackground": "ResumeDataItem",  # (Not Null)
   "references": "SelfVerifiedReferenceConnection",
   "skills": "ResumeDataItem",  # (Not Null)
   "training": "SelfVerifiedTrainingConnection",
}

"""---------- ResumeAdditionalCreditsCategories ---------"""
ResumeAdditionalCreditsCategories = {
   "categories": "ResumeAdditionalCreditsCategory",  # (Not Null)
   "total": int,  # (Not Null)
}

"""
-------------- ResumeAdditionalCreditsCategory -------------
These categories differ from normal credit categories and
are specific to the   unvetted additional credits pro
customers can add to their resume.
------------------------------------------------------------
"""
ResumeAdditionalCreditsCategory = {
   "credits": "AdditionalCreditItem",  # (Not Null)
   "id": str,  # (Not Null)
   "title": "LocalizedString",  # (Not Null)
   "total": int,  # (Not Null)
}

"""------------------- ResumeDataItem -------------------"""
ResumeDataItem = {
   "label": "LocalizedString",  # (Not Null)
   "values": "LocalizedString",  # (Not Null)
}

"""-------------- RetrieveAccountDataOutput -------------"""
RetrieveAccountDataOutput = {
   "fileMetadata": "FileMetadata",  # (Not Null)
   "message": "LocalizedMarkdown",  # (Not Null)
   "success": bool,  # (Not Null)
   "title": "LocalizedMarkdown",  # (Not Null)
}

"""
-------------------------- Review --------------------------
Cacheable except when query includes correctionLink and/or
deletionLink fields.
------------------------------------------------------------
"""
Review = {
   "author": "UserProfile",
   "authorRating": int,
   "_correctionLink": "ContributionLink",
   "deletionLink": "ContributionLink",
   "helpfulness": "ReviewHelpfulness",
   "id": str,  # (Not Null)
   "language": str,
   "_reportingLink": "ContributionLink",
   "spoiler": bool,
   "submissionDate": str,
   "summary": "ReviewSummary",
   "text": "ReviewText",
   "title": "TitleLimited",
}

"""------------------ ReviewHelpfulness -----------------"""
ReviewHelpfulness = {
   "downVotes": int,  # (Not Null)
   "score": float,  # (Not Null)
   "upVotes": int,  # (Not Null)
}

"""-------------------- ReviewSummary -------------------"""
ReviewSummary = {
   "originalText": str,  # (Not Null)
}

"""--------------------- ReviewText ---------------------"""
ReviewText = {
   "originalText": "Markdown",  # (Not Null)
}

"""----------------------- Runtime ----------------------"""
Runtime = {
   "attributes": "DisplayableAttribute",  # (Not Null)
   "country": "DisplayableCountry",
   "displayableProperty": "DisplayableTitleRuntimeProperty",  # (Not Null)
   "id": str,  # (Not Null)
   "seconds": int,  # (Not Null)
}

"""----------------------- Salary -----------------------"""
Salary = {
   "amount": "Money",
   "attributes": "DisplayableAttribute",  # (Not Null)
   "displayableProperty": "DisplayableSalaryProperty",  # (Not Null)
   "id": str,  # (Not Null)
   "title": "TitleLimited",  # (Not Null)
}

"""
--------------------- ScreeningDateTime --------------------
Date and time of a screening. The screening time will be in
the timezone of the Cinema.
------------------------------------------------------------
"""
ScreeningDateTime = {
   "dateTime": str,  # (Not Null)
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""----------------- SearchAwardCategory ----------------"""
SearchAwardCategory = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""------------------ SearchAwardEvent ------------------"""
SearchAwardEvent = {
   "awardCategories": "SearchAwardCategory",  # (Not Null)
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""--------------- SearchAwardEventOptions --------------"""
SearchAwardEventOptions = {
   "events": "SearchAwardEvent",  # (Not Null)
}

"""--------------------- SearchFacet --------------------"""
SearchFacet = {
   "filterId": str,  # (Not Null)
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
   "total": int,  # (Not Null)
}

"""------------------- SearchMetadata -------------------"""
SearchMetadata = {
   "advancedSearchAwardOptions": "SearchAwardEventOptions",  # (Not Null)
}

"""----------- SeasonValueDisplayableProperty -----------"""
SeasonValueDisplayableProperty = {
   "value": "Markdown",  # (Not Null)
}

"""----------------- SectionCallToAction ----------------"""
SectionCallToAction = {
   "action": "ActionLink",  # (Not Null)
   "resultId": int,  # (Not Null)
   "sectionContent": "CallToActionText",
   "sectionTitle": "CallToActionText",
}

"""-------------------- SelfVerified --------------------"""
SelfVerified = {
   "isSelfVerified": bool,  # (Not Null)
}

"""------------------ SelfVerifiedAward -----------------"""
SelfVerifiedAward = {
   "awardTitle": "LocalizedString",
   "details": "LocalizedString",
   "event": "LocalizedString",
   "id": str,  # (Not Null)
   "year": int,
}

"""---------------- SelfVerifiedEducation ---------------"""
SelfVerifiedEducation = {
   "degree": "LocalizedString",
   "details": "LocalizedString",
   "id": str,  # (Not Null)
   "location": "LocalizedString",
   "school": "LocalizedString",
   "year": int,
}

"""-------------- SelfVerifiedNameAttribute -------------"""
SelfVerifiedNameAttribute = {
   "total": int,  # (Not Null)
   "values": "SelfVerifiedNameAttributeValue",  # (Not Null)
}

"""---------- SelfVerifiedNameAttributeMetadata ---------"""
SelfVerifiedNameAttributeMetadata = {
   "allowFreeFormText": bool,  # (Not Null)
   "limit": int,
   "validValues": "SelfVerifiedNameAttributeValue",  # (Not Null)
}

"""----------- SelfVerifiedNameAttributeValue -----------"""
SelfVerifiedNameAttributeValue = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""---------------- SelfVerifiedNameAward ---------------"""
SelfVerifiedNameAward = {
   "details": "SelfVerifiedNameAttributeValue",
   "event": "SelfVerifiedNameAttributeValue",  # (Not Null)
   "id": str,  # (Not Null)
   "name": "SelfVerifiedNameAttributeValue",  # (Not Null)
   "year": int,  # (Not Null)
}

"""--------------- SelfVerifiedNameCredit ---------------"""
SelfVerifiedNameCredit = {
   "companyOrDirector": "SelfVerifiedNameAttributeValue",
   "id": str,  # (Not Null)
   "projectTitle": "SelfVerifiedNameAttributeValue",  # (Not Null)
   "roleOrPosition": "SelfVerifiedNameAttributeValue",
   "type": "SelfVerifiedNameCreditType",  # (Not Null)
}

"""----------- SelfVerifiedNameCreditMetadata -----------"""
SelfVerifiedNameCreditMetadata = {
   "creditTypes": "SelfVerifiedNameCreditType",  # (Not Null)
   "limit": int,  # (Not Null)
}

"""------------- SelfVerifiedNameCreditType -------------"""
SelfVerifiedNameCreditType = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""-------- SelfVerifiedNameCreditTypeWithCredits -------"""
SelfVerifiedNameCreditTypeWithCredits = {
   "credits": "SelfVerifiedNameCreditConnection",
   "creditType": "SelfVerifiedNameCreditType",  # (Not Null)
}

"""---------------- SelfVerifiedNameData ----------------"""
SelfVerifiedNameData = {
   "accents": "SelfVerifiedNameAttribute",
   "agePlayingRange": "AgePlayingRange",
   "athleticSkills": "SelfVerifiedNameAttribute",
   "awards": "SelfVerifiedNameAwardConnection",
   "blog": "BlogLink",
   "creditTypes": "SelfVerifiedNameCreditTypeWithCredits",  # (Not Null)
   "danceSkills": "SelfVerifiedNameAttribute",
   "educationalHistory": "SelfVerifiedNameEducationConnection",
   "ethnicAppearances": "SelfVerifiedNameAttribute",
   "eyeColor": "SelfVerifiedNameAttributeValue",
   "guildAffiliations": "GuildAffiliationVerificationStatusConnection",
   "guildAffiliationVisibilities": "GuildAffiliationVisibilityStatusConnection",
   "guildStatus": "GuildStatus",
   "hairColor": "SelfVerifiedNameAttributeValue",
   "hairLength": "SelfVerifiedNameAttributeValue",
   "hasValidPassport": bool,
   "isWillingToWorkUnpaid": bool,
   "jobCategories": "SelfVerifiedNameAttribute",
   "jobTitles": "SelfVerifiedNameAttribute",
   "musicalInstruments": "SelfVerifiedNameAttribute",
   "performerSkills": "SelfVerifiedNameAttribute",
   "personalLocations": "NamePersonalLocations",
   "physique": "SelfVerifiedNameAttributeValue",
   "primaryCitizenship": "LocalizedDisplayableCountry",
   "references": "SelfVerifiedNameReferenceConnection",
   "resumeCustomSections": "SelfVerifiedResumeCustomSectionConnection",
   "resumeDetails": "SelfVerifiedNameAttributeValue",
   "spokenLanguages": "SelfVerifiedNameAttribute",
   "trainings": "SelfVerifiedNameTrainingConnection",
   "twitter": "TwitterLink",
   "uniqueTraits": "SelfVerifiedNameAttribute",
   "voiceTypes": "SelfVerifiedNameAttribute",
   "weight": "NameWeight",
   "workAuthorizationCountries": "WorkAuthorizationCountries",
   "workHistoryCreditTypes": "SelfVerifiedNameAttribute",
}

"""-------------- SelfVerifiedNameEducation -------------"""
SelfVerifiedNameEducation = {
   "degree": "SelfVerifiedNameAttributeValue",  # (Not Null)
   "details": "SelfVerifiedNameAttributeValue",
   "id": str,  # (Not Null)
   "location": "SelfVerifiedNameAttributeValue",  # (Not Null)
   "school": "SelfVerifiedNameAttributeValue",  # (Not Null)
   "year": int,  # (Not Null)
}

"""
----------------- SelfVerifiedNameMetadata -----------------
Metadata for some self-verified name data attributes
------------------------------------------------------------
"""
SelfVerifiedNameMetadata = {
   "accent": "SelfVerifiedNameAttributeMetadata",
   "athleticSkill": "SelfVerifiedNameAttributeMetadata",
   "award": "SelfVerifiedNameAttributeMetadata",
   "credit": "SelfVerifiedNameCreditMetadata",
   "danceSkill": "SelfVerifiedNameAttributeMetadata",
   "educationalHistory": "SelfVerifiedNameAttributeMetadata",
   "ethnicAppearance": "SelfVerifiedNameAttributeMetadata",
   "eyeColor": "SelfVerifiedNameAttributeMetadata",
   "guildAffiliation": "SelfVerifiedNameAttributeMetadata",
   "hairColor": "SelfVerifiedNameAttributeMetadata",
   "hairLength": "SelfVerifiedNameAttributeMetadata",
   "jobCategory": "SelfVerifiedNameAttributeMetadata",
   "jobTitle": "SelfVerifiedNameAttributeMetadata",
   "musicalInstrument": "SelfVerifiedNameAttributeMetadata",
   "performerSkill": "SelfVerifiedNameAttributeMetadata",
   "personalLocation": "NamePersonalLocationMetadata",
   "physique": "SelfVerifiedNameAttributeMetadata",
   "primaryCitizenship": "CountryAttributeMetadata",
   "reference": "SelfVerifiedNameAttributeMetadata",
   "resumeCustomSection": "SelfVerifiedNameAttributeMetadata",
   "spokenLanguage": "SelfVerifiedNameAttributeMetadata",
   "training": "SelfVerifiedNameAttributeMetadata",
   "uniqueTrait": "SelfVerifiedNameAttributeMetadata",
   "voiceType": "SelfVerifiedNameAttributeMetadata",
   "workAuthorizationCountry": "CountryAttributeMetadata",
   "workHistoryCreditType": "SelfVerifiedNameAttributeMetadata",
}

"""-------------- SelfVerifiedNameReference -------------"""
SelfVerifiedNameReference = {
   "contactInfo": "SelfVerifiedNameAttributeValue",
   "id": str,  # (Not Null)
   "name": "SelfVerifiedNameAttributeValue",  # (Not Null)
   "relationship": "SelfVerifiedNameAttributeValue",  # (Not Null)
}

"""-------------- SelfVerifiedNameTraining --------------"""
SelfVerifiedNameTraining = {
   "details": "SelfVerifiedNameAttributeValue",
   "id": str,  # (Not Null)
   "instructor": "SelfVerifiedNameAttributeValue",  # (Not Null)
   "location": "SelfVerifiedNameAttributeValue",  # (Not Null)
   "school": "SelfVerifiedNameAttributeValue",  # (Not Null)
   "type": "SelfVerifiedNameAttributeValue",
   "year": int,  # (Not Null)
}

"""---------------- SelfVerifiedReference ---------------"""
SelfVerifiedReference = {
   "contact": "LocalizedString",
   "id": str,  # (Not Null)
   "name": "LocalizedString",
   "relationship": "LocalizedString",
}

"""----------- SelfVerifiedResumeCustomSection ----------"""
SelfVerifiedResumeCustomSection = {
   "body": "SelfVerifiedNameAttributeValue",  # (Not Null)
   "id": str,  # (Not Null)
   "title": "SelfVerifiedNameAttributeValue",  # (Not Null)
}

"""---------------- SelfVerifiedTraining ----------------"""
SelfVerifiedTraining = {
   "details": "LocalizedString",
   "id": str,  # (Not Null)
   "instructor": "LocalizedString",
   "location": "LocalizedString",
   "school": "LocalizedString",
   "training": "LocalizedString",
   "year": int,
}

"""----------------------- Series -----------------------"""
Series = {
   "displayableEpisodeNumber": "DisplayableEpisodeNumber",  # (Not Null)
   "nextEpisode": "TitleLimited",
   "previousEpisode": "TitleLimited",
   "series": "TitleLimited",  # (Not Null)
}

"""---------------- SeriesCreditAttribute ---------------"""
SeriesCreditAttribute = {
    "id": str,
    "total": int,
    "text": str,
    "language": "DisplayableLanguage",
}

"""
----------------------- SeverityLevel ----------------------
The severity level of a particular title, together with the
number of users who voted for this level of severity.
------------------------------------------------------------
"""
SeverityLevel = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
   "votedFor": int,  # (Not Null)
   "voteType": str,  # (Not Null)
}

"""
---------------- SharedCreditCategorySummary ---------------
Count for a CreditCategory, used to fiter the name
connections data
------------------------------------------------------------
"""
SharedCreditCategorySummary = {
   "creditCategory": "CreditCategory",  # (Not Null)
   "total": int,  # (Not Null)
}

"""
---------------------- SharedNameItem ----------------------
A shared name item containing all the data related to mutual
nmconst
------------------------------------------------------------
"""
SharedNameItem = {
   "mutualName": "NameLimited",  # (Not Null)
   "sharedTitlesWithNameInput": "SharedTitle",  # (Not Null)
   "sharedTitlesWithNamePage": "SharedTitle",  # (Not Null)
   "totalSharedTitlesWithNameInput": int,  # (Not Null)
   "totalSharedTitlesWithNamePage": int,  # (Not Null)
}

"""------------------ SharedNamesResult -----------------"""
SharedNamesResult = {
   "sharedCreditCategorySummary": "SharedCreditCategorySummary",  # (Not Null)
   "sharedNames": "SharedNameItemConnection",
   "statusMessage": "LocalizedMarkdown",
}

"""----------------- SharedNamesSummary -----------------"""
SharedNamesSummary = {
   "inNetwork": bool,  # (Not Null)
   "summaryText": "LocalizedString",
   "totalSharedConnections": int,  # (Not Null)
}

"""--------------------- SharedTitle --------------------"""
SharedTitle = {
   "nameInputCreditedJobCategories": "CreditCategory",  # (Not Null)
   "namePageCreditedJobCategories": "CreditCategory",  # (Not Null)
   "title": "TitleLimited",  # (Not Null)
}

"""
------------------------- Showtime -------------------------
A single showtime for a title at a particular cinema.
------------------------------------------------------------
"""
Showtime = {
   "id": str,  # (Not Null)
   "primaryTicketing": "ShowtimeTicketing",
   "screeningStart": "ScreeningDateTime",  # (Not Null)
   "screeningType": "ShowtimeScreeningType",  # (Not Null)
}

"""
----------------- ShowtimesByScreeningType -----------------
List of showtimes for this screening type and title at this
cinema.
------------------------------------------------------------
"""
ShowtimesByScreeningType = {
   "screeningType": "ShowtimeScreeningType",  # (Not Null)
   "showtimes": "Showtime",  # (Not Null)
}

"""
------------------- ShowtimeScreeningType ------------------
The type of showtime screening with displayable text.
------------------------------------------------------------
"""
ShowtimeScreeningType = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""
--------------------- ShowtimeTicketing --------------------
Ticketing information for a showtime.
------------------------------------------------------------
"""
ShowtimeTicketing = {
   "link": str,  # (Not Null)
}

"""-------------------- SignInOption --------------------"""
SignInOption = {
   "redirectURL": str,  # (Not Null)
   "type": str,  # (Not Null)
}

"""------------ SignInOptionRedirectURLOutput -----------"""
SignInOptionRedirectURLOutput = {
   "signInOption": "SignInOption",  # (Not Null)
}

"""----------- SignInOptionsRedirectURLsOutput ----------"""
SignInOptionsRedirectURLsOutput = {
   "signInOptions": "SignInOption",  # (Not Null)
}

"""
------------------------- SoundMix -------------------------
A sound mix, along with any attributes. For example, we
could have a DTS sound that used an RCA sound system.
------------------------------------------------------------
"""
SoundMix = {
   "attributes": "DisplayableAttribute",  # (Not Null)
   "displayableProperty": "DisplayableTechnicalSpecificationProperty",  # (Not Null)
   "id": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""
------------------------ SoundMixes ------------------------
Sound mixes for this title.
------------------------------------------------------------
"""
SoundMixes = {
   "items": "SoundMix",  # (Not Null)
   "restriction": "TechnicalSpecificationsRestriction",
   "total": int,  # (Not Null)
}

"""
------------------- SoundtrackRestriction ------------------
Restriction information applied to Soundtracks
------------------------------------------------------------
"""
SoundtrackRestriction = {
   "explanations": "RestrictionExplanation",  # (Not Null)
   "reasons": str,  # (Not Null)
   "restrictionReason": str,  # (Not Null)
   "unrestrictedTotal": int,
}

"""
-------------------------- Source --------------------------
Image source details, including attribution requirements.
------------------------------------------------------------
"""
Source = {
   "attributionUrl": str,
   "banner": "Banner",
   "id": str,  # (Not Null)
   "text": str,
}

"""------------------- SpokenLanguage -------------------"""
SpokenLanguage = {
   "displayableProperty": "DisplayableTitleSpokenLanguageProperty",  # (Not Null)
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""------------------- SpokenLanguages ------------------"""
SpokenLanguages = {
   "language": "DisplayableLanguage",  # (Not Null)
   "spokenLanguages": "SpokenLanguage",  # (Not Null)
}

"""------------------ SpouseAttributes ------------------"""
SpouseAttributes = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""--------------------- SpouseName ---------------------"""
SpouseName = {
   "asMarkdown": "Markdown",  # (Not Null)
   "name": "NameLimited",
}

"""
------------------------ StaffStatus -----------------------
StaffStatus: contains related staff information
------------------------------------------------------------
"""
StaffStatus = {
   "category": str,  # (Not Null)
}

"""------------------- StreamingTitle -------------------"""
StreamingTitle = {
   "refTag": str,  # (Not Null)
   "title": "TitleLimited",  # (Not Null)
}

"""------------------- StreamingTitles ------------------"""
StreamingTitles = {
   "provider": "WatchProvider",
   "titles": "StreamingTitleConnection",
}

"""---------------- SuggestionSearchItem ----------------"""
SuggestionSearchItem = {
   "constId": str,
   "displayLabels": "DisplayLabels",
   "id": str,  # (Not Null)
   "image": "MediaServiceImage",
   "rank": int,
   "refTagFragment": str,
   "releaseYear": "YearRange",
   "titleTypeId": str,
   "topVideos": "VideoMedia",  # (Not Null)
   "url": str,
   "videoCount": int,
}

"""-------------- SupportedQuestionFilters --------------"""
SupportedQuestionFilters = {
   "countries": str,  # (Not Null)
   "dataTypes": str,  # (Not Null)
   "languages": str,  # (Not Null)
}

"""------------------ SymphonyArgument ------------------"""
SymphonyArgument = {
   "name": str,  # (Not Null)
   "value": str,  # (Not Null)
}

"""------------------ SymphonyMetadata ------------------"""
SymphonyMetadata = {
   "contentId": str,
   "creativeId": str,
   "multiSlotGroupName": str,
   "multiSlotOrder": int,
   "placementId": str,
}

"""------------------ SymphonyPlacement -----------------"""
SymphonyPlacement = {
   "componentArguments": "SymphonyArgument",  # (Not Null)
   "componentMetadata": "SymphonyMetadata",
   "componentName": str,  # (Not Null)
   "slot": str,  # (Not Null)
}

"""
-------------------------- Tagline -------------------------
Tagline details
------------------------------------------------------------
"""
Tagline = {
   "displayableProperty": "DisplayableTitleTaglineProperty",  # (Not Null)
   "text": str,  # (Not Null)
}

"""
------------------ TechnicalSpecifications -----------------
A set of technical specifications
------------------------------------------------------------
"""
TechnicalSpecifications = {
   "aspectRatios": "AspectRatios",  # (Not Null)
   "cameras": "Cameras",  # (Not Null)
   "colorations": "Colorations",  # (Not Null)
   "filmLengths": "FilmLengths",  # (Not Null)
   "laboratories": "Laboratories",  # (Not Null)
   "negativeFormats": "NegativeFormats",  # (Not Null)
   "printedFormats": "PrintedFormats",  # (Not Null)
   "processes": "Processes",  # (Not Null)
   "soundMixes": "SoundMixes",  # (Not Null)
}

"""
------------ TechnicalSpecificationsRestriction ------------
Information about restrictions applied to
technicalSpecifications
------------------------------------------------------------
"""
TechnicalSpecificationsRestriction = {
   "explanations": "RestrictionExplanation",  # (Not Null)
   "reasons": str,  # (Not Null)
   "restrictionReason": str,  # (Not Null)
   "unrestrictedTotal": int,
}

"""------------------------ Test ------------------------"""
Test = {
   "error": str,
   "experimental": str,
   "result": str,
   "testItems": "TestItem",  # (Not Null)
}

"""---------------------- TestAuth ----------------------"""
TestAuth = {
   "cacheableResult": str,
   "cacheableResultWithNoCacheCustomerId": str,
   "cacheableResultWithNoCacheUserId": str,
   "clientIp": str,
   "detectedCountry": str,
   "hasAuthenticationHeaders": bool,
   "hasGatewayName": bool,
   "hasTransitiveAuthenticationHeaders": bool,
   "isInternalClient": bool,
   "isNon1PInternalClient": bool,
   "nonCacheableResult": str,
   "operationName": str,
   "result": str,
}

"""-------------------- TestAuthTimer -------------------"""
TestAuthTimer = {
   "authTimer": str,
}

"""------------------- TestEntitlement ------------------"""
TestEntitlement = {
   "entitlement": str,  # (Not Null)
   "result": str,  # (Not Null)
}

"""---------------------- TestItem ----------------------"""
TestItem = {
   "id": str,  # (Not Null)
}

"""----------------- ThirdPartyTrackers -----------------"""
ThirdPartyTrackers = {
   "impressionTrackers": str,  # (Not Null)
   "titlePosterClickTrackers": str,  # (Not Null)
   "videoCompleteTrackers": str,  # (Not Null)
   "videoFirstQuartileTrackers": str,  # (Not Null)
   "videoMidpointTrackers": str,  # (Not Null)
   "videoStartTrackers": str,  # (Not Null)
   "videoThirdQuartileTrackers": str,  # (Not Null)
}

"""---------------------- Thumbnail ---------------------"""
Thumbnail = {
   "height": int,  # (Not Null)
   "url": str,  # (Not Null)
   "width": int,  # (Not Null)
}

"""
--------------------------- Title --------------------------
Title type Extends external type.
------------------------------------------------------------
"""
Title = {
   "aggregateRatingsBreakdown": "AggregateRatingsBreakdown",
   "akas": "AkaConnection",
   "alexaTopQuestions": "AlexaQuestionConnection",
   "alternateVersions": "AlternateVersionConnection",
   "amazonMusicAlbums": "AmazonMusicProduct",  # (Not Null)
   "awardNominations": "AwardNominationConnection",
   "canonicalUrl": str,
   "canHaveEpisodes": bool,
   "canRate": "CanRate",
   "certificate": "Certificate",
   "certificates": "CertificatesConnection",
   "cinemaShowtimesByScreeningType": "TitleCinemaShowtimesByScreeningTypeConnection",
   "companyCreditCategories": "CompanyCreditCategoryWithCompanyCredits",  # (Not Null)
   "companyCredits": "CompanyCreditConnection",
   "connectionCategories": "ConnectionCategoryWithConnections",  # (Not Null)
   "connections": "TitleConnectionConnection",
   "contributionQuestions": "QuestionConnection",
   "countriesOfOrigin": "CountriesOfOrigin",
   "crazyCredits": "CrazyCreditConnection",
   "creditCategories": "TitleCreditCategoryWithCredits",  # (Not Null)
   "creditGroupings": "CreditGroupingConnection",
   "credits": "CreditConnection",
   "creditsV2": "CreditV2LimitedConnection",
   "engagementStatistics": "EngagementStatistics",
   "episodeCredits": "CreditV2LimitedConnection",
   "episodes": "Episodes",
   "experimental_credits": "ExperimentalCreditConnection",
   "experimental_trackNotificationPreferences": "Experimental_TrackNotificationPreferences",
   "externalLinkCategories": "ExternalLinkCategoryWithExternalLinks",  # (Not Null)
   "externalLinks": "ExternalLinkConnection",
   "faqs": "FaqConnection",
   "featuredPolls": "PollsConnection",
   "featuredReviews": "ReviewsConnection",
   "filmingDates": "FilmingDatesConnection",
   "filmingLocations": "FilmingLocationConnection",
   "genres": "Genres",
   "goofCategories": "GoofCategoryWithGoofs",  # (Not Null)
   "goofs": "GoofConnection",
   "id": str,  # (Not Null)
   "images": "ImageConnection",
   "imageTypes": "ImageTypeWithImages",  # (Not Null)
   "_imageUploadLink": "ContributionLink",
   "interests": "InterestConnection",
   "isAdult": bool,
   "isWGAVerified": bool,
   "keywordItemCategories": "TitleKeywordItemCategoryWithKeywords",  # (Not Null)
   "keywords": "TitleKeywordConnection",
   "latestTrailer": "Video",
   "latestTrailerWebviewPlayer": "WebviewVideoPlayer",
   "lifetimeGross": "BoxOfficeGross",
   "meta": "TitleMeta",
   "metacritic": "Metacritic",
   "meterRank": "TitleMeterRanking",
   "meterRankingHistory": "TitleMeterRankingHistory",
   "moreLikeThisTitles": "TitleLimitedConnection",
   "news": "NewsConnection",
   "nominations": "NominationLimitedConnection",
   "openingWeekendGross": "OpeningWeekendGross",
   "openingWeekendGrosses": "OpeningWeekendGrossConnection",
   "originalTitleText": "TitleText",
   "parentsGuide": "ParentsGuide",
   "_parentsGuideContributionLink": "ContributionLink",
   "plot": "Plot",
   "_plotContributionLink": "ContributionLink",
   "plots": "PlotConnection",
   "prestigiousAwardSummary": "PrestigiousAwardSummary",
   "primaryImage": "ImageLimited",
   "primaryVideos": "VideoConnection",
   "primaryWatchOption": "PrimaryWatchOption",
   "principalCredits": "PrincipalCreditsForCategory",  # (Not Null)
   "principalCreditsV2": "PrincipalCreditsForGrouping",  # (Not Null)
   "productionBudget": "ProductionBudget",
   "productionDates": "ProductionDatesConnection",
   "productionStatus": "ProductionStatusDetails",
   "quotes": "TitleQuoteConnection",
   "rankedLifetimeGross": "RankedLifetimeBoxOfficeGross",
   "rankedLifetimeGrosses": "RankedLifetimeBoxOfficeGrossConnection",
   "ratingsSummary": "RatingsSummary",
   "relatedInterests": "InterestConnection",
   "relatedLists": "ListConnection",
   "releaseDate": "ReleaseDate",
   "releaseDates": "ReleaseDateConnection",
   "releaseYear": "YearRange",
   "_reviewContributionLink": "ContributionLink",
   "reviews": "ReviewsConnection",
   "reviewSummary": "TitleReviewSummary",
   "runtime": "Runtime",
   "runtimes": "RuntimeConnection",
   "series": "Series",
   "soundtrack": "TrackConnection",
   "spokenLanguages": "SpokenLanguages",
   "taglines": "TaglineConnection",
   "technicalSpecifications": "TechnicalSpecifications",
   "titleGenres": "TitleGenres",
   "titleText": "TitleText",
   "titleType": "TitleType",
   "trackNotificationPreferences": "TrackNotificationPreferences",
   "trivia": "TitleTriviaConnection",
   "triviaCategories": "TriviaCategoryWithTrivia",  # (Not Null)
   "_triviaContributionLink": "ContributionLink",
   "userRating": "Rating",
   "userWatchedStatus": "WatchedStatus",
   "videos": "TitleRelatedVideos",
   "videoStrip": "VideoConnection",
   "videoTypes": "VideoTypeWithVideos",  # (Not Null)
   "watchOption": "WatchOption",
   "watchOptionsByCategory": "CategorizedWatchOptionsList",
}

"""----------------- TitleChartMetadata -----------------"""
TitleChartMetadata = {
   "chartDescription": "LocalizedString",  # (Not Null)
   "chartName": "LocalizedString",  # (Not Null)
}

"""--------------- TitleChartRankingsNode ---------------"""
TitleChartRankingsNode = {
   "chartRating": float,  # (Not Null)
   "chartVoteCount": int,  # (Not Null)
   "item": "TitleLimited",  # (Not Null)
}

"""
------------ TitleCinemaShowtimesByScreeningType -----------
Showtimes grouped by screening type for a specific title and
cinema.
------------------------------------------------------------
"""
TitleCinemaShowtimesByScreeningType = {
   "cinema": "Cinema",  # (Not Null)
   "distanceToCinema": "DistanceToCinema",
   "id": str,  # (Not Null)
   "showtimesByScreeningType": "ShowtimesByScreeningType",  # (Not Null)
   "title": "TitleLimited",  # (Not Null)
}

"""
------------ TitleCinemaShowtimesFallbackResult ------------
Contains information about fallback results when the
original query returned no showtimes data. Only populated
when fallback option is specified and fallback results are
found. See calling field for more information.
------------------------------------------------------------
"""
TitleCinemaShowtimesFallbackResult = {
   "fallbackDate": str,  # (Not Null)
}

"""--------------- TitleConnectionCategory --------------"""
TitleConnectionCategory = {
   "id": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""----------- TitleCreditCategoryWithCredits -----------"""
TitleCreditCategoryWithCredits = {
   "category": "CreditCategory",  # (Not Null)
   "credits": "CreditConnection",
}

"""----------------- TitleDisplayOutput -----------------"""
TitleDisplayOutput = {
   "country": str,
   "language": str,
   "prefersReferenceView": bool,  # (Not Null)
}

"""--------------------- TitleGenre ---------------------"""
TitleGenre = {
   "genre": "GenreItem",  # (Not Null)
   "relevanceRanking": int,  # (Not Null)
   "subGenres": "TitleKeyword",  # (Not Null)
}

"""-------------- TitleGenreRecommendation --------------"""
TitleGenreRecommendation = {
   "explanation": "LocalizedMarkdown",  # (Not Null)
   "label": "LocalizedString",  # (Not Null)
   "refTag": str,  # (Not Null)
   "titles": "TitleGenreRecommendationConnection",
}

"""--------------------- TitleGenres --------------------"""
TitleGenres = {
   "genres": "TitleGenre",  # (Not Null)
}

"""
----------------------- TitleKeyword -----------------------
TitleKeyword details
------------------------------------------------------------
"""
TitleKeyword = {
   "interestScore": "InterestScore",  # (Not Null)
   "itemCategory": "TitleKeywordItemCategory",
   "keyword": "Keyword",  # (Not Null)
   "legacyId": str,  # (Not Null)
}

"""
----------------- TitleKeywordItemCategory -----------------
TitleKeyword item scope category details
------------------------------------------------------------
"""
TitleKeywordItemCategory = {
   "id": str,  # (Not Null)
   "itemCategoryId": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""-------- TitleKeywordItemCategoryWithKeywords --------"""
TitleKeywordItemCategoryWithKeywords = {
   "itemCategory": "TitleKeywordItemCategory",  # (Not Null)
   "keywords": "TitleKeywordConnection",  # (Not Null)
}

"""---------------------- TitleMeta ---------------------"""
TitleMeta = {
   "canonicalId": str,  # (Not Null)
   "publicationStatus": str,  # (Not Null)
   "restrictions": "TitleMetaRestrictions",
}

"""-------------------- TitleMetadata -------------------"""
TitleMetadata = {
   "externalLinkCategories": "ExternalLinkCategory",  # (Not Null)
   "goofCategories": "GoofCategory",  # (Not Null)
   "titleConnectionCategories": "TitleConnectionCategory",  # (Not Null)
   "titleGenres": "GenreItem",  # (Not Null)
   "titleTypeCategories": "TitleTypeCategoryWithTitleTypes",  # (Not Null)
   "titleTypes": "TitleType",  # (Not Null)
}

"""
------------------- TitleMetaRestrictions ------------------
Information about restrictions applied to meta
------------------------------------------------------------
"""
TitleMetaRestrictions = {
   "explanations": "RestrictionExplanation",  # (Not Null)
   "reasons": str,  # (Not Null)
   "restrictionReason": str,  # (Not Null)
}

"""------------------ TitleMeterRanking -----------------"""
TitleMeterRanking = {
   "currentRank": int,  # (Not Null)
   "meterType": str,
   "rankChange": "MeterRankChange",
}

"""
----------------- TitleMeterRankingHistory -----------------
Requires entitlement proving Pro subscription.
------------------------------------------------------------
"""
TitleMeterRankingHistory = {
   "bestRank": "MeterRankingHistoryEntry",
   "ranks": "MeterRankingHistoryEntry",  # (Not Null)
   "restriction": "MeterRestriction",
}

"""
------------------------ TitleQuote ------------------------
Quote details
------------------------------------------------------------
"""
TitleQuote = {
   "displayableArticle": "DisplayableArticle",  # (Not Null)
   "id": str,  # (Not Null)
   "interestScore": "InterestScore",  # (Not Null)
   "isSpoiler": bool,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "lines": "TitleQuoteLine",  # (Not Null)
}

"""
-------------------- TitleQuoteCharacter -------------------
A character speaking a line in a Title Quote
------------------------------------------------------------
"""
TitleQuoteCharacter = {
   "character": str,  # (Not Null)
   "name": "NameLimited",
}

"""
---------------------- TitleQuoteLine ----------------------
A specific line in the Title Quote. Can be a verbal line
with characters speaking or stage directions
------------------------------------------------------------
"""
TitleQuoteLine = {
   "characters": "TitleQuoteCharacter",  # (Not Null)
   "stageDirection": str,
   "text": str,
}

"""----------------- TitleRecommendation ----------------"""
TitleRecommendation = {
   "explanations": "RecommendationExplanation",  # (Not Null)
   "refTag": str,  # (Not Null)
   "title": "TitleLimited",  # (Not Null)
}

"""------------------ TitleRelatedVideos ----------------"""
TitleRelatedVideos = {
    "total": int,
}

"""
-------------------- TitleReviewExcerpt --------------------
A review that mentions a theme, and an excerpt from it.
------------------------------------------------------------
"""
TitleReviewExcerpt = {
   "excerpt": "LocalizedMarkdown",
   "review": "Review",  # (Not Null)
}

"""
---------------- TitleReviewSentimentSection ---------------
Review summaries at different length levels for a particular
sentiment
------------------------------------------------------------
"""
TitleReviewSentimentSection = {
   "long": "LocalizedMarkdown",  # (Not Null)
   "medium": "LocalizedMarkdown",  # (Not Null)
   "short": "LocalizedMarkdown",  # (Not Null)
}

"""
-------------------- TitleReviewSummary --------------------
Summary and themes of reviews for a title
------------------------------------------------------------
"""
TitleReviewSummary = {
   "negative": "TitleReviewSentimentSection",
   "overall": "TitleReviewSentimentSection",  # (Not Null)
   "positive": "TitleReviewSentimentSection",
   "themes": "TitleReviewTheme",  # (Not Null)
}

"""
--------------------- TitleReviewTheme ---------------------
A theme identified across multiple reviews
------------------------------------------------------------
"""
TitleReviewTheme = {
   "label": "LocalizedString",  # (Not Null)
   "reviews": "TitleReviewExcerpt",  # (Not Null)
   "sentiment": str,  # (Not Null)
   "summary": "LocalizedMarkdown",  # (Not Null)
   "themeId": str,  # (Not Null)
}

"""---------------------- TitleText ---------------------"""
TitleText = {
   "country": "DisplayableCountry",
   "isOriginalTitle": bool,  # (Not Null)
   "language": "DisplayableLanguage",
   "text": str,  # (Not Null)
}

"""--------------------- TitleTrivia --------------------"""
TitleTrivia = {
   "category": "TriviaCategory",  # (Not Null)
   "_correctionLink": "ContributionLink",
   "displayableArticle": "DisplayableArticle",  # (Not Null)
   "id": str,  # (Not Null)
   "interestScore": "InterestScore",  # (Not Null)
   "isSpoiler": bool,  # (Not Null)
   "relatedNames": "NameLimited",  # (Not Null)
   "_reportingLink": "ContributionLink",
   "text": "Markdown",  # (Not Null)
   "title": "TitleLimited",
   "trademark": "Markdown",
}

"""---------------------- TitleType ---------------------"""
TitleType = {
   "canHaveEpisodes": bool,  # (Not Null)
   "categories": "TitleTypeCategory",  # (Not Null)
   "displayableProperty": "DisplayableTitleTypeProperty",  # (Not Null)
   "id": str,  # (Not Null)
   "isEpisode": bool,  # (Not Null)
   "isSeries": bool,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
}

"""------------------ TitleTypeCategory -----------------"""
TitleTypeCategory = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
   "value": list,  # (Not Null)
}

"""-------------- TitleTypeCategorySummary --------------"""
TitleTypeCategorySummary = {
   "titleTypeCategory": "TitleTypeCategory",  # (Not Null)
   "total": int,  # (Not Null)
}

"""----------- TitleTypeCategoryWithTitleTypes ----------"""
TitleTypeCategoryWithTitleTypes = {
   "category": "TitleTypeCategory",  # (Not Null)
   "titleTypes": "TitleType",  # (Not Null)
}

"""------------------ TitleTypeSummary ------------------"""
TitleTypeSummary = {
   "titleType": "TitleType",  # (Not Null)
   "total": int,  # (Not Null)
}

"""----------------- TitleWatchedStatus -----------------"""
TitleWatchedStatus = {
   "title": "TitleLimited",  # (Not Null)
   "watchedStatus": "WatchedStatus",  # (Not Null)
}

"""------------ TitleWatchlistRecommendation ------------"""
TitleWatchlistRecommendation = {
   "explanation": "LocalizedMarkdown",  # (Not Null)
   "title": "TitleLimited",  # (Not Null)
}

"""--------------- TopGrossingReleasesNode --------------"""
TopGrossingReleasesNode = {
   "gross": "BoxOfficeGross",  # (Not Null)
   "release": "BoxOfficeRelease",  # (Not Null)
}

"""--------------------- TopRanking ---------------------"""
TopRanking = {
   "id": str,  # (Not Null)
   "rank": int,  # (Not Null)
   "text": "LocalizedString",  # (Not Null)
}

"""-------------------- TotalCredits --------------------"""
TotalCredits = {
   "restriction": "CreditRestriction",
   "total": int,  # (Not Null)
}

"""------------------------ Track -----------------------"""
Track = {
   "amazonMusicProducts": "AmazonMusicProduct",  # (Not Null)
   "comments": "Markdown",  # (Not Null)
   "displayableArticle": "DisplayableArticle",  # (Not Null)
   "id": str,  # (Not Null)
   "text": str,
}

"""------------- TrackNotificationPreference ------------"""
TrackNotificationPreference = {
   "interested": bool,  # (Not Null)
   "type": "TrackNotificationPreferenceType",  # (Not Null)
}

"""------------ TrackNotificationPreferences ------------"""
TrackNotificationPreferences = {
   "isTracking": bool,  # (Not Null)
   "notificationPreferences": "TrackNotificationPreference",  # (Not Null)
}

"""
-------------- TrackNotificationPreferenceType -------------
Preference type for a tracked page
------------------------------------------------------------
"""
TrackNotificationPreferenceType = {
   "id": str,  # (Not Null)
   "language": "DisplayableLanguage",  # (Not Null)
   "text": str,  # (Not Null)
   "typeId": str,  # (Not Null)
}

"""---------------------- Trademark ---------------------"""
Trademark = {
   "displayableArticle": "DisplayableArticle",
   "text": "Markdown",  # (Not Null)
}

"""-------------- TrendingCollectionOption --------------"""
TrendingCollectionOption = {
   "country": "DisplayableCountry",  # (Not Null)
   "dataWindow": str,  # (Not Null)
   "trafficSource": str,  # (Not Null)
}

"""--------------- TrendingNameCollection ---------------"""
TrendingNameCollection = {
   "items": "TrendingNameNodeConnection",  # (Not Null)
   "option": "TrendingCollectionOption",  # (Not Null)
}

"""------------ TrendingNameCollectionOptions -----------"""
TrendingNameCollectionOptions = {
   "options": "TrendingCollectionOption",  # (Not Null)
   "selectedItem": "TrendingNameCollection",  # (Not Null)
}

"""------------------ TrendingNameNode ------------------"""
TrendingNameNode = {
   "item": "NameLimited",  # (Not Null)
   "rank": int,  # (Not Null)
   "weightRank": int,  # (Not Null)
}

"""--------------- TrendingTitleCollection --------------"""
TrendingTitleCollection = {
   "items": "TrendingTitleNodeConnection",  # (Not Null)
   "option": "TrendingCollectionOption",  # (Not Null)
}

"""----------- TrendingTitleCollectionOptions -----------"""
TrendingTitleCollectionOptions = {
   "options": "TrendingCollectionOption",  # (Not Null)
   "selectedItem": "TrendingTitleCollection",  # (Not Null)
}

"""------------------ TrendingTitleNode -----------------"""
TrendingTitleNode = {
   "item": "TitleLimited",  # (Not Null)
   "rank": int,  # (Not Null)
   "weightRank": int,  # (Not Null)
}

"""------------------ TrendingVideoNode -----------------"""
TrendingVideoNode = {
   "item": "Video",  # (Not Null)
   "rank": int,  # (Not Null)
   "weightRank": int,  # (Not Null)
}

"""
---------------------- TriviaCategory ----------------------
A category of trivia describing the nature of a subset of
trivia, e.g. 'Director Trademark'. Not all trivia has a
category.
------------------------------------------------------------
"""
TriviaCategory = {
   "id": str,  # (Not Null)
   "text": str,  # (Not Null)
}

"""-------------- TriviaCategoryWithTrivia --------------"""
TriviaCategoryWithTrivia = {
   "category": "TriviaCategory",
   "restriction": "TriviaRestriction",
   "trivia": "TitleTriviaConnection",
}

"""
--------------------- TriviaRestriction --------------------
Information about restrictions applied to trivia
------------------------------------------------------------
"""
TriviaRestriction = {
   "explanations": "RestrictionExplanation",  # (Not Null)
   "reasons": str,  # (Not Null)
   "restrictionReason": str,  # (Not Null)
   "unrestrictedTotal": int,
}

"""--------------------- TwitterLink --------------------"""
TwitterLink = {
   "label": str,
   "url": str,  # (Not Null)
   "username": str,  # (Not Null)
}

"""
------------------------ UIWorkflow ------------------------
The top-level model for a server-driven UI-based workflow
editing experience.
------------------------------------------------------------
"""
UIWorkflow = {
   "actionTray": "UIWorkflowActionTray",  # (Not Null)
   # "body": "UIWorkflowBody",  # (Not Null) # TODO: Only has a union, need to handle it.
   "contentHeader": "UIWorkflowContentHeader",  # (Not Null)
   "contextHeader": "UIWorkflowContextHeader",  # (Not Null)
   # "globalMenu": "UIWorkflowGlobalMenu",  # TODO: Only has a union, need to handle it.
   "workflowState": "UIWorkflowExecutionState",  # (Not Null)
   "workflowType": str,  # (Not Null)
}

"""
--------------------- UIWorkflowAction ---------------------
Represents an actionable button within a UI workflow.
Contains all the necessary information to render and handle
a workflow action.
------------------------------------------------------------
"""
UIWorkflowAction = {
   "id": str,  # (Not Null)
   "label": "LocalizedString",  # (Not Null)
   "navigationDirection": str,
   "requiresFormData": bool,  # (Not Null)
   "type": str,  # (Not Null)
}

"""
------------------- UIWorkflowActionTray -------------------
Represents the action tray component of a UI workflow.
Contains the available actions that can be performed in the
current workflow state.
------------------------------------------------------------
"""
UIWorkflowActionTray = {
   "actions": "UIWorkflowAction",  # (Not Null)
}

"""
---------------------- UIWorkflowBody ----------------------
Represents the main body content of a UI workflow. Contains
an ordered collection of UI elements that form the
workflow's content.
------------------------------------------------------------
"""
UIWorkflowBody = {
   # "elements": "UIWorkflowElementOrGroup",  # (Not Null) # TODO: This is a union type, needs handling.
}

"""
------------------ UIWorkflowContentHeader -----------------
Represents the content header section of a UI workflow.
Contains the main heading and optional help resources for
the workflow.
------------------------------------------------------------
"""
UIWorkflowContentHeader = {
   "heading": "LocalizedMarkdown",  # (Not Null)
   "helpLink": "HelpLink",
}

"""
------------------ UIWorkflowContextHeader -----------------
Represents the context header section of a UI workflow.
Provides contextual information about the current workflow
being performed.
------------------------------------------------------------
"""
UIWorkflowContextHeader = {
   "heading": "LocalizedMarkdown",  # (Not Null)
   # "subject": "UIWorkflowSubject",  # TODO: UNION
}

"""-------------- UIWorkflowExecutionState --------------"""
UIWorkflowExecutionState = {
   "executionId": str,  # (Not Null)
   "interactionId": str,  # (Not Null)
   "status": str,  # (Not Null)
   "workflowId": str,  # (Not Null)
}

"""
------------------- UIWorkflowGlobalMenu -------------------
Represents the global menu structure for the UI workflow
system. Contains navigation items that appear in the global
header.
------------------------------------------------------------
"""
UIWorkflowGlobalMenu = {
   # "menuItems": "UIWorkflowGlobalMenuItem",  # (Not Null) # TODO: UNION
}

"""-------------- UpdateUserProfileFeedback -------------"""
UpdateUserProfileFeedback = {
   "validationFeedback": "ValidationFeedback",
}

"""
--------------------------- User ---------------------------
User Type available only for authenticated users Includes
private info. Also includes public info in profile field.
Includes optional ProStatus and StaffStatus fields.
------------------------------------------------------------
"""
User = {
   "displayName": str,  # (Not Null)
   "feedbackGiven": "FeedbackGiven",  # (Not Null)
   "fullName": str,  # (Not Null)
   "interests": "InterestConnection",  # (Not Null)
   "linkedAuthProviders": "LinkedAuthProvider",  # (Not Null)
   "preferredLanguage": str,
   "preferredStreamingProviders": "UserPreferredStreamingProvidersOutput",  # (Not Null)
   "profile": "UserProfile",  # (Not Null)
   "proStatus": "ProStatus",
   "ratingsPrivacy": "RatingsPrivacy",
   "staffStatus": "StaffStatus",
   "titleDisplay": "TitleDisplayOutput",  # (Not Null)
}

"""------------------ UserConsentOutput -----------------"""
UserConsentOutput = {
   "consent": "Consent",
   "consentOperation": str,
   "consentType": str,  # (Not Null)
}

"""-------- UserLinkedAuthProviderStatusesOutput --------"""
UserLinkedAuthProviderStatusesOutput = {
   "providers": "AuthProviderStatus",  # (Not Null)
}

"""
--------------------- UserNotification ---------------------
Entity type of a single notification in the Notification
Center.
------------------------------------------------------------
"""
UserNotification = {
   "header": "LocalizedString",  # (Not Null)
   "id": str,  # (Not Null)
   "image": "MediaServiceImage",
   "lastUpdated": str,  # (Not Null)
   "primaryContent": "LocalizedMarkdown",  # (Not Null)
   "secondaryContent": "LocalizedString",
   "url": str,
}

"""-------- UserPreferredStreamingProvidersOutput -------"""
UserPreferredStreamingProvidersOutput = {
   "streamingProviders": "WatchProviderConnection",  # (Not Null)
   "total": int,  # (Not Null)
}

"""
------------------------ UserProfile -----------------------
User type Extends external type.
------------------------------------------------------------
"""
UserProfile = {
   "bio": "UserProfileBio",
   "creationDate": str,
   "primaryImage": "UserProfileImage",
   "userId": str,  # (Not Null)
   "username": "UserProfileUsername",
}

"""------------------- UserProfileBio -------------------"""
UserProfileBio = {
   "status": "UserProfileBioUpdateStatus",
   "text": "Markdown",
}

"""------------- UserProfileBioUpdateStatus -------------"""
UserProfileBioUpdateStatus = {
   "lastUpdated": str,
   "modifiedItem": "Markdown",
   "updateFeedback": "UpdateUserProfileFeedback",  # (Not Null)
   "updateStatus": str,  # (Not Null)
}

"""------------------ UserProfileImage ------------------"""
UserProfileImage = {
   "image": "ImageLimited",
   "status": "UserProfileImageUpdateStatus",
}

"""------------ UserProfileImageUpdateStatus ------------"""
UserProfileImageUpdateStatus = {
   "lastUpdated": str,
   "modifiedItem": "ImageLimited",
   "updateFeedback": "UpdateUserProfileFeedback",  # (Not Null)
   "updateStatus": str,  # (Not Null)
}

"""----------------- UserProfileUsername ----------------"""
UserProfileUsername = {
   "status": "UserProfileUsernameUpdateStatus",
   "text": str,
}

"""----------- UserProfileUsernameUpdateStatus ----------"""
UserProfileUsernameUpdateStatus = {
   "lastUpdated": str,
   "modifiedItem": str,
   "updateFeedback": "UpdateUserProfileFeedback",  # (Not Null)
   "updateStatus": str,  # (Not Null)
}

"""
----------------------- UserReaction -----------------------
Defines a reaction made by a user
------------------------------------------------------------
"""
UserReaction = {
   "entityId": str,  # (Not Null)
   "lastUpdated": str,  # (Not Null)
   "reaction": "Reaction",  # (Not Null)
}

"""----------------- ValidationFeedback -----------------"""
ValidationFeedback = {
   "message": "LocalizedMarkdown",
   "status": str,  # (Not Null)
   "title": "LocalizedMarkdown",  # (Not Null)
}

"""---------------------- VanityUrl ---------------------"""
VanityUrl = {
   "label": str,
   "name": "NameLimited",  # (Not Null)
   "url": str,  # (Not Null)
   "urlPath": str,  # (Not Null)
}

"""
--------------------------- Video --------------------------
Video type Extends external type.
------------------------------------------------------------
"""
Video = {
   "appAdURL": str,
   "appAdURLV2": str,
   "contentType": "VideoContentType",
   "createdDate": str,
   "description": "LocalizedString",
   "id": str,  # (Not Null)
   "isMature": bool,  # (Not Null)
   "name": "LocalizedString",  # (Not Null)
   "personalizedSuggestedVideos": "VideoLimitedConnection",
   "playbackURLs": "PlaybackURL",  # (Not Null)
   "previewURLs": "PlaybackURL",  # (Not Null)
   "primaryTitle": "TitleLimited",
   "providerType": "VideoProviderType",  # (Not Null)
   "reactionsSummary": "ReactionsSummary",
   "recommendedTimedTextTrack": "VideoTimedTextTrack",
   "relatedNames": "VideoNameRelationConnection",
   "relatedTitles": "VideoTitleRelationConnection",
   "relatedVideos": "VideoLimitedConnection",
   "runtime": "VideoRuntime",
   "thumbnail": "Thumbnail",  # (Not Null)
   "timedTextTracks": "VideoTimedTextTrack",  # (Not Null)
   "userReactions": "UserReaction",  # (Not Null)
   "videoDimensions": "VideoDimensions",
   "webAdURL": str,
   "webAdURLV2": str,
}

"""------------------ VideoContentType ------------------"""
VideoContentType = {
   "displayName": "LocalizedString",  # (Not Null)
   "id": str,  # (Not Null)
}

"""------------------- VideoDimensions ------------------"""
VideoDimensions = {
   "appearance": str,  # (Not Null)
   "aspectRatio": float,  # (Not Null)
   "height": int,  # (Not Null)
   "width": int,  # (Not Null)
}

"""
------------------------ VideoFacets -----------------------
Response facets are impacted by the VideosQueryFilter. All
types, nameConstraints, and titleConstraints filter options
will be included in the facet results, even if just set to a
count of 0
------------------------------------------------------------
"""
VideoFacets = {
   "names": "VideoNameFacet",  # (Not Null)
   "titles": "VideoTitleFacet",  # (Not Null)
   "types": "VideoTypeFacet",  # (Not Null)
}

"""--------------------- VideoMedia ---------------------"""
VideoMedia = {
   "id": str,  # (Not Null)
   "name": "LocalizedString",  # (Not Null)
   "primaryImage": "MediaServiceImage",
   "runtime": "VideoRuntime",
}

"""
---------------------- VideoNameFacet ----------------------
Provides information on how many videos in a gallery match
the specified video name
------------------------------------------------------------
"""
VideoNameFacet = {
   "name": "NameLimited",  # (Not Null)
   "total": int,  # (Not Null)
}

"""------------------ VideoNameRelation -----------------"""
VideoNameRelation = {
    "name": "NameLimited",
}

"""------------------ VideoProviderType -----------------"""
VideoProviderType = {
   "id": str,  # (Not Null)
}

"""
----------------------- VideoRuntime -----------------------
Types
------------------------------------------------------------
"""
VideoRuntime = {
   "unit": str,  # (Not Null)
   "value": int,  # (Not Null)
}

"""
-------------------- VideoTimedTextTrack -------------------
Represents a single VideoTimedTextTrack that can be used to
display text that is synced with a video's audio during
video playback. Contains a URL, language, and a descriptive
displayName. For a given video language (ex. en-US) pairing
only a single VideoTimedTextTrack will be returned, based on
accessibility criteria defined by business.
------------------------------------------------------------
"""
VideoTimedTextTrack = {
   "displayName": "LocalizedString",  # (Not Null)
   "language": str,  # (Not Null)
   "refTagFragment": str,  # (Not Null)
   "type": str,  # (Not Null)
   "url": str,  # (Not Null)
}

"""
---------------------- VideoTitleFacet ---------------------
Provides information on how many videos in a gallery match
the specified video title
------------------------------------------------------------
"""
VideoTitleFacet = {
   "title": "TitleLimited",  # (Not Null)
   "total": int,  # (Not Null)
}

"""------------------ VideoTitleRelation ----------------"""
VideoTitleRelation = {
    'title': "TitleLimited",
}

"""
---------------------- VideoTypeFacet ----------------------
Provides information on how many videos in a gallery match
the specified video type
------------------------------------------------------------
"""
VideoTypeFacet = {
   "total": int,  # (Not Null)
   "type": "VideoContentType",  # (Not Null)
}

"""----------------- VideoTypeWithVideos ----------------"""
VideoTypeWithVideos = {
   "videos": "VideoConnection",
   "videoType": "VideoContentType",  # (Not Null)
}

"""-------------------- WatchedStatus -------------------"""
WatchedStatus = {
   "firstWatched": str,
   "isWatched": bool,  # (Not Null)
   "remainingWatchedSourceTypes": str,  # (Not Null)
}

"""----------------- WatchlistStatistics ----------------"""
WatchlistStatistics = {
   "displayableCount": "LocalizedDisplayableCount",
   "totalCount": int,
}

"""--------------------- WatchOption --------------------"""
WatchOption = {
   "description": "LocalizedString",
   "link": str,  # (Not Null)
   "promoted": bool,
   "provider": "WatchProvider",  # (Not Null)
   "providerName": "LocalizedString",  # (Not Null)
   "providerRefTagFragment": str,  # (Not Null)
   "shortDescription": "LocalizedString",
   "shortTitle": "LocalizedString",  # (Not Null)
   "title": "LocalizedString",  # (Not Null)
}

"""-------------------- WatchProvider -------------------"""
WatchProvider = {
   "description": "LocalizedString",
   "id": str,  # (Not Null)
   "isPopular": bool,  # (Not Null)
   "isSupported": bool,  # (Not Null)
   "logos": "WatchProviderLogos",
   "name": "LocalizedString",  # (Not Null)
   "refTagFragment": str,  # (Not Null)
   "watchOptionCategoryType": str,
}

"""
-------------------- WatchProviderLogos --------------------
Types
------------------------------------------------------------
"""
WatchProviderLogos = {
   "icon": "MediaServiceImage",
   "slate": "MediaServiceImage",
}

"""--------------------- WebsiteLink --------------------"""
WebsiteLink = {
   "label": str,
   "url": str,  # (Not Null)
}

"""----------------- WebviewVideoPlayer -----------------"""
WebviewVideoPlayer = {
   "audioLanguage": str,  # (Not Null)
   "burnedInCaptionsLanguage": str,
   "description": "LocalizedString",
   "webviewUrl": str,  # (Not Null)
}

"""------------- WorkAuthorizationCountries -------------"""
WorkAuthorizationCountries = {
   "total": int,  # (Not Null)
   "workAuthorizations": "WorkAuthorizationInCountry",  # (Not Null)
}

"""------------- WorkAuthorizationInCountry -------------"""
WorkAuthorizationInCountry = {
   "country": "LocalizedDisplayableCountry",  # (Not Null)
   "isAuthorized": bool,  # (Not Null)
}

"""--------------- YearDisplayableProperty --------------"""
YearDisplayableProperty = {
   "value": "Markdown",  # (Not Null)
}

"""
------------------------- YearRange ------------------------
A range of years
------------------------------------------------------------
"""
YearRange = {
   "endYear": int,
   "year": int,
}

