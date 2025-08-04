# fmt: off
class Edge:
    def __init__(self, **kwargs):
        self.pageInfo = kwargs.get("PageInfo", {})
        self.edges = kwargs.get("edges", [])
    def __str__(self):
        return str(self.edges)
    def __repr__(self):
        return f"Edge(pageInfo={self.pageInfo}, edges={self.edges})"

class AccountDataDialogOutput:
    def __init__(self, **kwargs):
        if kwargs.get('prompt'):
            self.prompt = LocalizedMarkdown(**kwargs.get('prompt', {}))
        else:
            self.prompt = None
        if kwargs.get('redirectionPrompt'):
            self.redirectionPrompt = AccountDataDialogRedirectionPrompt(**kwargs.get('redirectionPrompt', {}))
        else:
            self.redirectionPrompt = None
        if kwargs.get('supportMessage'):
            self.supportMessage = LocalizedMarkdown(**kwargs.get('supportMessage', {}))
        else:
            self.supportMessage = None
    def __str__(self):
        return str(self.prompt)
    def __repr__(self):
        return f"AccountDataDialogOutput(prompt={self.prompt}, redirectionPrompt={self.redirectionPrompt}, supportMessage={self.supportMessage})"
    def __eq__(self, other):
        if not isinstance(other, AccountDataDialogOutput):
            return False
        return (self.prompt == other.prompt and self.redirectionPrompt == other.redirectionPrompt and self.supportMessage == other.supportMessage)

class AccountDataDialogRedirectionPrompt:
    def __init__(self, **kwargs):
        if kwargs.get('action'):
            self.action = RedirectLink(**kwargs.get('action', {}))
        else:
            self.action = None
        if kwargs.get('message'):
            self.message = LocalizedMarkdown(**kwargs.get('message', {}))
        else:
            self.message = None
    def __str__(self):
        if self.action and self.message:
            return f"{self.message} ({self.action})"
        elif self.message:
            return str(self.message)
        elif self.action:
            return str(self.action)
        return ""
    def __repr__(self):
        return f"AccountDataDialogRedirectionPrompt(action={self.action}, message={self.message})"
    def __eq__(self, other):
        if not isinstance(other, AccountDataDialogRedirectionPrompt):
            return False
        return (self.action == other.action and self.message == other.message)

class ActionLink:
    def __init__(self, **kwargs):
        if kwargs.get('label'):
            self.label = CallToActionText(**kwargs.get('label', {}))
        else:
            self.label = None
        self.url = kwargs.get('url', "")
    def __str__(self):
        return self.url
    def __repr__(self):
        return f"ActionLink(label={self.label}, url={self.url})"
    def __eq__(self, other):
        if not isinstance(other, ActionLink):
            return False
        return (self.label == other.label and self.url == other.url)

class AdCreativeInfo:
    def __init__(self, **kwargs):
        self.hasAutoplay = kwargs.get('hasAutoplay', False)
        self.isEligibleFor3pAd = kwargs.get('isEligibleFor3pAd', False)
        self.isPremium = kwargs.get('isPremium', False)
        self.shouldFitToWidth = kwargs.get('shouldFitToWidth', False)
        if kwargs.get('size'):
            self.size = CreativeSize(**kwargs.get('size', {}))
        else:
            self.size = None
        self.slotMarkup = kwargs.get('slotMarkup', "")
    def __str__(self):
        return self.__repr__()
    def __repr__(self):
        return f"AdCreativeInfo(hasAutoplay={self.hasAutoplay}, isEligibleFor3pAd={self.isEligibleFor3pAd}, isPremium={self.isPremium}, shouldFitToWidth={self.shouldFitToWidth}, size={self.size}, slotMarkup={self.slotMarkup})"
    def __eq__(self, other):
        if not isinstance(other, AdCreativeInfo):
            return False
        return (self.hasAutoplay == other.hasAutoplay and self.isEligibleFor3pAd == other.isEligibleFor3pAd and self.isPremium == other.isPremium and self.shouldFitToWidth == other.shouldFitToWidth and self.size == other.size and self.slotMarkup == other.slotMarkup)

class AdLayoutConfiguration:
    def __init__(self, **kwargs):
        self.adLayoutType = kwargs.get('adLayoutType', "")
        if kwargs.get('adSlotConfigs'):
            self.adSlotConfigs = AdSlotConfiguration(**kwargs.get('adSlotConfigs', {}))
        else:
            self.adSlotConfigs = None
    def __str__(self):
        return self.adLayoutType
    def __repr__(self):
        return f"AdLayoutConfiguration(adLayoutType={self.adLayoutType}, adSlotConfigs={self.adSlotConfigs})"
    def __eq__(self, other):
        if not isinstance(other, AdLayoutConfiguration):
            return False
        return (self.adLayoutType == other.adLayoutType and self.adSlotConfigs == other.adSlotConfigs)

class AdSlot:
    def __init__(self, **kwargs):
        self.adFeedbackUrl = kwargs.get('adFeedbackUrl', "")
        if kwargs.get('creativeInfo'):
            self.creativeInfo = AdCreativeInfo(**kwargs.get('creativeInfo', {}))
        else:
            self.creativeInfo = None
        self.name = kwargs.get('name', "")
    def __str__(self):
        return self.adFeedbackUrl
    def __repr__(self):
        return f"AdSlot(adFeedbackUrl={self.adFeedbackUrl}, creativeInfo={self.creativeInfo}, name={self.name})"
    def __eq__(self, other):
        if not isinstance(other, AdSlot):
            return False
        return (self.adFeedbackUrl == other.adFeedbackUrl and self.creativeInfo == other.creativeInfo and self.name == other.name)

class AdSlotConfiguration:
    def __init__(self, **kwargs):
        if kwargs.get('apsConfig'):
            self.apsConfig = ApsConfiguration(**kwargs.get('apsConfig', {}))
        else:
            self.apsConfig = None
        self.name = kwargs.get('name', "")
        if kwargs.get('size'):
            self.size = CreativeSize(**kwargs.get('size', {}))
        else:
            self.size = None
    def __str__(self):
        if self.apsConfig and self.name:
            return f"{self.name} ({self.apsConfig})"
        elif self.apsConfig:
            return str(self.apsConfig)
        elif self.name:
            return self.name
        return ""
    def __repr__(self):
        return f"AdSlotConfiguration(apsConfig={self.apsConfig}, name={self.name}, size={self.size})"
    def __eq__(self, other):
        if not isinstance(other, AdSlotConfiguration):
            return False
        return (self.apsConfig == other.apsConfig and self.name == other.name and self.size == other.size)

class AdditionalCreditItem:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = LocalizedString(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('details'):
            self.details = LocalizedString(**kwargs.get('details', {}))
        else:
            self.details = None
        self.id = kwargs.get('id', "")
        if kwargs.get('job'):
            self.job = LocalizedString(**kwargs.get('job', {}))
        else:
            self.job = None
        if kwargs.get('title'):
            self.title = LocalizedString(**kwargs.get('title', {}))
        else:
            self.title = None
    def __str__(self):
        return str(self.title)
    def __repr__(self):
        return f"AdditionalCreditItem(category={self.category}, details={self.details}, id={self.id}, job={self.job}, title={self.title})"
    def __eq__(self, other):
        if not isinstance(other, AdditionalCreditItem):
            return False
        return self.id == other.id

class AdditionalResumeInfo:
    def __init__(self, **kwargs):
        if kwargs.get('details'):
            self.details = LocalizedString(**kwargs.get('details', {}))
        else:
            self.details = None
        self.id = kwargs.get('id', "")
        if kwargs.get('title'):
            self.title = LocalizedString(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, AdditionalResumeInfo):
            return False
        return self.id == other.id


class AdditionalResumeInfoConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(AdditionalResumeInfo(**node.get("node", {})))

class AdvancedNameSearchResult:
    def __init__(self, **kwargs):
        if kwargs.get('name'):
            self.name = Name(**kwargs.get('name', {}))
        else:
            self.name = None
    def __eq__(self, other):
        if not isinstance(other, AdvancedNameSearchResult):
            return False
        return (self.name == other.name)

class AdvancedTitleSearchResult:
    def __init__(self, **kwargs):
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, AdvancedTitleSearchResult):
            return False
        return (self.title == other.title)

class AgeDetails:
    def __init__(self, **kwargs):
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableNameAgeDetailsProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
        self.value = kwargs.get('value', 0)
    def __str__(self):
        return str(self.text) if self.text else f"{self.value} years"
    def __repr__(self):
        return f"AgeDetails(displayableProperty={self.displayableProperty}, id={self.id}, language={self.language}, text={self.text}, value={self.value})"
    def __int__(self):
        return int(self.value) if self.value else 0
    def __float__(self):
        return float(self.value) if self.value else 0.0
    def __eq__(self, other):
        if not isinstance(other, AgeDetails):
            return False
        return self.id == other.id

class AgePlayingRange:
    def __init__(self, **kwargs):
        self.from_date = kwargs.get('from_date', 0)
        self.to_date = kwargs.get('to_date', 0)
    def __str__(self):
        if self.from_date and self.to_date:
            return f"{self.from_date} - {self.to_date} years"
        return ""
    def __repr__(self):
        return f"AgePlayingRange(from_date={self.from_date}, to_date={self.to_date})"
    def __int__(self):
        if self.from_date and self.to_date:
            return int(self.from_date)
        return 0
    def __float__(self):
        if self.from_date and self.to_date:
            return float(self.from_date)
        return 0.0
    def __eq__(self, other):
        if not isinstance(other, AgePlayingRange):
            return False
        return (self.from_date == other.from_date and self.to_date == other.to_date)

class Agency:
    def __init__(self, **kwargs):
        if kwargs.get('agents'):
            self.agents = Agent(**kwargs.get('agents', {}))
        else:
            self.agents = None
        if kwargs.get('company'):
            self.company = Company(**kwargs.get('company', {}))
        else:
            self.company = None
    def __str__(self):
        return str(self.company) if self.company else ""
    def __repr__(self):
        return f"Agency(agents={self.agents}, company={self.company})"
    def __eq__(self, other):
        if not isinstance(other, Agency):
            return False
        return (self.agents == other.agents and self.company == other.company)

class Agent:
    def __init__(self, **kwargs):
        if kwargs.get('branch'):
            self.branch = CompanyBranch(**kwargs.get('branch', {}))
        else:
            self.branch = None
        if kwargs.get('company'):
            self.company = Company(**kwargs.get('company', {}))
        else:
            self.company = None
        if kwargs.get('employeeContact'):
            self.employeeContact = CompanyContactDetails(**kwargs.get('employeeContact', {}))
        else:
            self.employeeContact = None
        self.id = kwargs.get('id', "")
        self.isPrimaryAgent = kwargs.get('isPrimaryAgent', False)
        if kwargs.get('jobTitle'):
            self.jobTitle = LocalizedString(**kwargs.get('jobTitle', {}))
        else:
            self.jobTitle = None
        if kwargs.get('name'):
            self.name = Name(**kwargs.get('name', {}))
        else:
            self.name = None
        if kwargs.get('occupation'):
            self.occupation = OccupationValue(**kwargs.get('occupation', {}))
        else:
            self.occupation = None
        if kwargs.get('relationshipType'):
            self.relationshipType = RepresentationRelationshipType(**kwargs.get('relationshipType', {}))
        else:
            self.relationshipType = None
    def __eq__(self, other):
        if not isinstance(other, Agent):
            return False
        return self.id == other.id

class AggregateRatingsBreakdown:
    def __init__(self, **kwargs):
        if kwargs.get('histogram'):
            self.histogram = Histogram(**kwargs.get('histogram', {}))
        else:
            self.histogram = None
        self.isCollapsed = kwargs.get('isCollapsed', False)
        if kwargs.get('ratingsSummaryByCountry'):
            self.ratingsSummaryByCountry = RatingsSummaryByCountry(**kwargs.get('ratingsSummaryByCountry', {}))
        else:
            self.ratingsSummaryByCountry = None
        if kwargs.get('ratingsSummaryByDemographics'):
            self.ratingsSummaryByDemographics = DemographicRatings(**kwargs.get('ratingsSummaryByDemographics', {}))
        else:
            self.ratingsSummaryByDemographics = None
    def __eq__(self, other):
        if not isinstance(other, AggregateRatingsBreakdown):
            return False
        return (self.histogram == other.histogram and self.isCollapsed == other.isCollapsed and self.ratingsSummaryByCountry == other.ratingsSummaryByCountry and self.ratingsSummaryByDemographics == other.ratingsSummaryByDemographics)

class Aka:
    def __init__(self, **kwargs):
        if kwargs.get('attributes'):
            self.attributes = [DisplayableAttribute(**attr) for attr in kwargs.get('attributes', [])]
        else:
            self.attributes = None
        if kwargs.get('country'):
            self.country = DisplayableCountry(**kwargs.get('country', {}))
        else:
            self.country = None
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableTitleAkaProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, Aka):
            return False
        return (self.attributes == other.attributes and self.country == other.country and self.displayableProperty == other.displayableProperty and self.language == other.language and self.text == other.text)


class AkaConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Aka(**node.get("node", {})))

class AlexaQuestion:
    def __init__(self, **kwargs):
        if kwargs.get('answer'):
            self.answer = Markdown(**kwargs.get('answer', {}))
        else:
            self.answer = None
        self.attributeId = kwargs.get('attributeId', "")
        if kwargs.get('question'):
            self.question = Markdown(**kwargs.get('question', {}))
        else:
            self.question = None
    def __eq__(self, other):
        if not isinstance(other, AlexaQuestion):
            return False
        return (self.answer == other.answer and self.attributeId == other.attributeId and self.question == other.question)


class AlexaQuestionConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(AlexaQuestion(**node.get("node", {})))

class AlternateVersion:
    def __init__(self, **kwargs):
        if kwargs.get('displayableArticle'):
            self.displayableArticle = DisplayableArticle(**kwargs.get('displayableArticle', {}))
        else:
            self.displayableArticle = None
        if kwargs.get('text'):
            self.text = Markdown(**kwargs.get('text', {}))
        else:
            self.text = None
    def __eq__(self, other):
        if not isinstance(other, AlternateVersion):
            return False
        return (self.displayableArticle == other.displayableArticle and self.text == other.text)


class AlternateVersionConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(AlternateVersion(**node.get("node", {})))

class AmazonMusicProduct:
    def __init__(self, **kwargs):
        if kwargs.get('amazonId'):
            self.amazonId = AmazonStandardId(**kwargs.get('amazonId', {}))
        else:
            self.amazonId = None
        if kwargs.get('artists'):
            self.artists = AmazonMusicProductArtist(**kwargs.get('artists', {}))
        else:
            self.artists = None
        if kwargs.get('format'):
            self.format = AmazonMusicProductFormat(**kwargs.get('format', {}))
        else:
            self.format = None
        if kwargs.get('image'):
            self.image = Image(**kwargs.get('image', {}))
        else:
            self.image = None
        if kwargs.get('productTitle'):
            self.productTitle = AmazonMusicProductTitle(**kwargs.get('productTitle', {}))
        else:
            self.productTitle = None
    def __eq__(self, other):
        if not isinstance(other, AmazonMusicProduct):
            return False
        return (self.amazonId == other.amazonId and self.artists == other.artists and self.format == other.format and self.image == other.image and self.productTitle == other.productTitle)

class AmazonMusicProductArtist:
    def __init__(self, **kwargs):
        if kwargs.get('artistName'):
            self.artistName = AmazonMusicProductArtistName(**kwargs.get('artistName', {}))
        else:
            self.artistName = None
    def __eq__(self, other):
        if not isinstance(other, AmazonMusicProductArtist):
            return False
        return (self.artistName == other.artistName)

class AmazonMusicProductArtistName:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, AmazonMusicProductArtistName):
            return False
        return self.id == other.id

class AmazonMusicProductFormat:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, AmazonMusicProductFormat):
            return False
        return self.id == other.id

class AmazonMusicProductTitle:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, AmazonMusicProductTitle):
            return False
        return self.id == other.id

class AmazonStandardId:
    def __init__(self, **kwargs):
        self.asin = kwargs.get('asin', "")
        self.obfuscatedMarketplaceId = kwargs.get('obfuscatedMarketplaceId', "")
        self.region = kwargs.get('region', "")
    def __eq__(self, other):
        if not isinstance(other, AmazonStandardId):
            return False
        return (self.asin == other.asin and self.obfuscatedMarketplaceId == other.obfuscatedMarketplaceId and self.region == other.region)

class AnswerOption:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, AnswerOption):
            return False
        return self.id == other.id

class AppAdsInfoOutput:
    def __init__(self, **kwargs):
        if kwargs.get('adLayoutSlotConfig'):
            self.adLayoutSlotConfig = AdLayoutConfiguration(**kwargs.get('adLayoutSlotConfig', {}))
        else:
            self.adLayoutSlotConfig = None
        self.thirdPartyAdsEligibility = kwargs.get('thirdPartyAdsEligibility', False)
    def __eq__(self, other):
        if not isinstance(other, AppAdsInfoOutput):
            return False
        return (self.adLayoutSlotConfig == other.adLayoutSlotConfig and self.thirdPartyAdsEligibility == other.thirdPartyAdsEligibility)

class ApsConfiguration:
    def __init__(self, **kwargs):
        if kwargs.get('apsSlot'):
            self.apsSlot = ApsSlot(**kwargs.get('apsSlot', {}))
        else:
            self.apsSlot = None
        if kwargs.get('apsSlotAdRefresh'):
            self.apsSlotAdRefresh = ApsSlot(**kwargs.get('apsSlotAdRefresh', {}))
        else:
            self.apsSlotAdRefresh = None
    def __eq__(self, other):
        if not isinstance(other, ApsConfiguration):
            return False
        return (self.apsSlot == other.apsSlot and self.apsSlotAdRefresh == other.apsSlotAdRefresh)

class ApsSlot:
    def __init__(self, **kwargs):
        self.apsSlotId = kwargs.get('apsSlotId', "")
        self.apsSlotName = kwargs.get('apsSlotName', "")
    def __eq__(self, other):
        if not isinstance(other, ApsSlot):
            return False
        return (self.apsSlotId == other.apsSlotId and self.apsSlotName == other.apsSlotName)

class AspectRatio:
    def __init__(self, **kwargs):
        self.aspectRatio = kwargs.get('aspectRatio', "")
        if kwargs.get('attributes'):
            self.attributes = [DisplayableAttribute(**attr) for attr in kwargs.get('attributes', [])]
        else:
            self.attributes = None
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableTechnicalSpecificationProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
    def __eq__(self, other):
        if not isinstance(other, AspectRatio):
            return False
        return (self.aspectRatio == other.aspectRatio and self.attributes == other.attributes and self.displayableProperty == other.displayableProperty)

class AspectRatios:
    def __init__(self, **kwargs):
        if kwargs.get('items'):
            self.items = AspectRatio(**kwargs.get('items', {}))
        else:
            self.items = None
        if kwargs.get('restriction'):
            self.restriction = TechnicalSpecificationsRestriction(**kwargs.get('restriction', {}))
        else:
            self.restriction = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, AspectRatios):
            return False
        return (self.items == other.items and self.restriction == other.restriction and self.total == other.total)

class AuthProviderDeprecationMessage:
    def __init__(self, **kwargs):
        if kwargs.get('message'):
            self.message = LocalizedMarkdown(**kwargs.get('message', {}))
        else:
            self.message = None
        if kwargs.get('urls'):
            self.urls = AuthProviderDeprecationUrl(**kwargs.get('urls', {}))
        else:
            self.urls = None
    def __eq__(self, other):
        if not isinstance(other, AuthProviderDeprecationMessage):
            return False
        return (self.message == other.message and self.urls == other.urls)

class AuthProviderDeprecationUrl:
    def __init__(self, **kwargs):
        if kwargs.get('label'):
            self.label = AuthProviderDeprecationUrlLabel(**kwargs.get('label', {}))
        else:
            self.label = None
        self.value = kwargs.get('value', "")
    def __eq__(self, other):
        if not isinstance(other, AuthProviderDeprecationUrl):
            return False
        return (self.label == other.label and self.value == other.value)

class AuthProviderDeprecationUrlLabel:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, AuthProviderDeprecationUrlLabel):
            return False
        return self.id == other.id

class AuthProviderStatus:
    def __init__(self, **kwargs):
        self.provider = kwargs.get('provider', "")
        self.providerLinkingURL = kwargs.get('providerLinkingURL', "")
    def __eq__(self, other):
        if not isinstance(other, AuthProviderStatus):
            return False
        return (self.provider == other.provider and self.providerLinkingURL == other.providerLinkingURL)

class AwardCategory:
    def __init__(self, **kwargs):
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, AwardCategory):
            return False
        return (self.text == other.text)

class AwardDetails:
    def __init__(self, **kwargs):
        if kwargs.get('eventEdition'):
            self.eventEdition = EventEdition(**kwargs.get('eventEdition', {}))
        else:
            self.eventEdition = None
        self.id = kwargs.get('id', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, AwardDetails):
            return False
        return self.id == other.id


class AwardDetailsConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(AwardDetails(**node.get("node", {})))

class AwardNomination:
    def __init__(self, **kwargs):
        if kwargs.get('award'):
            self.award = AwardDetails(**kwargs.get('award', {}))
        else:
            self.award = None
        if kwargs.get('category'):
            self.category = AwardCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('forEpisodes'):
            self.forEpisodes = Title(**kwargs.get('forEpisodes', {}))
        else:
            self.forEpisodes = None
        self.forSongTitles = kwargs.get('forSongTitles', "")
        self.id = kwargs.get('id', "")
        self.isWinner = kwargs.get('isWinner', False)
        if kwargs.get('notes'):
            self.notes = Markdown(**kwargs.get('notes', {}))
        else:
            self.notes = None
        if kwargs.get('winAnnouncementDate'):
            self.winAnnouncementDate = DisplayableDate(**kwargs.get('winAnnouncementDate', {}))
        else:
            self.winAnnouncementDate = None
        self.winningRank = kwargs.get('winningRank', 0)
    def __eq__(self, other):
        if not isinstance(other, AwardNomination):
            return False
        return self.id == other.id


class AwardNominationConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(AwardNomination(**node.get("node", {})))

class AwardNominationsWithCategory:
    def __init__(self, **kwargs):
        if kwargs.get('awardNominations'):
            self.awardNominations = AwardNominationConnection(**kwargs.get('awardNominations', {}))
        else:
            self.awardNominations = None
        if kwargs.get('category'):
            self.category = AwardCategory(**kwargs.get('category', {}))
        else:
            self.category = None
    def __eq__(self, other):
        if not isinstance(other, AwardNominationsWithCategory):
            return False
        return (self.awardNominations == other.awardNominations and self.category == other.category)

class AwardsEvent:
    def __init__(self, **kwargs):
        if kwargs.get('editions'):
            self.editions = EventEditionConnection(**kwargs.get('editions', {}))
        else:
            self.editions = None
        self.id = kwargs.get('id', "")
        if kwargs.get('location'):
            self.location = DisplayableLocation(**kwargs.get('location', {}))
        else:
            self.location = None
        self.text = kwargs.get('text', "")
        if kwargs.get('trivia'):
            self.trivia = Markdown(**kwargs.get('trivia', {}))
        else:
            self.trivia = None
        if kwargs.get('urls'):
            self.urls = EventUrl(**kwargs.get('urls', {}))
        else:
            self.urls = None
    def __eq__(self, other):
        if not isinstance(other, AwardsEvent):
            return False
        return self.id == other.id


class AwardsEventConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(AwardsEvent(**node.get("node", {})))

class Badge:
    def __init__(self, **kwargs):
        if kwargs.get('description'):
            self.description = LocalizedMarkdown(**kwargs.get('description', {}))
        else:
            self.description = None
        self.id = kwargs.get('id', "")
        if kwargs.get('image'):
            self.image = MediaServiceImage(**kwargs.get('image', {}))
        else:
            self.image = None
        if kwargs.get('subtitle'):
            self.subtitle = CommonLocalizedDisplayableConcept(**kwargs.get('subtitle', {}))
        else:
            self.subtitle = None
        if kwargs.get('title'):
            self.title = CommonLocalizedDisplayableConcept(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, Badge):
            return False
        return self.id == other.id

class BadgeGuideEntry:
    def __init__(self, **kwargs):
        if kwargs.get('description'):
            self.description = LocalizedMarkdown(**kwargs.get('description', {}))
        else:
            self.description = None
        if kwargs.get('image'):
            self.image = MediaServiceImage(**kwargs.get('image', {}))
        else:
            self.image = None
        if kwargs.get('subtitle'):
            self.subtitle = CommonLocalizedDisplayableConcept(**kwargs.get('subtitle', {}))
        else:
            self.subtitle = None
        if kwargs.get('title'):
            self.title = CommonLocalizedDisplayableConcept(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, BadgeGuideEntry):
            return False
        return (self.description == other.description and self.image == other.image and self.subtitle == other.subtitle and self.title == other.title)

class Banner:
    def __init__(self, **kwargs):
        self.attributionUrl = kwargs.get('attributionUrl', "")
        self.height = kwargs.get('height', 0)
        self.imageUrl = kwargs.get('imageUrl', "")
        self.url = kwargs.get('url', "")
        self.width = kwargs.get('width', 0)
    def __eq__(self, other):
        if not isinstance(other, Banner):
            return False
        return (self.attributionUrl == other.attributionUrl and self.height == other.height and self.imageUrl == other.imageUrl and self.url == other.url and self.width == other.width)

class BirthName:
    def __init__(self, **kwargs):
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableBirthNameProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, BirthName):
            return False
        return (self.displayableProperty == other.displayableProperty and self.text == other.text)

class BlogLink:
    def __init__(self, **kwargs):
        self.label = kwargs.get('label', "")
        self.url = kwargs.get('url', "")
    def __eq__(self, other):
        if not isinstance(other, BlogLink):
            return False
        return (self.label == other.label and self.url == other.url)

class BoxOfficeAreaType:
    def __init__(self, **kwargs):
        self.code = kwargs.get('code', "")
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, BoxOfficeAreaType):
            return False
        return self.id == other.id

class BoxOfficeGross:
    def __init__(self, **kwargs):
        if kwargs.get('total'):
            self.total = Money(**kwargs.get('total', {}))
        else:
            self.total = None
    def __eq__(self, other):
        if not isinstance(other, BoxOfficeGross):
            return False
        return (self.total == other.total)

class BoxOfficeRelease:
    def __init__(self, **kwargs):
        if kwargs.get('titles'):
            self.titles = Title(**kwargs.get('titles', {}))
        else:
            self.titles = None
        self.weeksRunning = kwargs.get('weeksRunning', 0)
    def __eq__(self, other):
        if not isinstance(other, BoxOfficeRelease):
            return False
        return (self.titles == other.titles and self.weeksRunning == other.weeksRunning)

class BoxOfficeWeekendChart:
    def __init__(self, **kwargs):
        if kwargs.get('entries'):
            self.entries = ChartEntry(**kwargs.get('entries', {}))
        else:
            self.entries = None
        self.weekendEndDate = kwargs.get('weekendEndDate', "")
        self.weekendStartDate = kwargs.get('weekendStartDate', "")
    def __eq__(self, other):
        if not isinstance(other, BoxOfficeWeekendChart):
            return False
        return (self.entries == other.entries and self.weekendEndDate == other.weekendEndDate and self.weekendStartDate == other.weekendStartDate)

class CallToAction:
    def __init__(self, **kwargs):
        if kwargs.get('landingPagePro'):
            self.landingPagePro = LinkCallToAction(**kwargs.get('landingPagePro', {}))
        else:
            self.landingPagePro = None
        if kwargs.get('nameBanner'):
            self.nameBanner = MarkdownSlotCallToAction(**kwargs.get('nameBanner', {}))
        else:
            self.nameBanner = None
        if kwargs.get('nameClaimPageForFree'):
            self.nameClaimPageForFree = SectionCallToAction(**kwargs.get('nameClaimPageForFree', {}))
        else:
            self.nameClaimPageForFree = None
        if kwargs.get('nameDiscoverMoreInsights'):
            self.nameDiscoverMoreInsights = LinkCallToAction(**kwargs.get('nameDiscoverMoreInsights', {}))
        else:
            self.nameDiscoverMoreInsights = None
        if kwargs.get('nameImagesReels'):
            self.nameImagesReels = LinkCallToAction(**kwargs.get('nameImagesReels', {}))
        else:
            self.nameImagesReels = None
        if kwargs.get('nameProUpsell'):
            self.nameProUpsell = MultiLinkCallToAction(**kwargs.get('nameProUpsell', {}))
        else:
            self.nameProUpsell = None
        if kwargs.get('nameViewStarMeter'):
            self.nameViewStarMeter = LinkCallToAction(**kwargs.get('nameViewStarMeter', {}))
        else:
            self.nameViewStarMeter = None
        if kwargs.get('navbarProFlyout'):
            self.navbarProFlyout = ImageAndLinkCallToAction(**kwargs.get('navbarProFlyout', {}))
        else:
            self.navbarProFlyout = None
        if kwargs.get('titleProUpsell'):
            self.titleProUpsell = LinkCallToAction(**kwargs.get('titleProUpsell', {}))
        else:
            self.titleProUpsell = None
    def __eq__(self, other):
        if not isinstance(other, CallToAction):
            return False
        return (self.landingPagePro == other.landingPagePro and self.nameBanner == other.nameBanner and self.nameClaimPageForFree == other.nameClaimPageForFree and self.nameDiscoverMoreInsights == other.nameDiscoverMoreInsights and self.nameImagesReels == other.nameImagesReels and self.nameProUpsell == other.nameProUpsell and self.nameViewStarMeter == other.nameViewStarMeter and self.navbarProFlyout == other.navbarProFlyout and self.titleProUpsell == other.titleProUpsell)

class CallToActionImage:
    def __init__(self, **kwargs):
        if kwargs.get('caption'):
            self.caption = LocalizedMarkdown(**kwargs.get('caption', {}))
        else:
            self.caption = None
        self.height = kwargs.get('height', 0)
        self.url = kwargs.get('url', "")
        self.width = kwargs.get('width', 0)
    def __eq__(self, other):
        if not isinstance(other, CallToActionImage):
            return False
        return (self.caption == other.caption and self.height == other.height and self.url == other.url and self.width == other.width)

class CallToActionText:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, CallToActionText):
            return False
        return self.id == other.id

class Camera:
    def __init__(self, **kwargs):
        if kwargs.get('attributes'):
            self.attributes = [DisplayableAttribute(**attr) for attr in kwargs.get('attributes', [])]
        else:
            self.attributes = None
        self.camera = kwargs.get('camera', "")
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableTechnicalSpecificationProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
    def __eq__(self, other):
        if not isinstance(other, Camera):
            return False
        return (self.attributes == other.attributes and self.camera == other.camera and self.displayableProperty == other.displayableProperty)

class Cameras:
    def __init__(self, **kwargs):
        if kwargs.get('items'):
            self.items = Camera(**kwargs.get('items', {}))
        else:
            self.items = None
        if kwargs.get('restriction'):
            self.restriction = TechnicalSpecificationsRestriction(**kwargs.get('restriction', {}))
        else:
            self.restriction = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, Cameras):
            return False
        return (self.items == other.items and self.restriction == other.restriction and self.total == other.total)

class CanRate:
    def __init__(self, **kwargs):
        self.isRatable = kwargs.get('isRatable', False)
    def __eq__(self, other):
        if not isinstance(other, CanRate):
            return False
        return (self.isRatable == other.isRatable)

class CategorizedWatchOptions:
    def __init__(self, **kwargs):
        if kwargs.get('categoryName'):
            self.categoryName = LocalizedString(**kwargs.get('categoryName', {}))
        else:
            self.categoryName = None
        if kwargs.get('watchOptions'):
            self.watchOptions = WatchOption(**kwargs.get('watchOptions', {}))
        else:
            self.watchOptions = None
    def __eq__(self, other):
        if not isinstance(other, CategorizedWatchOptions):
            return False
        return (self.categoryName == other.categoryName and self.watchOptions == other.watchOptions)

class CategorizedWatchOptionsList:
    def __init__(self, **kwargs):
        if kwargs.get('categorizedWatchOptionsList'):
            self.categorizedWatchOptionsList = CategorizedWatchOptions(**kwargs.get('categorizedWatchOptionsList', {}))
        else:
            self.categorizedWatchOptionsList = None
    def __eq__(self, other):
        if not isinstance(other, CategorizedWatchOptionsList):
            return False
        return (self.categorizedWatchOptionsList == other.categorizedWatchOptionsList)

class Certificate:
    def __init__(self, **kwargs):
        if kwargs.get('attributes'):
            self.attributes = [DisplayableAttribute(**attr) for attr in kwargs.get('attributes', [])]
        else:
            self.attributes = None
        if kwargs.get('country'):
            self.country = DisplayableCountry(**kwargs.get('country', {}))
        else:
            self.country = None
        self.id = kwargs.get('id', "")
        self.rating = kwargs.get('rating', "")
        self.ratingReason = kwargs.get('ratingReason', "")
        if kwargs.get('ratingsBody'):
            self.ratingsBody = RatingsBody(**kwargs.get('ratingsBody', {}))
        else:
            self.ratingsBody = None
        self.ratingsBodyCertificateId = kwargs.get('ratingsBodyCertificateId', "")
    def __eq__(self, other):
        if not isinstance(other, Certificate):
            return False
        return self.id == other.id


class CertificatesConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Certificate(**node.get("node", {})))

class ChangeLoginSecurityRedirectURLOutput:
    def __init__(self, **kwargs):
        self.redirectURL = kwargs.get('redirectURL', "")
    def __eq__(self, other):
        if not isinstance(other, ChangeLoginSecurityRedirectURLOutput):
            return False
        return (self.redirectURL == other.redirectURL)

class Character:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.name = kwargs.get('name', "")
    def __eq__(self, other):
        if not isinstance(other, Character):
            return False
        return self.id == other.id


class CharacterConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Character(**node.get("node", {})))

class ChartEntry:
    def __init__(self, **kwargs):
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
        if kwargs.get('weekendGross'):
            self.weekendGross = BoxOfficeGross(**kwargs.get('weekendGross', {}))
        else:
            self.weekendGross = None
    def __eq__(self, other):
        if not isinstance(other, ChartEntry):
            return False
        return (self.title == other.title and self.weekendGross == other.weekendGross)

class Cinema:
    def __init__(self, **kwargs):
        if kwargs.get('accessibility'):
            self.accessibility = CinemaAccessibility(**kwargs.get('accessibility', {}))
        else:
            self.accessibility = None
        if kwargs.get('contactDetails'):
            self.contactDetails = CinemaContactDetails(**kwargs.get('contactDetails', {}))
        else:
            self.contactDetails = None
        if kwargs.get('distanceToCinema'):
            self.distanceToCinema = DistanceToCinema(**kwargs.get('distanceToCinema', {}))
        else:
            self.distanceToCinema = None
        self.id = kwargs.get('id', "")
        if kwargs.get('location'):
            self.location = CinemaLocation(**kwargs.get('location', {}))
        else:
            self.location = None
        if kwargs.get('name'):
            self.name = CinemaName(**kwargs.get('name', {}))
        else:
            self.name = None
    def __eq__(self, other):
        if not isinstance(other, Cinema):
            return False
        return self.id == other.id

class CinemaAccessibility:
    def __init__(self, **kwargs):
        if kwargs.get('audioAccessibility'):
            self.audioAccessibility = CinemaAudioAccessibility(**kwargs.get('audioAccessibility', {}))
        else:
            self.audioAccessibility = None
        if kwargs.get('wheelchairAccessibility'):
            self.wheelchairAccessibility = CinemaWheelchairAccessibility(**kwargs.get('wheelchairAccessibility', {}))
        else:
            self.wheelchairAccessibility = None
    def __eq__(self, other):
        if not isinstance(other, CinemaAccessibility):
            return False
        return (self.audioAccessibility == other.audioAccessibility and self.wheelchairAccessibility == other.wheelchairAccessibility)

class CinemaAudioAccessibility:
    def __init__(self, **kwargs):
        self.hasHearingDevices = kwargs.get('hasHearingDevices', False)
    def __eq__(self, other):
        if not isinstance(other, CinemaAudioAccessibility):
            return False
        return (self.hasHearingDevices == other.hasHearingDevices)

class CinemaContactDetails:
    def __init__(self, **kwargs):
        self.phoneNumber = kwargs.get('phoneNumber', "")
    def __eq__(self, other):
        if not isinstance(other, CinemaContactDetails):
            return False
        return (self.phoneNumber == other.phoneNumber)

class CinemaLocation:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, CinemaLocation):
            return False
        return self.id == other.id

class CinemaName:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, CinemaName):
            return False
        return self.id == other.id

class CinemaWheelchairAccessibility:
    def __init__(self, **kwargs):
        self.hasWheelchairAccess = kwargs.get('hasWheelchairAccess', False)
    def __eq__(self, other):
        if not isinstance(other, CinemaWheelchairAccessibility):
            return False
        return (self.hasWheelchairAccess == other.hasWheelchairAccess)

class ClaimedName:
    def __init__(self, **kwargs):
        if kwargs.get('name'):
            self.name = Name(**kwargs.get('name', {}))
        else:
            self.name = None
        self.status = kwargs.get('status', "")
    def __eq__(self, other):
        if not isinstance(other, ClaimedName):
            return False
        return (self.name == other.name and self.status == other.status)

class Coloration:
    def __init__(self, **kwargs):
        if kwargs.get('attributes'):
            self.attributes = [DisplayableAttribute(**attr) for attr in kwargs.get('attributes', [])]
        else:
            self.attributes = None
        self.conceptId = kwargs.get('conceptId', "")
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableTechnicalSpecificationProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.id = kwargs.get('id', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, Coloration):
            return False
        return self.id == other.id

class Colorations:
    def __init__(self, **kwargs):
        if kwargs.get('items'):
            self.items = Coloration(**kwargs.get('items', {}))
        else:
            self.items = None
        if kwargs.get('restriction'):
            self.restriction = TechnicalSpecificationsRestriction(**kwargs.get('restriction', {}))
        else:
            self.restriction = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, Colorations):
            return False
        return (self.items == other.items and self.restriction == other.restriction and self.total == other.total)

class CommonLocalizedDisplayableConcept:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, CommonLocalizedDisplayableConcept):
            return False
        return self.id == other.id

class Company:
    def __init__(self, **kwargs):
        if kwargs.get('acronyms'):
            self.acronyms = CompanyAcronymConnection(**kwargs.get('acronyms', {}))
        else:
            self.acronyms = None
        if kwargs.get('affiliations'):
            self.affiliations = CompanyAffiliationConnection(**kwargs.get('affiliations', {}))
        else:
            self.affiliations = None
        if kwargs.get('bio'):
            self.bio = CompanyBio(**kwargs.get('bio', {}))
        else:
            self.bio = None
        if kwargs.get('branches'):
            self.branches = CompanyBranchConnection(**kwargs.get('branches', {}))
        else:
            self.branches = None
        if kwargs.get('clients'):
            self.clients = CompanyClientConnection(**kwargs.get('clients', {}))
        else:
            self.clients = None
        if kwargs.get('companyText'):
            self.companyText = CompanyText(**kwargs.get('companyText', {}))
        else:
            self.companyText = None
        if kwargs.get('companyTypes'):
            self.companyTypes = CompanyType(**kwargs.get('companyTypes', {}))
        else:
            self.companyTypes = None
        if kwargs.get('country'):
            self.country = LocalizedDisplayableCountry(**kwargs.get('country', {}))
        else:
            self.country = None
        if kwargs.get('experimental_branches'):
            self.experimental_branches = Experimental_CompanyBranchConnection(**kwargs.get('experimental_branches', {}))
        else:
            self.experimental_branches = None
        if kwargs.get('experimental_clients'):
            self.experimental_clients = Experimental_CompanyClientConnection(**kwargs.get('experimental_clients', {}))
        else:
            self.experimental_clients = None
        self.id = kwargs.get('id', "")
        if kwargs.get('images'):
            self.images = ImageConnection(**kwargs.get('images', {}))
        else:
            self.images = None
        if kwargs.get('keyStaff'):
            self.keyStaff = CompanyKeyStaffConnection(**kwargs.get('keyStaff', {}))
        else:
            self.keyStaff = None
        if kwargs.get('knownForClients'):
            self.knownForClients = CompanyKnownForClientConnection(**kwargs.get('knownForClients', {}))
        else:
            self.knownForClients = None
        if kwargs.get('knownForTitles'):
            self.knownForTitles = CompanyKnownForTitleConnection(**kwargs.get('knownForTitles', {}))
        else:
            self.knownForTitles = None
        if kwargs.get('managedData'):
            self.managedData = ManagedCompanyData(**kwargs.get('managedData', {}))
        else:
            self.managedData = None
        if kwargs.get('meterRank'):
            self.meterRank = CompanyMeterRanking(**kwargs.get('meterRank', {}))
        else:
            self.meterRank = None
        if kwargs.get('meterRankingHistory'):
            self.meterRankingHistory = CompanyMeterRankingHistory(**kwargs.get('meterRankingHistory', {}))
        else:
            self.meterRankingHistory = None
        if kwargs.get('primaryImage'):
            self.primaryImage = Image(**kwargs.get('primaryImage', {}))
        else:
            self.primaryImage = None
    def __eq__(self, other):
        if not isinstance(other, Company):
            return False
        return self.id == other.id

class CompanyAcronym:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, CompanyAcronym):
            return False
        return self.id == other.id


class CompanyAcronymConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(CompanyAcronym(**node.get("node", {})))

class CompanyAffiliation:
    def __init__(self, **kwargs):
        if kwargs.get('company'):
            self.company = Company(**kwargs.get('company', {}))
        else:
            self.company = None
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, CompanyAffiliation):
            return False
        return self.id == other.id


class CompanyAffiliationConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(CompanyAffiliation(**node.get("node", {})))

class CompanyBio:
    def __init__(self, **kwargs):
        if kwargs.get('displayableArticle'):
            self.displayableArticle = DisplayableArticle(**kwargs.get('displayableArticle', {}))
        else:
            self.displayableArticle = None
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('text'):
            self.text = Markdown(**kwargs.get('text', {}))
        else:
            self.text = None
    def __eq__(self, other):
        if not isinstance(other, CompanyBio):
            return False
        return self.id == other.id

class CompanyBranch:
    def __init__(self, **kwargs):
        if kwargs.get('directContact'):
            self.directContact = CompanyContactDetails(**kwargs.get('directContact', {}))
        else:
            self.directContact = None
        self.id = kwargs.get('id', "")
        if kwargs.get('name'):
            self.name = LocalizedString(**kwargs.get('name', {}))
        else:
            self.name = None
    def __eq__(self, other):
        if not isinstance(other, CompanyBranch):
            return False
        return self.id == other.id


class CompanyBranchConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(CompanyBranch(**node.get("node", {})))

class CompanyClient:
    def __init__(self, **kwargs):
        if kwargs.get('agents'):
            self.agents = Agent(**kwargs.get('agents', {}))
        else:
            self.agents = None
        if kwargs.get('client'):
            self.client = Name(**kwargs.get('client', {}))
        else:
            self.client = None
        self.id = kwargs.get('id', "")
    def __eq__(self, other):
        if not isinstance(other, CompanyClient):
            return False
        return self.id == other.id


class CompanyClientConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(CompanyClient(**node.get("node", {})))

class CompanyContactDetails:
    def __init__(self, **kwargs):
        self.emailAddress = kwargs.get('emailAddress', "")
        if kwargs.get('faxNumber'):
            self.faxNumber = LocalizedString(**kwargs.get('faxNumber', {}))
        else:
            self.faxNumber = None
        if kwargs.get('phoneNumbers'):
            self.phoneNumbers = LocalizedString(**kwargs.get('phoneNumbers', {}))
        else:
            self.phoneNumbers = None
        if kwargs.get('physicalAddress'):
            self.physicalAddress = Location(**kwargs.get('physicalAddress', {}))
        else:
            self.physicalAddress = None
        if kwargs.get('website'):
            self.website = WebsiteLink(**kwargs.get('website', {}))
        else:
            self.website = None
    def __eq__(self, other):
        if not isinstance(other, CompanyContactDetails):
            return False
        return (self.emailAddress == other.emailAddress and self.faxNumber == other.faxNumber and self.phoneNumbers == other.phoneNumbers and self.physicalAddress == other.physicalAddress and self.website == other.website)

class CompanyCredit:
    def __init__(self, **kwargs):
        if kwargs.get('attributes'):
            self.attributes = [DisplayableAttribute(**attr) for attr in kwargs.get('attributes', [])]
        else:
            self.attributes = None
        if kwargs.get('category'):
            self.category = CompanyCreditCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('company'):
            self.company = Company(**kwargs.get('company', {}))
        else:
            self.company = None
        if kwargs.get('countries'):
            self.countries = DisplayableCountry(**kwargs.get('countries', {}))
        else:
            self.countries = None
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableTitleCompanyCreditProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        if kwargs.get('distributionFormats'):
            self.distributionFormats = DistributionFormat(**kwargs.get('distributionFormats', {}))
        else:
            self.distributionFormats = None
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
        if kwargs.get('yearsInvolved'):
            self.yearsInvolved = YearRange(**kwargs.get('yearsInvolved', {}))
        else:
            self.yearsInvolved = None
    def __eq__(self, other):
        if not isinstance(other, CompanyCredit):
            return False
        return (self.attributes == other.attributes and self.category == other.category and self.company == other.company and self.countries == other.countries and self.displayableProperty == other.displayableProperty and self.distributionFormats == other.distributionFormats and self.title == other.title and self.yearsInvolved == other.yearsInvolved)

class CompanyCreditCategory:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, CompanyCreditCategory):
            return False
        return self.id == other.id

class CompanyCreditCategoryWithCompanyCredits:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = CompanyCreditCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('companyCredits'):
            self.companyCredits = CompanyCreditConnection(**kwargs.get('companyCredits', {}))
        else:
            self.companyCredits = None
        if kwargs.get('restriction'):
            self.restriction = CompanyCreditRestriction(**kwargs.get('restriction', {}))
        else:
            self.restriction = None
    def __eq__(self, other):
        if not isinstance(other, CompanyCreditCategoryWithCompanyCredits):
            return False
        return (self.category == other.category and self.companyCredits == other.companyCredits and self.restriction == other.restriction)


class CompanyCreditConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(CompanyCredit(**node.get("node", {})))

class CompanyCreditRestriction:
    def __init__(self, **kwargs):
        if kwargs.get('explanations'):
            self.explanations = RestrictionExplanation(**kwargs.get('explanations', {}))
        else:
            self.explanations = None
        self.reasons = kwargs.get('reasons', "")
        self.restrictionReason = kwargs.get('restrictionReason', "")
        self.unrestrictedTotal = kwargs.get('unrestrictedTotal', 0)
    def __eq__(self, other):
        if not isinstance(other, CompanyCreditRestriction):
            return False
        return (self.explanations == other.explanations and self.reasons == other.reasons and self.restrictionReason == other.restrictionReason and self.unrestrictedTotal == other.unrestrictedTotal)

class CompanyEmployeeOccupation:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, CompanyEmployeeOccupation):
            return False
        return self.id == other.id

class CompanyEmployeeTitle:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, CompanyEmployeeTitle):
            return False
        return self.id == other.id

class CompanyEmployment:
    def __init__(self, **kwargs):
        if kwargs.get('branch'):
            self.branch = EmployeeBranchName(**kwargs.get('branch', {}))
        else:
            self.branch = None
        if kwargs.get('occupation'):
            self.occupation = CompanyEmployeeOccupation(**kwargs.get('occupation', {}))
        else:
            self.occupation = None
        if kwargs.get('title'):
            self.title = CompanyEmployeeTitle(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, CompanyEmployment):
            return False
        return (self.branch == other.branch and self.occupation == other.occupation and self.title == other.title)

class CompanyJob:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, CompanyJob):
            return False
        return self.id == other.id

class CompanyKeyStaff:
    def __init__(self, **kwargs):
        if kwargs.get('name'):
            self.name = Name(**kwargs.get('name', {}))
        else:
            self.name = None
        if kwargs.get('summary'):
            self.summary = CompanyKeyStaffSummary(**kwargs.get('summary', {}))
        else:
            self.summary = None
    def __eq__(self, other):
        if not isinstance(other, CompanyKeyStaff):
            return False
        return (self.name == other.name and self.summary == other.summary)


class CompanyKeyStaffConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(CompanyKeyStaff(**node.get("node", {})))

class CompanyKeyStaffSummary:
    def __init__(self, **kwargs):
        if kwargs.get('employment'):
            self.employment = CompanyEmployment(**kwargs.get('employment', {}))
        else:
            self.employment = None
    def __eq__(self, other):
        if not isinstance(other, CompanyKeyStaffSummary):
            return False
        return (self.employment == other.employment)

class CompanyKnownForClient:
    def __init__(self, **kwargs):
        if kwargs.get('name'):
            self.name = Name(**kwargs.get('name', {}))
        else:
            self.name = None
        if kwargs.get('summary'):
            self.summary = CompanyKnownForClientSummary(**kwargs.get('summary', {}))
        else:
            self.summary = None
    def __eq__(self, other):
        if not isinstance(other, CompanyKnownForClient):
            return False
        return (self.name == other.name and self.summary == other.summary)


class CompanyKnownForClientConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(CompanyKnownForClient(**node.get("node", {})))

class CompanyKnownForClientSummary:
    def __init__(self, **kwargs):
        if kwargs.get('representation'):
            self.representation = CompanyRepresentationCategory(**kwargs.get('representation', {}))
        else:
            self.representation = None
        if kwargs.get('representationCategories'):
            self.representationCategories = CompanyRepresentationCategories(**kwargs.get('representationCategories', {}))
        else:
            self.representationCategories = None
    def __eq__(self, other):
        if not isinstance(other, CompanyKnownForClientSummary):
            return False
        return (self.representation == other.representation and self.representationCategories == other.representationCategories)

class CompanyKnownForCreditCategory:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, CompanyKnownForCreditCategory):
            return False
        return self.id == other.id

class CompanyKnownForJob:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = CompanyKnownForCreditCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('job'):
            self.job = CompanyJob(**kwargs.get('job', {}))
        else:
            self.job = None
    def __eq__(self, other):
        if not isinstance(other, CompanyKnownForJob):
            return False
        return (self.category == other.category and self.job == other.job)

class CompanyKnownForTitle:
    def __init__(self, **kwargs):
        if kwargs.get('summary'):
            self.summary = CompanyKnownForTitleSummary(**kwargs.get('summary', {}))
        else:
            self.summary = None
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, CompanyKnownForTitle):
            return False
        return (self.summary == other.summary and self.title == other.title)


class CompanyKnownForTitleConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(CompanyKnownForTitle(**node.get("node", {})))

class CompanyKnownForTitleSummary:
    def __init__(self, **kwargs):
        if kwargs.get('countries'):
            self.countries = DisplayableCountry(**kwargs.get('countries', {}))
        else:
            self.countries = None
        if kwargs.get('jobs'):
            self.jobs = CompanyKnownForJob(**kwargs.get('jobs', {}))
        else:
            self.jobs = None
        if kwargs.get('yearRange'):
            self.yearRange = YearRange(**kwargs.get('yearRange', {}))
        else:
            self.yearRange = None
    def __eq__(self, other):
        if not isinstance(other, CompanyKnownForTitleSummary):
            return False
        return (self.countries == other.countries and self.jobs == other.jobs and self.yearRange == other.yearRange)

class CompanyMetadata:
    def __init__(self, **kwargs):
        if kwargs.get('companyCreditCategories'):
            self.companyCreditCategories = CompanyCreditCategory(**kwargs.get('companyCreditCategories', {}))
        else:
            self.companyCreditCategories = None
    def __eq__(self, other):
        if not isinstance(other, CompanyMetadata):
            return False
        return (self.companyCreditCategories == other.companyCreditCategories)

class CompanyMeterRanking:
    def __init__(self, **kwargs):
        self.currentRank = kwargs.get('currentRank', 0)
        if kwargs.get('rankChange'):
            self.rankChange = MeterRankChange(**kwargs.get('rankChange', {}))
        else:
            self.rankChange = None
    def __eq__(self, other):
        if not isinstance(other, CompanyMeterRanking):
            return False
        return (self.currentRank == other.currentRank and self.rankChange == other.rankChange)

class CompanyMeterRankingHistory:
    def __init__(self, **kwargs):
        if kwargs.get('bestRank'):
            self.bestRank = MeterRankingHistoryEntry(**kwargs.get('bestRank', {}))
        else:
            self.bestRank = None
        if kwargs.get('ranks'):
            self.ranks = MeterRankingHistoryEntry(**kwargs.get('ranks', {}))
        else:
            self.ranks = None
        if kwargs.get('restriction'):
            self.restriction = MeterRestriction(**kwargs.get('restriction', {}))
        else:
            self.restriction = None
    def __eq__(self, other):
        if not isinstance(other, CompanyMeterRankingHistory):
            return False
        return (self.bestRank == other.bestRank and self.ranks == other.ranks and self.restriction == other.restriction)

class CompanyRepresentationCategories:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, CompanyRepresentationCategories):
            return False
        return self.id == other.id

class CompanyRepresentationCategory:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, CompanyRepresentationCategory):
            return False
        return self.id == other.id

class CompanyText:
    def __init__(self, **kwargs):
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, CompanyText):
            return False
        return (self.text == other.text)

class CompanyType:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, CompanyType):
            return False
        return self.id == other.id

class ConnectionCategoryWithConnections:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = TitleConnectionCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('connections'):
            self.connections = TitleConnectionConnection(**kwargs.get('connections', {}))
        else:
            self.connections = None
    def __eq__(self, other):
        if not isinstance(other, ConnectionCategoryWithConnections):
            return False
        return (self.category == other.category and self.connections == other.connections)

class Consent:
    def __init__(self, **kwargs):
        self.consentOperation = kwargs.get('consentOperation', "")
        self.consentType = kwargs.get('consentType', "")
        self.expirationDate = kwargs.get('expirationDate', "")
    def __eq__(self, other):
        if not isinstance(other, Consent):
            return False
        return (self.consentOperation == other.consentOperation and self.consentType == other.consentType and self.expirationDate == other.expirationDate)

class ContentWarnings:
    def __init__(self, **kwargs):
        self.isPrimarilyAdultActor = kwargs.get('isPrimarilyAdultActor', False)
    def __eq__(self, other):
        if not isinstance(other, ContentWarnings):
            return False
        return (self.isPrimarilyAdultActor == other.isPrimarilyAdultActor)

class ContributionLink:
    def __init__(self, **kwargs):
        self.url = kwargs.get('url', "")
    def __eq__(self, other):
        if not isinstance(other, ContributionLink):
            return False
        return (self.url == other.url)

class ContributionQuestionsLink:
    def __init__(self, **kwargs):
        self.url = kwargs.get('url', "")
    def __eq__(self, other):
        if not isinstance(other, ContributionQuestionsLink):
            return False
        return (self.url == other.url)

class Contributor:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('user'):
            self.user = UserProfile(**kwargs.get('user', {}))
        else:
            self.user = None
    def __eq__(self, other):
        if not isinstance(other, Contributor):
            return False
        return self.id == other.id

class ContributorLeaderboard:
    def __init__(self, **kwargs):
        if kwargs.get('description'):
            self.description = LocalizedString(**kwargs.get('description', {}))
        else:
            self.description = None
        self.id = kwargs.get('id', "")
        self.isFinalized = kwargs.get('isFinalized', False)
        self.lastUpdated = kwargs.get('lastUpdated', "")
        self.leaderboardUrl = kwargs.get('leaderboardUrl', "")
        self.month = kwargs.get('month', 0)
        if kwargs.get('period'):
            self.period = ContributorLeaderboardPeriodType(**kwargs.get('period', {}))
        else:
            self.period = None
        if kwargs.get('rankings'):
            self.rankings = ContributorRankingsConnection(**kwargs.get('rankings', {}))
        else:
            self.rankings = None
        if kwargs.get('title'):
            self.title = LocalizedString(**kwargs.get('title', {}))
        else:
            self.title = None
        self.totalApprovedItems = kwargs.get('totalApprovedItems', 0)
        self.totalContributors = kwargs.get('totalContributors', 0)
        self.year = kwargs.get('year', 0)
    def __eq__(self, other):
        if not isinstance(other, ContributorLeaderboard):
            return False
        return self.id == other.id


class ContributorLeaderboardConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(ContributorLeaderboard(**node.get("node", {})))

class ContributorLeaderboardPeriodType:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
    def __eq__(self, other):
        if not isinstance(other, ContributorLeaderboardPeriodType):
            return False
        return self.id == other.id

class ContributorLeaderboardRank:
    def __init__(self, **kwargs):
        if kwargs.get('leaderboard'):
            self.leaderboard = ContributorLeaderboard(**kwargs.get('leaderboard', {}))
        else:
            self.leaderboard = None
        if kwargs.get('ranking'):
            self.ranking = ContributorRank(**kwargs.get('ranking', {}))
        else:
            self.ranking = None
    def __eq__(self, other):
        if not isinstance(other, ContributorLeaderboardRank):
            return False
        return (self.leaderboard == other.leaderboard and self.ranking == other.ranking)

class ContributorLeaderboards:
    def __init__(self, **kwargs):
        if kwargs.get('all'):
            self.all = ContributorLeaderboardConnection(**kwargs.get('all', {}))
        else:
            self.all = None
        if kwargs.get('allTime'):
            self.allTime = ContributorLeaderboard(**kwargs.get('allTime', {}))
        else:
            self.allTime = None
        if kwargs.get('month'):
            self.month = ContributorLeaderboard(**kwargs.get('month', {}))
        else:
            self.month = None
        if kwargs.get('months'):
            self.months = ContributorLeaderboardConnection(**kwargs.get('months', {}))
        else:
            self.months = None
        if kwargs.get('year'):
            self.year = ContributorLeaderboard(**kwargs.get('year', {}))
        else:
            self.year = None
        if kwargs.get('years'):
            self.years = ContributorLeaderboardConnection(**kwargs.get('years', {}))
        else:
            self.years = None
    def __eq__(self, other):
        if not isinstance(other, ContributorLeaderboards):
            return False
        return (self.all == other.all and self.allTime == other.allTime and self.month == other.month and self.months == other.months and self.year == other.year and self.years == other.years)

class ContributorRank:
    def __init__(self, **kwargs):
        self.approvedItems = kwargs.get('approvedItems', 0)
        self.approvedItemsDelta = kwargs.get('approvedItemsDelta', 0)
        if kwargs.get('contributor'):
            self.contributor = Contributor(**kwargs.get('contributor', {}))
        else:
            self.contributor = None
        self.id = kwargs.get('id', "")
        self.rank = kwargs.get('rank', 0)
        self.rankDelta = kwargs.get('rankDelta', 0)
    def __eq__(self, other):
        if not isinstance(other, ContributorRank):
            return False
        return self.id == other.id


class ContributorRankingsConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(ContributorRank(**node.get("node", {})))

class CountriesOfOrigin:
    def __init__(self, **kwargs):
        if kwargs.get('countries'):
            self.countries = [CountryOfOrigin(**country) for country in kwargs.get('countries', [])]
        else:
            self.countries = None
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
    def __eq__(self, other):
        if not isinstance(other, CountriesOfOrigin):
            return False
        return (self.countries == other.countries and self.language == other.language)

class CountryAttributeMetadata:
    def __init__(self, **kwargs):
        self.limit = kwargs.get('limit', 0)
        if kwargs.get('validValues'):
            self.validValues = LocalizedDisplayableCountry(**kwargs.get('validValues', {}))
        else:
            self.validValues = None
    def __eq__(self, other):
        if not isinstance(other, CountryAttributeMetadata):
            return False
        return (self.limit == other.limit and self.validValues == other.validValues)

class CountryOfOrigin:
    def __init__(self, **kwargs):
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableTitleCountryOfOriginProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, CountryOfOrigin):
            return False
        return self.id == other.id

class CrazyCredit:
    def __init__(self, **kwargs):
        if kwargs.get('displayableArticle'):
            self.displayableArticle = DisplayableArticle(**kwargs.get('displayableArticle', {}))
        else:
            self.displayableArticle = None
        self.id = kwargs.get('id', "")
        if kwargs.get('interestScore'):
            self.interestScore = InterestScore(**kwargs.get('interestScore', {}))
        else:
            self.interestScore = None
        if kwargs.get('text'):
            self.text = Markdown(**kwargs.get('text', {}))
        else:
            self.text = None
    def __eq__(self, other):
        if not isinstance(other, CrazyCredit):
            return False
        return self.id == other.id


class CrazyCreditConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(CrazyCredit(**node.get("node", {})))

class CreateAccountRedirectURLOutput:
    def __init__(self, **kwargs):
        self.redirectURL = kwargs.get('redirectURL', "")
    def __eq__(self, other):
        if not isinstance(other, CreateAccountRedirectURLOutput):
            return False
        return (self.redirectURL == other.redirectURL)

class CreativeSize:
    def __init__(self, **kwargs):
        self.height = kwargs.get('height', 0)
        self.width = kwargs.get('width', 0)
    def __eq__(self, other):
        if not isinstance(other, CreativeSize):
            return False
        return (self.height == other.height and self.width == other.width)

class Credit:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = CreditCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('name'):
            self.name = Name(**kwargs.get('name', {}))
        else:
            self.name = None
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, Credit):
            return False
        return (self.category == other.category and self.name == other.name and self.title == other.title)

class CreditAttribute:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.text = kwargs.get('text', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('SeriesCreditAttribute'):
            self.SeriesCreditAttribute = SeriesCreditAttribute(**kwargs.get('SeriesCreditAttribute', {}))
        else:
            self.SeriesCreditAttribute = None
    def __eq__(self, other):
        if not isinstance(other, CreditAttribute):
            return False
        return self.id == other.id

class CreditCategory:
    def __init__(self, **kwargs):
        self.categoryId = kwargs.get('categoryId', "")
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, CreditCategory):
            return False
        return self.id == other.id

class CreditCategorySummary:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = CreditCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, CreditCategorySummary):
            return False
        return (self.category == other.category and self.total == other.total)


class CreditConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Credit(**node.get("node", {})))

class CreditGrouping:
    def __init__(self, **kwargs):
        self.groupingId = kwargs.get('groupingId', "")
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, CreditGrouping):
            return False
        return self.id == other.id


class CreditGroupingConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(CreditGrouping(**node.get("node", {})))

class CreditGroupingNode:
    def __init__(self, **kwargs):
        if kwargs.get('credits'):
            self.credits = CreditV2Connection(**kwargs.get('credits', {}))
        else:
            self.credits = None
        if kwargs.get('grouping'):
            self.grouping = CreditGrouping(**kwargs.get('grouping', {}))
        else:
            self.grouping = None
        if kwargs.get('hierarchy'):
            self.hierarchy = CreditHierarchy(**kwargs.get('hierarchy', {}))
        else:
            self.hierarchy = None
    def __eq__(self, other):
        if not isinstance(other, CreditGroupingNode):
            return False
        return (self.credits == other.credits and self.grouping == other.grouping and self.hierarchy == other.hierarchy)

class CreditHierarchy:
    def __init__(self, **kwargs):
        if kwargs.get('levelDetails'):
            self.levelDetails = CreditHierarchyLevelDetail(**kwargs.get('levelDetails', {}))
        else:
            self.levelDetails = None
        self.levels = kwargs.get('levels', "")
    def __eq__(self, other):
        if not isinstance(other, CreditHierarchy):
            return False
        return (self.levelDetails == other.levelDetails and self.levels == other.levels)

class CreditHierarchyDetail:
    def __init__(self, **kwargs):
        self.level = kwargs.get('level', "")
        self.position = kwargs.get('position', 0)
    def __eq__(self, other):
        if not isinstance(other, CreditHierarchyDetail):
            return False
        return (self.level == other.level and self.position == other.position)

class CreditHierarchyLevelDetail:
    def __init__(self, **kwargs):
        self.childCount = kwargs.get('childCount', 0)
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.levelsKey = kwargs.get('levelsKey', "")
        if kwargs.get('text'):
            self.text = Markdown(**kwargs.get('text', {}))
        else:
            self.text = None
    def __eq__(self, other):
        if not isinstance(other, CreditHierarchyLevelDetail):
            return False
        return self.id == other.id

class CreditRestriction:
    def __init__(self, **kwargs):
        if kwargs.get('explanations'):
            self.explanations = RestrictionExplanation(**kwargs.get('explanations', {}))
        else:
            self.explanations = None
        self.reasons = kwargs.get('reasons', "")
        self.restrictionReason = kwargs.get('restrictionReason', "")
        self.unrestrictedTotal = kwargs.get('unrestrictedTotal', 0)
    def __eq__(self, other):
        if not isinstance(other, CreditRestriction):
            return False
        return (self.explanations == other.explanations and self.reasons == other.reasons and self.restrictionReason == other.restrictionReason and self.unrestrictedTotal == other.unrestrictedTotal)

class CreditV2:
    def __init__(self, **kwargs):
        if kwargs.get('creditedRoles'):
            self.creditedRoles = CreditedRoleConnection(**kwargs.get('creditedRoles', {}))
        else:
            self.creditedRoles = None
        if kwargs.get('episodeCredits'):
            self.episodeCredits = CreditV2Connection(**kwargs.get('episodeCredits', {}))
        else:
            self.episodeCredits = None
        if kwargs.get('hierarchyDetails'):
            self.hierarchyDetails = CreditHierarchyDetail(**kwargs.get('hierarchyDetails', {}))
        else:
            self.hierarchyDetails = None
        self.id = kwargs.get('id', "")
        if kwargs.get('name'):
            self.name = Name(**kwargs.get('name', {}))
        else:
            self.name = None
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, CreditV2):
            return False
        return self.id == other.id


class CreditV2Connection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(CreditV2(**node.get("node", {})))

class CreditedRole:
    def __init__(self, **kwargs):
        if kwargs.get('attributes'):
            self.attributes = CreditAttribute(**kwargs.get('attributes', {}))
        else:
            self.attributes = None
        if kwargs.get('category'):
            self.category = CreditCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('characters'):
            self.characters = CharacterConnection(**kwargs.get('characters', {}))
        else:
            self.characters = None
        if kwargs.get('episodeCredits'):
            self.episodeCredits = CreditV2Connection(**kwargs.get('episodeCredits', {}))
        else:
            self.episodeCredits = None
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, CreditedRole):
            return False
        return self.id == other.id


class CreditedRoleConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(CreditedRole(**node.get("node", {})))

class CreditedWithName:
    def __init__(self, **kwargs):
        if kwargs.get('name'):
            self.name = Name(**kwargs.get('name', {}))
        else:
            self.name = None
    def __eq__(self, other):
        if not isinstance(other, CreditedWithName):
            return False
        return (self.name == other.name)


class CreditedWithNamesConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(CreditedWithName(**node.get("node", {})))

class CreditsCompletenessStatus:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, CreditsCompletenessStatus):
            return False
        return self.id == other.id

class CreditsOrderedBy:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, CreditsOrderedBy):
            return False
        return self.id == other.id

class CroppingParameters:
    def __init__(self, **kwargs):
        self.height = kwargs.get('height', 0)
        self.width = kwargs.get('width', 0)
        self.xOffset = kwargs.get('xOffset', 0)
        self.yOffset = kwargs.get('yOffset', 0)
    def __eq__(self, other):
        if not isinstance(other, CroppingParameters):
            return False
        return (self.height == other.height and self.width == other.width and self.xOffset == other.xOffset and self.yOffset == other.yOffset)

class CustomFeaturedImages:
    def __init__(self, **kwargs):
        if kwargs.get('images'):
            self.images = Image(**kwargs.get('images', {}))
        else:
            self.images = None
        self.isAdminEdited = kwargs.get('isAdminEdited', False)
        self.isAdminNotificationSeen = kwargs.get('isAdminNotificationSeen', False)
        self.isBlocked = kwargs.get('isBlocked', False)
        self.isPublished = kwargs.get('isPublished', False)
        self.isReset = kwargs.get('isReset', False)
        self.lastEdited = kwargs.get('lastEdited', "")
        self.lastEditedByAdmin = kwargs.get('lastEditedByAdmin', "")
    def __eq__(self, other):
        if not isinstance(other, CustomFeaturedImages):
            return False
        return (self.images == other.images and self.isAdminEdited == other.isAdminEdited and self.isAdminNotificationSeen == other.isAdminNotificationSeen and self.isBlocked == other.isBlocked and self.isPublished == other.isPublished and self.isReset == other.isReset and self.lastEdited == other.lastEdited and self.lastEditedByAdmin == other.lastEditedByAdmin)

class CustomKnownFor:
    def __init__(self, **kwargs):
        self.isAdminEdited = kwargs.get('isAdminEdited', False)
        self.isAdminNotificationSeen = kwargs.get('isAdminNotificationSeen', False)
        self.isBlocked = kwargs.get('isBlocked', False)
        self.isPublished = kwargs.get('isPublished', False)
        self.isReset = kwargs.get('isReset', False)
        self.lastEdited = kwargs.get('lastEdited', "")
        self.lastEditedByAdmin = kwargs.get('lastEditedByAdmin', "")
        if kwargs.get('titles'):
            self.titles = Title(**kwargs.get('titles', {}))
        else:
            self.titles = None
    def __eq__(self, other):
        if not isinstance(other, CustomKnownFor):
            return False
        return (self.isAdminEdited == other.isAdminEdited and self.isAdminNotificationSeen == other.isAdminNotificationSeen and self.isBlocked == other.isBlocked and self.isPublished == other.isPublished and self.isReset == other.isReset and self.lastEdited == other.lastEdited and self.lastEditedByAdmin == other.lastEditedByAdmin and self.titles == other.titles)

class CustomPrimaryImage:
    def __init__(self, **kwargs):
        if kwargs.get('imageEditParameters'):
            self.imageEditParameters = ImageEditParameters(**kwargs.get('imageEditParameters', {}))
        else:
            self.imageEditParameters = None
        if kwargs.get('originalImage'):
            self.originalImage = Image(**kwargs.get('originalImage', {}))
        else:
            self.originalImage = None
    def __eq__(self, other):
        if not isinstance(other, CustomPrimaryImage):
            return False
        return (self.imageEditParameters == other.imageEditParameters and self.originalImage == other.originalImage)

class DateComponents:
    def __init__(self, **kwargs):
        self.day = kwargs.get('day', 0)
        self.isApproximate = kwargs.get('isApproximate', False)
        self.isBCE = kwargs.get('isBCE', False)
        self.month = kwargs.get('month', 0)
        self.partialYear = kwargs.get('partialYear', "")
        self.year = kwargs.get('year', 0)
    def __str__(self):
        if self.day and self.month and self.year:
            return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"
        elif self.year and self.month:
            return f"{self.year:04d}-{self.month:02d}"
        elif self.year:
            return f"{self.year:04d}"
        elif self.partialYear:
            return self.partialYear
        return ""
    def __repr__(self):
        return f"DateComponents(day={self.day}, month={self.month}, year={self.year}, isApproximate={self.isApproximate}, isBCE={self.isBCE}, partialYear='{self.partialYear}')"
    def __eq__(self, other):
        if not isinstance(other, DateComponents):
            return False
        return (self.day == other.day and self.isApproximate == other.isApproximate and self.isBCE == other.isBCE and self.month == other.month and self.partialYear == other.partialYear and self.year == other.year)

class DeathCause:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __str__(self):
        return str(self.text) if self.text else ""
    def __repr__(self):
        return f"DeathCause(id={self.id}, language={self.language}, text={self.text})"
    def __eq__(self, other):
        if not isinstance(other, DeathCause):
            return False
        return self.id == other.id

class DeletionDialogOutput:
    def __init__(self, **kwargs):
        if kwargs.get('deletionPrompt'):
            self.deletionPrompt = LocalizedMarkdown(**kwargs.get('deletionPrompt', {}))
        else:
            self.deletionPrompt = None
        if kwargs.get('redirectionPrompt'):
            self.redirectionPrompt = DeletionDialogRedirectionPrompt(**kwargs.get('redirectionPrompt', {}))
        else:
            self.redirectionPrompt = None
        self.requestId = kwargs.get('requestId', "")
    def __eq__(self, other):
        if not isinstance(other, DeletionDialogOutput):
            return False
        return (self.deletionPrompt == other.deletionPrompt and self.redirectionPrompt == other.redirectionPrompt and self.requestId == other.requestId)

class DeletionDialogRedirectionPrompt:
    def __init__(self, **kwargs):
        if kwargs.get('action'):
            self.action = RedirectLink(**kwargs.get('action', {}))
        else:
            self.action = None
        if kwargs.get('message'):
            self.message = LocalizedMarkdown(**kwargs.get('message', {}))
        else:
            self.message = None
    def __eq__(self, other):
        if not isinstance(other, DeletionDialogRedirectionPrompt):
            return False
        return (self.action == other.action and self.message == other.message)

class Demographic:
    def __init__(self, **kwargs):
        self.age = kwargs.get('age', "")
        self.country = kwargs.get('country', "")
        if kwargs.get('displayText'):
            self.displayText = LocalizedString(**kwargs.get('displayText', {}))
        else:
            self.displayText = None
        self.gender = kwargs.get('gender', "")
        self.userCategory = kwargs.get('userCategory', "")
    def __str__(self):
        return str(self.displayText)
    def __repr__(self):
        return f"Demographic(age={self.age}, country={self.country}, displayText={self.displayText}, gender={self.gender}, userCategory={self.userCategory})"
    def __eq__(self, other):
        if not isinstance(other, Demographic):
            return False
        return (self.age == other.age and self.country == other.country and self.displayText == other.displayText and self.gender == other.gender and self.userCategory == other.userCategory)

class DemographicDataComponent:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, DemographicDataComponent):
            return False
        return self.id == other.id

class DemographicDataItem:
    def __init__(self, **kwargs):
        if kwargs.get('selfVerified'):
            self.selfVerified = SelfVerified(**kwargs.get('selfVerified', {}))
        else:
            self.selfVerified = None
        if kwargs.get('type'):
            self.type = DemographicDataType(**kwargs.get('type', {}))
        else:
            self.type = None
        if kwargs.get('value'):
            self.value = DemographicDataValue(**kwargs.get('value', {}))
        else:
            self.value = None
    def __eq__(self, other):
        if not isinstance(other, DemographicDataItem):
            return False
        return (self.selfVerified == other.selfVerified and self.type == other.type and self.value == other.value)

class DemographicDataType:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
        self.value = kwargs.get('value', "")
    def __eq__(self, other):
        if not isinstance(other, DemographicDataType):
            return False
        return self.id == other.id

class DemographicDataValue:
    def __init__(self, **kwargs):
        if kwargs.get('components'):
            self.components = DemographicDataComponent(**kwargs.get('components', {}))
        else:
            self.components = None
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, DemographicDataValue):
            return False
        return self.id == other.id

class DemographicRatings:
    def __init__(self, **kwargs):
        self.aggregate = kwargs.get('aggregate', 0.0)
        if kwargs.get('demographic'):
            self.demographic = Demographic(**kwargs.get('demographic', {}))
        else:
            self.demographic = None
        self.voteCount = kwargs.get('voteCount', 0)
    def __eq__(self, other):
        if not isinstance(other, DemographicRatings):
            return False
        return (self.aggregate == other.aggregate and self.demographic == other.demographic and self.voteCount == other.voteCount)

class DirectContactDetails:
    def __init__(self, **kwargs):
        self.emailAddress = kwargs.get('emailAddress', "")
        if kwargs.get('faxNumber'):
            self.faxNumber = LocalizedString(**kwargs.get('faxNumber', {}))
        else:
            self.faxNumber = None
        if kwargs.get('phoneNumbers'):
            self.phoneNumbers = LocalizedString(**kwargs.get('phoneNumbers', {}))
        else:
            self.phoneNumbers = None
        if kwargs.get('website'):
            self.website = WebsiteLink(**kwargs.get('website', {}))
        else:
            self.website = None
    def __eq__(self, other):
        if not isinstance(other, DirectContactDetails):
            return False
        return (self.emailAddress == other.emailAddress and self.faxNumber == other.faxNumber and self.phoneNumbers == other.phoneNumbers and self.website == other.website)

class Disambiguation:
    def __init__(self, **kwargs):
        self.number = kwargs.get('number', 0)
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, Disambiguation):
            return False
        return (self.number == other.number and self.text == other.text)

class DisplayLabels:
    def __init__(self, **kwargs):
        self.primaryLabel = kwargs.get('primaryLabel', "")
        self.secondaryLabel = kwargs.get('secondaryLabel', "")
    def __str__(self):
        if self.primaryLabel and self.secondaryLabel:
            return f"{self.primaryLabel}, {self.secondaryLabel}"
        elif self.primaryLabel:
            return str(self.primaryLabel)
        return ""
    def __repr__(self):
        return f"DisplayLabels(primaryLabel={self.primaryLabel}, secondaryLabel={self.secondaryLabel})"
    def __eq__(self, other):
        if not isinstance(other, DisplayLabels):
            return False
        return (self.primaryLabel == other.primaryLabel and self.secondaryLabel == other.secondaryLabel)

class DisplayableArticle:
    def __init__(self, **kwargs):
        if kwargs.get('body'):
            self.body = Markdown(**kwargs.get('body', {}))
        else:
            self.body = None
        if kwargs.get('footer'):
            self.footer = Markdown(**kwargs.get('footer', {}))
        else:
            self.footer = None
        if kwargs.get('header'):
            self.header = Markdown(**kwargs.get('header', {}))
        else:
            self.header = None
    def __str__(self):
        string = ""
        if self.header:
            string += f"Header: {self.header}\n"
        if self.body:
            string += f"Body: {self.body}\n"
        if self.footer:
            string += f"Footer: {self.footer}\n"
        return string.strip()
    def __repr__(self):
        return f"<--- DisplayableArticle(header={self.header}) --->"
    def __eq__(self, other):
        if not isinstance(other, DisplayableArticle):
            return False
        return (self.body == other.body and self.footer == other.footer and self.header == other.header)

class DisplayableAttribute:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.text = kwargs.get('text', "")
    def __str__(self):
        if self.text:
            return str(self.text)
        elif self.id:
            return str(self.id)
        return ""
    def __repr__(self):
        return f"DisplayableAttribute(id={self.id}, text={self.text})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableAttribute):
            return False
        return self.id == other.id

class DisplayableBirthNameProperty:
    def __init__(self, **kwargs):
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        if self.value:
            return str(self.value)
        return ""
    def __repr__(self):
        return f"DisplayableBirthNameProperty(value={self.value})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableBirthNameProperty):
            return False
        return (self.value == other.value)

class DisplayableCountry:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.text = kwargs.get('text', "")
    def __str__(self):
        if self.text:
            return str(self.text)
        elif self.id:
            return str(self.id)
        return ""
    def __repr__(self):
        return f"DisplayableCountry(id={self.id}, text={self.text})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableCountry):
            return False
        return self.id == other.id

class DisplayableDate:
    def __init__(self, **kwargs):
        self.date = kwargs.get('date', "")
        if kwargs.get('dateComponents'):
            self.dateComponents = DateComponents(**kwargs.get('dateComponents', {}))
        else:
            self.dateComponents = None
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableDateProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
    def __str__(self):
        return self.date if self.date else ""
    def __repr__(self):
        return f"DisplayableDate(date={self.date}, dateComponents={self.dateComponents}, displayableProperty={self.displayableProperty})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableDate):
            return False
        return (self.date == other.date and self.dateComponents == other.dateComponents and self.displayableProperty == other.displayableProperty)

class DisplayableDateProperty:
    def __init__(self, **kwargs):
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        if self.value:
            return str(self.value)
        return ""
    def __repr__(self):
        return f"DisplayableDateProperty(language={self.language}, value={self.value})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableDateProperty):
            return False
        return (self.language == other.language and self.value == other.value)

class DisplayableDateRange:
    def __init__(self, **kwargs):
        if kwargs.get('endDate'):
            self.endDate = DisplayableDate(**kwargs.get('endDate', {}))
        else:
            self.endDate = None
        if kwargs.get('startDate'):
            self.startDate = DisplayableDate(**kwargs.get('startDate', {}))
        else:
            self.startDate = None
    def __eq__(self, other):
        if not isinstance(other, DisplayableDateRange):
            return False
        return (self.endDate == other.endDate and self.startDate == other.startDate)

class DisplayableEpisodeNumber:
    def __init__(self, **kwargs):
        if kwargs.get('displayableSeason'):
            self.displayableSeason = LocalizedDisplayableSeason(**kwargs.get('displayableSeason', {}))
        else:
            self.displayableSeason = None
        if kwargs.get('episodeNumber'):
            self.episodeNumber = LocalizedDisplayableEpisodeNumber(**kwargs.get('episodeNumber', {}))
        else:
            self.episodeNumber = None
    def __str(self):
        if self.displayableSeason and self.episodeNumber:
            return f"{self.displayableSeason}{self.episodeNumber}"
        elif self.displayableSeason:
            return str(self.displayableSeason)
        elif self.episodeNumber:
            return str(self.episodeNumber)
        return ""
    def __repr__(self):
        return f"DisplayableEpisodeNumber(displayableSeason={self.displayableSeason}, episodeNumber={self.episodeNumber})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableEpisodeNumber):
            return False
        return (self.displayableSeason == other.displayableSeason and self.episodeNumber == other.episodeNumber)

class DisplayableExternalLinkProperty:
    def __init__(self, **kwargs):
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value) if self.value else ""
    def __repr__(self):
        return f"DisplayableExternalLinkProperty(value={self.value})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableExternalLinkProperty):
            return False
        return (self.value == other.value)

class DisplayableLanguage:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.text = kwargs.get('text', "")
    def __str__(self):
        if self.text:
            return str(self.text)
        elif self.id:
            return str(self.id)
        return ""
    def __repr__(self):
        return f"DisplayableLanguage(id={self.id}, text={self.text})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableLanguage):
            return False
        return self.id == other.id

class DisplayableLocation:
    def __init__(self, **kwargs):
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableLocationProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.text = kwargs.get('text', "")
    def __str__(self):
        return self.text
    def __repr__(self):
        return f"DisplayableLocation(displayableProperty={self.displayableProperty}, text={self.text})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableLocation):
            return False
        return (self.displayableProperty == other.displayableProperty and self.text == other.text)

class DisplayableLocationProperty:
    def __init__(self, **kwargs):
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value) if self.value else ""
    def __repr__(self):
        return f"DisplayableLocationProperty(language={self.language}, value={self.value})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableLocationProperty):
            return False
        return (self.language == other.language and self.value == other.value)

class DisplayableNameAgeDetailsProperty:
    def __init__(self, **kwargs):
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value) if self.value else ""
    def __repr__(self):
        return f"DisplayableNameAgeDetailsProperty(value={self.value})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableNameAgeDetailsProperty):
            return False
        return (self.value == other.value)

class DisplayableNameAkaProperty:
    def __init__(self, **kwargs):
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value) if self.value else ""
    def __repr__(self):
        return f"DisplayableNameAkaProperty(value={self.value})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableNameAkaProperty):
            return False
        return (self.value == other.value)

class DisplayableNameDeathCause:
    def __init__(self, **kwargs):
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableNameDeathCauseProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.text = kwargs.get('text', "")
    def __str__(self):
        return str(self.text)
    def __repr__(self):
        return f"DisplayableNameDeathCause(text={self.text}, displayableProperty={self.displayableProperty})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableNameDeathCause):
            return False
        return (self.displayableProperty == other.displayableProperty and self.text == other.text)

class DisplayableNameDeathCauseProperty:
    def __init__(self, **kwargs):
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"DisplayableNameDeathCauseProperty(value={self.value}, language={self.language})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableNameDeathCauseProperty):
            return False
        return (self.language == other.language and self.value == other.value)

class DisplayableNameHeightProperty:
    def __init__(self, **kwargs):
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"DisplayableNameHeightProperty(value={self.value}, language={self.language})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableNameHeightProperty):
            return False
        return (self.language == other.language and self.value == other.value)

class DisplayableNameOtherWorkProperty:
    def __init__(self, **kwargs):
        if kwargs.get('qualifiersInMarkdownList'):
            self.qualifiersInMarkdownList = Markdown(**kwargs.get('qualifiersInMarkdownList', {}))
        else:
            self.qualifiersInMarkdownList = None
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"DisplayableNameOtherWorkProperty(value={self.value}, qualifiersInMarkdownList={self.qualifiersInMarkdownList})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableNameOtherWorkProperty):
            return False
        return (self.qualifiersInMarkdownList == other.qualifiersInMarkdownList and self.value == other.value)

class DisplayableNameSpouseProperty:
    def __init__(self, **kwargs):
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('qualifiersInMarkdownList'):
            self.qualifiersInMarkdownList = Markdown(**kwargs.get('qualifiersInMarkdownList', {}))
        else:
            self.qualifiersInMarkdownList = None
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"DisplayableNameSpouseProperty(value={self.value}, language={self.language}, qualifiersInMarkdownList={self.qualifiersInMarkdownList})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableNameSpouseProperty):
            return False
        return (self.language == other.language and self.qualifiersInMarkdownList == other.qualifiersInMarkdownList and self.value == other.value)

class DisplayableNickNameProperty:
    def __init__(self, **kwargs):
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"DisplayableNickNameProperty(value={self.value})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableNickNameProperty):
            return False
        return (self.value == other.value)

class DisplayableProfession:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __str__(self):
        return str(self.text)
    def __repr__(self):
        return f"DisplayableProfession(text={self.text}, id={self.id}, language={self.language})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableProfession):
            return False
        return self.id == other.id

class DisplayableProfessionCategory:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __str__(self):
        return str(self.text)
    def __repr__(self):
        return f"DisplayableProfessionCategory(text={self.text}, id={self.id}, language={self.language})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableProfessionCategory):
            return False
        return self.id == other.id

class DisplayableProfessionDescription:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __str__(self):
        return str(self.text)
    def __repr__(self):
        return f"DisplayableProfessionDescription(text={self.text}, id={self.id}, language={self.language})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableProfessionDescription):
            return False
        return self.id == other.id

class DisplayablePrompt:
    def __init__(self, **kwargs):
        self.constId = kwargs.get('constId', "")
        self.display = kwargs.get('display', False)
        self.promptType = kwargs.get('promptType', "")
    def __str__(self):
        string = ""
        string += f"Const ID: {self.constId}\n"
        string += f"Display: {self.display}\n"
        string += f"Prompt Type: {self.promptType}\n"
        return string
    def __repr__(self):
        return f"DisplayablePrompt(constId={self.constId}, display={self.display}, promptType={self.promptType})"
    def __eq__(self, other):
        if not isinstance(other, DisplayablePrompt):
            return False
        return (self.constId == other.constId and self.display == other.display and self.promptType == other.promptType)

class DisplayableRelationNameProperty:
    def __init__(self, **kwargs):
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"DisplayableRelationNameProperty(value={self.value})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableRelationNameProperty):
            return False
        return (self.value == other.value)

class DisplayableSalaryProperty:
    def __init__(self, **kwargs):
        if kwargs.get('key'):
            self.key = Markdown(**kwargs.get('key', {}))
        else:
            self.key = None
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"DisplayableSalaryProperty(value={self.value}, key={self.key})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableSalaryProperty):
            return False
        return (self.key == other.key and self.value == other.value)

class DisplayableSongTitle:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __str__(self):
        return str(self.text)
    def __repr__(self):
        return f"DisplayableSongTitle(text={self.text}, id={self.id}, language={self.language})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableSongTitle):
            return False
        return self.id == other.id

class DisplayableSpouseTimeRange:
    def __init__(self, **kwargs):
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableSpouseTimeRangeProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        if kwargs.get('fromDate'):
            self.fromDate = DisplayableDate(**kwargs.get('fromDate', {}))
        else:
            self.fromDate = None
        if kwargs.get('toDate'):
            self.toDate = DisplayableDate(**kwargs.get('toDate', {}))
        else:
            self.toDate = None
    def __str__(self):
        if self.fromDate and self.toDate:
            return f"{self.fromDate} - {self.toDate}"
        elif self.fromDate:
            return f"{self.fromDate} - Present"
        elif self.toDate:
            return f"Unknown - {self.toDate}"
        return ""
    def __repr__(self):
        return f"DisplayableSpouseTimeRange(fromDate={self.fromDate}, toDate={self.toDate}, displayableProperty={self.displayableProperty})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableSpouseTimeRange):
            return False
        return (self.displayableProperty == other.displayableProperty and self.fromDate == other.fromDate and self.toDate == other.toDate)

class DisplayableSpouseTimeRangeProperty:
    def __init__(self, **kwargs):
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"DisplayableSpouseTimeRangeProperty(value={self.value}, language={self.language})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableSpouseTimeRangeProperty):
            return False
        return (self.language == other.language and self.value == other.value)

class DisplayableTechnicalSpecificationLocalizedProperty:
    def __init__(self, **kwargs):
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('qualifiersInMarkdownList'):
            self.qualifiersInMarkdownList = Markdown(**kwargs.get('qualifiersInMarkdownList', {}))
        else:
            self.qualifiersInMarkdownList = None
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"DisplayableTechnicalSpecificationLocalizedProperty(value={self.value}, language={self.language}, qualifiersInMarkdownList={self.qualifiersInMarkdownList})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableTechnicalSpecificationLocalizedProperty):
            return False
        return (self.language == other.language and self.qualifiersInMarkdownList == other.qualifiersInMarkdownList and self.value == other.value)

class DisplayableTechnicalSpecificationProperty:
    def __init__(self, **kwargs):
        if kwargs.get('qualifiersInMarkdownList'):
            self.qualifiersInMarkdownList = Markdown(**kwargs.get('qualifiersInMarkdownList', {}))
        else:
            self.qualifiersInMarkdownList = None
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"DisplayableTechnicalSpecificationProperty(value={self.value}, qualifiersInMarkdownList={self.qualifiersInMarkdownList})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableTechnicalSpecificationProperty):
            return False
        return (self.qualifiersInMarkdownList == other.qualifiersInMarkdownList and self.value == other.value)

class DisplayableTitleAkaProperty:
    def __init__(self, **kwargs):
        if kwargs.get('key'):
            self.key = Markdown(**kwargs.get('key', {}))
        else:
            self.key = None
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('qualifiersInMarkdownList'):
            self.qualifiersInMarkdownList = Markdown(**kwargs.get('qualifiersInMarkdownList', {}))
        else:
            self.qualifiersInMarkdownList = None
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"DisplayableTitleAkaProperty(key={self.key}, value={self.value}, language={self.language}, qualifiersInMarkdownList={self.qualifiersInMarkdownList})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableTitleAkaProperty):
            return False
        return (self.key == other.key and self.language == other.language and self.qualifiersInMarkdownList == other.qualifiersInMarkdownList and self.value == other.value)

class DisplayableTitleCompanyCreditProperty:
    def __init__(self, **kwargs):
        if kwargs.get('qualifiersInMarkdownList'):
            self.qualifiersInMarkdownList = Markdown(**kwargs.get('qualifiersInMarkdownList', {}))
        else:
            self.qualifiersInMarkdownList = None
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"DisplayableTitleCompanyCreditProperty(value={self.value}, qualifiersInMarkdownList={self.qualifiersInMarkdownList})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableTitleCompanyCreditProperty):
            return False
        return (self.qualifiersInMarkdownList == other.qualifiersInMarkdownList and self.value == other.value)

class DisplayableTitleCountryOfOriginProperty:
    def __init__(self, **kwargs):
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"DisplayableTitleCompanyCreditProperty(value={self.value}, language={self.language})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableTitleCountryOfOriginProperty):
            return False
        return (self.language == other.language and self.value == other.value)

class DisplayableTitleFilmingLocationProperty:
    def __init__(self, **kwargs):
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('qualifiersInMarkdownList'):
            self.qualifiersInMarkdownList = Markdown(**kwargs.get('qualifiersInMarkdownList', {}))
        else:
            self.qualifiersInMarkdownList = None
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"DisplayableTitleFilmingLocationProperty(value={self.value}, language={self.language}, qualifiersInMarkdownList={self.qualifiersInMarkdownList})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableTitleFilmingLocationProperty):
            return False
        return (self.language == other.language and self.qualifiersInMarkdownList == other.qualifiersInMarkdownList and self.value == other.value)

class DisplayableTitleGenreProperty:
    def __init__(self, **kwargs):
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"DisplayableTitleGenreProperty(value={self.value}, language={self.language})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableTitleGenreProperty):
            return False
        return (self.language == other.language and self.value == other.value)

class DisplayableTitleReleaseDateProperty:
    def __init__(self, **kwargs):
        if kwargs.get('key'):
            self.key = Markdown(**kwargs.get('key', {}))
        else:
            self.key = None
        if kwargs.get('qualifiersInMarkdownList'):
            self.qualifiersInMarkdownList = Markdown(**kwargs.get('qualifiersInMarkdownList', {}))
        else:
            self.qualifiersInMarkdownList = None
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"DisplayableTitleReleaseDateProperty(key={self.key}, value={self.value}, qualifiersInMarkdownList={self.qualifiersInMarkdownList})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableTitleReleaseDateProperty):
            return False
        return (self.key == other.key and self.qualifiersInMarkdownList == other.qualifiersInMarkdownList and self.value == other.value)

class DisplayableTitleRuntimeProperty:
    def __init__(self, **kwargs):
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('qualifiersInMarkdownList'):
            self.qualifiersInMarkdownList = Markdown(**kwargs.get('qualifiersInMarkdownList', {}))
        else:
            self.qualifiersInMarkdownList = None
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"DisplayableTitleRuntimeProperty(value={self.value}, qualifiersInMarkdownList={self.qualifiersInMarkdownList}, language={self.language})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableTitleRuntimeProperty):
            return False
        return (self.language == other.language and self.qualifiersInMarkdownList == other.qualifiersInMarkdownList and self.value == other.value)

class DisplayableTitleSpokenLanguageProperty:
    def __init__(self, **kwargs):
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"DisplayableTitleSpokenLanguageProperty(value={self.value}, language={self.language})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableTitleSpokenLanguageProperty):
            return False
        return (self.language == other.language and self.value == other.value)

class DisplayableTitleTaglineProperty:
    def __init__(self, **kwargs):
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"DisplayableTitleTaglineProperty(value={self.value})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableTitleTaglineProperty):
            return False
        return (self.value == other.value)

class DisplayableTitleTypeProperty:
    def __init__(self, **kwargs):
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"DisplayableTitleTypeProperty(value={self.value})"
    def __eq__(self, other):
        if not isinstance(other, DisplayableTitleTypeProperty):
            return False
        return (self.value == other.value)

class DistanceToCinema:
    def __init__(self, **kwargs):
        self.distanceInMeters = kwargs.get('distanceInMeters', 0)
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __str__(self):
        return str(self.text)
    def __repr__(self):
        return f"DistanceToCinema(text={self.text}, distanceInMeters={self.distanceInMeters}, id={self.id}, language={self.language})"
    def __eq__(self, other):
        if not isinstance(other, DistanceToCinema):
            return False
        return self.id == other.id

class DistributionFormat:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __str__(self):
        return str(self.text)
    def __repr__(self):
        return f"DistributionFormat(text={self.text}, id={self.id}, language={self.language})"
    def __eq__(self, other):
        if not isinstance(other, DistributionFormat):
            return False
        return self.id == other.id

class EmployeeBranchName:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __str__(self):
        return str(self.text)
    def __repr__(self):
        return f"EmployeeBranchName(text={self.text}, id={self.id}, language={self.language})"
    def __eq__(self, other):
        if not isinstance(other, EmployeeBranchName):
            return False
        return self.id == other.id

class Employment:
    def __init__(self, **kwargs):
        if kwargs.get('branch'):
            self.branch = CompanyBranch(**kwargs.get('branch', {}))
        else:
            self.branch = None
        if kwargs.get('company'):
            self.company = Company(**kwargs.get('company', {}))
        else:
            self.company = None
        if kwargs.get('employeeContact'):
            self.employeeContact = CompanyContactDetails(**kwargs.get('employeeContact', {}))
        else:
            self.employeeContact = None
        self.id = kwargs.get('id', "")
        if kwargs.get('jobTitle'):
            self.jobTitle = LocalizedString(**kwargs.get('jobTitle', {}))
        else:
            self.jobTitle = None
        if kwargs.get('name'):
            self.name = Name(**kwargs.get('name', {}))
        else:
            self.name = None
        if kwargs.get('occupation'):
            self.occupation = OccupationValue(**kwargs.get('occupation', {}))
        else:
            self.occupation = None
    def __str__(self):
        string = ""
        if self.name and self.employeeContact:
            string = f"{self.name} ({self.employeeContact})"
        if self.jobTitle and self.occupation:
            string = f"{string}\n{self.jobTitle}: {self.occupation}" if string else f"{self.jobTitle}: {self.occupation}"
        elif self.jobTitle:
            string = f"{string}\n{self.jobTitle}" if string else f"{self.jobTitle}"
        if self.company and self.branch:
            string = f"{string}\n{self.company} ({self.branch})" if string else f"{self.company} ({self.branch})"
        elif self.company:
            string = f"{string}\n{self.company}" if string else str(self.company)
        return string
    def __repr__(self):
        return f"Employment(name={self.name}, employeeContact={self.employeeContact}, jobTitle={self.jobTitle}, occupation={self.occupation}, company={self.company}, branch={self.branch}, id={self.id})"
    def __eq__(self, other):
        if not isinstance(other, Employment):
            return False
        return self.id == other.id


class EmploymentConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Employment(**node.get("node", {})))

class EngagementStatistics:
    def __init__(self, **kwargs):
        if kwargs.get('followerStatistics'):
            self.followerStatistics = FollowerStatistics(**kwargs.get('followerStatistics', {}))
        else:
            self.followerStatistics = None
        if kwargs.get('watchlistStatistics'):
            self.watchlistStatistics = WatchlistStatistics(**kwargs.get('watchlistStatistics', {}))
        else:
            self.watchlistStatistics = None
    def __str__(self):
        if self.followerStatistics and self.watchlistStatistics:
            return f"Followers: {self.followerStatistics}, Watchlist: {self.watchlistStatistics}"
        elif self.followerStatistics:
            return f"Followers: {self.followerStatistics}"
        elif self.watchlistStatistics:
            return f"Watchlist: {self.watchlistStatistics}"
        return ""
    def __repr__(self):
        return f"EngagementStatistics(watchlistStatistics={self.watchlistStatistics}, followerStatistics={self.followerStatistics})"
    def __eq__(self, other):
        if not isinstance(other, EngagementStatistics):
            return False
        return (self.followerStatistics == other.followerStatistics and self.watchlistStatistics == other.watchlistStatistics)

class Episode:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.canonicalUrl = kwargs.get('canonicalUrl', "")
        if kwargs.get('titleType'):
            self.titleType = TitleType(**kwargs.get('titleType', {}))
        else:
            self.titleType = None
        if kwargs.get('releaseYear'):
            self.releaseYear = ReleaseYear(**kwargs.get('releaseYear', {}))
        else:
            self.releaseYear = None
        if kwargs.get('titleText'):
            self.titleText = TitleText(**kwargs.get('titleText', {}))
        else:
            self.titleText = None
        if kwargs.get('originalTitleText'):
            self.originalTitleText = TitleText(**kwargs.get('originalTitleText', {}))
        else:
            self.originalTitleText = None
    def __eq__(self, other):
        if not isinstance(other, Episode):
            return False
        return self.id == other.id


class EpisodeConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Episode(**node.get("node", {})))

class EpisodeNumberDisplayableProperty:
    def __init__(self, **kwargs):
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __eq__(self, other):
        if not isinstance(other, EpisodeNumberDisplayableProperty):
            return False
        return (self.value == other.value)

class Episodes:
    def __init__(self, **kwargs):
        if kwargs.get('displayableSeasons'):
            self.displayableSeasons = LocalizedDisplayableSeasonConnection(**kwargs.get('displayableSeasons', {}))
        else:
            self.displayableSeasons = None
        if kwargs.get('displayableYears'):
            self.displayableYears = LocalizedDisplayableEpisodeYearConnection(**kwargs.get('displayableYears', {}))
        else:
            self.displayableYears = None
        if kwargs.get('episodes'):
            self.episodes = EpisodeConnection(**kwargs.get('episodes', {}))
        else:
            self.episodes = None
        self.isOngoing = kwargs.get('isOngoing', False)
    def __eq__(self, other):
        if not isinstance(other, Episodes):
            return False
        return (self.displayableSeasons == other.displayableSeasons and self.displayableYears == other.displayableYears and self.episodes == other.episodes and self.isOngoing == other.isOngoing)

class EventEdition:
    def __init__(self, **kwargs):
        if kwargs.get('awards'):
            self.awards = AwardDetailsConnection(**kwargs.get('awards', {}))
        else:
            self.awards = None
        if kwargs.get('event'):
            self.event = AwardsEvent(**kwargs.get('event', {}))
        else:
            self.event = None
        self.id = kwargs.get('id', "")
        self.instanceWithinYear = kwargs.get('instanceWithinYear', 0)
        if kwargs.get('trivia'):
            self.trivia = Markdown(**kwargs.get('trivia', {}))
        else:
            self.trivia = None
        self.year = kwargs.get('year', 0)
    def __eq__(self, other):
        if not isinstance(other, EventEdition):
            return False
        return self.id == other.id

class EventEditionAward:
    def __init__(self, **kwargs):
        self.awardName = kwargs.get('awardName', "")
        self.id = kwargs.get('id', "")
        if kwargs.get('winners'):
            self.winners = AwardNomination(**kwargs.get('winners', {}))
        else:
            self.winners = None
    def __eq__(self, other):
        if not isinstance(other, EventEditionAward):
            return False
        return self.id == other.id


class EventEditionConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(EventEdition(**node.get("node", {})))

class EventLiveResults:
    def __init__(self, **kwargs):
        if kwargs.get('displayDescription'):
            self.displayDescription = LocalizedString(**kwargs.get('displayDescription', {}))
        else:
            self.displayDescription = None
        if kwargs.get('displayTitle'):
            self.displayTitle = LocalizedString(**kwargs.get('displayTitle', {}))
        else:
            self.displayTitle = None
        if kwargs.get('eventEditionAward'):
            self.eventEditionAward = EventEditionAward(**kwargs.get('eventEditionAward', {}))
        else:
            self.eventEditionAward = None
        self.eventId = kwargs.get('eventId', "")
        self.eventPageUrl = kwargs.get('eventPageUrl', "")
        if kwargs.get('noWinnersBlurb'):
            self.noWinnersBlurb = LocalizedString(**kwargs.get('noWinnersBlurb', {}))
        else:
            self.noWinnersBlurb = None
    def __eq__(self, other):
        if not isinstance(other, EventLiveResults):
            return False
        return (self.displayDescription == other.displayDescription and self.displayTitle == other.displayTitle and self.eventEditionAward == other.eventEditionAward and self.eventId == other.eventId and self.eventPageUrl == other.eventPageUrl and self.noWinnersBlurb == other.noWinnersBlurb)

class EventMetadata:
    def __init__(self, **kwargs):
        if kwargs.get('event'):
            self.event = AwardsEvent(**kwargs.get('event', {}))
        else:
            self.event = None
        if kwargs.get('events'):
            self.events = AwardsEventConnection(**kwargs.get('events', {}))
        else:
            self.events = None
    def __eq__(self, other):
        if not isinstance(other, EventMetadata):
            return False
        return (self.event == other.event and self.events == other.events)

class EventUrl:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = EventUrlCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        self.url = kwargs.get('url', "")
    def __eq__(self, other):
        if not isinstance(other, EventUrl):
            return False
        return (self.category == other.category and self.url == other.url)

class EventUrlCategory:
    def __init__(self, **kwargs):
        self.categoryId = kwargs.get('categoryId', "")
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, EventUrlCategory):
            return False
        return self.id == other.id

class ExperimentalCredit:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = CreditCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('name'):
            self.name = Name(**kwargs.get('name', {}))
        else:
            self.name = None
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, ExperimentalCredit):
            return False
        return (self.category == other.category and self.name == other.name and self.title == other.title)


class ExperimentalCreditConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(ExperimentalCredit(**node.get("node", {})))

class ExperimentalNameCreditCategoryWithCredits:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = CreditCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('credits'):
            self.credits = ExperimentalCreditConnection(**kwargs.get('credits', {}))
        else:
            self.credits = None
    def __eq__(self, other):
        if not isinstance(other, ExperimentalNameCreditCategoryWithCredits):
            return False
        return (self.category == other.category and self.credits == other.credits)

class Experimental_AdProductType:
    def __init__(self, **kwargs):
        self.grade = kwargs.get('grade', "")
        self.name = kwargs.get('name', "")
        self.symbol = kwargs.get('symbol', "")
    def __eq__(self, other):
        if not isinstance(other, Experimental_AdProductType):
            return False
        return (self.grade == other.grade and self.name == other.name and self.symbol == other.symbol)

class Experimental_AdditionalCreditItem:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = LocalizedString(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('details'):
            self.details = LocalizedString(**kwargs.get('details', {}))
        else:
            self.details = None
        self.id = kwargs.get('id', "")
        if kwargs.get('job'):
            self.job = LocalizedString(**kwargs.get('job', {}))
        else:
            self.job = None
        if kwargs.get('title'):
            self.title = LocalizedString(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, Experimental_AdditionalCreditItem):
            return False
        return self.id == other.id


class Experimental_AdditionalCreditItemConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Experimental_AdditionalCreditItem(**node.get("node", {})))

class Experimental_AdditionalResumeInfo:
    def __init__(self, **kwargs):
        if kwargs.get('details'):
            self.details = LocalizedString(**kwargs.get('details', {}))
        else:
            self.details = None
        self.id = kwargs.get('id', "")
        if kwargs.get('title'):
            self.title = LocalizedString(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, Experimental_AdditionalResumeInfo):
            return False
        return self.id == other.id


class Experimental_AdditionalResumeInfoConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Experimental_AdditionalResumeInfo(**node.get("node", {})))

class Experimental_Agency:
    def __init__(self, **kwargs):
        if kwargs.get('company'):
            self.company = Company(**kwargs.get('company', {}))
        else:
            self.company = None
        if kwargs.get('experimental_agents'):
            self.experimental_agents = Experimental_Agent(**kwargs.get('experimental_agents', {}))
        else:
            self.experimental_agents = None
    def __eq__(self, other):
        if not isinstance(other, Experimental_Agency):
            return False
        return (self.company == other.company and self.experimental_agents == other.experimental_agents)

class Experimental_Agent:
    def __init__(self, **kwargs):
        if kwargs.get('branch'):
            self.branch = Experimental_CompanyBranch(**kwargs.get('branch', {}))
        else:
            self.branch = None
        if kwargs.get('company'):
            self.company = Company(**kwargs.get('company', {}))
        else:
            self.company = None
        if kwargs.get('experimental_employeeContact'):
            self.experimental_employeeContact = Experimental_CompanyContactDetails(**kwargs.get('experimental_employeeContact', {}))
        else:
            self.experimental_employeeContact = None
        self.id = kwargs.get('id', "")
        self.isPrimaryAgent = kwargs.get('isPrimaryAgent', False)
        if kwargs.get('jobTitle'):
            self.jobTitle = LocalizedString(**kwargs.get('jobTitle', {}))
        else:
            self.jobTitle = None
        if kwargs.get('name'):
            self.name = Name(**kwargs.get('name', {}))
        else:
            self.name = None
        if kwargs.get('occupation'):
            self.occupation = OccupationValue(**kwargs.get('occupation', {}))
        else:
            self.occupation = None
        if kwargs.get('relationshipType'):
            self.relationshipType = Experimental_RepresentationRelationshipType(**kwargs.get('relationshipType', {}))
        else:
            self.relationshipType = None
    def __eq__(self, other):
        if not isinstance(other, Experimental_Agent):
            return False
        return self.id == other.id

class Experimental_ApsSlotInfo:
    def __init__(self, **kwargs):
        self.apsSlotId = kwargs.get('apsSlotId', "")
        self.apsSlotName = kwargs.get('apsSlotName', "")
        if kwargs.get('apsSlotParams'):
            self.apsSlotParams = Experimental_ApsSlotParam(**kwargs.get('apsSlotParams', {}))
        else:
            self.apsSlotParams = None
        self.slotName = kwargs.get('slotName', "")
    def __eq__(self, other):
        if not isinstance(other, Experimental_ApsSlotInfo):
            return False
        return (self.apsSlotId == other.apsSlotId and self.apsSlotName == other.apsSlotName and self.apsSlotParams == other.apsSlotParams and self.slotName == other.slotName)

class Experimental_ApsSlotParam:
    def __init__(self, **kwargs):
        self.key = kwargs.get('key', "")
        self.value = kwargs.get('value', "")
    def __eq__(self, other):
        if not isinstance(other, Experimental_ApsSlotParam):
            return False
        return (self.key == other.key and self.value == other.value)

class Experimental_CompanyBranch:
    def __init__(self, **kwargs):
        if kwargs.get('experimental_directContact'):
            self.experimental_directContact = Experimental_CompanyContactDetails(**kwargs.get('experimental_directContact', {}))
        else:
            self.experimental_directContact = None
        self.id = kwargs.get('id', "")
        if kwargs.get('name'):
            self.name = LocalizedString(**kwargs.get('name', {}))
        else:
            self.name = None
    def __eq__(self, other):
        if not isinstance(other, Experimental_CompanyBranch):
            return False
        return self.id == other.id


class Experimental_CompanyBranchConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Experimental_CompanyBranch(**node.get("node", {})))

class Experimental_CompanyClient:
    def __init__(self, **kwargs):
        if kwargs.get('client'):
            self.client = Name(**kwargs.get('client', {}))
        else:
            self.client = None
        if kwargs.get('experimental_agents'):
            self.experimental_agents = Experimental_Agent(**kwargs.get('experimental_agents', {}))
        else:
            self.experimental_agents = None
        self.id = kwargs.get('id', "")
    def __eq__(self, other):
        if not isinstance(other, Experimental_CompanyClient):
            return False
        return self.id == other.id


class Experimental_CompanyClientConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Experimental_CompanyClient(**node.get("node", {})))

class Experimental_CompanyContactDetails:
    def __init__(self, **kwargs):
        self.emailAddress = kwargs.get('emailAddress', "")
        if kwargs.get('faxNumber'):
            self.faxNumber = LocalizedString(**kwargs.get('faxNumber', {}))
        else:
            self.faxNumber = None
        if kwargs.get('phoneNumbers'):
            self.phoneNumbers = LocalizedString(**kwargs.get('phoneNumbers', {}))
        else:
            self.phoneNumbers = None
        if kwargs.get('physicalAddress'):
            self.physicalAddress = Location(**kwargs.get('physicalAddress', {}))
        else:
            self.physicalAddress = None
        if kwargs.get('website'):
            self.website = WebsiteLink(**kwargs.get('website', {}))
        else:
            self.website = None
    def __eq__(self, other):
        if not isinstance(other, Experimental_CompanyContactDetails):
            return False
        return (self.emailAddress == other.emailAddress and self.faxNumber == other.faxNumber and self.phoneNumbers == other.phoneNumbers and self.physicalAddress == other.physicalAddress and self.website == other.website)

class Experimental_DirectContactDetails:
    def __init__(self, **kwargs):
        self.emailAddress = kwargs.get('emailAddress', "")
        if kwargs.get('faxNumber'):
            self.faxNumber = LocalizedString(**kwargs.get('faxNumber', {}))
        else:
            self.faxNumber = None
        if kwargs.get('phoneNumbers'):
            self.phoneNumbers = LocalizedString(**kwargs.get('phoneNumbers', {}))
        else:
            self.phoneNumbers = None
        if kwargs.get('website'):
            self.website = WebsiteLink(**kwargs.get('website', {}))
        else:
            self.website = None
    def __eq__(self, other):
        if not isinstance(other, Experimental_DirectContactDetails):
            return False
        return (self.emailAddress == other.emailAddress and self.faxNumber == other.faxNumber and self.phoneNumbers == other.phoneNumbers and self.website == other.website)

class Experimental_NameRepresentation:
    def __init__(self, **kwargs):
        if kwargs.get('client'):
            self.client = Name(**kwargs.get('client', {}))
        else:
            self.client = None
        if kwargs.get('experimental_agency'):
            self.experimental_agency = Experimental_Agency(**kwargs.get('experimental_agency', {}))
        else:
            self.experimental_agency = None
        self.id = kwargs.get('id', "")
        if kwargs.get('independentRepresentative'):
            self.independentRepresentative = Name(**kwargs.get('independentRepresentative', {}))
        else:
            self.independentRepresentative = None
        if kwargs.get('relationshipType'):
            self.relationshipType = Experimental_RepresentationRelationshipType(**kwargs.get('relationshipType', {}))
        else:
            self.relationshipType = None
    def __eq__(self, other):
        if not isinstance(other, Experimental_NameRepresentation):
            return False
        return self.id == other.id


class Experimental_NameRepresentationConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Experimental_NameRepresentation(**node.get("node", {})))

class Experimental_NotificationPreference:
    def __init__(self, **kwargs):
        self.interested = kwargs.get('interested', False)
        if kwargs.get('type'):
            self.type = Experimental_NotificationPreferenceType(**kwargs.get('type', {}))
        else:
            self.type = None
    def __eq__(self, other):
        if not isinstance(other, Experimental_NotificationPreference):
            return False
        return (self.interested == other.interested and self.type == other.type)

class Experimental_NotificationPreferenceType:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, Experimental_NotificationPreferenceType):
            return False
        return self.id == other.id

class Experimental_PersonalEmployment:
    def __init__(self, **kwargs):
        if kwargs.get('branch'):
            self.branch = Experimental_CompanyBranch(**kwargs.get('branch', {}))
        else:
            self.branch = None
        if kwargs.get('company'):
            self.company = Company(**kwargs.get('company', {}))
        else:
            self.company = None
        if kwargs.get('experimental_employeeContact'):
            self.experimental_employeeContact = Experimental_CompanyContactDetails(**kwargs.get('experimental_employeeContact', {}))
        else:
            self.experimental_employeeContact = None
        self.id = kwargs.get('id', "")
        if kwargs.get('jobTitle'):
            self.jobTitle = LocalizedString(**kwargs.get('jobTitle', {}))
        else:
            self.jobTitle = None
        if kwargs.get('name'):
            self.name = Name(**kwargs.get('name', {}))
        else:
            self.name = None
        if kwargs.get('occupation'):
            self.occupation = OccupationValue(**kwargs.get('occupation', {}))
        else:
            self.occupation = None
    def __eq__(self, other):
        if not isinstance(other, Experimental_PersonalEmployment):
            return False
        return self.id == other.id


class Experimental_PersonalEmploymentConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Experimental_PersonalEmployment(**node.get("node", {})))

class Experimental_PlaidOverride:
    def __init__(self, **kwargs):
        self.key = kwargs.get('key', "")
        self.value = kwargs.get('value', "")
    def __eq__(self, other):
        if not isinstance(other, Experimental_PlaidOverride):
            return False
        return (self.key == other.key and self.value == other.value)

class Experimental_RepresentationRelationshipType:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.relationshipTypeId = kwargs.get('relationshipTypeId', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, Experimental_RepresentationRelationshipType):
            return False
        return self.id == other.id

class Experimental_Resume:
    def __init__(self, **kwargs):
        if kwargs.get('experimental_additionalAwards'):
            self.experimental_additionalAwards = Experimental_SelfVerifiedAwardConnection(**kwargs.get('experimental_additionalAwards', {}))
        else:
            self.experimental_additionalAwards = None
        if kwargs.get('experimental_additionalCreditCategories'):
            self.experimental_additionalCreditCategories = Experimental_ResumeAdditionalCreditsCategories(**kwargs.get('experimental_additionalCreditCategories', {}))
        else:
            self.experimental_additionalCreditCategories = None
        if kwargs.get('experimental_additionalCredits'):
            self.experimental_additionalCredits = Experimental_AdditionalCreditItemConnection(**kwargs.get('experimental_additionalCredits', {}))
        else:
            self.experimental_additionalCredits = None
        if kwargs.get('experimental_additionalResumeInfo'):
            self.experimental_additionalResumeInfo = Experimental_AdditionalResumeInfoConnection(**kwargs.get('experimental_additionalResumeInfo', {}))
        else:
            self.experimental_additionalResumeInfo = None
        if kwargs.get('experimental_education'):
            self.experimental_education = Experimental_SelfVerifiedEducationConnection(**kwargs.get('experimental_education', {}))
        else:
            self.experimental_education = None
        if kwargs.get('experimental_performerProfile'):
            self.experimental_performerProfile = Experimental_ResumeDataItem(**kwargs.get('experimental_performerProfile', {}))
        else:
            self.experimental_performerProfile = None
        if kwargs.get('experimental_personalDetails'):
            self.experimental_personalDetails = Experimental_ResumeDataItem(**kwargs.get('experimental_personalDetails', {}))
        else:
            self.experimental_personalDetails = None
        if kwargs.get('experimental_professionalBackground'):
            self.experimental_professionalBackground = Experimental_ResumeDataItem(**kwargs.get('experimental_professionalBackground', {}))
        else:
            self.experimental_professionalBackground = None
        if kwargs.get('experimental_references'):
            self.experimental_references = Experimental_SelfVerifiedReferenceConnection(**kwargs.get('experimental_references', {}))
        else:
            self.experimental_references = None
        if kwargs.get('experimental_skills'):
            self.experimental_skills = Experimental_ResumeDataItem(**kwargs.get('experimental_skills', {}))
        else:
            self.experimental_skills = None
        if kwargs.get('experimental_training'):
            self.experimental_training = Experimental_SelfVerifiedTrainingConnection(**kwargs.get('experimental_training', {}))
        else:
            self.experimental_training = None
    def __eq__(self, other):
        if not isinstance(other, Experimental_Resume):
            return False
        return (self.experimental_additionalAwards == other.experimental_additionalAwards and self.experimental_additionalCreditCategories == other.experimental_additionalCreditCategories and self.experimental_additionalCredits == other.experimental_additionalCredits and self.experimental_additionalResumeInfo == other.experimental_additionalResumeInfo and self.experimental_education == other.experimental_education and self.experimental_performerProfile == other.experimental_performerProfile and self.experimental_personalDetails == other.experimental_personalDetails and self.experimental_professionalBackground == other.experimental_professionalBackground and self.experimental_references == other.experimental_references and self.experimental_skills == other.experimental_skills and self.experimental_training == other.experimental_training)

class Experimental_ResumeAdditionalCreditsCategories:
    def __init__(self, **kwargs):
        if kwargs.get('categories'):
            self.categories = Experimental_ResumeAdditionalCreditsCategory(**kwargs.get('categories', {}))
        else:
            self.categories = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, Experimental_ResumeAdditionalCreditsCategories):
            return False
        return (self.categories == other.categories and self.total == other.total)

class Experimental_ResumeAdditionalCreditsCategory:
    def __init__(self, **kwargs):
        if kwargs.get('credits'):
            self.credits = Experimental_AdditionalCreditItem(**kwargs.get('credits', {}))
        else:
            self.credits = None
        self.id = kwargs.get('id', "")
        if kwargs.get('title'):
            self.title = LocalizedString(**kwargs.get('title', {}))
        else:
            self.title = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, Experimental_ResumeAdditionalCreditsCategory):
            return False
        return self.id == other.id

class Experimental_ResumeDataItem:
    def __init__(self, **kwargs):
        if kwargs.get('label'):
            self.label = LocalizedString(**kwargs.get('label', {}))
        else:
            self.label = None
        if kwargs.get('values'):
            self.values = LocalizedString(**kwargs.get('values', {}))
        else:
            self.values = None
    def __eq__(self, other):
        if not isinstance(other, Experimental_ResumeDataItem):
            return False
        return (self.label == other.label and self.values == other.values)

class Experimental_SelfVerifiedAward:
    def __init__(self, **kwargs):
        if kwargs.get('awardTitle'):
            self.awardTitle = LocalizedString(**kwargs.get('awardTitle', {}))
        else:
            self.awardTitle = None
        if kwargs.get('details'):
            self.details = LocalizedString(**kwargs.get('details', {}))
        else:
            self.details = None
        if kwargs.get('event'):
            self.event = LocalizedString(**kwargs.get('event', {}))
        else:
            self.event = None
        self.id = kwargs.get('id', "")
        self.year = kwargs.get('year', 0)
    def __eq__(self, other):
        if not isinstance(other, Experimental_SelfVerifiedAward):
            return False
        return self.id == other.id


class Experimental_SelfVerifiedAwardConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Experimental_SelfVerifiedAward(**node.get("node", {})))

class Experimental_SelfVerifiedEducation:
    def __init__(self, **kwargs):
        if kwargs.get('degree'):
            self.degree = LocalizedString(**kwargs.get('degree', {}))
        else:
            self.degree = None
        if kwargs.get('details'):
            self.details = LocalizedString(**kwargs.get('details', {}))
        else:
            self.details = None
        self.id = kwargs.get('id', "")
        if kwargs.get('location'):
            self.location = LocalizedString(**kwargs.get('location', {}))
        else:
            self.location = None
        if kwargs.get('school'):
            self.school = LocalizedString(**kwargs.get('school', {}))
        else:
            self.school = None
        self.year = kwargs.get('year', 0)
    def __eq__(self, other):
        if not isinstance(other, Experimental_SelfVerifiedEducation):
            return False
        return self.id == other.id


class Experimental_SelfVerifiedEducationConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Experimental_SelfVerifiedEducation(**node.get("node", {})))

class Experimental_SelfVerifiedReference:
    def __init__(self, **kwargs):
        self.contact = kwargs.get('contact', "")
        self.id = kwargs.get('id', "")
        if kwargs.get('name'):
            self.name = LocalizedString(**kwargs.get('name', {}))
        else:
            self.name = None
        if kwargs.get('relationship'):
            self.relationship = LocalizedString(**kwargs.get('relationship', {}))
        else:
            self.relationship = None
    def __eq__(self, other):
        if not isinstance(other, Experimental_SelfVerifiedReference):
            return False
        return self.id == other.id


class Experimental_SelfVerifiedReferenceConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Experimental_SelfVerifiedReference(**node.get("node", {})))

class Experimental_SelfVerifiedTraining:
    def __init__(self, **kwargs):
        if kwargs.get('details'):
            self.details = LocalizedString(**kwargs.get('details', {}))
        else:
            self.details = None
        self.id = kwargs.get('id', "")
        if kwargs.get('instructor'):
            self.instructor = LocalizedString(**kwargs.get('instructor', {}))
        else:
            self.instructor = None
        if kwargs.get('location'):
            self.location = LocalizedString(**kwargs.get('location', {}))
        else:
            self.location = None
        if kwargs.get('school'):
            self.school = LocalizedString(**kwargs.get('school', {}))
        else:
            self.school = None
        if kwargs.get('training'):
            self.training = LocalizedString(**kwargs.get('training', {}))
        else:
            self.training = None
        self.year = kwargs.get('year', 0)
    def __eq__(self, other):
        if not isinstance(other, Experimental_SelfVerifiedTraining):
            return False
        return self.id == other.id


class Experimental_SelfVerifiedTrainingConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Experimental_SelfVerifiedTraining(**node.get("node", {})))

class Experimental_TrackNotificationPreferences:
    def __init__(self, **kwargs):
        self.isTracking = kwargs.get('isTracking', False)
        if kwargs.get('notificationPreferences'):
            self.notificationPreferences = Experimental_NotificationPreference(**kwargs.get('notificationPreferences', {}))
        else:
            self.notificationPreferences = None
    def __eq__(self, other):
        if not isinstance(other, Experimental_TrackNotificationPreferences):
            return False
        return (self.isTracking == other.isTracking and self.notificationPreferences == other.notificationPreferences)

class Experimental_WebAdCreativeInfo:
    def __init__(self, **kwargs):
        self.aaxAdType = kwargs.get('aaxAdType', "")
        if kwargs.get('adProductType'):
            self.adProductType = Experimental_AdProductType(**kwargs.get('adProductType', {}))
        else:
            self.adProductType = None
        self.creativeId = kwargs.get('creativeId', "")
        self.hasAutoplay = kwargs.get('hasAutoplay', False)
        self.isEligibleFor3pAd = kwargs.get('isEligibleFor3pAd', False)
        self.isPremium = kwargs.get('isPremium', False)
        if kwargs.get('plaidOverrides'):
            self.plaidOverrides = Experimental_PlaidOverride(**kwargs.get('plaidOverrides', {}))
        else:
            self.plaidOverrides = None
        self.responsiveResizingDisabledRange = kwargs.get('responsiveResizingDisabledRange', "")
        self.shouldFitToWidth = kwargs.get('shouldFitToWidth', False)
        if kwargs.get('size'):
            self.size = CreativeSize(**kwargs.get('size', {}))
        else:
            self.size = None
        self.slotMarkup = kwargs.get('slotMarkup', "")
    def __eq__(self, other):
        if not isinstance(other, Experimental_WebAdCreativeInfo):
            return False
        return (self.aaxAdType == other.aaxAdType and self.adProductType == other.adProductType and self.creativeId == other.creativeId and self.hasAutoplay == other.hasAutoplay and self.isEligibleFor3pAd == other.isEligibleFor3pAd and self.isPremium == other.isPremium and self.plaidOverrides == other.plaidOverrides and self.responsiveResizingDisabledRange == other.responsiveResizingDisabledRange and self.shouldFitToWidth == other.shouldFitToWidth and self.size == other.size and self.slotMarkup == other.slotMarkup)

class Experimental_WebAdFetchingInfo:
    def __init__(self, **kwargs):
        self.endpoint = kwargs.get('endpoint', "")
        self.params = kwargs.get('params', "")
        self.query = kwargs.get('query', "")
    def __eq__(self, other):
        if not isinstance(other, Experimental_WebAdFetchingInfo):
            return False
        return (self.endpoint == other.endpoint and self.params == other.params and self.query == other.query)

class Experimental_WebAdSlot:
    def __init__(self, **kwargs):
        self.abpAcceptable = kwargs.get('abpAcceptable', False)
        self.adFeedbackUrl = kwargs.get('adFeedbackUrl', "")
        if kwargs.get('creativeInfo'):
            self.creativeInfo = Experimental_WebAdCreativeInfo(**kwargs.get('creativeInfo', {}))
        else:
            self.creativeInfo = None
        self.name = kwargs.get('name', "")
    def __eq__(self, other):
        if not isinstance(other, Experimental_WebAdSlot):
            return False
        return (self.abpAcceptable == other.abpAcceptable and self.adFeedbackUrl == other.adFeedbackUrl and self.creativeInfo == other.creativeInfo and self.name == other.name)

class Experimental_WebAdsConfigOutput:
    def __init__(self, **kwargs):
        if kwargs.get('adFetchingInfo'):
            self.adFetchingInfo = Experimental_WebAdFetchingInfo(**kwargs.get('adFetchingInfo', {}))
        else:
            self.adFetchingInfo = None
        self.adRefreshEnabled = kwargs.get('adRefreshEnabled', False)
        if kwargs.get('apsSlotInfoMap'):
            self.apsSlotInfoMap = Experimental_ApsSlotInfo(**kwargs.get('apsSlotInfoMap', {}))
        else:
            self.apsSlotInfoMap = None
        self.hasPremiumAd = kwargs.get('hasPremiumAd', False)
        self.headerMarkup = kwargs.get('headerMarkup', "")
        if kwargs.get('plaidOverrides'):
            self.plaidOverrides = Experimental_PlaidOverride(**kwargs.get('plaidOverrides', {}))
        else:
            self.plaidOverrides = None
        if kwargs.get('responsiveSlotSizes'):
            self.responsiveSlotSizes = Experimental_WebResponsiveSlotSize(**kwargs.get('responsiveSlotSizes', {}))
        else:
            self.responsiveSlotSizes = None
        if kwargs.get('slots'):
            self.slots = Experimental_WebAdSlot(**kwargs.get('slots', {}))
        else:
            self.slots = None
        self.slotsEnabled = kwargs.get('slotsEnabled', False)
    def __eq__(self, other):
        if not isinstance(other, Experimental_WebAdsConfigOutput):
            return False
        return (self.adFetchingInfo == other.adFetchingInfo and self.adRefreshEnabled == other.adRefreshEnabled and self.apsSlotInfoMap == other.apsSlotInfoMap and self.hasPremiumAd == other.hasPremiumAd and self.headerMarkup == other.headerMarkup and self.plaidOverrides == other.plaidOverrides and self.responsiveSlotSizes == other.responsiveSlotSizes and self.slots == other.slots and self.slotsEnabled == other.slotsEnabled)

class Experimental_WebAdsOutput:
    def __init__(self, **kwargs):
        self.hasPremiumAd = kwargs.get('hasPremiumAd', False)
        if kwargs.get('plaidOverrides'):
            self.plaidOverrides = Experimental_PlaidOverride(**kwargs.get('plaidOverrides', {}))
        else:
            self.plaidOverrides = None
        if kwargs.get('responsiveResizingDisabledSlots'):
            self.responsiveResizingDisabledSlots = Experimental_WebResponsiveResizingDisabledSlot(**kwargs.get('responsiveResizingDisabledSlots', {}))
        else:
            self.responsiveResizingDisabledSlots = None
        if kwargs.get('slots'):
            self.slots = Experimental_WebAdSlot(**kwargs.get('slots', {}))
        else:
            self.slots = None
    def __eq__(self, other):
        if not isinstance(other, Experimental_WebAdsOutput):
            return False
        return (self.hasPremiumAd == other.hasPremiumAd and self.plaidOverrides == other.plaidOverrides and self.responsiveResizingDisabledSlots == other.responsiveResizingDisabledSlots and self.slots == other.slots)

class Experimental_WebResponsiveResizingDisabledBreakpoint:
    def __init__(self, **kwargs):
        self.breakpoint = kwargs.get('breakpoint', 0)
        self.disabled = kwargs.get('disabled', False)
    def __eq__(self, other):
        if not isinstance(other, Experimental_WebResponsiveResizingDisabledBreakpoint):
            return False
        return (self.breakpoint == other.breakpoint and self.disabled == other.disabled)

class Experimental_WebResponsiveResizingDisabledSlot:
    def __init__(self, **kwargs):
        if kwargs.get('breakpoints'):
            self.breakpoints = Experimental_WebResponsiveResizingDisabledBreakpoint(**kwargs.get('breakpoints', {}))
        else:
            self.breakpoints = None
        self.name = kwargs.get('name', "")
    def __eq__(self, other):
        if not isinstance(other, Experimental_WebResponsiveResizingDisabledSlot):
            return False
        return (self.breakpoints == other.breakpoints and self.name == other.name)

class Experimental_WebResponsiveSlotSize:
    def __init__(self, **kwargs):
        if kwargs.get('breakpoints'):
            self.breakpoints = Experimental_WebViewportBreakpointSlotSize(**kwargs.get('breakpoints', {}))
        else:
            self.breakpoints = None
        self.slotName = kwargs.get('slotName', "")
    def __eq__(self, other):
        if not isinstance(other, Experimental_WebResponsiveSlotSize):
            return False
        return (self.breakpoints == other.breakpoints and self.slotName == other.slotName)

class Experimental_WebViewportBreakpointSlotSize:
    def __init__(self, **kwargs):
        self.breakpoint = kwargs.get('breakpoint', "")
        if kwargs.get('slotSize'):
            self.slotSize = CreativeSize(**kwargs.get('slotSize', {}))
        else:
            self.slotSize = None
    def __eq__(self, other):
        if not isinstance(other, Experimental_WebViewportBreakpointSlotSize):
            return False
        return (self.breakpoint == other.breakpoint and self.slotSize == other.slotSize)

class ExternalLink:
    def __init__(self, **kwargs):
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableExternalLinkProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        if kwargs.get('externalLinkCategory'):
            self.externalLinkCategory = ExternalLinkCategory(**kwargs.get('externalLinkCategory', {}))
        else:
            self.externalLinkCategory = None
        if kwargs.get('externalLinkLanguages'):
            self.externalLinkLanguages = DisplayableLanguage(**kwargs.get('externalLinkLanguages', {}))
        else:
            self.externalLinkLanguages = None
        if kwargs.get('externalLinkRegion'):
            self.externalLinkRegion = DisplayableCountry(**kwargs.get('externalLinkRegion', {}))
        else:
            self.externalLinkRegion = None
        self.id = kwargs.get('id', "")
        self.label = kwargs.get('label', "")
        if kwargs.get('labelLanguage'):
            self.labelLanguage = DisplayableLanguage(**kwargs.get('labelLanguage', {}))
        else:
            self.labelLanguage = None
        self.url = kwargs.get('url', "")
    def __eq__(self, other):
        if not isinstance(other, ExternalLink):
            return False
        return self.id == other.id

class ExternalLinkCategory:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, ExternalLinkCategory):
            return False
        return self.id == other.id

class ExternalLinkCategoryWithExternalLinks:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = ExternalLinkCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('externalLinks'):
            self.externalLinks = ExternalLinkConnection(**kwargs.get('externalLinks', {}))
        else:
            self.externalLinks = None
        if kwargs.get('restriction'):
            self.restriction = ExternalLinkRestriction(**kwargs.get('restriction', {}))
        else:
            self.restriction = None
    def __eq__(self, other):
        if not isinstance(other, ExternalLinkCategoryWithExternalLinks):
            return False
        return (self.category == other.category and self.externalLinks == other.externalLinks and self.restriction == other.restriction)

class ExternalLinkCategoryWithFeaturedExternalLinks:
    def __init__(self, **kwargs):
        if kwargs.get('externalLinks'):
            self.externalLinks = ExternalLink(**kwargs.get('externalLinks', {}))
        else:
            self.externalLinks = None
        if kwargs.get('featuredCategory'):
            self.featuredCategory = ExternalLinkCategory(**kwargs.get('featuredCategory', {}))
        else:
            self.featuredCategory = None
    def __eq__(self, other):
        if not isinstance(other, ExternalLinkCategoryWithFeaturedExternalLinks):
            return False
        return (self.externalLinks == other.externalLinks and self.featuredCategory == other.featuredCategory)


class ExternalLinkConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(ExternalLink(**node.get("node", {})))

class ExternalLinkRestriction:
    def __init__(self, **kwargs):
        if kwargs.get('explanations'):
            self.explanations = RestrictionExplanation(**kwargs.get('explanations', {}))
        else:
            self.explanations = None
        self.reasons = kwargs.get('reasons', "")
        self.restrictionReason = kwargs.get('restrictionReason', "")
        self.unrestrictedTotal = kwargs.get('unrestrictedTotal', 0)
    def __eq__(self, other):
        if not isinstance(other, ExternalLinkRestriction):
            return False
        return (self.explanations == other.explanations and self.reasons == other.reasons and self.restrictionReason == other.restrictionReason and self.unrestrictedTotal == other.unrestrictedTotal)

class Faq:
    def __init__(self, **kwargs):
        if kwargs.get('answer'):
            self.answer = Markdown(**kwargs.get('answer', {}))
        else:
            self.answer = None
        self.id = kwargs.get('id', "")
        self.isSpoiler = kwargs.get('isSpoiler', False)
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('question'):
            self.question = Markdown(**kwargs.get('question', {}))
        else:
            self.question = None
    def __eq__(self, other):
        if not isinstance(other, Faq):
            return False
        return self.id == other.id


class FaqConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Faq(**node.get("node", {})))

class FeatureAccess:
    def __init__(self, **kwargs):
        self.proAppFunctionality = kwargs.get('proAppFunctionality', False)
    def __eq__(self, other):
        if not isinstance(other, FeatureAccess):
            return False
        return (self.proAppFunctionality == other.proAppFunctionality)

class FeedbackGiven:
    def __init__(self, **kwargs):
        self.hasGivenFeedback = kwargs.get('hasGivenFeedback', False)
    def __eq__(self, other):
        if not isinstance(other, FeedbackGiven):
            return False
        return (self.hasGivenFeedback == other.hasGivenFeedback)

class FileMetadata:
    def __init__(self, **kwargs):
        self.accountDataURL = kwargs.get('accountDataURL', "")
        self.creationDate = kwargs.get('creationDate', "")
        self.expirationDate = kwargs.get('expirationDate', "")
        self.name = kwargs.get('name', "")
        if kwargs.get('sizeLabel'):
            self.sizeLabel = LocalizedString(**kwargs.get('sizeLabel', {}))
        else:
            self.sizeLabel = None
    def __eq__(self, other):
        if not isinstance(other, FileMetadata):
            return False
        return (self.accountDataURL == other.accountDataURL and self.creationDate == other.creationDate and self.expirationDate == other.expirationDate and self.name == other.name and self.sizeLabel == other.sizeLabel)

class FilmLength:
    def __init__(self, **kwargs):
        if kwargs.get('attributes'):
            self.attributes = [DisplayableAttribute(**attr) for attr in kwargs.get('attributes', [])]
        else:
            self.attributes = None
        if kwargs.get('countries'):
            self.countries = DisplayableCountry(**kwargs.get('countries', {}))
        else:
            self.countries = None
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableTechnicalSpecificationLocalizedProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.filmLength = kwargs.get('filmLength', 0.0)
        self.isSplitReel = kwargs.get('isSplitReel', False)
        self.numReels = kwargs.get('numReels', 0.0)
    def __eq__(self, other):
        if not isinstance(other, FilmLength):
            return False
        return (self.attributes == other.attributes and self.countries == other.countries and self.displayableProperty == other.displayableProperty and self.filmLength == other.filmLength and self.isSplitReel == other.isSplitReel and self.numReels == other.numReels)

class FilmLengths:
    def __init__(self, **kwargs):
        if kwargs.get('items'):
            self.items = FilmLength(**kwargs.get('items', {}))
        else:
            self.items = None
        if kwargs.get('restriction'):
            self.restriction = TechnicalSpecificationsRestriction(**kwargs.get('restriction', {}))
        else:
            self.restriction = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, FilmLengths):
            return False
        return (self.items == other.items and self.restriction == other.restriction and self.total == other.total)

class FilmingDates:
    def __init__(self, **kwargs):
        if kwargs.get('dateRange'):
            self.dateRange = DisplayableDateRange(**kwargs.get('dateRange', {}))
        else:
            self.dateRange = None
    def __eq__(self, other):
        if not isinstance(other, FilmingDates):
            return False
        return (self.dateRange == other.dateRange)


class FilmingDatesConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(FilmingDates(**node.get("node", {})))

class FilmingLocation:
    def __init__(self, **kwargs):
        if kwargs.get('attributes'):
            self.attributes = [DisplayableAttribute(**attr) for attr in kwargs.get('attributes', [])]
        else:
            self.attributes = None
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableTitleFilmingLocationProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.id = kwargs.get('id', "")
        if kwargs.get('interestScore'):
            self.interestScore = InterestScore(**kwargs.get('interestScore', {}))
        else:
            self.interestScore = None
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.location = kwargs.get('location', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, FilmingLocation):
            return False
        return self.id == other.id


class FilmingLocationConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(FilmingLocation(**node.get("node", {})))

class FilmingLocationRestriction:
    def __init__(self, **kwargs):
        if kwargs.get('explanations'):
            self.explanations = RestrictionExplanation(**kwargs.get('explanations', {}))
        else:
            self.explanations = None
        self.reasons = kwargs.get('reasons', "")
        self.restrictionReason = kwargs.get('restrictionReason', "")
        self.unrestrictedTotal = kwargs.get('unrestrictedTotal', 0)
    def __eq__(self, other):
        if not isinstance(other, FilmingLocationRestriction):
            return False
        return (self.explanations == other.explanations and self.reasons == other.reasons and self.restrictionReason == other.restrictionReason and self.unrestrictedTotal == other.unrestrictedTotal)

class FollowerStatistics:
    def __init__(self, **kwargs):
        if kwargs.get('displayableCount'):
            self.displayableCount = LocalizedDisplayableCount(**kwargs.get('displayableCount', {}))
        else:
            self.displayableCount = None
        self.totalCount = kwargs.get('totalCount', 0)
    def __eq__(self, other):
        if not isinstance(other, FollowerStatistics):
            return False
        return (self.displayableCount == other.displayableCount and self.totalCount == other.totalCount)

class ForgotPasswordRedirectURLOutput:
    def __init__(self, **kwargs):
        self.redirectURL = kwargs.get('redirectURL', "")
    def __eq__(self, other):
        if not isinstance(other, ForgotPasswordRedirectURLOutput):
            return False
        return (self.redirectURL == other.redirectURL)

class GenderIdentity:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, GenderIdentity):
            return False
        return self.id == other.id

class Genre:
    def __init__(self, **kwargs):
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableTitleGenreProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.relevanceRanking = kwargs.get('relevanceRanking', 0)
        if kwargs.get('subgenres'):
            self.subgenres = [TitleKeyword(**subgenre) for subgenre in kwargs.get('subgenres', [])]
        else:
            self.subgenres = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, Genre):
            return False
        return self.id == other.id

class GenreItem:
    def __init__(self, **kwargs):
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableTitleGenreProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.genreId = kwargs.get('genreId', "")
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, GenreItem):
            return False
        return self.id == other.id

class GenreSummary:
    def __init__(self, **kwargs):
        if kwargs.get('genre'):
            self.genre = GenreItem(**kwargs.get('genre', {}))
        else:
            self.genre = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, GenreSummary):
            return False
        return (self.genre == other.genre and self.total == other.total)

class Genres:
    def __init__(self, **kwargs):
        if kwargs.get('genres'):
            self.genres = [Genre(**genre) for genre in kwargs.get('genres', [])]
        else:
            self.genres = None
    def __eq__(self, other):
        if not isinstance(other, Genres):
            return False
        return (self.genres == other.genres)

class GetLatestUIWorkflowOutput:
    def __init__(self, **kwargs):
        if kwargs.get('workflow'):
            self.workflow = UIWorkflow(**kwargs.get('workflow', {}))
        else:
            self.workflow = None
    def __eq__(self, other):
        if not isinstance(other, GetLatestUIWorkflowOutput):
            return False
        return (self.workflow == other.workflow)

class Goof:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = GoofCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('displayableArticle'):
            self.displayableArticle = DisplayableArticle(**kwargs.get('displayableArticle', {}))
        else:
            self.displayableArticle = None
        self.id = kwargs.get('id', "")
        if kwargs.get('interestScore'):
            self.interestScore = InterestScore(**kwargs.get('interestScore', {}))
        else:
            self.interestScore = None
        self.isSpoiler = kwargs.get('isSpoiler', False)
        if kwargs.get('text'):
            self.text = Markdown(**kwargs.get('text', {}))
        else:
            self.text = None
    def __eq__(self, other):
        if not isinstance(other, Goof):
            return False
        return self.id == other.id

class GoofCategory:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, GoofCategory):
            return False
        return self.id == other.id

class GoofCategoryWithGoofs:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = GoofCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('goofs'):
            self.goofs = GoofConnection(**kwargs.get('goofs', {}))
        else:
            self.goofs = None
    def __eq__(self, other):
        if not isinstance(other, GoofCategoryWithGoofs):
            return False
        return (self.category == other.category and self.goofs == other.goofs)


class GoofConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Goof(**node.get("node", {})))

class GranularDirective:
    def __init__(self, **kwargs):
        self.allow = kwargs.get('allow', False)
        self.id = kwargs.get('id', "")
    def __eq__(self, other):
        if not isinstance(other, GranularDirective):
            return False
        return self.id == other.id

class GuildAffiliationVerificationStatus:
    def __init__(self, **kwargs):
        if kwargs.get('company'):
            self.company = Company(**kwargs.get('company', {}))
        else:
            self.company = None
        self.isVerifiedByGuild = kwargs.get('isVerifiedByGuild', False)
    def __eq__(self, other):
        if not isinstance(other, GuildAffiliationVerificationStatus):
            return False
        return (self.company == other.company and self.isVerifiedByGuild == other.isVerifiedByGuild)


class GuildAffiliationVerificationStatusConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(GuildAffiliationVerificationStatus(**node.get("node", {})))

class GuildAffiliationVisibilityStatus:
    def __init__(self, **kwargs):
        if kwargs.get('company'):
            self.company = Company(**kwargs.get('company', {}))
        else:
            self.company = None
        self.visibility = kwargs.get('visibility', "")
    def __eq__(self, other):
        if not isinstance(other, GuildAffiliationVisibilityStatus):
            return False
        return (self.company == other.company and self.visibility == other.visibility)


class GuildAffiliationVisibilityStatusConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(GuildAffiliationVisibilityStatus(**node.get("node", {})))

class GuildMembershipDetail:
    def __init__(self, **kwargs):
        if kwargs.get('company'):
            self.company = Company(**kwargs.get('company', {}))
        else:
            self.company = None
        self.membershipId = kwargs.get('membershipId', "")
    def __eq__(self, other):
        if not isinstance(other, GuildMembershipDetail):
            return False
        return (self.company == other.company and self.membershipId == other.membershipId)

class GuildStatus:
    def __init__(self, **kwargs):
        self.isActraApprentice = kwargs.get('isActraApprentice', False)
        self.isNonUnion = kwargs.get('isNonUnion', False)
        self.isSagEligible = kwargs.get('isSagEligible', False)
    def __eq__(self, other):
        if not isinstance(other, GuildStatus):
            return False
        return (self.isActraApprentice == other.isActraApprentice and self.isNonUnion == other.isNonUnion and self.isSagEligible == other.isSagEligible)

class HelpLink:
    def __init__(self, **kwargs):
        if kwargs.get('label'):
            self.label = LocalizedString(**kwargs.get('label', {}))
        else:
            self.label = None
        self.url = kwargs.get('url', "")
    def __eq__(self, other):
        if not isinstance(other, HelpLink):
            return False
        return (self.label == other.label and self.url == other.url)

class Histogram:
    def __init__(self, **kwargs):
        if kwargs.get('demographic'):
            self.demographic = Demographic(**kwargs.get('demographic', {}))
        else:
            self.demographic = None
        if kwargs.get('histogramValues'):
            self.histogramValues = HistogramValues(**kwargs.get('histogramValues', {}))
        else:
            self.histogramValues = None
    def __eq__(self, other):
        if not isinstance(other, Histogram):
            return False
        return (self.demographic == other.demographic and self.histogramValues == other.histogramValues)

class HistogramValues:
    def __init__(self, **kwargs):
        self.rating = kwargs.get('rating', 0)
        self.voteCount = kwargs.get('voteCount', 0)
    def __eq__(self, other):
        if not isinstance(other, HistogramValues):
            return False
        return (self.rating == other.rating and self.voteCount == other.voteCount)

class Image:
    def __init__(self, **kwargs):
        if kwargs.get('caption'):
            self.caption = Markdown(**kwargs.get('caption', {}))
        else:
            self.caption = None
        self.copyright = kwargs.get('copyright', "")
        if kwargs.get('_correctionLink'):
            self._correctionLink = ContributionLink(**kwargs.get('_correctionLink', {}))
        else:
            self._correctionLink = None
        if kwargs.get('countries'):
            self.countries = DisplayableCountry(**kwargs.get('countries', {}))
        else:
            self.countries = None
        self.createdBy = kwargs.get('createdBy', "")
        if kwargs.get('createdOn'):
            self.createdOn = DisplayableDate(**kwargs.get('createdOn', {}))
        else:
            self.createdOn = None
        self.height = kwargs.get('height', 0)
        self.id = kwargs.get('id', "")
        if kwargs.get('languages'):
            self.languages = [DisplayableLanguage(**lang) for lang in kwargs.get('languages', [])]
        else:
            self.languages = None
        if kwargs.get('names'):
            self.names = Name(**kwargs.get('names', {}))
        else:
            self.names = None
        if kwargs.get('_reportingLink'):
            self._reportingLink = ContributionLink(**kwargs.get('_reportingLink', {}))
        else:
            self._reportingLink = None
        if kwargs.get('source'):
            self.source = Source(**kwargs.get('source', {}))
        else:
            self.source = None
        if kwargs.get('titles'):
            self.titles = Title(**kwargs.get('titles', {}))
        else:
            self.titles = None
        self.type = kwargs.get('type', "")
        self.url = kwargs.get('url', "")
        self.width = kwargs.get('width', 0)
    def __eq__(self, other):
        if not isinstance(other, Image):
            return False
        return self.id == other.id

class ImageAndLinkCallToAction:
    def __init__(self, **kwargs):
        if kwargs.get('action'):
            self.action = ActionLink(**kwargs.get('action', {}))
        else:
            self.action = None
        if kwargs.get('backgroundImage'):
            self.backgroundImage = CallToActionImage(**kwargs.get('backgroundImage', {}))
        else:
            self.backgroundImage = None
        self.resultId = kwargs.get('resultId', 0)
    def __eq__(self, other):
        if not isinstance(other, ImageAndLinkCallToAction):
            return False
        return (self.action == other.action and self.backgroundImage == other.backgroundImage and self.resultId == other.resultId)


class ImageConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Image(**node.get("node", {})))

class ImageEditParameters:
    def __init__(self, **kwargs):
        if kwargs.get('cropBox'):
            self.cropBox = CroppingParameters(**kwargs.get('cropBox', {}))
        else:
            self.cropBox = None
        self.rotation = kwargs.get('rotation', 0.0)
    def __eq__(self, other):
        if not isinstance(other, ImageEditParameters):
            return False
        return (self.cropBox == other.cropBox and self.rotation == other.rotation)

class ImageFacets:
    def __init__(self, **kwargs):
        if kwargs.get('galleries'):
            self.galleries = ImageGalleryConnection(**kwargs.get('galleries', {}))
        else:
            self.galleries = None
        if kwargs.get('names'):
            self.names = NameConnection(**kwargs.get('names', {}))
        else:
            self.names = None
        if kwargs.get('titles'):
            self.titles = TitleConnection(**kwargs.get('titles', {}))
        else:
            self.titles = None
        if kwargs.get('types'):
            self.types = ImageTypeFacet(**kwargs.get('types', {}))
        else:
            self.types = None
    def __eq__(self, other):
        if not isinstance(other, ImageFacets):
            return False
        return (self.galleries == other.galleries and self.names == other.names and self.titles == other.titles and self.types == other.types)

class ImageGallery:
    def __init__(self, **kwargs):
        self.galleryText = kwargs.get('galleryText', "")
        self.id = kwargs.get('id', "")
        if kwargs.get('images'):
            self.images = ImageConnection(**kwargs.get('images', {}))
        else:
            self.images = None
    def __eq__(self, other):
        if not isinstance(other, ImageGallery):
            return False
        return self.id == other.id


class ImageGalleryConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(ImageGallery(**node.get("node", {})))

class ImageRestriction:
    def __init__(self, **kwargs):
        if kwargs.get('explanations'):
            self.explanations = RestrictionExplanation(**kwargs.get('explanations', {}))
        else:
            self.explanations = None
        self.reasons = kwargs.get('reasons', "")
        self.restrictionReason = kwargs.get('restrictionReason', "")
        self.unrestrictedTotal = kwargs.get('unrestrictedTotal', 0)
    def __eq__(self, other):
        if not isinstance(other, ImageRestriction):
            return False
        return (self.explanations == other.explanations and self.reasons == other.reasons and self.restrictionReason == other.restrictionReason and self.unrestrictedTotal == other.unrestrictedTotal)

class ImageType:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.imageTypeId = kwargs.get('imageTypeId', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, ImageType):
            return False
        return self.id == other.id

class ImageTypeFacet:
    def __init__(self, **kwargs):
        self.total = kwargs.get('total', 0)
        if kwargs.get('type'):
            self.type = ImageType(**kwargs.get('type', {}))
        else:
            self.type = None
    def __eq__(self, other):
        if not isinstance(other, ImageTypeFacet):
            return False
        return (self.total == other.total and self.type == other.type)

class ImageTypeWithImages:
    def __init__(self, **kwargs):
        if kwargs.get('images'):
            self.images = ImageTypesConnection(**kwargs.get('images', {}))
        else:
            self.images = None
        if kwargs.get('imageType'):
            self.imageType = ImageType(**kwargs.get('imageType', {}))
        else:
            self.imageType = None
    def __eq__(self, other):
        if not isinstance(other, ImageTypeWithImages):
            return False
        return (self.images == other.images and self.imageType == other.imageType)


class ImageTypesConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(ImageType(**node.get("node", {})))

class Interest:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = InterestCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('description'):
            self.description = LocalizedMarkdown(**kwargs.get('description', {}))
        else:
            self.description = None
        if kwargs.get('engagementStatistics'):
            self.engagementStatistics = EngagementStatistics(**kwargs.get('engagementStatistics', {}))
        else:
            self.engagementStatistics = None
        self.id = kwargs.get('id', "")
        if kwargs.get('primaryImage'):
            self.primaryImage = Image(**kwargs.get('primaryImage', {}))
        else:
            self.primaryImage = None
        if kwargs.get('primaryText'):
            self.primaryText = InterestText(**kwargs.get('primaryText', {}))
        else:
            self.primaryText = None
        if kwargs.get('score'):
            self.score = InterestImportanceScore(**kwargs.get('score', {}))
        else:
            self.score = None
        if kwargs.get('secondaryText'):
            self.secondaryText = InterestText(**kwargs.get('secondaryText', {}))
        else:
            self.secondaryText = None
        if kwargs.get('similarInterests'):
            self.similarInterests = InterestConnection(**kwargs.get('similarInterests', {}))
        else:
            self.similarInterests = None
        self.visibilityLevel = kwargs.get('visibilityLevel', "")
    def __eq__(self, other):
        if not isinstance(other, Interest):
            return False
        return self.id == other.id

class InterestCategory:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('interests'):
            self.interests = InterestConnection(**kwargs.get('interests', {}))
        else:
            self.interests = None
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, InterestCategory):
            return False
        return self.id == other.id


class InterestConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Interest(**node.get("node", {})))

class InterestImportanceScore:
    def __init__(self, **kwargs):
        self.currentScore = kwargs.get('currentScore', 0)
    def __eq__(self, other):
        if not isinstance(other, InterestImportanceScore):
            return False
        return (self.currentScore == other.currentScore)

class InterestScore:
    def __init__(self, **kwargs):
        self.usersInterested = kwargs.get('usersInterested', 0)
        self.usersVoted = kwargs.get('usersVoted', 0)
    def __eq__(self, other):
        if not isinstance(other, InterestScore):
            return False
        return (self.usersInterested == other.usersInterested and self.usersVoted == other.usersVoted)

class InterestText:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, InterestText):
            return False
        return self.id == other.id

class IsElementInList:
    def __init__(self, **kwargs):
        self.isElementInList = kwargs.get('isElementInList', False)
        self.itemElementId = kwargs.get('itemElementId', "")
        self.itemIds = kwargs.get('itemIds', "")
    def __eq__(self, other):
        if not isinstance(other, IsElementInList):
            return False
        return (self.isElementInList == other.isElementInList and self.itemElementId == other.itemElementId and self.itemIds == other.itemIds)

class Keyword:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = KeywordCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        self.id = kwargs.get('id', "")
        if kwargs.get('text'):
            self.text = KeywordText(**kwargs.get('text', {}))
        else:
            self.text = None
        if kwargs.get('titles'):
            self.titles = TitleConnection(**kwargs.get('titles', {}))
        else:
            self.titles = None
    def __eq__(self, other):
        if not isinstance(other, Keyword):
            return False
        return self.id == other.id

class KeywordCategory:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
    def __eq__(self, other):
        if not isinstance(other, KeywordCategory):
            return False
        return self.id == other.id

class KeywordMetadata:
    def __init__(self, **kwargs):
        if kwargs.get('keywordCategories'):
            self.keywordCategories = KeywordCategory(**kwargs.get('keywordCategories', {}))
        else:
            self.keywordCategories = None
    def __eq__(self, other):
        if not isinstance(other, KeywordMetadata):
            return False
        return (self.keywordCategories == other.keywordCategories)

class KeywordText:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, KeywordText):
            return False
        return self.id == other.id

class KnownForV2:
    def __init__(self, **kwargs):
        if kwargs.get('credits'):
            self.credits = CreditV2(**kwargs.get('credits', {}))
        else:
            self.credits = None
        if kwargs.get('restriction'):
            self.restriction = NameKnownForRestriction(**kwargs.get('restriction', {}))
        else:
            self.restriction = None
    def __eq__(self, other):
        if not isinstance(other, KnownForV2):
            return False
        return (self.credits == other.credits and self.restriction == other.restriction)

class Laboratories:
    def __init__(self, **kwargs):
        if kwargs.get('items'):
            self.items = Laboratory(**kwargs.get('items', {}))
        else:
            self.items = None
        if kwargs.get('restriction'):
            self.restriction = TechnicalSpecificationsRestriction(**kwargs.get('restriction', {}))
        else:
            self.restriction = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, Laboratories):
            return False
        return (self.items == other.items and self.restriction == other.restriction and self.total == other.total)

class Laboratory:
    def __init__(self, **kwargs):
        if kwargs.get('attributes'):
            self.attributes = [DisplayableAttribute(**attr) for attr in kwargs.get('attributes', [])]
        else:
            self.attributes = None
        self.creditedAs = kwargs.get('creditedAs', "")
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableTechnicalSpecificationProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.isUncredited = kwargs.get('isUncredited', False)
        self.laboratory = kwargs.get('laboratory', "")
    def __eq__(self, other):
        if not isinstance(other, Laboratory):
            return False
        return (self.attributes == other.attributes and self.creditedAs == other.creditedAs and self.displayableProperty == other.displayableProperty and self.isUncredited == other.isUncredited and self.laboratory == other.laboratory)

class Language:
    def __init__(self, **kwargs):
        self.language = kwargs.get('language', "")
    def __eq__(self, other):
        if not isinstance(other, Language):
            return False
        return (self.language == other.language)

class LengthMeasurement:
    def __init__(self, **kwargs):
        self.unit = kwargs.get('unit', "")
        self.value = kwargs.get('value', 0.0)
    def __eq__(self, other):
        if not isinstance(other, LengthMeasurement):
            return False
        return (self.unit == other.unit and self.value == other.value)

class LinkCallToAction:
    def __init__(self, **kwargs):
        if kwargs.get('action'):
            self.action = ActionLink(**kwargs.get('action', {}))
        else:
            self.action = None
        self.resultId = kwargs.get('resultId', 0)
    def __eq__(self, other):
        if not isinstance(other, LinkCallToAction):
            return False
        return (self.action == other.action and self.resultId == other.resultId)

class LinkedAuthProvider:
    def __init__(self, **kwargs):
        if kwargs.get('deprecationMessage'):
            self.deprecationMessage = AuthProviderDeprecationMessage(**kwargs.get('deprecationMessage', {}))
        else:
            self.deprecationMessage = None
        self.type = kwargs.get('type', "")
    def __eq__(self, other):
        if not isinstance(other, LinkedAuthProvider):
            return False
        return (self.deprecationMessage == other.deprecationMessage and self.type == other.type)

class List:
    def __init__(self, **kwargs):
        if kwargs.get('areElementsInList'):
            self.areElementsInList = IsElementInList(**kwargs.get('areElementsInList', {}))
        else:
            self.areElementsInList = None
        if kwargs.get('author'):
            self.author = UserProfile(**kwargs.get('author', {}))
        else:
            self.author = None
        self.createdDate = kwargs.get('createdDate', "")
        if kwargs.get('description'):
            self.description = ListDescription(**kwargs.get('description', {}))
        else:
            self.description = None
        self.id = kwargs.get('id', "")
        self.isElementInList = kwargs.get('isElementInList', False)
        self.isPredefined = kwargs.get('isPredefined', False)
        if kwargs.get('items'):
            self.items = ListConnection(**kwargs.get('items', {}))
        else:
            self.items = None
        self.lastModifiedDate = kwargs.get('lastModifiedDate', "")
        if kwargs.get('listClass'):
            self.listClass = ListClass(**kwargs.get('listClass', {}))
        else:
            self.listClass = None
        if kwargs.get('listInteractionCounts'):
            self.listInteractionCounts = ListInteractionCounts(**kwargs.get('listInteractionCounts', {}))
        else:
            self.listInteractionCounts = None
        if kwargs.get('listType'):
            self.listType = ListType(**kwargs.get('listType', {}))
        else:
            self.listType = None
        if kwargs.get('name'):
            self.name = ListName(**kwargs.get('name', {}))
        else:
            self.name = None
        if kwargs.get('nameListItemSearch'):
            self.nameListItemSearch = SearchFacetConnection(**kwargs.get('nameListItemSearch', {}))
        else:
            self.nameListItemSearch = None
        if kwargs.get('primaryImage'):
            self.primaryImage = ListPrimaryImage(**kwargs.get('primaryImage', {}))
        else:
            self.primaryImage = None
        if kwargs.get('titleListItemSearch'):
            self.titleListItemSearch = ListItemSearchNodeConnection(**kwargs.get('titleListItemSearch', {}))
        else:
            self.titleListItemSearch = None
        if kwargs.get('visibility'):
            self.visibility = ListVisibility(**kwargs.get('visibility', {}))
        else:
            self.visibility = None
    def __eq__(self, other):
        if not isinstance(other, List):
            return False
        return self.id == other.id

class ListClass:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('name'):
            self.name = ListClassName(**kwargs.get('name', {}))
        else:
            self.name = None
    def __eq__(self, other):
        if not isinstance(other, ListClass):
            return False
        return self.id == other.id

class ListClassName:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, ListClassName):
            return False
        return self.id == other.id


class ListConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(List(**node.get("node", {})))

class ListDescription:
    def __init__(self, **kwargs):
        if kwargs.get('originalText'):
            self.originalText = Markdown(**kwargs.get('originalText', {}))
        else:
            self.originalText = None
    def __eq__(self, other):
        if not isinstance(other, ListDescription):
            return False
        return (self.originalText == other.originalText)

class ListFieldAttributeMetadata:
    def __init__(self, **kwargs):
        if kwargs.get('listDescription'):
            self.listDescription = ListTextFieldMetadata(**kwargs.get('listDescription', {}))
        else:
            self.listDescription = None
        if kwargs.get('listItemDescription'):
            self.listItemDescription = ListTextFieldMetadata(**kwargs.get('listItemDescription', {}))
        else:
            self.listItemDescription = None
        if kwargs.get('listName'):
            self.listName = ListTextFieldMetadata(**kwargs.get('listName', {}))
        else:
            self.listName = None
    def __eq__(self, other):
        if not isinstance(other, ListFieldAttributeMetadata):
            return False
        return (self.listDescription == other.listDescription and self.listItemDescription == other.listItemDescription and self.listName == other.listName)

class ListInteractionCounts:
    def __init__(self, **kwargs):
        self.clicks = kwargs.get('clicks', 0)
        self.listId = kwargs.get('listId', "")
        self.timeRange = kwargs.get('timeRange', "")
        self.views = kwargs.get('views', 0)
    def __eq__(self, other):
        if not isinstance(other, ListInteractionCounts):
            return False
        return (self.clicks == other.clicks and self.listId == other.listId and self.timeRange == other.timeRange and self.views == other.views)

class ListItemNode:
    def __init__(self, **kwargs):
        self.absolutePosition = kwargs.get('absolutePosition', 0)
        self.createdDate = kwargs.get('createdDate', "")
        if kwargs.get('description'):
            self.description = ListDescription(**kwargs.get('description', {}))
        else:
            self.description = None
        self.itemId = kwargs.get('itemId', "")
        self.lastModifiedDate = kwargs.get('lastModifiedDate', "")
    def __eq__(self, other):
        if not isinstance(other, ListItemNode):
            return False
        return (self.absolutePosition == other.absolutePosition and self.createdDate == other.createdDate and self.description == other.description and self.itemId == other.itemId and self.lastModifiedDate == other.lastModifiedDate)

class ListItemSearchNode:
    def __init__(self, **kwargs):
        self.absolutePosition = kwargs.get('absolutePosition', 0)
        self.createdDate = kwargs.get('createdDate', "")
        if kwargs.get('description'):
            self.description = ListDescription(**kwargs.get('description', {}))
        else:
            self.description = None
        self.itemId = kwargs.get('itemId', "")
        self.lastModifiedDate = kwargs.get('lastModifiedDate', "")
    def __eq__(self, other):
        if not isinstance(other, ListItemSearchNode):
            return False
        return (self.absolutePosition == other.absolutePosition and self.createdDate == other.createdDate and self.description == other.description and self.itemId == other.itemId and self.lastModifiedDate == other.lastModifiedDate)


class ListItemSearchNodeConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(ListItemSearchNode(**node.get("node", {})))

class ListName:
    def __init__(self, **kwargs):
        self.originalText = kwargs.get('originalText', "")
    def __eq__(self, other):
        if not isinstance(other, ListName):
            return False
        return (self.originalText == other.originalText)

class ListPrimaryImage:
    def __init__(self, **kwargs):
        if kwargs.get('image'):
            self.image = Image(**kwargs.get('image', {}))
        else:
            self.image = None
    def __eq__(self, other):
        if not isinstance(other, ListPrimaryImage):
            return False
        return (self.image == other.image)

class ListTextFieldMetadata:
    def __init__(self, **kwargs):
        self.maxCharacters = kwargs.get('maxCharacters', 0)
    def __eq__(self, other):
        if not isinstance(other, ListTextFieldMetadata):
            return False
        return (self.maxCharacters == other.maxCharacters)

class ListType:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
    def __eq__(self, other):
        if not isinstance(other, ListType):
            return False
        return self.id == other.id

class ListVisibility:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('name'):
            self.name = ListVisibilityName(**kwargs.get('name', {}))
        else:
            self.name = None
    def __eq__(self, other):
        if not isinstance(other, ListVisibility):
            return False
        return self.id == other.id

class ListVisibilityName:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, ListVisibilityName):
            return False
        return self.id == other.id

class LocalizedDisplayableCount:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, LocalizedDisplayableCount):
            return False
        return self.id == other.id

class LocalizedDisplayableCountry:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, LocalizedDisplayableCountry):
            return False
        return self.id == other.id

class LocalizedDisplayableEpisodeNumber:
    def __init__(self, **kwargs):
        if kwargs.get('displayableProperty'):
            self.displayableProperty = EpisodeNumberDisplayableProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.episodeNumber = kwargs.get('episodeNumber', "")
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, LocalizedDisplayableEpisodeNumber):
            return False
        return self.id == other.id

class LocalizedDisplayableEpisodeYear:
    def __init__(self, **kwargs):
        if kwargs.get('displayableProperty'):
            self.displayableProperty = YearDisplayableProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
        self.year = kwargs.get('year', "")
    def __eq__(self, other):
        if not isinstance(other, LocalizedDisplayableEpisodeYear):
            return False
        return self.id == other.id


class LocalizedDisplayableEpisodeYearConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(LocalizedDisplayableEpisodeYear(**node.get("node", {})))

class LocalizedDisplayableSeason:
    def __init__(self, **kwargs):
        if kwargs.get('displayableProperty'):
            self.displayableProperty = SeasonValueDisplayableProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.season = kwargs.get('season', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, LocalizedDisplayableSeason):
            return False
        return self.id == other.id


class LocalizedDisplayableSeasonConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(LocalizedDisplayableSeason(**node.get("node", {})))

class LocalizedMarkdown:
    def __init__(self, **kwargs):
        self.language = kwargs.get('language', "")
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"LocalizedMarkdown(value={self.value}, language={self.language})"
    def __eq__(self, other):
        if not isinstance(other, LocalizedMarkdown):
            return False
        return (self.language == other.language and self.value == other.value)

class LocalizedString:
    def __init__(self, **kwargs):
        self.language = kwargs.get('language', "")
        self.value = kwargs.get('value', "")
    def __str__(self):
        return self.value
    def __repr__(self):
        return f"LocalizedString(language={self.language}, value={self.value})"
    def __eq__(self, other):
        if not isinstance(other, LocalizedString):
            return False
        return (self.language == other.language and self.value == other.value)

class Location:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __str__(self):
        return self.text if self.text else self.id
    def __repr__(self):
        return f"Location(id={self.id}, language={self.language}, text={self.text})"
    def __eq__(self, other):
        if not isinstance(other, Location):
            return False
        return self.id == other.id

class LogoutRedirectURLOutput:
    def __init__(self, **kwargs):
        self.redirectURL = kwargs.get('redirectURL', "")
    def __eq__(self, other):
        if not isinstance(other, LogoutRedirectURLOutput):
            return False
        return (self.redirectURL == other.redirectURL)

class MainSearchNode:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
    def __eq__(self, other):
        if not isinstance(other, MainSearchNode):
            return False
        return self.id == other.id

class ManagedClient:
    def __init__(self, **kwargs):
        if kwargs.get('client'):
            self.client = Name(**kwargs.get('client', {}))
        else:
            self.client = None
        self.status = kwargs.get('status', "")
    def __eq__(self, other):
        if not isinstance(other, ManagedClient):
            return False
        return (self.client == other.client and self.status == other.status)

class ManagedCompanyData:
    def __init__(self, **kwargs):
        if kwargs.get('knownFor'):
            self.knownFor = ManagedCompanyKnownForGroup(**kwargs.get('knownFor', {}))
        else:
            self.knownFor = None
    def __eq__(self, other):
        if not isinstance(other, ManagedCompanyData):
            return False
        return (self.knownFor == other.knownFor)

class ManagedCompanyKeyStaffCategory:
    def __init__(self, **kwargs):
        if kwargs.get('staff'):
            self.staff = CompanyKeyStaffConnection(**kwargs.get('staff', {}))
        else:
            self.staff = None
        self.status = kwargs.get('status', "")
    def __eq__(self, other):
        if not isinstance(other, ManagedCompanyKeyStaffCategory):
            return False
        return (self.staff == other.staff and self.status == other.status)

class ManagedCompanyKeyStaffGroup:
    def __init__(self, **kwargs):
        if kwargs.get('automatic'):
            self.automatic = ManagedCompanyKeyStaffCategory(**kwargs.get('automatic', {}))
        else:
            self.automatic = None
        if kwargs.get('automaticHistory'):
            self.automaticHistory = ManagedCompanyKeyStaffHistory(**kwargs.get('automaticHistory', {}))
        else:
            self.automaticHistory = None
        if kwargs.get('custom'):
            self.custom = ManagedCompanyKeyStaffCategory(**kwargs.get('custom', {}))
        else:
            self.custom = None
        if kwargs.get('customHistory'):
            self.customHistory = ManagedCompanyKeyStaffHistory(**kwargs.get('customHistory', {}))
        else:
            self.customHistory = None
        self.sourcePreference = kwargs.get('sourcePreference', "")
    def __eq__(self, other):
        if not isinstance(other, ManagedCompanyKeyStaffGroup):
            return False
        return (self.automatic == other.automatic and self.automaticHistory == other.automaticHistory and self.custom == other.custom and self.customHistory == other.customHistory and self.sourcePreference == other.sourcePreference)

class ManagedCompanyKeyStaffHistory:
    def __init__(self, **kwargs):
        if kwargs.get('keyStaffHistory'):
            self.keyStaffHistory = ManagedCompanyKeyStaffHistoryConnection(**kwargs.get('keyStaffHistory', {}))
        else:
            self.keyStaffHistory = None
    def __eq__(self, other):
        if not isinstance(other, ManagedCompanyKeyStaffHistory):
            return False
        return (self.keyStaffHistory == other.keyStaffHistory)


class ManagedCompanyKeyStaffHistoryConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(ManagedCompanyKeyStaffHistory(**node.get("node", {})))

class ManagedCompanyKnownForClientCategory:
    def __init__(self, **kwargs):
        if kwargs.get('clients'):
            self.clients = CompanyKnownForClientConnection(**kwargs.get('clients', {}))
        else:
            self.clients = None
        self.status = kwargs.get('status', "")
    def __eq__(self, other):
        if not isinstance(other, ManagedCompanyKnownForClientCategory):
            return False
        return (self.clients == other.clients and self.status == other.status)

class ManagedCompanyKnownForClientGroup:
    def __init__(self, **kwargs):
        if kwargs.get('automatic'):
            self.automatic = ManagedCompanyKnownForClientCategory(**kwargs.get('automatic', {}))
        else:
            self.automatic = None
        if kwargs.get('automaticHistory'):
            self.automaticHistory = ManagedCompanyKnownForClientHistory(**kwargs.get('automaticHistory', {}))
        else:
            self.automaticHistory = None
        if kwargs.get('custom'):
            self.custom = ManagedCompanyKnownForClientCategory(**kwargs.get('custom', {}))
        else:
            self.custom = None
        if kwargs.get('customHistory'):
            self.customHistory = ManagedCompanyKnownForClientHistory(**kwargs.get('customHistory', {}))
        else:
            self.customHistory = None
        self.sourcePreference = kwargs.get('sourcePreference', "")
    def __eq__(self, other):
        if not isinstance(other, ManagedCompanyKnownForClientGroup):
            return False
        return (self.automatic == other.automatic and self.automaticHistory == other.automaticHistory and self.custom == other.custom and self.customHistory == other.customHistory and self.sourcePreference == other.sourcePreference)

class ManagedCompanyKnownForClientHistory:
    def __init__(self, **kwargs):
        if kwargs.get('clientHistory'):
            self.clientHistory = ManagedCompanyKnownForClientHistoryConnection(**kwargs.get('clientHistory', {}))
        else:
            self.clientHistory = None
    def __eq__(self, other):
        if not isinstance(other, ManagedCompanyKnownForClientHistory):
            return False
        return (self.clientHistory == other.clientHistory)


class ManagedCompanyKnownForClientHistoryConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(ManagedCompanyKnownForClientHistory(**node.get("node", {})))

class ManagedCompanyKnownForClientVersion:
    def __init__(self, **kwargs):
        if kwargs.get('clients'):
            self.clients = CompanyKnownForClientConnection(**kwargs.get('clients', {}))
        else:
            self.clients = None
        self.createdDate = kwargs.get('createdDate', "")
        if kwargs.get('modifiedBy'):
            self.modifiedBy = ModifiedBy(**kwargs.get('modifiedBy', {}))
        else:
            self.modifiedBy = None
        self.status = kwargs.get('status', "")
        self.versionNumber = kwargs.get('versionNumber', 0)
    def __eq__(self, other):
        if not isinstance(other, ManagedCompanyKnownForClientVersion):
            return False
        return (self.clients == other.clients and self.createdDate == other.createdDate and self.modifiedBy == other.modifiedBy and self.status == other.status and self.versionNumber == other.versionNumber)

class ManagedCompanyKnownForGroup:
    def __init__(self, **kwargs):
        if kwargs.get('keyStaff'):
            self.keyStaff = ManagedCompanyKeyStaffGroup(**kwargs.get('keyStaff', {}))
        else:
            self.keyStaff = None
        if kwargs.get('knownForClient'):
            self.knownForClient = ManagedCompanyKnownForClientGroup(**kwargs.get('knownForClient', {}))
        else:
            self.knownForClient = None
        if kwargs.get('knownForTitle'):
            self.knownForTitle = ManagedCompanyKnownForTitleGroup(**kwargs.get('knownForTitle', {}))
        else:
            self.knownForTitle = None
    def __eq__(self, other):
        if not isinstance(other, ManagedCompanyKnownForGroup):
            return False
        return (self.keyStaff == other.keyStaff and self.knownForClient == other.knownForClient and self.knownForTitle == other.knownForTitle)

class ManagedCompanyKnownForKeyStaffVersion:
    def __init__(self, **kwargs):
        self.createdDate = kwargs.get('createdDate', "")
        if kwargs.get('modifiedBy'):
            self.modifiedBy = ModifiedBy(**kwargs.get('modifiedBy', {}))
        else:
            self.modifiedBy = None
        if kwargs.get('staff'):
            self.staff = CompanyKeyStaffConnection(**kwargs.get('staff', {}))
        else:
            self.staff = None
        self.status = kwargs.get('status', "")
        self.versionNumber = kwargs.get('versionNumber', 0)
    def __eq__(self, other):
        if not isinstance(other, ManagedCompanyKnownForKeyStaffVersion):
            return False
        return (self.createdDate == other.createdDate and self.modifiedBy == other.modifiedBy and self.staff == other.staff and self.status == other.status and self.versionNumber == other.versionNumber)

class ManagedCompanyKnownForTitleCategory:
    def __init__(self, **kwargs):
        self.status = kwargs.get('status', "")
        if kwargs.get('titles'):
            self.titles = CompanyKnownForTitleConnection(**kwargs.get('titles', {}))
        else:
            self.titles = None
    def __eq__(self, other):
        if not isinstance(other, ManagedCompanyKnownForTitleCategory):
            return False
        return (self.status == other.status and self.titles == other.titles)

class ManagedCompanyKnownForTitleGroup:
    def __init__(self, **kwargs):
        if kwargs.get('automatic'):
            self.automatic = ManagedCompanyKnownForTitleCategory(**kwargs.get('automatic', {}))
        else:
            self.automatic = None
        if kwargs.get('automaticHistory'):
            self.automaticHistory = ManagedCompanyKnownForTitleHistory(**kwargs.get('automaticHistory', {}))
        else:
            self.automaticHistory = None
        if kwargs.get('custom'):
            self.custom = ManagedCompanyKnownForTitleCategory(**kwargs.get('custom', {}))
        else:
            self.custom = None
        if kwargs.get('customHistory'):
            self.customHistory = ManagedCompanyKnownForTitleHistory(**kwargs.get('customHistory', {}))
        else:
            self.customHistory = None
        self.sourcePreference = kwargs.get('sourcePreference', "")
    def __eq__(self, other):
        if not isinstance(other, ManagedCompanyKnownForTitleGroup):
            return False
        return (self.automatic == other.automatic and self.automaticHistory == other.automaticHistory and self.custom == other.custom and self.customHistory == other.customHistory and self.sourcePreference == other.sourcePreference)

class ManagedCompanyKnownForTitleHistory:
    def __init__(self, **kwargs):
        if kwargs.get('titleHistory'):
            self.titleHistory = ManagedCompanyKnownForTitleHistoryConnection(**kwargs.get('titleHistory', {}))
        else:
            self.titleHistory = None
    def __eq__(self, other):
        if not isinstance(other, ManagedCompanyKnownForTitleHistory):
            return False
        return (self.titleHistory == other.titleHistory)


class ManagedCompanyKnownForTitleHistoryConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(ManagedCompanyKnownForTitleHistory(**node.get("node", {})))

class ManagedCompanyKnownForTitleVersion:
    def __init__(self, **kwargs):
        self.createdDate = kwargs.get('createdDate', "")
        if kwargs.get('modifiedBy'):
            self.modifiedBy = ModifiedBy(**kwargs.get('modifiedBy', {}))
        else:
            self.modifiedBy = None
        self.status = kwargs.get('status', "")
        if kwargs.get('titles'):
            self.titles = CompanyKnownForTitleConnection(**kwargs.get('titles', {}))
        else:
            self.titles = None
        self.versionNumber = kwargs.get('versionNumber', 0)
    def __eq__(self, other):
        if not isinstance(other, ManagedCompanyKnownForTitleVersion):
            return False
        return (self.createdDate == other.createdDate and self.modifiedBy == other.modifiedBy and self.status == other.status and self.titles == other.titles and self.versionNumber == other.versionNumber)

class ManagingRepresentative:
    def __init__(self, **kwargs):
        if kwargs.get('manager'):
            self.manager = Name(**kwargs.get('manager', {}))
        else:
            self.manager = None
        self.status = kwargs.get('status', "")
    def __eq__(self, other):
        if not isinstance(other, ManagingRepresentative):
            return False
        return (self.manager == other.manager and self.status == other.status)

class Markdown:
    def __init__(self, **kwargs):
        self.expandedMarkdown = kwargs.get('expandedMarkdown', "")
        self.markdown = kwargs.get('markdown', "")
        self.plaidHtml = kwargs.get('plaidHtml', "")
        self.plainText = kwargs.get('plainText', "")
    def __str__(self):
        return self.expandedMarkdown or self.markdown or self.plainText or ""
    def __repr__(self):
        return f"Markdown(expandedMarkdown={self.expandedMarkdown}, markdown={self.markdown}, plaidHtml={self.plaidHtml}, plainText={self.plainText})"
    def __eq__(self, other):
        if not isinstance(other, Markdown):
            return False
        return (self.expandedMarkdown == other.expandedMarkdown and self.markdown == other.markdown and self.plaidHtml == other.plaidHtml and self.plainText == other.plainText)

class MarkdownEntity:
    def __init__(self, **kwargs):
        if kwargs.get('markdown'):
            self.markdown = Markdown(**kwargs.get('markdown', {}))
        else:
            self.markdown = None
    def __str__(self):
        return str(self.markdown) if self.markdown else ""
    def __repr__(self):
        return self.markdown.__repr__() if self.markdown else "MarkdownEntity(markdown=None)"
    def __eq__(self, other):
        if not isinstance(other, MarkdownEntity):
            return False
        return (self.markdown == other.markdown)

class MarkdownSlotCallToAction:
    def __init__(self, **kwargs):
        if kwargs.get('markdown'):
            self.markdown = LocalizedMarkdown(**kwargs.get('markdown', {}))
        else:
            self.markdown = None
        self.resultId = kwargs.get('resultId', 0)
    def __eq__(self, other):
        if not isinstance(other, MarkdownSlotCallToAction):
            return False
        return (self.markdown == other.markdown and self.resultId == other.resultId)

class MediaServiceImage:
    def __init__(self, **kwargs):
        if kwargs.get('accessibilityText'):
            self.accessibilityText = CommonLocalizedDisplayableConcept(**kwargs.get('accessibilityText', {}))
        else:
            self.accessibilityText = None
        self.fileType = kwargs.get('fileType', "")
        self.height = kwargs.get('height', 0)
        self.url = kwargs.get('url', "")
        self.width = kwargs.get('width', 0)
    def __eq__(self, other):
        if not isinstance(other, MediaServiceImage):
            return False
        return (self.accessibilityText == other.accessibilityText and self.fileType == other.fileType and self.height == other.height and self.url == other.url and self.width == other.width)

class Metacritic:
    def __init__(self, **kwargs):
        if kwargs.get('metascore'):
            self.metascore = Metascore(**kwargs.get('metascore', {}))
        else:
            self.metascore = None
        if kwargs.get('reviews'):
            self.reviews = MetacriticReviewConnection(**kwargs.get('reviews', {}))
        else:
            self.reviews = None
        self.url = kwargs.get('url', "")
    def __eq__(self, other):
        if not isinstance(other, Metacritic):
            return False
        return (self.metascore == other.metascore and self.reviews == other.reviews and self.url == other.url)

class MetacriticReview:
    def __init__(self, **kwargs):
        if kwargs.get('quote'):
            self.quote = LocalizedString(**kwargs.get('quote', {}))
        else:
            self.quote = None
        self.reviewer = kwargs.get('reviewer', "")
        self.score = kwargs.get('score', 0)
        self.site = kwargs.get('site', "")
        self.url = kwargs.get('url', "")
    def __eq__(self, other):
        if not isinstance(other, MetacriticReview):
            return False
        return (self.quote == other.quote and self.reviewer == other.reviewer and self.score == other.score and self.site == other.site and self.url == other.url)


class MetacriticReviewConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(MetacriticReview(**node.get("node", {})))

class Metascore:
    def __init__(self, **kwargs):
        self.reviewCount = kwargs.get('reviewCount', 0)
        self.score = kwargs.get('score', 0)
    def __eq__(self, other):
        if not isinstance(other, Metascore):
            return False
        return (self.reviewCount == other.reviewCount and self.score == other.score)

class MeterEvent:
    def __init__(self, **kwargs):
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
        if kwargs.get('type'):
            self.type = LocalizedString(**kwargs.get('type', {}))
        else:
            self.type = None
    def __eq__(self, other):
        if not isinstance(other, MeterEvent):
            return False
        return (self.title == other.title and self.type == other.type)

class MeterRankChange:
    def __init__(self, **kwargs):
        self.changeDirection = kwargs.get('changeDirection', "")
        self.difference = kwargs.get('difference', 0)
    def __eq__(self, other):
        if not isinstance(other, MeterRankChange):
            return False
        return (self.changeDirection == other.changeDirection and self.difference == other.difference)

class MeterRankingHistoryEntry:
    def __init__(self, **kwargs):
        self.date = kwargs.get('date', "")
        if kwargs.get('events'):
            self.events = MeterEvent(**kwargs.get('events', {}))
        else:
            self.events = None
        self.rank = kwargs.get('rank', 0)
    def __eq__(self, other):
        if not isinstance(other, MeterRankingHistoryEntry):
            return False
        return (self.date == other.date and self.events == other.events and self.rank == other.rank)

class MeterRestriction:
    def __init__(self, **kwargs):
        if kwargs.get('explanations'):
            self.explanations = RestrictionExplanation(**kwargs.get('explanations', {}))
        else:
            self.explanations = None
        self.reasons = kwargs.get('reasons', "")
        self.restrictionReason = kwargs.get('restrictionReason', "")
    def __eq__(self, other):
        if not isinstance(other, MeterRestriction):
            return False
        return (self.explanations == other.explanations and self.reasons == other.reasons and self.restrictionReason == other.restrictionReason)

class MigrationTestOutput:
    def __init__(self, **kwargs):
        self.result = kwargs.get('result', "")
    def __eq__(self, other):
        if not isinstance(other, MigrationTestOutput):
            return False
        return (self.result == other.result)

class ModifiedBy:
    def __init__(self, **kwargs):
        self.role = kwargs.get('role', "")
    def __eq__(self, other):
        if not isinstance(other, ModifiedBy):
            return False
        return (self.role == other.role)

class Money:
    def __init__(self, **kwargs):
        self.amount = kwargs.get('amount', 0.0)
        self.currency = kwargs.get('currency', "")
    def __str__(self):
        if self.amount and self.currency:
            return f"{self.amount} {self.currency}"
        if self.amount:
            return str(self.amount)
        return ""
    def __float__(self):
        return float(self.amount) if self.amount else 0.0
    def __int__(self):
        return int(self.amount) if self.amount else 0
    def __repr__(self):
        return f"Money(amount={self.amount}, currency={self.currency})"
    def __eq__(self, other):
        if not isinstance(other, Money):
            return False
        return (self.amount == other.amount and self.currency == other.currency)

class MultiLinkCallToAction:
    def __init__(self, **kwargs):
        if kwargs.get('abbreviatedActions'):
            self.abbreviatedActions = NamedActionLink(**kwargs.get('abbreviatedActions', {}))
        else:
            self.abbreviatedActions = None
        self.resultId = kwargs.get('resultId', 0)
        if kwargs.get('standardActions'):
            self.standardActions = NamedActionLink(**kwargs.get('standardActions', {}))
        else:
            self.standardActions = None
    def __eq__(self, other):
        if not isinstance(other, MultiLinkCallToAction):
            return False
        return (self.abbreviatedActions == other.abbreviatedActions and self.resultId == other.resultId and self.standardActions == other.standardActions)

class Name:
    def __init__(self, **kwargs):
        if kwargs.get('age'):
            self.age = AgeDetails(**kwargs.get('age', {}))
        else:
            self.age = None
        if kwargs.get('akas'):
            self.akas = NameAkaConnection(**kwargs.get('akas', {}))
        else:
            self.akas = None
        if kwargs.get('alexaTopQuestions'):
            self.alexaTopQuestions = AlexaQuestionConnection(**kwargs.get('alexaTopQuestions', {}))
        else:
            self.alexaTopQuestions = None
        if kwargs.get('autoSelectedProfessions'):
            self.autoSelectedProfessions = NameProfession(**kwargs.get('autoSelectedProfessions', {}))
        else:
            self.autoSelectedProfessions = None
        if kwargs.get('awardNominations'):
            self.awardNominations = AwardNominationConnection(**kwargs.get('awardNominations', {}))
        else:
            self.awardNominations = None
        if kwargs.get('bio'):
            self.bio = NameBio(**kwargs.get('bio', {}))
        else:
            self.bio = None
        if kwargs.get('bios'):
            self.bios = NameBiosConnection(**kwargs.get('bios', {}))
        else:
            self.bios = None
        if kwargs.get('birthDate'):
            self.birthDate = DisplayableDate(**kwargs.get('birthDate', {}))
        else:
            self.birthDate = None
        if kwargs.get('birthLocation'):
            self.birthLocation = DisplayableLocation(**kwargs.get('birthLocation', {}))
        else:
            self.birthLocation = None
        if kwargs.get('birthName'):
            self.birthName = BirthName(**kwargs.get('birthName', {}))
        else:
            self.birthName = None
        self.canonicalUrl = kwargs.get('canonicalUrl', "")
        if kwargs.get('clients'):
            self.clients = NameRepresentationConnection(**kwargs.get('clients', {}))
        else:
            self.clients = None
        if kwargs.get('contentWarnings'):
            self.contentWarnings = ContentWarnings(**kwargs.get('contentWarnings', {}))
        else:
            self.contentWarnings = None
        if kwargs.get('creditCategories'):
            self.creditCategories = NameCreditCategoryWithCredits(**kwargs.get('creditCategories', {}))
        else:
            self.creditCategories = None
        if kwargs.get('creditedWithNames'):
            self.creditedWithNames = CreditedWithNamesConnection(**kwargs.get('creditedWithNames', {}))
        else:
            self.creditedWithNames = None
        if kwargs.get('creditGroupings'):
            self.creditGroupings = CreditGroupingConnection(**kwargs.get('creditGroupings', {}))
        else:
            self.creditGroupings = None
        if kwargs.get('credits'):
            self.credits = CreditConnection(**kwargs.get('credits', {}))
        else:
            self.credits = None
        if kwargs.get('creditSummary'):
            self.creditSummary = NameCreditSummary(**kwargs.get('creditSummary', {}))
        else:
            self.creditSummary = None
        if kwargs.get('creditsV2'):
            self.creditsV2 = CreditV2Connection(**kwargs.get('creditsV2', {}))
        else:
            self.creditsV2 = None
        if kwargs.get('currentProfessions'):
            self.currentProfessions = NameProfession(**kwargs.get('currentProfessions', {}))
        else:
            self.currentProfessions = None
        if kwargs.get('deathCause'):
            self.deathCause = DisplayableNameDeathCause(**kwargs.get('deathCause', {}))
        else:
            self.deathCause = None
        if kwargs.get('deathDate'):
            self.deathDate = DisplayableDate(**kwargs.get('deathDate', {}))
        else:
            self.deathDate = None
        if kwargs.get('deathLocation'):
            self.deathLocation = DisplayableLocation(**kwargs.get('deathLocation', {}))
        else:
            self.deathLocation = None
        self.deathStatus = kwargs.get('deathStatus', "")
        if kwargs.get('demographicData'):
            self.demographicData = DemographicDataItem(**kwargs.get('demographicData', {}))
        else:
            self.demographicData = None
        if kwargs.get('directContact'):
            self.directContact = DirectContactDetails(**kwargs.get('directContact', {}))
        else:
            self.directContact = None
        if kwargs.get('disambiguator'):
            self.disambiguator = Disambiguation(**kwargs.get('disambiguator', {}))
        else:
            self.disambiguator = None
        if kwargs.get('employment'):
            self.employment = EmploymentConnection(**kwargs.get('employment', {}))
        else:
            self.employment = None
        if kwargs.get('engagementStatistics'):
            self.engagementStatistics = EngagementStatistics(**kwargs.get('engagementStatistics', {}))
        else:
            self.engagementStatistics = None
        if kwargs.get('episodeCredits'):
            self.episodeCredits = CreditV2Connection(**kwargs.get('episodeCredits', {}))
        else:
            self.episodeCredits = None
        if kwargs.get('experimental_clients'):
            self.experimental_clients = Experimental_NameRepresentationConnection(**kwargs.get('experimental_clients', {}))
        else:
            self.experimental_clients = None
        if kwargs.get('experimental_creditCategories'):
            self.experimental_creditCategories = ExperimentalNameCreditCategoryWithCredits(**kwargs.get('experimental_creditCategories', {}))
        else:
            self.experimental_creditCategories = None
        if kwargs.get('experimental_credits'):
            self.experimental_credits = ExperimentalCreditConnection(**kwargs.get('experimental_credits', {}))
        else:
            self.experimental_credits = None
        if kwargs.get('experimental_directContact'):
            self.experimental_directContact = Experimental_DirectContactDetails(**kwargs.get('experimental_directContact', {}))
        else:
            self.experimental_directContact = None
        if kwargs.get('experimental_employment'):
            self.experimental_employment = Experimental_PersonalEmploymentConnection(**kwargs.get('experimental_employment', {}))
        else:
            self.experimental_employment = None
        if kwargs.get('experimental_representation'):
            self.experimental_representation = Experimental_NameRepresentationConnection(**kwargs.get('experimental_representation', {}))
        else:
            self.experimental_representation = None
        if kwargs.get('experimental_resume'):
            self.experimental_resume = Experimental_Resume(**kwargs.get('experimental_resume', {}))
        else:
            self.experimental_resume = None
        if kwargs.get('experimental_trackNotificationPreferences'):
            self.experimental_trackNotificationPreferences = Experimental_TrackNotificationPreferences(**kwargs.get('experimental_trackNotificationPreferences', {}))
        else:
            self.experimental_trackNotificationPreferences = None
        if kwargs.get('externalLinkCategories'):
            self.externalLinkCategories = ExternalLinkCategoryWithExternalLinks(**kwargs.get('externalLinkCategories', {}))
        else:
            self.externalLinkCategories = None
        if kwargs.get('externalLinks'):
            self.externalLinks = ExternalLinkConnection(**kwargs.get('externalLinks', {}))
        else:
            self.externalLinks = None
        if kwargs.get('featuredExternalLinkCategories'):
            self.featuredExternalLinkCategories = ExternalLinkCategoryWithFeaturedExternalLinks(**kwargs.get('featuredExternalLinkCategories', {}))
        else:
            self.featuredExternalLinkCategories = None
        if kwargs.get('featuredPolls'):
            self.featuredPolls = PollsConnection(**kwargs.get('featuredPolls', {}))
        else:
            self.featuredPolls = None
        if kwargs.get('height'):
            self.height = NameHeight(**kwargs.get('height', {}))
        else:
            self.height = None
        self.id = kwargs.get('id', "")
        if kwargs.get('images'):
            self.images = ImageConnection(**kwargs.get('images', {}))
        else:
            self.images = None
        if kwargs.get('imageTypes'):
            self.imageTypes = ImageTypeWithImages(**kwargs.get('imageTypes', {}))
        else:
            self.imageTypes = None
        if kwargs.get('_imageUploadLink'):
            self._imageUploadLink = ContributionLink(**kwargs.get('_imageUploadLink', {}))
        else:
            self._imageUploadLink = None
        self.isClaimed = kwargs.get('isClaimed', False)
        if kwargs.get('knownFor'):
            self.knownFor = NameKnownForConnection(**kwargs.get('knownFor', {}))
        else:
            self.knownFor = None
        if kwargs.get('knownForV2'):
            self.knownForV2 = KnownForV2(**kwargs.get('knownForV2', {}))
        else:
            self.knownForV2 = None
        if kwargs.get('managedData'):
            self.managedData = NameManagedData(**kwargs.get('managedData', {}))
        else:
            self.managedData = None
        if kwargs.get('meta'):
            self.meta = NameMeta(**kwargs.get('meta', {}))
        else:
            self.meta = None
        if kwargs.get('meterRank'):
            self.meterRank = NameMeterRanking(**kwargs.get('meterRank', {}))
        else:
            self.meterRank = None
        if kwargs.get('meterRankingHistory'):
            self.meterRankingHistory = NameMeterRankingHistory(**kwargs.get('meterRankingHistory', {}))
        else:
            self.meterRankingHistory = None
        if kwargs.get('moreLikeThisNames'):
            self.moreLikeThisNames = NameConnection(**kwargs.get('moreLikeThisNames', {}))
        else:
            self.moreLikeThisNames = None
        if kwargs.get('nameText'):
            self.nameText = NameText(**kwargs.get('nameText', {}))
        else:
            self.nameText = None
        if kwargs.get('news'):
            self.news = NewsConnection(**kwargs.get('news', {}))
        else:
            self.news = None
        if kwargs.get('nickNames'):
            self.nickNames = NickName(**kwargs.get('nickNames', {}))
        else:
            self.nickNames = None
        if kwargs.get('nominations'):
            self.nominations = NominationConnection(**kwargs.get('nominations', {}))
        else:
            self.nominations = None
        if kwargs.get('otherWorks'):
            self.otherWorks = NameOtherWorkConnection(**kwargs.get('otherWorks', {}))
        else:
            self.otherWorks = None
        if kwargs.get('prestigiousAwardSummary'):
            self.prestigiousAwardSummary = PrestigiousAwardSummary(**kwargs.get('prestigiousAwardSummary', {}))
        else:
            self.prestigiousAwardSummary = None
        if kwargs.get('primaryImage'):
            self.primaryImage = Image(**kwargs.get('primaryImage', {}))
        else:
            self.primaryImage = None
        if kwargs.get('primaryProfessions'):
            self.primaryProfessions = PrimaryProfession(**kwargs.get('primaryProfessions', {}))
        else:
            self.primaryProfessions = None
        if kwargs.get('primaryVideos'):
            self.primaryVideos = VideoConnection(**kwargs.get('primaryVideos', {}))
        else:
            self.primaryVideos = None
        if kwargs.get('professions'):
            self.professions = NameProfession(**kwargs.get('professions', {}))
        else:
            self.professions = None
        if kwargs.get('publicityCategories'):
            self.publicityCategories = PublicityCategoryWithListings(**kwargs.get('publicityCategories', {}))
        else:
            self.publicityCategories = None
        if kwargs.get('publicityListings'):
            self.publicityListings = PublicityListingCategoryConnection(**kwargs.get('publicityListings', {}))
        else:
            self.publicityListings = None
        if kwargs.get('quotes'):
            self.quotes = NameQuoteConnection(**kwargs.get('quotes', {}))
        else:
            self.quotes = None
        if kwargs.get('recentlyViewedStatistics'):
            self.recentlyViewedStatistics = RecentlyViewedStatistics(**kwargs.get('recentlyViewedStatistics', {}))
        else:
            self.recentlyViewedStatistics = None
        if kwargs.get('relatedLists'):
            self.relatedLists = ListConnection(**kwargs.get('relatedLists', {}))
        else:
            self.relatedLists = None
        if kwargs.get('relations'):
            self.relations = NameRelationsConnection(**kwargs.get('relations', {}))
        else:
            self.relations = None
        if kwargs.get('representation'):
            self.representation = NameRepresentationConnection(**kwargs.get('representation', {}))
        else:
            self.representation = None
        if kwargs.get('resume'):
            self.resume = Resume(**kwargs.get('resume', {}))
        else:
            self.resume = None
        if kwargs.get('searchIndexing'):
            self.searchIndexing = NameSearchIndexing(**kwargs.get('searchIndexing', {}))
        else:
            self.searchIndexing = None
        if kwargs.get('selfVerifiedData'):
            self.selfVerifiedData = SelfVerifiedNameData(**kwargs.get('selfVerifiedData', {}))
        else:
            self.selfVerifiedData = None
        if kwargs.get('sharedNames'):
            self.sharedNames = SharedNamesResult(**kwargs.get('sharedNames', {}))
        else:
            self.sharedNames = None
        if kwargs.get('sharedNamesSummary'):
            self.sharedNamesSummary = SharedNamesSummary(**kwargs.get('sharedNamesSummary', {}))
        else:
            self.sharedNamesSummary = None
        if kwargs.get('sharedTitles'):
            self.sharedTitles = SharedTitlesConnection(**kwargs.get('sharedTitles', {}))
        else:
            self.sharedTitles = None
        if kwargs.get('spouses'):
            self.spouses = NameSpouse(**kwargs.get('spouses', {}))
        else:
            self.spouses = None
        if kwargs.get('titleSalaries'):
            self.titleSalaries = SalaryConnection(**kwargs.get('titleSalaries', {}))
        else:
            self.titleSalaries = None
        if kwargs.get('trackNotificationPreferences'):
            self.trackNotificationPreferences = TrackNotificationPreferences(**kwargs.get('trackNotificationPreferences', {}))
        else:
            self.trackNotificationPreferences = None
        if kwargs.get('trademarks'):
            self.trademarks = TrademarkConnection(**kwargs.get('trademarks', {}))
        else:
            self.trademarks = None
        if kwargs.get('trivia'):
            self.trivia = NameTriviaConnection(**kwargs.get('trivia', {}))
        else:
            self.trivia = None
        if kwargs.get('userSelectedProfessions'):
            self.userSelectedProfessions = NameProfession(**kwargs.get('userSelectedProfessions', {}))
        else:
            self.userSelectedProfessions = None
        if kwargs.get('vanityUrl'):
            self.vanityUrl = VanityUrl(**kwargs.get('vanityUrl', {}))
        else:
            self.vanityUrl = None
        if kwargs.get('videos'):
            self.videos = VideoConnection(**kwargs.get('videos', {}))
        else:
            self.videos = None
        if kwargs.get('videoTypes'):
            self.videoTypes = VideoTypeWithVideos(**kwargs.get('videoTypes', {}))
        else:
            self.videoTypes = None
    def __str__(self):
        string = ""
        if self.nameText:
            string = str(self.nameText)
        else:
            string = str(self.id)
        if self.birthDate and self.deathDate:
            string += f" ({self.birthDate} - {self.deathDate})"
        elif self.birthDate:
            string += f" ({self.birthDate})"
        return string
    def __repr__(self):
        return f"<--- Name(id={self.id}, nameText={self.nameText}, birthDate={self.birthDate}, deathDate={self.deathDate}) --->"
    def __eq__(self, other):
        if not isinstance(other, Name):
            return False
        return self.id == other.id

class NameAka:
    def __init__(self, **kwargs):
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableNameAkaProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, NameAka):
            return False
        return (self.displayableProperty == other.displayableProperty and self.text == other.text)


class NameAkaConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(NameAka(**node.get("node", {})))

class NameBio:
    def __init__(self, **kwargs):
        if kwargs.get('author'):
            self.author = Markdown(**kwargs.get('author', {}))
        else:
            self.author = None
        if kwargs.get('category'):
            self.category = NameBioCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('displayableArticle'):
            self.displayableArticle = DisplayableArticle(**kwargs.get('displayableArticle', {}))
        else:
            self.displayableArticle = None
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('text'):
            self.text = Markdown(**kwargs.get('text', {}))
        else:
            self.text = None
    def __eq__(self, other):
        if not isinstance(other, NameBio):
            return False
        return self.id == other.id

class NameBioCategory:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, NameBioCategory):
            return False
        return self.id == other.id


class NameBiosConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(NameBio(**node.get("node", {})))

class NameBirth:
    def __init__(self, **kwargs):
        self.date = kwargs.get('date', "")
        if kwargs.get('location'):
            self.location = Location(**kwargs.get('location', {}))
        else:
            self.location = None
    def __eq__(self, other):
        if not isinstance(other, NameBirth):
            return False
        return (self.date == other.date and self.location == other.location)

class NameChartRankingsNode:
    def __init__(self, **kwargs):
        if kwargs.get('item'):
            self.item = Name(**kwargs.get('item', {}))
        else:
            self.item = None
        self.rank = kwargs.get('rank', 0)
    def __eq__(self, other):
        if not isinstance(other, NameChartRankingsNode):
            return False
        return (self.item == other.item and self.rank == other.rank)

class NameCreditCategory:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, NameCreditCategory):
            return False
        return self.id == other.id

class NameCreditCategoryWithCredits:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = CreditCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('credits'):
            self.credits = CreditConnection(**kwargs.get('credits', {}))
        else:
            self.credits = None
    def __eq__(self, other):
        if not isinstance(other, NameCreditCategoryWithCredits):
            return False
        return (self.category == other.category and self.credits == other.credits)

class NameCreditSummary:
    def __init__(self, **kwargs):
        if kwargs.get('categories'):
            self.categories = CreditCategorySummary(**kwargs.get('categories', {}))
        else:
            self.categories = None
        if kwargs.get('genres'):
            self.genres = GenreSummary(**kwargs.get('genres', {}))
        else:
            self.genres = None
        if kwargs.get('titleTypeCategories'):
            self.titleTypeCategories = TitleTypeCategorySummary(**kwargs.get('titleTypeCategories', {}))
        else:
            self.titleTypeCategories = None
        if kwargs.get('titleTypes'):
            self.titleTypes = TitleTypeSummary(**kwargs.get('titleTypes', {}))
        else:
            self.titleTypes = None
        if kwargs.get('totalCredits'):
            self.totalCredits = TotalCredits(**kwargs.get('totalCredits', {}))
        else:
            self.totalCredits = None
    def __eq__(self, other):
        if not isinstance(other, NameCreditSummary):
            return False
        return (self.categories == other.categories and self.genres == other.genres and self.titleTypeCategories == other.titleTypeCategories and self.titleTypes == other.titleTypes and self.totalCredits == other.totalCredits)

class NameDeath:
    def __init__(self, **kwargs):
        if kwargs.get('cause'):
            self.cause = DeathCause(**kwargs.get('cause', {}))
        else:
            self.cause = None
        self.date = kwargs.get('date', "")
        if kwargs.get('location'):
            self.location = Location(**kwargs.get('location', {}))
        else:
            self.location = None
    def __eq__(self, other):
        if not isinstance(other, NameDeath):
            return False
        return (self.cause == other.cause and self.date == other.date and self.location == other.location)

class NameDisplayPreferences:
    def __init__(self, **kwargs):
        self.akas = kwargs.get('akas', "")
        self.awards = kwargs.get('awards', "")
        self.biography = kwargs.get('biography', "")
        self.height = kwargs.get('height', "")
    def __eq__(self, other):
        if not isinstance(other, NameDisplayPreferences):
            return False
        return (self.akas == other.akas and self.awards == other.awards and self.biography == other.biography and self.height == other.height)

class NameHeight:
    def __init__(self, **kwargs):
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableNameHeightProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        if kwargs.get('measurement'):
            self.measurement = LengthMeasurement(**kwargs.get('measurement', {}))
        else:
            self.measurement = None
    def __eq__(self, other):
        if not isinstance(other, NameHeight):
            return False
        return (self.displayableProperty == other.displayableProperty and self.measurement == other.measurement)

class NameKnownFor:
    def __init__(self, **kwargs):
        if kwargs.get('credit'):
            self.credit = Credit(**kwargs.get('credit', {}))
        else:
            self.credit = None
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, NameKnownFor):
            return False
        return (self.credit == other.credit and self.title == other.title)


class NameKnownForConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(NameKnownFor(**node.get("node", {})))

class NameKnownForRestriction:
    def __init__(self, **kwargs):
        if kwargs.get('explanations'):
            self.explanations = RestrictionExplanation(**kwargs.get('explanations', {}))
        else:
            self.explanations = None
        self.reasons = kwargs.get('reasons', "")
        self.restrictionReason = kwargs.get('restrictionReason', "")
        self.unrestrictedTotal = kwargs.get('unrestrictedTotal', 0)
    def __eq__(self, other):
        if not isinstance(other, NameKnownForRestriction):
            return False
        return (self.explanations == other.explanations and self.reasons == other.reasons and self.restrictionReason == other.restrictionReason and self.unrestrictedTotal == other.unrestrictedTotal)


class NameConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Name(**node.get("node", {})))

class NameManagedData:
    def __init__(self, **kwargs):
        if kwargs.get('automaticFeaturedImages'):
            self.automaticFeaturedImages = Image(**kwargs.get('automaticFeaturedImages', {}))
        else:
            self.automaticFeaturedImages = None
        if kwargs.get('automaticKnownFor'):
            self.automaticKnownFor = Title(**kwargs.get('automaticKnownFor', {}))
        else:
            self.automaticKnownFor = None
        if kwargs.get('customFeaturedImages'):
            self.customFeaturedImages = CustomFeaturedImages(**kwargs.get('customFeaturedImages', {}))
        else:
            self.customFeaturedImages = None
        if kwargs.get('customKnownFor'):
            self.customKnownFor = CustomKnownFor(**kwargs.get('customKnownFor', {}))
        else:
            self.customKnownFor = None
        if kwargs.get('customPrimaryImage'):
            self.customPrimaryImage = CustomPrimaryImage(**kwargs.get('customPrimaryImage', {}))
        else:
            self.customPrimaryImage = None
        if kwargs.get('displayPreferences'):
            self.displayPreferences = NameDisplayPreferences(**kwargs.get('displayPreferences', {}))
        else:
            self.displayPreferences = None
        if kwargs.get('latestPrimaryImage'):
            self.latestPrimaryImage = Image(**kwargs.get('latestPrimaryImage', {}))
        else:
            self.latestPrimaryImage = None
        if kwargs.get('managedClients'):
            self.managedClients = ManagedClient(**kwargs.get('managedClients', {}))
        else:
            self.managedClients = None
        if kwargs.get('managingRepresentatives'):
            self.managingRepresentatives = ManagingRepresentative(**kwargs.get('managingRepresentatives', {}))
        else:
            self.managingRepresentatives = None
    def __eq__(self, other):
        if not isinstance(other, NameManagedData):
            return False
        return (self.automaticFeaturedImages == other.automaticFeaturedImages and self.automaticKnownFor == other.automaticKnownFor and self.customFeaturedImages == other.customFeaturedImages and self.customKnownFor == other.customKnownFor and self.customPrimaryImage == other.customPrimaryImage and self.displayPreferences == other.displayPreferences and self.latestPrimaryImage == other.latestPrimaryImage and self.managedClients == other.managedClients and self.managingRepresentatives == other.managingRepresentatives)

class NameManagingPermissionRequestResponse:
    def __init__(self, **kwargs):
        self.isValid = kwargs.get('isValid', False)
        if kwargs.get('requester'):
            self.requester = Name(**kwargs.get('requester', {}))
        else:
            self.requester = None
        if kwargs.get('target'):
            self.target = Name(**kwargs.get('target', {}))
        else:
            self.target = None
    def __eq__(self, other):
        if not isinstance(other, NameManagingPermissionRequestResponse):
            return False
        return (self.isValid == other.isValid and self.requester == other.requester and self.target == other.target)

class NameMeta:
    def __init__(self, **kwargs):
        self.canonicalId = kwargs.get('canonicalId', "")
        self.publicationStatus = kwargs.get('publicationStatus', "")
    def __eq__(self, other):
        if not isinstance(other, NameMeta):
            return False
        return (self.canonicalId == other.canonicalId and self.publicationStatus == other.publicationStatus)

class NameMetadata:
    def __init__(self, **kwargs):
        if kwargs.get('nameCreditCategories'):
            self.nameCreditCategories = NameCreditCategory(**kwargs.get('nameCreditCategories', {}))
        else:
            self.nameCreditCategories = None
    def __eq__(self, other):
        if not isinstance(other, NameMetadata):
            return False
        return (self.nameCreditCategories == other.nameCreditCategories)

class NameMeterRanking:
    def __init__(self, **kwargs):
        self.currentRank = kwargs.get('currentRank', 0)
        if kwargs.get('rankChange'):
            self.rankChange = MeterRankChange(**kwargs.get('rankChange', {}))
        else:
            self.rankChange = None
    def __eq__(self, other):
        if not isinstance(other, NameMeterRanking):
            return False
        return (self.currentRank == other.currentRank and self.rankChange == other.rankChange)

class NameMeterRankingHistory:
    def __init__(self, **kwargs):
        if kwargs.get('bestRank'):
            self.bestRank = MeterRankingHistoryEntry(**kwargs.get('bestRank', {}))
        else:
            self.bestRank = None
        if kwargs.get('ranks'):
            self.ranks = MeterRankingHistoryEntry(**kwargs.get('ranks', {}))
        else:
            self.ranks = None
        if kwargs.get('restriction'):
            self.restriction = MeterRestriction(**kwargs.get('restriction', {}))
        else:
            self.restriction = None
    def __eq__(self, other):
        if not isinstance(other, NameMeterRankingHistory):
            return False
        return (self.bestRank == other.bestRank and self.ranks == other.ranks and self.restriction == other.restriction)

class NameOtherWork:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = NameOtherWorkCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableNameOtherWorkProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.fromDate = kwargs.get('fromDate', "")
        self.id = kwargs.get('id', "")
        if kwargs.get('text'):
            self.text = Markdown(**kwargs.get('text', {}))
        else:
            self.text = None
        self.toDate = kwargs.get('toDate', "")
    def __eq__(self, other):
        if not isinstance(other, NameOtherWork):
            return False
        return self.id == other.id

class NameOtherWorkCategory:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, NameOtherWorkCategory):
            return False
        return self.id == other.id


class NameOtherWorkConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(NameOtherWork(**node.get("node", {})))

class NamePersonalLocation:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.latitude = kwargs.get('latitude', "")
        self.longitude = kwargs.get('longitude', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, NamePersonalLocation):
            return False
        return self.id == other.id

class NamePersonalLocationMetadata:
    def __init__(self, **kwargs):
        self.limit = kwargs.get('limit', 0)
        if kwargs.get('validValues'):
            self.validValues = NamePersonalLocation(**kwargs.get('validValues', {}))
        else:
            self.validValues = None
    def __eq__(self, other):
        if not isinstance(other, NamePersonalLocationMetadata):
            return False
        return (self.limit == other.limit and self.validValues == other.validValues)

class NamePersonalLocations:
    def __init__(self, **kwargs):
        if kwargs.get('locations'):
            self.locations = NamePersonalLocation(**kwargs.get('locations', {}))
        else:
            self.locations = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, NamePersonalLocations):
            return False
        return (self.locations == other.locations and self.total == other.total)

class NameProfession:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.isCustomerSelectable = kwargs.get('isCustomerSelectable', False)
        if kwargs.get('profession'):
            self.profession = DisplayableProfession(**kwargs.get('profession', {}))
        else:
            self.profession = None
        if kwargs.get('professionCategory'):
            self.professionCategory = ProfessionCategory(**kwargs.get('professionCategory', {}))
        else:
            self.professionCategory = None
        if kwargs.get('shortDescription'):
            self.shortDescription = DisplayableProfessionDescription(**kwargs.get('shortDescription', {}))
        else:
            self.shortDescription = None
    def __eq__(self, other):
        if not isinstance(other, NameProfession):
            return False
        return self.id == other.id

class NameQuote:
    def __init__(self, **kwargs):
        if kwargs.get('displayableArticle'):
            self.displayableArticle = DisplayableArticle(**kwargs.get('displayableArticle', {}))
        else:
            self.displayableArticle = None
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('text'):
            self.text = Markdown(**kwargs.get('text', {}))
        else:
            self.text = None
    def __eq__(self, other):
        if not isinstance(other, NameQuote):
            return False
        return self.id == other.id


class NameQuoteConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(NameQuote(**node.get("node", {})))

class NameRecommendation:
    def __init__(self, **kwargs):
        if kwargs.get('explanation'):
            self.explanation = LocalizedMarkdown(**kwargs.get('explanation', {}))
        else:
            self.explanation = None
        if kwargs.get('name'):
            self.name = Name(**kwargs.get('name', {}))
        else:
            self.name = None
    def __eq__(self, other):
        if not isinstance(other, NameRecommendation):
            return False
        return (self.explanation == other.explanation and self.name == other.name)


class NameRecommendationConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(NameRecommendation(**node.get("node", {})))

class NameRecommendations:
    def __init__(self, **kwargs):
        if kwargs.get('names'):
            self.names = NameRecommendationConnection(**kwargs.get('names', {}))
        else:
            self.names = None
        self.refTag = kwargs.get('refTag', "")
    def __eq__(self, other):
        if not isinstance(other, NameRecommendations):
            return False
        return (self.names == other.names and self.refTag == other.refTag)

class NameRelation:
    def __init__(self, **kwargs):
        if kwargs.get('birthDate'):
            self.birthDate = DisplayableDate(**kwargs.get('birthDate', {}))
        else:
            self.birthDate = None
        if kwargs.get('genderIdentity'):
            self.genderIdentity = GenderIdentity(**kwargs.get('genderIdentity', {}))
        else:
            self.genderIdentity = None
        self.id = kwargs.get('id', "")
        if kwargs.get('relationName'):
            self.relationName = RelationName(**kwargs.get('relationName', {}))
        else:
            self.relationName = None
        if kwargs.get('relationshipType'):
            self.relationshipType = NameRelationType(**kwargs.get('relationshipType', {}))
        else:
            self.relationshipType = None
    def __eq__(self, other):
        if not isinstance(other, NameRelation):
            return False
        return self.id == other.id

class NameRelationType:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, NameRelationType):
            return False
        return self.id == other.id


class NameRelationsConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(NameRelation(**node.get("node", {})))

class NameRepresentation:
    def __init__(self, **kwargs):
        if kwargs.get('agency'):
            self.agency = Agency(**kwargs.get('agency', {}))
        else:
            self.agency = None
        if kwargs.get('client'):
            self.client = Name(**kwargs.get('client', {}))
        else:
            self.client = None
        self.id = kwargs.get('id', "")
        if kwargs.get('independentRepresentative'):
            self.independentRepresentative = Name(**kwargs.get('independentRepresentative', {}))
        else:
            self.independentRepresentative = None
        if kwargs.get('relationshipType'):
            self.relationshipType = RepresentationRelationshipType(**kwargs.get('relationshipType', {}))
        else:
            self.relationshipType = None
    def __eq__(self, other):
        if not isinstance(other, NameRepresentation):
            return False
        return self.id == other.id


class NameRepresentationConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(NameRepresentation(**node.get("node", {})))

class NameSearchIndexing:
    def __init__(self, **kwargs):
        self.disableIndexing = kwargs.get('disableIndexing', False)
    def __eq__(self, other):
        if not isinstance(other, NameSearchIndexing):
            return False
        return (self.disableIndexing == other.disableIndexing)

class NameSpouse:
    def __init__(self, **kwargs):
        if kwargs.get('attributes'):
            self.attributes = SpouseAttributes(**kwargs.get('attributes', {}))
        else:
            self.attributes = None
        self.current = kwargs.get('current', False)
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableNameSpouseProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        if kwargs.get('spouse'):
            self.spouse = SpouseName(**kwargs.get('spouse', {}))
        else:
            self.spouse = None
        if kwargs.get('timeRange'):
            self.timeRange = DisplayableSpouseTimeRange(**kwargs.get('timeRange', {}))
        else:
            self.timeRange = None
    def __eq__(self, other):
        if not isinstance(other, NameSpouse):
            return False
        return (self.attributes == other.attributes and self.current == other.current and self.displayableProperty == other.displayableProperty and self.spouse == other.spouse and self.timeRange == other.timeRange)

class NameText:
    def __init__(self, **kwargs):
        self.text = kwargs.get('text', "")
    def __str__(self):
        return self.text
    def __repr__(self):
        return f"NameText(text={self.text})"
    def __eq__(self, other):
        if not isinstance(other, NameText):
            return False
        return (self.text == other.text)

class NameToTitleAttachment:
    def __init__(self, **kwargs):
        self.attachmentTime = kwargs.get('attachmentTime', "")
        self.characterList = kwargs.get('characterList', "")
        if kwargs.get('creditCategories'):
            self.creditCategories = CreditCategory(**kwargs.get('creditCategories', {}))
        else:
            self.creditCategories = None
        self.id = kwargs.get('id', "")
        if kwargs.get('name'):
            self.name = Name(**kwargs.get('name', {}))
        else:
            self.name = None
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, NameToTitleAttachment):
            return False
        return self.id == other.id

class NameTrivia:
    def __init__(self, **kwargs):
        self.date = kwargs.get('date', "")
        if kwargs.get('displayableArticle'):
            self.displayableArticle = DisplayableArticle(**kwargs.get('displayableArticle', {}))
        else:
            self.displayableArticle = None
        self.id = kwargs.get('id', "")
        if kwargs.get('interestScore'):
            self.interestScore = InterestScore(**kwargs.get('interestScore', {}))
        else:
            self.interestScore = None
        if kwargs.get('text'):
            self.text = Markdown(**kwargs.get('text', {}))
        else:
            self.text = None
    def __eq__(self, other):
        if not isinstance(other, NameTrivia):
            return False
        return self.id == other.id


class NameTriviaConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(NameTrivia(**node.get("node", {})))

class NameWeight:
    def __init__(self, **kwargs):
        self.unit = kwargs.get('unit', "")
        self.value = kwargs.get('value', 0.0)
    def __eq__(self, other):
        if not isinstance(other, NameWeight):
            return False
        return (self.unit == other.unit and self.value == other.value)

class NamedActionLink:
    def __init__(self, **kwargs):
        self.actionName = kwargs.get('actionName', 0)
        if kwargs.get('label'):
            self.label = CallToActionText(**kwargs.get('label', {}))
        else:
            self.label = None
        self.url = kwargs.get('url', "")
    def __eq__(self, other):
        if not isinstance(other, NamedActionLink):
            return False
        return (self.actionName == other.actionName and self.label == other.label and self.url == other.url)

class NegativeFormat:
    def __init__(self, **kwargs):
        if kwargs.get('attributes'):
            self.attributes = [DisplayableAttribute(**attr) for attr in kwargs.get('attributes', [])]
        else:
            self.attributes = None
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableTechnicalSpecificationProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.negativeFormat = kwargs.get('negativeFormat', "")
    def __eq__(self, other):
        if not isinstance(other, NegativeFormat):
            return False
        return (self.attributes == other.attributes and self.displayableProperty == other.displayableProperty and self.negativeFormat == other.negativeFormat)

class NegativeFormats:
    def __init__(self, **kwargs):
        if kwargs.get('items'):
            self.items = NegativeFormat(**kwargs.get('items', {}))
        else:
            self.items = None
        if kwargs.get('restriction'):
            self.restriction = TechnicalSpecificationsRestriction(**kwargs.get('restriction', {}))
        else:
            self.restriction = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, NegativeFormats):
            return False
        return (self.items == other.items and self.restriction == other.restriction and self.total == other.total)

class News:
    def __init__(self, **kwargs):
        if kwargs.get('articleTitle'):
            self.articleTitle = Markdown(**kwargs.get('articleTitle', {}))
        else:
            self.articleTitle = None
        self.byline = kwargs.get('byline', "")
        self.date = kwargs.get('date', "")
        self.externalUrl = kwargs.get('externalUrl', "")
        self.id = kwargs.get('id', "")
        if kwargs.get('image'):
            self.image = Image(**kwargs.get('image', {}))
        else:
            self.image = None
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('similarNewsItems'):
            self.similarNewsItems = News(**kwargs.get('similarNewsItems', {}))
        else:
            self.similarNewsItems = None
        if kwargs.get('source'):
            self.source = NewsSource(**kwargs.get('source', {}))
        else:
            self.source = None
        if kwargs.get('text'):
            self.text = Markdown(**kwargs.get('text', {}))
        else:
            self.text = None
    def __eq__(self, other):
        if not isinstance(other, News):
            return False
        return self.id == other.id

class NewsCategoryMetadata:
    def __init__(self, **kwargs):
        self.category = kwargs.get('category', "")
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, NewsCategoryMetadata):
            return False
        return self.id == other.id


class NewsConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(News(**node.get("node", {})))

class NewsLink:
    def __init__(self, **kwargs):
        self.label = kwargs.get('label', "")
        self.url = kwargs.get('url', "")
    def __eq__(self, other):
        if not isinstance(other, NewsLink):
            return False
        return (self.label == other.label and self.url == other.url)

class NewsPageInfo:
    def __init__(self, **kwargs):
        self.endCursor = kwargs.get('endCursor', "")
        self.hasNextPage = kwargs.get('hasNextPage', False)
    def __eq__(self, other):
        if not isinstance(other, NewsPageInfo):
            return False
        return (self.endCursor == other.endCursor and self.hasNextPage == other.hasNextPage)

class NewsRestriction:
    def __init__(self, **kwargs):
        if kwargs.get('explanations'):
            self.explanations = RestrictionExplanation(**kwargs.get('explanations', {}))
        else:
            self.explanations = None
        self.reasons = kwargs.get('reasons', "")
        self.restrictionReason = kwargs.get('restrictionReason', "")
        self.unrestrictedTotal = kwargs.get('unrestrictedTotal', 0)
    def __eq__(self, other):
        if not isinstance(other, NewsRestriction):
            return False
        return (self.explanations == other.explanations and self.reasons == other.reasons and self.restrictionReason == other.restrictionReason and self.unrestrictedTotal == other.unrestrictedTotal)

class NewsSource:
    def __init__(self, **kwargs):
        self.description = kwargs.get('description', "")
        if kwargs.get('homepage'):
            self.homepage = NewsLink(**kwargs.get('homepage', {}))
        else:
            self.homepage = None
        if kwargs.get('icon'):
            self.icon = NewsSourceIconImage(**kwargs.get('icon', {}))
        else:
            self.icon = None
        self.id = kwargs.get('id', "")
        self.trustedSource = kwargs.get('trustedSource', False)
    def __eq__(self, other):
        if not isinstance(other, NewsSource):
            return False
        return self.id == other.id

class NewsSourceIconImage:
    def __init__(self, **kwargs):
        self.height = kwargs.get('height', 0)
        self.url = kwargs.get('url', "")
        self.width = kwargs.get('width', 0)
    def __eq__(self, other):
        if not isinstance(other, NewsSourceIconImage):
            return False
        return (self.height == other.height and self.url == other.url and self.width == other.width)

class NickName:
    def __init__(self, **kwargs):
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableNickNameProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, NickName):
            return False
        return (self.displayableProperty == other.displayableProperty and self.text == other.text)

class Nomination:
    def __init__(self, **kwargs):
        if kwargs.get('award'):
            self.award = NominationAward(**kwargs.get('award', {}))
        else:
            self.award = None
        if kwargs.get('category'):
            self.category = AwardCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('event'):
            self.event = NominationEvent(**kwargs.get('event', {}))
        else:
            self.event = None
        if kwargs.get('eventEdition'):
            self.eventEdition = NominationEventEdition(**kwargs.get('eventEdition', {}))
        else:
            self.eventEdition = None
        if kwargs.get('forEpisodes'):
            self.forEpisodes = Title(**kwargs.get('forEpisodes', {}))
        else:
            self.forEpisodes = None
        if kwargs.get('forSongTitles'):
            self.forSongTitles = DisplayableSongTitle(**kwargs.get('forSongTitles', {}))
        else:
            self.forSongTitles = None
        self.id = kwargs.get('id', "")
        self.isWinner = kwargs.get('isWinner', False)
        if kwargs.get('notes'):
            self.notes = Markdown(**kwargs.get('notes', {}))
        else:
            self.notes = None
        if kwargs.get('winAnnouncementDate'):
            self.winAnnouncementDate = DisplayableDate(**kwargs.get('winAnnouncementDate', {}))
        else:
            self.winAnnouncementDate = None
        self.winningRank = kwargs.get('winningRank', 0)
    def __eq__(self, other):
        if not isinstance(other, Nomination):
            return False
        return self.id == other.id

class NominationAward:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('nominationCategories'):
            self.nominationCategories = NominationsWithCategoryConnection(**kwargs.get('nominationCategories', {}))
        else:
            self.nominationCategories = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, NominationAward):
            return False
        return self.id == other.id

class NominationEvent:
    def __init__(self, **kwargs):
        if kwargs.get('akas'):
            self.akas = NominationEventAka(**kwargs.get('akas', {}))
        else:
            self.akas = None
        if kwargs.get('awards'):
            self.awards = NominationAward(**kwargs.get('awards', {}))
        else:
            self.awards = None
        if kwargs.get('editions'):
            self.editions = NominationEventEdition(**kwargs.get('editions', {}))
        else:
            self.editions = None
        self.id = kwargs.get('id', "")
        if kwargs.get('location'):
            self.location = DisplayableLocation(**kwargs.get('location', {}))
        else:
            self.location = None
        if kwargs.get('name'):
            self.name = NominationEventName(**kwargs.get('name', {}))
        else:
            self.name = None
        if kwargs.get('trivia'):
            self.trivia = Markdown(**kwargs.get('trivia', {}))
        else:
            self.trivia = None
        if kwargs.get('urls'):
            self.urls = EventUrl(**kwargs.get('urls', {}))
        else:
            self.urls = None
    def __eq__(self, other):
        if not isinstance(other, NominationEvent):
            return False
        return self.id == other.id

class NominationEventAka:
    def __init__(self, **kwargs):
        self.endYear = kwargs.get('endYear', 0)
        if kwargs.get('name'):
            self.name = NominationEventName(**kwargs.get('name', {}))
        else:
            self.name = None
        self.startYear = kwargs.get('startYear', 0)
    def __eq__(self, other):
        if not isinstance(other, NominationEventAka):
            return False
        return (self.endYear == other.endYear and self.name == other.name and self.startYear == other.startYear)

class NominationEventEdition:
    def __init__(self, **kwargs):
        if kwargs.get('awards'):
            self.awards = NominationAward(**kwargs.get('awards', {}))
        else:
            self.awards = None
        if kwargs.get('dateRange'):
            self.dateRange = DisplayableDateRange(**kwargs.get('dateRange', {}))
        else:
            self.dateRange = None
        if kwargs.get('event'):
            self.event = NominationEvent(**kwargs.get('event', {}))
        else:
            self.event = None
        self.id = kwargs.get('id', "")
        self.instanceWithinYear = kwargs.get('instanceWithinYear', 0)
        if kwargs.get('trivia'):
            self.trivia = Markdown(**kwargs.get('trivia', {}))
        else:
            self.trivia = None
        self.year = kwargs.get('year', 0)
    def __eq__(self, other):
        if not isinstance(other, NominationEventEdition):
            return False
        return self.id == other.id

class NominationEventName:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, NominationEventName):
            return False
        return self.id == other.id


class NominationConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Nomination(**node.get("node", {})))

class NominationsWithCategory:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = AwardCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('nominations'):
            self.nominations = NominationConnection(**kwargs.get('nominations', {}))
        else:
            self.nominations = None
    def __eq__(self, other):
        if not isinstance(other, NominationsWithCategory):
            return False
        return (self.category == other.category and self.nominations == other.nominations)


class NominationsWithCategoryConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(NominationsWithCategory(**node.get("node", {})))

class OccupationValue:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, OccupationValue):
            return False
        return self.id == other.id

class OpeningWeekendGross:
    def __init__(self, **kwargs):
        if kwargs.get('boxOfficeAreaType'):
            self.boxOfficeAreaType = BoxOfficeAreaType(**kwargs.get('boxOfficeAreaType', {}))
        else:
            self.boxOfficeAreaType = None
        if kwargs.get('gross'):
            self.gross = BoxOfficeGross(**kwargs.get('gross', {}))
        else:
            self.gross = None
        self.theaterCount = kwargs.get('theaterCount', 0)
        self.weekendEndDate = kwargs.get('weekendEndDate', "")
        self.weekendStartDate = kwargs.get('weekendStartDate', "")
    def __eq__(self, other):
        if not isinstance(other, OpeningWeekendGross):
            return False
        return (self.boxOfficeAreaType == other.boxOfficeAreaType and self.gross == other.gross and self.theaterCount == other.theaterCount and self.weekendEndDate == other.weekendEndDate and self.weekendStartDate == other.weekendStartDate)


class OpeningWeekendGrossConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(OpeningWeekendGross(**node.get("node", {})))

class PageInfo:
    def __init__(self, **kwargs):
        self.endCursor = kwargs.get('endCursor', "")
        self.hasNextPage = kwargs.get('hasNextPage', False)
        self.hasPreviousPage = kwargs.get('hasPreviousPage', False)
        self.startCursor = kwargs.get('startCursor', "")
    def __eq__(self, other):
        if not isinstance(other, PageInfo):
            return False
        return (self.endCursor == other.endCursor and self.hasNextPage == other.hasNextPage and self.hasPreviousPage == other.hasPreviousPage and self.startCursor == other.startCursor)

class PaginatedTitles:
    def __init__(self, **kwargs):
        self.paginationToken = kwargs.get('paginationToken', "")
        if kwargs.get('titles'):
            self.titles = Title(**kwargs.get('titles', {}))
        else:
            self.titles = None
    def __eq__(self, other):
        if not isinstance(other, PaginatedTitles):
            return False
        return (self.paginationToken == other.paginationToken and self.titles == other.titles)

class PaginatedVideos:
    def __init__(self, **kwargs):
        self.paginationToken = kwargs.get('paginationToken', "")
        if kwargs.get('videos'):
            self.videos = Video(**kwargs.get('videos', {}))
        else:
            self.videos = None
    def __eq__(self, other):
        if not isinstance(other, PaginatedVideos):
            return False
        return (self.paginationToken == other.paginationToken and self.videos == other.videos)

class ParentsGuide:
    def __init__(self, **kwargs):
        if kwargs.get('categories'):
            self.categories = ParentsGuideCategorySummary(**kwargs.get('categories', {}))
        else:
            self.categories = None
        if kwargs.get('guideItems'):
            self.guideItems = ParentsGuideConnection(**kwargs.get('guideItems', {}))
        else:
            self.guideItems = None
    def __eq__(self, other):
        if not isinstance(other, ParentsGuide):
            return False
        return (self.categories == other.categories and self.guideItems == other.guideItems)

class ParentsGuideCategory:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, ParentsGuideCategory):
            return False
        return self.id == other.id

class ParentsGuideCategorySummary:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = ParentsGuideCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('guideItems'):
            self.guideItems = ParentsGuideConnection(**kwargs.get('guideItems', {}))
        else:
            self.guideItems = None
        if kwargs.get('severity'):
            self.severity = SeverityLevel(**kwargs.get('severity', {}))
        else:
            self.severity = None
        if kwargs.get('severityBreakdown'):
            self.severityBreakdown = SeverityLevel(**kwargs.get('severityBreakdown', {}))
        else:
            self.severityBreakdown = None
        self.totalSeverityVotes = kwargs.get('totalSeverityVotes', 0)
    def __eq__(self, other):
        if not isinstance(other, ParentsGuideCategorySummary):
            return False
        return (self.category == other.category and self.guideItems == other.guideItems and self.severity == other.severity and self.severityBreakdown == other.severityBreakdown and self.totalSeverityVotes == other.totalSeverityVotes)


class ParentsGuideConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(ParentsGuide(**node.get("node", {})))

class ParentsGuideItem:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = ParentsGuideCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('_correctionLink'):
            self._correctionLink = ContributionLink(**kwargs.get('_correctionLink', {}))
        else:
            self._correctionLink = None
        self.id = kwargs.get('id', "")
        self.isSpoiler = kwargs.get('isSpoiler', False)
        if kwargs.get('_reportingLink'):
            self._reportingLink = ContributionLink(**kwargs.get('_reportingLink', {}))
        else:
            self._reportingLink = None
        if kwargs.get('text'):
            self.text = Markdown(**kwargs.get('text', {}))
        else:
            self.text = None
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, ParentsGuideItem):
            return False
        return self.id == other.id

class PersonalDetailsOutput:
    def __init__(self, **kwargs):
        self.countryOfResidence = kwargs.get('countryOfResidence', "")
        self.dateOfBirth = kwargs.get('dateOfBirth', "")
        self.gender = kwargs.get('gender', "")
    def __eq__(self, other):
        if not isinstance(other, PersonalDetailsOutput):
            return False
        return (self.countryOfResidence == other.countryOfResidence and self.dateOfBirth == other.dateOfBirth and self.gender == other.gender)

class PersonalEmployment:
    def __init__(self, **kwargs):
        if kwargs.get('branch'):
            self.branch = CompanyBranch(**kwargs.get('branch', {}))
        else:
            self.branch = None
        if kwargs.get('company'):
            self.company = Company(**kwargs.get('company', {}))
        else:
            self.company = None
        if kwargs.get('employeeContact'):
            self.employeeContact = CompanyContactDetails(**kwargs.get('employeeContact', {}))
        else:
            self.employeeContact = None
        self.id = kwargs.get('id', "")
        if kwargs.get('jobTitle'):
            self.jobTitle = LocalizedString(**kwargs.get('jobTitle', {}))
        else:
            self.jobTitle = None
        if kwargs.get('name'):
            self.name = Name(**kwargs.get('name', {}))
        else:
            self.name = None
        if kwargs.get('occupation'):
            self.occupation = OccupationValue(**kwargs.get('occupation', {}))
        else:
            self.occupation = None
    def __eq__(self, other):
        if not isinstance(other, PersonalEmployment):
            return False
        return self.id == other.id

class PlaybackURL:
    def __init__(self, **kwargs):
        if kwargs.get('displayName'):
            self.displayName = LocalizedString(**kwargs.get('displayName', {}))
        else:
            self.displayName = None
        self.url = kwargs.get('url', "")
        self.videoDefinition = kwargs.get('videoDefinition', "")
        self.videoMimeType = kwargs.get('videoMimeType', "")
    def __eq__(self, other):
        if not isinstance(other, PlaybackURL):
            return False
        return (self.displayName == other.displayName and self.url == other.url and self.videoDefinition == other.videoDefinition and self.videoMimeType == other.videoMimeType)

class Plot:
    def __init__(self, **kwargs):
        self.author = kwargs.get('author', "")
        if kwargs.get('_correctionLink'):
            self._correctionLink = ContributionLink(**kwargs.get('_correctionLink', {}))
        else:
            self._correctionLink = None
        self.id = kwargs.get('id', "")
        self.isSpoiler = kwargs.get('isSpoiler', False)
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('plotText'):
            self.plotText = Markdown(**kwargs.get('plotText', {}))
        else:
            self.plotText = None
        self.plotType = kwargs.get('plotType', "")
        if kwargs.get('_reportingLink'):
            self._reportingLink = ContributionLink(**kwargs.get('_reportingLink', {}))
        else:
            self._reportingLink = None
        if kwargs.get('restriction'):
            self.restriction = PlotRestriction(**kwargs.get('restriction', {}))
        else:
            self.restriction = None
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, Plot):
            return False
        return self.id == other.id


class PlotConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Plot(**node.get("node", {})))

class PlotRestriction:
    def __init__(self, **kwargs):
        if kwargs.get('explanations'):
            self.explanations = RestrictionExplanation(**kwargs.get('explanations', {}))
        else:
            self.explanations = None
        self.reasons = kwargs.get('reasons', "")
        self.restrictionReason = kwargs.get('restrictionReason', "")
    def __eq__(self, other):
        if not isinstance(other, PlotRestriction):
            return False
        return (self.explanations == other.explanations and self.reasons == other.reasons and self.restrictionReason == other.restrictionReason)

class Poll:
    def __init__(self, **kwargs):
        if kwargs.get('answers'):
            self.answers = PollAnswersConnection(**kwargs.get('answers', {}))
        else:
            self.answers = None
        if kwargs.get('author'):
            self.author = UserProfile(**kwargs.get('author', {}))
        else:
            self.author = None
        self.createdFromListId = kwargs.get('createdFromListId', "")
        if kwargs.get('currentCustomerVote'):
            self.currentCustomerVote = PollVote(**kwargs.get('currentCustomerVote', {}))
        else:
            self.currentCustomerVote = None
        if kwargs.get('description'):
            self.description = Markdown(**kwargs.get('description', {}))
        else:
            self.description = None
        self.id = kwargs.get('id', "")
        self.isClosed = kwargs.get('isClosed', False)
        if kwargs.get('primaryImage'):
            self.primaryImage = PollPrimaryImage(**kwargs.get('primaryImage', {}))
        else:
            self.primaryImage = None
        if kwargs.get('question'):
            self.question = PollQuestion(**kwargs.get('question', {}))
        else:
            self.question = None
        if kwargs.get('recentVotes'):
            self.recentVotes = PollVoteConnection(**kwargs.get('recentVotes', {}))
        else:
            self.recentVotes = None
        if kwargs.get('relatedPolls'):
            self.relatedPolls = PollsConnection(**kwargs.get('relatedPolls', {}))
        else:
            self.relatedPolls = None
        self.totalVotes = kwargs.get('totalVotes', 0)
        self.type = kwargs.get('type', "")
    def __eq__(self, other):
        if not isinstance(other, Poll):
            return False
        return self.id == other.id

class PollAdminActivity:
    def __init__(self, **kwargs):
        self.action = kwargs.get('action', "")
        self.actionTime = kwargs.get('actionTime', "")
        if kwargs.get('admin'):
            self.admin = UserProfile(**kwargs.get('admin', {}))
        else:
            self.admin = None
        if kwargs.get('poll'):
            self.poll = Poll(**kwargs.get('poll', {}))
        else:
            self.poll = None
    def __eq__(self, other):
        if not isinstance(other, PollAdminActivity):
            return False
        return (self.action == other.action and self.actionTime == other.actionTime and self.admin == other.admin and self.poll == other.poll)

class PollAnswer:
    def __init__(self, **kwargs):
        self.answerIndex = kwargs.get('answerIndex', 0)
        if kwargs.get('description'):
            self.description = Markdown(**kwargs.get('description', {}))
        else:
            self.description = None
        self.votePercentage = kwargs.get('votePercentage', 0.0)
        self.votes = kwargs.get('votes', 0)
    def __eq__(self, other):
        if not isinstance(other, PollAnswer):
            return False
        return (self.answerIndex == other.answerIndex and self.description == other.description and self.votePercentage == other.votePercentage and self.votes == other.votes)


class PollAnswersConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(PollAnswer(**node.get("node", {})))

class PollPrimaryImage:
    def __init__(self, **kwargs):
        if kwargs.get('image'):
            self.image = Image(**kwargs.get('image', {}))
        else:
            self.image = None
    def __eq__(self, other):
        if not isinstance(other, PollPrimaryImage):
            return False
        return (self.image == other.image)

class PollQuestion:
    def __init__(self, **kwargs):
        if kwargs.get('originalText'):
            self.originalText = Markdown(**kwargs.get('originalText', {}))
        else:
            self.originalText = None
    def __eq__(self, other):
        if not isinstance(other, PollQuestion):
            return False
        return (self.originalText == other.originalText)

class PollVote:
    def __init__(self, **kwargs):
        self.answerIndex = kwargs.get('answerIndex', 0)
        if kwargs.get('poll'):
            self.poll = Poll(**kwargs.get('poll', {}))
        else:
            self.poll = None
        if kwargs.get('user'):
            self.user = UserProfile(**kwargs.get('user', {}))
        else:
            self.user = None
        self.voteTime = kwargs.get('voteTime', "")
    def __eq__(self, other):
        if not isinstance(other, PollVote):
            return False
        return (self.answerIndex == other.answerIndex and self.poll == other.poll and self.user == other.user and self.voteTime == other.voteTime)


class PollVoteConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(PollVote(**node.get("node", {})))


class PollsConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Poll(**node.get("node", {})))

class PrestigiousAwardSummary:
    def __init__(self, **kwargs):
        if kwargs.get('awardNomination'):
            self.awardNomination = AwardNomination(**kwargs.get('awardNomination', {}))
        else:
            self.awardNomination = None
        self.nominations = kwargs.get('nominations', 0)
        self.wins = kwargs.get('wins', 0)
    def __eq__(self, other):
        if not isinstance(other, PrestigiousAwardSummary):
            return False
        return (self.awardNomination == other.awardNomination and self.nominations == other.nominations and self.wins == other.wins)

class PrimaryProfession:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = CreditCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('profession'):
            self.profession = Profession(**kwargs.get('profession', {}))
        else:
            self.profession = None
    def __eq__(self, other):
        if not isinstance(other, PrimaryProfession):
            return False
        return (self.category == other.category and self.profession == other.profession)

class PrimaryWatchOption:
    def __init__(self, **kwargs):
        self.additionalWatchOptionsCount = kwargs.get('additionalWatchOptionsCount', 0)
        if kwargs.get('watchOption'):
            self.watchOption = WatchOption(**kwargs.get('watchOption', {}))
        else:
            self.watchOption = None
    def __eq__(self, other):
        if not isinstance(other, PrimaryWatchOption):
            return False
        return (self.additionalWatchOptionsCount == other.additionalWatchOptionsCount and self.watchOption == other.watchOption)

class PrincipalCreditsForCategory:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = CreditCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('credits'):
            self.credits = Credit(**kwargs.get('credits', {}))
        else:
            self.credits = None
        if kwargs.get('restriction'):
            self.restriction = CreditRestriction(**kwargs.get('restriction', {}))
        else:
            self.restriction = None
        self.totalCredits = kwargs.get('totalCredits', 0)
    def __eq__(self, other):
        if not isinstance(other, PrincipalCreditsForCategory):
            return False
        return (self.category == other.category and self.credits == other.credits and self.restriction == other.restriction and self.totalCredits == other.totalCredits)

class PrincipalCreditsForGrouping:
    def __init__(self, **kwargs):
        if kwargs.get('credits'):
            self.credits = CreditV2(**kwargs.get('credits', {}))
        else:
            self.credits = None
        if kwargs.get('grouping'):
            self.grouping = CreditGrouping(**kwargs.get('grouping', {}))
        else:
            self.grouping = None
        if kwargs.get('restriction'):
            self.restriction = CreditRestriction(**kwargs.get('restriction', {}))
        else:
            self.restriction = None
        self.totalCredits = kwargs.get('totalCredits', 0)
    def __eq__(self, other):
        if not isinstance(other, PrincipalCreditsForGrouping):
            return False
        return (self.credits == other.credits and self.grouping == other.grouping and self.restriction == other.restriction and self.totalCredits == other.totalCredits)

class PrintedFormat:
    def __init__(self, **kwargs):
        if kwargs.get('attributes'):
            self.attributes = [DisplayableAttribute(**attr) for attr in kwargs.get('attributes', [])]
        else:
            self.attributes = None
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableTechnicalSpecificationProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.printedFormat = kwargs.get('printedFormat', "")
    def __eq__(self, other):
        if not isinstance(other, PrintedFormat):
            return False
        return (self.attributes == other.attributes and self.displayableProperty == other.displayableProperty and self.printedFormat == other.printedFormat)

class PrintedFormats:
    def __init__(self, **kwargs):
        if kwargs.get('items'):
            self.items = PrintedFormat(**kwargs.get('items', {}))
        else:
            self.items = None
        if kwargs.get('restriction'):
            self.restriction = TechnicalSpecificationsRestriction(**kwargs.get('restriction', {}))
        else:
            self.restriction = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, PrintedFormats):
            return False
        return (self.items == other.items and self.restriction == other.restriction and self.total == other.total)

class PrivacyDirectives:
    def __init__(self, **kwargs):
        self.avlTcfString = kwargs.get('avlTcfString', "")
        self.crossUseString = kwargs.get('crossUseString', "")
        self.directivesCookie = kwargs.get('directivesCookie', "")
        self.expirationDate = kwargs.get('expirationDate', "")
        self.gvlTcfString = kwargs.get('gvlTcfString', "")
        if kwargs.get('purposes'):
            self.purposes = GranularDirective(**kwargs.get('purposes', {}))
        else:
            self.purposes = None
        if kwargs.get('vendors'):
            self.vendors = GranularDirective(**kwargs.get('vendors', {}))
        else:
            self.vendors = None
    def __eq__(self, other):
        if not isinstance(other, PrivacyDirectives):
            return False
        return (self.avlTcfString == other.avlTcfString and self.crossUseString == other.crossUseString and self.directivesCookie == other.directivesCookie and self.expirationDate == other.expirationDate and self.gvlTcfString == other.gvlTcfString and self.purposes == other.purposes and self.vendors == other.vendors)

class PrivacyDirectivesOutput:
    def __init__(self, **kwargs):
        if kwargs.get('directives'):
            self.directives = PrivacyDirectives(**kwargs.get('directives', {}))
        else:
            self.directives = None
    def __eq__(self, other):
        if not isinstance(other, PrivacyDirectivesOutput):
            return False
        return (self.directives == other.directives)

class PrivacyPrompt:
    def __init__(self, **kwargs):
        if kwargs.get('acceptButtonLabel'):
            self.acceptButtonLabel = PrivacyPromptText(**kwargs.get('acceptButtonLabel', {}))
        else:
            self.acceptButtonLabel = None
        if kwargs.get('customizeButtonLabel'):
            self.customizeButtonLabel = PrivacyPromptText(**kwargs.get('customizeButtonLabel', {}))
        else:
            self.customizeButtonLabel = None
        self.customizeUrl = kwargs.get('customizeUrl', "")
        self.id = kwargs.get('id', "")
        if kwargs.get('promptMarkdown'):
            self.promptMarkdown = LocalizedMarkdown(**kwargs.get('promptMarkdown', {}))
        else:
            self.promptMarkdown = None
        if kwargs.get('rejectButtonLabel'):
            self.rejectButtonLabel = PrivacyPromptText(**kwargs.get('rejectButtonLabel', {}))
        else:
            self.rejectButtonLabel = None
        self.showPromptOnPageLoad = kwargs.get('showPromptOnPageLoad', False)
    def __eq__(self, other):
        if not isinstance(other, PrivacyPrompt):
            return False
        return self.id == other.id

class PrivacyPromptOutput:
    def __init__(self, **kwargs):
        self.expirationDate = kwargs.get('expirationDate', "")
        if kwargs.get('privacyPrompt'):
            self.privacyPrompt = PrivacyPrompt(**kwargs.get('privacyPrompt', {}))
        else:
            self.privacyPrompt = None
    def __eq__(self, other):
        if not isinstance(other, PrivacyPromptOutput):
            return False
        return (self.expirationDate == other.expirationDate and self.privacyPrompt == other.privacyPrompt)

class PrivacyPromptText:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, PrivacyPromptText):
            return False
        return self.id == other.id

class ProStatus:
    def __init__(self, **kwargs):
        self.hasSubscription = kwargs.get('hasSubscription', False)
    def __eq__(self, other):
        if not isinstance(other, ProStatus):
            return False
        return (self.hasSubscription == other.hasSubscription)

class Process:
    def __init__(self, **kwargs):
        if kwargs.get('attributes'):
            self.attributes = [DisplayableAttribute(**attr) for attr in kwargs.get('attributes', [])]
        else:
            self.attributes = None
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableTechnicalSpecificationProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.process = kwargs.get('process', "")
    def __eq__(self, other):
        if not isinstance(other, Process):
            return False
        return (self.attributes == other.attributes and self.displayableProperty == other.displayableProperty and self.process == other.process)

class Processes:
    def __init__(self, **kwargs):
        if kwargs.get('items'):
            self.items = Process(**kwargs.get('items', {}))
        else:
            self.items = None
        if kwargs.get('restriction'):
            self.restriction = TechnicalSpecificationsRestriction(**kwargs.get('restriction', {}))
        else:
            self.restriction = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, Processes):
            return False
        return (self.items == other.items and self.restriction == other.restriction and self.total == other.total)

class ProductionAnnouncement:
    def __init__(self, **kwargs):
        if kwargs.get('comment'):
            self.comment = ProductionAnnouncementComment(**kwargs.get('comment', {}))
        else:
            self.comment = None
        self.date = kwargs.get('date', "")
    def __eq__(self, other):
        if not isinstance(other, ProductionAnnouncement):
            return False
        return (self.comment == other.comment and self.date == other.date)

class ProductionAnnouncementComment:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, ProductionAnnouncementComment):
            return False
        return self.id == other.id

class ProductionBudget:
    def __init__(self, **kwargs):
        if kwargs.get('budget'):
            self.budget = Money(**kwargs.get('budget', {}))
        else:
            self.budget = None
    def __eq__(self, other):
        if not isinstance(other, ProductionBudget):
            return False
        return (self.budget == other.budget)

class ProductionDate:
    def __init__(self, **kwargs):
        if kwargs.get('attributes'):
            self.attributes = [DisplayableAttribute(**attr) for attr in kwargs.get('attributes', [])]
        else:
            self.attributes = None
        if kwargs.get('endDate'):
            self.endDate = DisplayableDate(**kwargs.get('endDate', {}))
        else:
            self.endDate = None
        if kwargs.get('startDate'):
            self.startDate = DisplayableDate(**kwargs.get('startDate', {}))
        else:
            self.startDate = None
    def __eq__(self, other):
        if not isinstance(other, ProductionDate):
            return False
        return (self.attributes == other.attributes and self.endDate == other.endDate and self.startDate == other.startDate)


class ProductionDatesConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(ProductionDate(**node.get("node", {})))

class ProductionStage:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, ProductionStage):
            return False
        return self.id == other.id

class ProductionStatus:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, ProductionStatus):
            return False
        return self.id == other.id

class ProductionStatusDetails:
    def __init__(self, **kwargs):
        if kwargs.get('announcements'):
            self.announcements = ProductionAnnouncement(**kwargs.get('announcements', {}))
        else:
            self.announcements = None
        if kwargs.get('currentProductionStage'):
            self.currentProductionStage = ProductionStage(**kwargs.get('currentProductionStage', {}))
        else:
            self.currentProductionStage = None
        if kwargs.get('productionStatusHistory'):
            self.productionStatusHistory = [ProductionStatusHistory(**history) for history in kwargs.get('productionStatusHistory', [])]
        else:
            self.productionStatusHistory = None
        if kwargs.get('restriction'):
            self.restriction = ProductionStatusHistoryRestriction(**kwargs.get('restriction', {}))
        else:
            self.restriction = None
    def __eq__(self, other):
        if not isinstance(other, ProductionStatusDetails):
            return False
        return (self.announcements == other.announcements and self.currentProductionStage == other.currentProductionStage and self.productionStatusHistory == other.productionStatusHistory and self.restriction == other.restriction)

class ProductionStatusHistory:
    def __init__(self, **kwargs):
        if kwargs.get('comment'):
            self.comment = ProductionStatusHistoryComment(**kwargs.get('comment', {}))
        else:
            self.comment = None
        self.date = kwargs.get('date', "")
        if kwargs.get('stage'):
            self.stage = ProductionStage(**kwargs.get('stage', {}))
        else:
            self.stage = None
        if kwargs.get('status'):
            self.status = ProductionStatus(**kwargs.get('status', {}))
        else:
            self.status = None
    def __eq__(self, other):
        if not isinstance(other, ProductionStatusHistory):
            return False
        return (self.comment == other.comment and self.date == other.date and self.stage == other.stage and self.status == other.status)

class ProductionStatusHistoryComment:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, ProductionStatusHistoryComment):
            return False
        return self.id == other.id

class ProductionStatusHistoryRestriction:
    def __init__(self, **kwargs):
        if kwargs.get('explanations'):
            self.explanations = RestrictionExplanation(**kwargs.get('explanations', {}))
        else:
            self.explanations = None
        self.reasons = kwargs.get('reasons', "")
        self.restrictionReason = kwargs.get('restrictionReason', "")
        self.unrestrictedTotal = kwargs.get('unrestrictedTotal', 0)
    def __eq__(self, other):
        if not isinstance(other, ProductionStatusHistoryRestriction):
            return False
        return (self.explanations == other.explanations and self.reasons == other.reasons and self.restrictionReason == other.restrictionReason and self.unrestrictedTotal == other.unrestrictedTotal)

class Profession:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, Profession):
            return False
        return self.id == other.id

class ProfessionCategory:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('linkedCreditCategory'):
            self.linkedCreditCategory = CreditCategory(**kwargs.get('linkedCreditCategory', {}))
        else:
            self.linkedCreditCategory = None
        self.listOrder = kwargs.get('listOrder', 0)
        if kwargs.get('text'):
            self.text = DisplayableProfessionCategory(**kwargs.get('text', {}))
        else:
            self.text = None
        self.traits = kwargs.get('traits', "")
    def __eq__(self, other):
        if not isinstance(other, ProfessionCategory):
            return False
        return self.id == other.id

class ProfessionCount:
    def __init__(self, **kwargs):
        if kwargs.get('profession'):
            self.profession = NameProfession(**kwargs.get('profession', {}))
        else:
            self.profession = None
        self.totalCount = kwargs.get('totalCount', 0)
    def __eq__(self, other):
        if not isinstance(other, ProfessionCount):
            return False
        return (self.profession == other.profession and self.totalCount == other.totalCount)

class ProfessionCountsSummary:
    def __init__(self, **kwargs):
        if kwargs.get('displayableCounts'):
            self.displayableCounts = LocalizedString(**kwargs.get('displayableCounts', {}))
        else:
            self.displayableCounts = None
        if kwargs.get('professionCounts'):
            self.professionCounts = ProfessionCount(**kwargs.get('professionCounts', {}))
        else:
            self.professionCounts = None
    def __eq__(self, other):
        if not isinstance(other, ProfessionCountsSummary):
            return False
        return (self.displayableCounts == other.displayableCounts and self.professionCounts == other.professionCounts)

class PromotedVideoAd:
    def __init__(self, **kwargs):
        self.adFeedbackUrl = kwargs.get('adFeedbackUrl', "")
        self.id = kwargs.get('id', "")
        if kwargs.get('thirdPartyTrackers'):
            self.thirdPartyTrackers = ThirdPartyTrackers(**kwargs.get('thirdPartyTrackers', {}))
        else:
            self.thirdPartyTrackers = None
        if kwargs.get('video'):
            self.video = Video(**kwargs.get('video', {}))
        else:
            self.video = None
    def __eq__(self, other):
        if not isinstance(other, PromotedVideoAd):
            return False
        return self.id == other.id

class PublicityCategoryWithListings:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = PublicityListingCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('publicityListings'):
            self.publicityListings = PublicityListingCategoryConnection(**kwargs.get('publicityListings', {}))
        else:
            self.publicityListings = None
    def __eq__(self, other):
        if not isinstance(other, PublicityCategoryWithListings):
            return False
        return (self.category == other.category and self.publicityListings == other.publicityListings)

class PublicityListingCategory:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, PublicityListingCategory):
            return False
        return self.id == other.id


class PublicityListingCategoryConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(PublicityListingCategory(**node.get("node", {})))

class PushNotificationUserSettings:
    def __init__(self, **kwargs):
        self.pushNotificationUserId = kwargs.get('pushNotificationUserId', "")
    def __eq__(self, other):
        if not isinstance(other, PushNotificationUserSettings):
            return False
        return (self.pushNotificationUserId == other.pushNotificationUserId)

class QueryStubs:
    def __init__(self, **kwargs):
        if kwargs.get('matrix'):
            self.matrix = Title(**kwargs.get('matrix', {}))
        else:
            self.matrix = None
    def __eq__(self, other):
        if not isinstance(other, QueryStubs):
            return False
        return (self.matrix == other.matrix)

class Question:
    def __init__(self, **kwargs):
        if kwargs.get('answerOptions'):
            self.answerOptions = AnswerOption(**kwargs.get('answerOptions', {}))
        else:
            self.answerOptions = None
        self.answerType = kwargs.get('answerType', "")
        if kwargs.get('contributionLink'):
            self.contributionLink = ContributionQuestionsLink(**kwargs.get('contributionLink', {}))
        else:
            self.contributionLink = None
        self.dataType = kwargs.get('dataType', "")
        self.entityId = kwargs.get('entityId', "")
        self.questionId = kwargs.get('questionId', "")
        if kwargs.get('questionText'):
            self.questionText = Markdown(**kwargs.get('questionText', {}))
        else:
            self.questionText = None
    def __eq__(self, other):
        if not isinstance(other, Question):
            return False
        return (self.answerOptions == other.answerOptions and self.answerType == other.answerType and self.contributionLink == other.contributionLink and self.dataType == other.dataType and self.entityId == other.entityId and self.questionId == other.questionId and self.questionText == other.questionText)


class QuestionConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Question(**node.get("node", {})))

class RankChange:
    def __init__(self, **kwargs):
        self.changeDirection = kwargs.get('changeDirection', "")
        self.difference = kwargs.get('difference', 0)
    def __eq__(self, other):
        if not isinstance(other, RankChange):
            return False
        return (self.changeDirection == other.changeDirection and self.difference == other.difference)

class RankedLifetimeBoxOfficeGross:
    def __init__(self, **kwargs):
        if kwargs.get('boxOfficeAreaType'):
            self.boxOfficeAreaType = BoxOfficeAreaType(**kwargs.get('boxOfficeAreaType', {}))
        else:
            self.boxOfficeAreaType = None
        self.rank = kwargs.get('rank', 0)
        if kwargs.get('total'):
            self.total = Money(**kwargs.get('total', {}))
        else:
            self.total = None
    def __eq__(self, other):
        if not isinstance(other, RankedLifetimeBoxOfficeGross):
            return False
        return (self.boxOfficeAreaType == other.boxOfficeAreaType and self.rank == other.rank and self.total == other.total)


class RankedLifetimeBoxOfficeGrossConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(RankedLifetimeBoxOfficeGross(**node.get("node", {})))

class Rating:
    def __init__(self, **kwargs):
        self.date = kwargs.get('date', "")
        self.value = kwargs.get('value', 0)
    def __eq__(self, other):
        if not isinstance(other, Rating):
            return False
        return (self.date == other.date and self.value == other.value)

class RatingsBody:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, RatingsBody):
            return False
        return self.id == other.id

class RatingsPrivacy:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.setting = kwargs.get('setting', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, RatingsPrivacy):
            return False
        return self.id == other.id

class RatingsResult:
    def __init__(self, **kwargs):
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
        if kwargs.get('userRating'):
            self.userRating = Rating(**kwargs.get('userRating', {}))
        else:
            self.userRating = None
    def __eq__(self, other):
        if not isinstance(other, RatingsResult):
            return False
        return (self.title == other.title and self.userRating == other.userRating)

class RatingsSummary:
    def __init__(self, **kwargs):
        self.aggregateRating = kwargs.get('aggregateRating', 0.0)
        if kwargs.get('notificationText'):
            self.notificationText = LocalizedMarkdown(**kwargs.get('notificationText', {}))
        else:
            self.notificationText = None
        if kwargs.get('topRanking'):
            self.topRanking = TopRanking(**kwargs.get('topRanking', {}))
        else:
            self.topRanking = None
        self.voteCount = kwargs.get('voteCount', 0)
    def __eq__(self, other):
        if not isinstance(other, RatingsSummary):
            return False
        return (self.aggregateRating == other.aggregateRating and self.notificationText == other.notificationText and self.topRanking == other.topRanking and self.voteCount == other.voteCount)

class RatingsSummaryByCountry:
    def __init__(self, **kwargs):
        self.aggregate = kwargs.get('aggregate', 0.0)
        self.country = kwargs.get('country', "")
        if kwargs.get('displayText'):
            self.displayText = LocalizedString(**kwargs.get('displayText', {}))
        else:
            self.displayText = None
        self.voteCount = kwargs.get('voteCount', 0)
    def __eq__(self, other):
        if not isinstance(other, RatingsSummaryByCountry):
            return False
        return (self.aggregate == other.aggregate and self.country == other.country and self.displayText == other.displayText and self.voteCount == other.voteCount)

class Reaction:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.reactionId = kwargs.get('reactionId', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, Reaction):
            return False
        return self.id == other.id

class ReactionSummary:
    def __init__(self, **kwargs):
        self.count = kwargs.get('count', 0)
        if kwargs.get('displayCount'):
            self.displayCount = LocalizedString(**kwargs.get('displayCount', {}))
        else:
            self.displayCount = None
        if kwargs.get('reaction'):
            self.reaction = Reaction(**kwargs.get('reaction', {}))
        else:
            self.reaction = None
    def __eq__(self, other):
        if not isinstance(other, ReactionSummary):
            return False
        return (self.count == other.count and self.displayCount == other.displayCount and self.reaction == other.reaction)

class ReactionSummaryGroup:
    def __init__(self, **kwargs):
        self.aggregateCount = kwargs.get('aggregateCount', 0)
        if kwargs.get('displayCount'):
            self.displayCount = LocalizedString(**kwargs.get('displayCount', {}))
        else:
            self.displayCount = None
        self.groupId = kwargs.get('groupId', "")
        if kwargs.get('reactionSummaries'):
            self.reactionSummaries = ReactionSummary(**kwargs.get('reactionSummaries', {}))
        else:
            self.reactionSummaries = None
        self.selectionType = kwargs.get('selectionType', "")
    def __eq__(self, other):
        if not isinstance(other, ReactionSummaryGroup):
            return False
        return (self.aggregateCount == other.aggregateCount and self.displayCount == other.displayCount and self.groupId == other.groupId and self.reactionSummaries == other.reactionSummaries and self.selectionType == other.selectionType)

class ReactionsSummary:
    def __init__(self, **kwargs):
        if kwargs.get('reactionSummaryGroups'):
            self.reactionSummaryGroups = ReactionSummaryGroup(**kwargs.get('reactionSummaryGroups', {}))
        else:
            self.reactionSummaryGroups = None
    def __eq__(self, other):
        if not isinstance(other, ReactionsSummary):
            return False
        return (self.reactionSummaryGroups == other.reactionSummaryGroups)

class RecentlyViewedStatistics:
    def __init__(self, **kwargs):
        if kwargs.get('professionCountsSummary'):
            self.professionCountsSummary = ProfessionCountsSummary(**kwargs.get('professionCountsSummary', {}))
        else:
            self.professionCountsSummary = None
        self.uniquePageViewCount = kwargs.get('uniquePageViewCount', 0)
    def __eq__(self, other):
        if not isinstance(other, RecentlyViewedStatistics):
            return False
        return (self.professionCountsSummary == other.professionCountsSummary and self.uniquePageViewCount == other.uniquePageViewCount)

class RecommendationExplanation:
    def __init__(self, **kwargs):
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, RecommendationExplanation):
            return False
        return (self.title == other.title)

class RedirectLink:
    def __init__(self, **kwargs):
        if kwargs.get('label'):
            self.label = LocalizedString(**kwargs.get('label', {}))
        else:
            self.label = None
        self.url = kwargs.get('url', "")
    def __eq__(self, other):
        if not isinstance(other, RedirectLink):
            return False
        return (self.label == other.label and self.url == other.url)

class RefTag:
    def __init__(self, **kwargs):
        self.ep13nReftag = kwargs.get('ep13nReftag', "")
    def __eq__(self, other):
        if not isinstance(other, RefTag):
            return False
        return (self.ep13nReftag == other.ep13nReftag)

class RelatedNews:
    def __init__(self, **kwargs):
        if kwargs.get('items'):
            self.items = News(**kwargs.get('items', {}))
        else:
            self.items = None
    def __eq__(self, other):
        if not isinstance(other, RelatedNews):
            return False
        return (self.items == other.items)

class RelationName:
    def __init__(self, **kwargs):
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableRelationNameProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        if kwargs.get('name'):
            self.name = Name(**kwargs.get('name', {}))
        else:
            self.name = None
        self.nameText = kwargs.get('nameText', "")
    def __eq__(self, other):
        if not isinstance(other, RelationName):
            return False
        return (self.displayableProperty == other.displayableProperty and self.name == other.name and self.nameText == other.nameText)

class ReleaseDate:
    def __init__(self, **kwargs):
        if kwargs.get('attributes'):
            self.attributes = [DisplayableAttribute(**attr) for attr in kwargs.get('attributes', [])]
        else:
            self.attributes = None
        if kwargs.get('country'):
            self.country = LocalizedDisplayableCountry(**kwargs.get('country', {}))
        else:
            self.country = None
        self.day = kwargs.get('day', 0)
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableTitleReleaseDateProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.month = kwargs.get('month', 0)
        if kwargs.get('restriction'):
            self.restriction = ReleaseDateRestriction(**kwargs.get('restriction', {}))
        else:
            self.restriction = None
        self.year = kwargs.get('year', 0)
    def __eq__(self, other):
        if not isinstance(other, ReleaseDate):
            return False
        return (self.attributes == other.attributes and self.country == other.country and self.day == other.day and self.displayableProperty == other.displayableProperty and self.month == other.month and self.restriction == other.restriction and self.year == other.year)


class ReleaseDateConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(ReleaseDate(**node.get("node", {})))

class ReleaseDateRestriction:
    def __init__(self, **kwargs):
        if kwargs.get('explanations'):
            self.explanations = RestrictionExplanation(**kwargs.get('explanations', {}))
        else:
            self.explanations = None
        self.reasons = kwargs.get('reasons', "")
        self.restrictionReason = kwargs.get('restrictionReason', "")
    def __eq__(self, other):
        if not isinstance(other, ReleaseDateRestriction):
            return False
        return (self.explanations == other.explanations and self.reasons == other.reasons and self.restrictionReason == other.restrictionReason)

class ReleaseYear:
    def __init__(self, **kwargs):
        self.year = kwargs.get('year', 0)
    def __eq__(self, other):
        if not isinstance(other, ReleaseYear):
            return False
        return (self.year == other.year)

class RepresentationRelationshipType:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.relationshipTypeId = kwargs.get('relationshipTypeId', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, RepresentationRelationshipType):
            return False
        return self.id == other.id

class RestrictionExplanation:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.reason = kwargs.get('reason', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, RestrictionExplanation):
            return False
        return self.id == other.id

class Resume:
    def __init__(self, **kwargs):
        if kwargs.get('additionalAwards'):
            self.additionalAwards = SelfVerifiedAwardConnection(**kwargs.get('additionalAwards', {}))
        else:
            self.additionalAwards = None
        if kwargs.get('additionalCreditCategories'):
            self.additionalCreditCategories = ResumeAdditionalCreditsCategories(**kwargs.get('additionalCreditCategories', {}))
        else:
            self.additionalCreditCategories = None
        if kwargs.get('additionalResumeInfo'):
            self.additionalResumeInfo = AdditionalResumeInfoConnection(**kwargs.get('additionalResumeInfo', {}))
        else:
            self.additionalResumeInfo = None
        if kwargs.get('education'):
            self.education = SelfVerifiedEducationConnection(**kwargs.get('education', {}))
        else:
            self.education = None
        if kwargs.get('performerProfile'):
            self.performerProfile = ResumeDataItem(**kwargs.get('performerProfile', {}))
        else:
            self.performerProfile = None
        if kwargs.get('personalDetails'):
            self.personalDetails = ResumeDataItem(**kwargs.get('personalDetails', {}))
        else:
            self.personalDetails = None
        if kwargs.get('professionalBackground'):
            self.professionalBackground = ResumeDataItem(**kwargs.get('professionalBackground', {}))
        else:
            self.professionalBackground = None
        if kwargs.get('references'):
            self.references = SelfVerifiedReferenceConnection(**kwargs.get('references', {}))
        else:
            self.references = None
        if kwargs.get('skills'):
            self.skills = ResumeDataItem(**kwargs.get('skills', {}))
        else:
            self.skills = None
        if kwargs.get('training'):
            self.training = SelfVerifiedTrainingConnection(**kwargs.get('training', {}))
        else:
            self.training = None
    def __eq__(self, other):
        if not isinstance(other, Resume):
            return False
        return (self.additionalAwards == other.additionalAwards and self.additionalCreditCategories == other.additionalCreditCategories and self.additionalResumeInfo == other.additionalResumeInfo and self.education == other.education and self.performerProfile == other.performerProfile and self.personalDetails == other.personalDetails and self.professionalBackground == other.professionalBackground and self.references == other.references and self.skills == other.skills and self.training == other.training)

class ResumeAdditionalCreditsCategories:
    def __init__(self, **kwargs):
        if kwargs.get('categories'):
            self.categories = ResumeAdditionalCreditsCategory(**kwargs.get('categories', {}))
        else:
            self.categories = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, ResumeAdditionalCreditsCategories):
            return False
        return (self.categories == other.categories and self.total == other.total)

class ResumeAdditionalCreditsCategory:
    def __init__(self, **kwargs):
        if kwargs.get('credits'):
            self.credits = AdditionalCreditItem(**kwargs.get('credits', {}))
        else:
            self.credits = None
        self.id = kwargs.get('id', "")
        if kwargs.get('title'):
            self.title = LocalizedString(**kwargs.get('title', {}))
        else:
            self.title = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, ResumeAdditionalCreditsCategory):
            return False
        return self.id == other.id

class ResumeDataItem:
    def __init__(self, **kwargs):
        if kwargs.get('label'):
            self.label = LocalizedString(**kwargs.get('label', {}))
        else:
            self.label = None
        if kwargs.get('values'):
            self.values = LocalizedString(**kwargs.get('values', {}))
        else:
            self.values = None
    def __eq__(self, other):
        if not isinstance(other, ResumeDataItem):
            return False
        return (self.label == other.label and self.values == other.values)

class RetrieveAccountDataOutput:
    def __init__(self, **kwargs):
        if kwargs.get('fileMetadata'):
            self.fileMetadata = FileMetadata(**kwargs.get('fileMetadata', {}))
        else:
            self.fileMetadata = None
        if kwargs.get('message'):
            self.message = LocalizedMarkdown(**kwargs.get('message', {}))
        else:
            self.message = None
        self.success = kwargs.get('success', False)
        if kwargs.get('title'):
            self.title = LocalizedMarkdown(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, RetrieveAccountDataOutput):
            return False
        return (self.fileMetadata == other.fileMetadata and self.message == other.message and self.success == other.success and self.title == other.title)

class Review:
    def __init__(self, **kwargs):
        if kwargs.get('author'):
            self.author = UserProfile(**kwargs.get('author', {}))
        else:
            self.author = None
        self.authorRating = kwargs.get('authorRating', 0)
        if kwargs.get('_correctionLink'):
            self._correctionLink = ContributionLink(**kwargs.get('_correctionLink', {}))
        else:
            self._correctionLink = None
        if kwargs.get('deletionLink'):
            self.deletionLink = ContributionLink(**kwargs.get('deletionLink', {}))
        else:
            self.deletionLink = None
        if kwargs.get('helpfulness'):
            self.helpfulness = ReviewHelpfulness(**kwargs.get('helpfulness', {}))
        else:
            self.helpfulness = None
        self.id = kwargs.get('id', "")
        self.language = kwargs.get('language', "")
        if kwargs.get('_reportingLink'):
            self._reportingLink = ContributionLink(**kwargs.get('_reportingLink', {}))
        else:
            self._reportingLink = None
        self.spoiler = kwargs.get('spoiler', False)
        self.submissionDate = kwargs.get('submissionDate', "")
        if kwargs.get('summary'):
            self.summary = ReviewSummary(**kwargs.get('summary', {}))
        else:
            self.summary = None
        if kwargs.get('text'):
            self.text = ReviewText(**kwargs.get('text', {}))
        else:
            self.text = None
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
    def __str__(self):
        return str(self.text) if self.text else str(self.summary)
    def __repr__(self):
        return f"Review(id={self.id}, language={self.language}, text={self.text}, summary={self.summary})"
    def __eq__(self, other):
        if not isinstance(other, Review):
            return False
        return self.id == other.id

class ReviewHelpfulness:
    def __init__(self, **kwargs):
        self.downVotes = kwargs.get('downVotes', 0)
        self.score = kwargs.get('score', 0.0)
        self.upVotes = kwargs.get('upVotes', 0)
    def __str__(self):
        if self.score:
            return str(self.score)
        elif self.upVotes and self.downVotes:
            return str(self.upVotes/self.downVotes)
        return "0"
    def __float__(self):
        return float(self.score)
    def __int__(self):
        return int(self.score)
    def __repr__(self):
        return f"ReviewHelpfulness(downVotes={self.downVotes}, score={self.score}, upVotes={self.upVotes})"
    def __eq__(self, other):
        if not isinstance(other, ReviewHelpfulness):
            return False
        return (self.downVotes == other.downVotes and self.score == other.score and self.upVotes == other.upVotes)

class ReviewSummary:
    def __init__(self, **kwargs):
        self.originalText = kwargs.get('originalText', "")
    def __str__(self):
        return self.originalText
    def __repr__(self):
        return f"ReviewSummary(originalText={self.originalText})"
    def __eq__(self, other):
        if not isinstance(other, ReviewSummary):
            return False
        return (self.originalText == other.originalText)

class ReviewText:
    def __init__(self, **kwargs):
        if kwargs.get('originalText'):
            self.originalText = Markdown(**kwargs.get('originalText', {}))
        else:
            self.originalText = None
    def __str__(self):
        return str(self.originalText) if self.originalText else ""
    def __repr__(self):
        return f"ReviewText(originalText={self.originalText})"
    def __eq__(self, other):
        if not isinstance(other, ReviewText):
            return False
        return (self.originalText == other.originalText)


class ReviewsConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Review(**node.get("node", {})))

class Runtime:
    def __init__(self, **kwargs):
        if kwargs.get('attributes'):
            self.attributes = [DisplayableAttribute(**attr) for attr in kwargs.get('attributes', [])]
        else:
            self.attributes = None
        if kwargs.get('country'):
            self.country = DisplayableCountry(**kwargs.get('country', {}))
        else:
            self.country = None
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableTitleRuntimeProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.id = kwargs.get('id', "")
        self.seconds = kwargs.get('seconds', 0)
    def __str__(self):
        return str(self.displayableProperty) if self.displayableProperty else f"{self.seconds} seconds"
    def __repr__(self):
        return f"Runtime(id={self.id}, seconds={self.seconds}, displayableProperty={self.displayableProperty})"
    def __int__(self):
        return self.seconds
    def __eq__(self, other):
        if not isinstance(other, Runtime):
            return False
        return self.id == other.id


class RuntimeConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Runtime(**node.get("node", {})))

class Salary:
    def __init__(self, **kwargs):
        if kwargs.get('amount'):
            self.amount = Money(**kwargs.get('amount', {}))
        else:
            self.amount = None
        if kwargs.get('attributes'):
            self.attributes = [DisplayableAttribute(**attr) for attr in kwargs.get('attributes', [])]
        else:
            self.attributes = None
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableSalaryProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.id = kwargs.get('id', "")
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
    def __str__(self):
        return str(self.displayableProperty) if self.displayableProperty else str(self.amount)
    def __repr__(self):
        return f"Salary(id={self.id}, amount={self.amount}, displayableProperty={self.displayableProperty}, title={self.title})"
    def __int__(self):
        return int(self.amount) if self.amount else 0
    def __float__(self):
        return float(self.amount) if self.amount else 0.0
    def __eq__(self, other):
        if not isinstance(other, Salary):
            return False
        return self.id == other.id

# GOTO HERE
class SalaryConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Salary(**node.get("node", {})))

class ScreeningDateTime:
    def __init__(self, **kwargs):
        self.dateTime = kwargs.get('dateTime', "")
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, ScreeningDateTime):
            return False
        return self.id == other.id

class SearchAwardCategory:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, SearchAwardCategory):
            return False
        return self.id == other.id

class SearchAwardEvent:
    def __init__(self, **kwargs):
        if kwargs.get('awardCategories'):
            self.awardCategories = SearchAwardCategory(**kwargs.get('awardCategories', {}))
        else:
            self.awardCategories = None
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, SearchAwardEvent):
            return False
        return self.id == other.id

class SearchAwardEventOptions:
    def __init__(self, **kwargs):
        if kwargs.get('events'):
            self.events = SearchAwardEvent(**kwargs.get('events', {}))
        else:
            self.events = None
    def __eq__(self, other):
        if not isinstance(other, SearchAwardEventOptions):
            return False
        return (self.events == other.events)

class SearchFacet:
    def __init__(self, **kwargs):
        self.filterId = kwargs.get('filterId', "")
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, SearchFacet):
            return False
        return self.id == other.id


class SearchFacetConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(SearchFacet(**node.get("node", {})))

class SearchMetadata:
    def __init__(self, **kwargs):
        if kwargs.get('advancedSearchAwardOptions'):
            self.advancedSearchAwardOptions = SearchAwardEventOptions(**kwargs.get('advancedSearchAwardOptions', {}))
        else:
            self.advancedSearchAwardOptions = None
    def __eq__(self, other):
        if not isinstance(other, SearchMetadata):
            return False
        return (self.advancedSearchAwardOptions == other.advancedSearchAwardOptions)

class SeasonValueDisplayableProperty:
    def __init__(self, **kwargs):
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __eq__(self, other):
        if not isinstance(other, SeasonValueDisplayableProperty):
            return False
        return (self.value == other.value)

class SectionCallToAction:
    def __init__(self, **kwargs):
        if kwargs.get('action'):
            self.action = ActionLink(**kwargs.get('action', {}))
        else:
            self.action = None
        self.resultId = kwargs.get('resultId', 0)
        if kwargs.get('sectionContent'):
            self.sectionContent = CallToActionText(**kwargs.get('sectionContent', {}))
        else:
            self.sectionContent = None
        if kwargs.get('sectionTitle'):
            self.sectionTitle = CallToActionText(**kwargs.get('sectionTitle', {}))
        else:
            self.sectionTitle = None
    def __eq__(self, other):
        if not isinstance(other, SectionCallToAction):
            return False
        return (self.action == other.action and self.resultId == other.resultId and self.sectionContent == other.sectionContent and self.sectionTitle == other.sectionTitle)

class SelfVerified:
    def __init__(self, **kwargs):
        self.isSelfVerified = kwargs.get('isSelfVerified', False)
    def __eq__(self, other):
        if not isinstance(other, SelfVerified):
            return False
        return (self.isSelfVerified == other.isSelfVerified)

class SelfVerifiedAward:
    def __init__(self, **kwargs):
        if kwargs.get('awardTitle'):
            self.awardTitle = LocalizedString(**kwargs.get('awardTitle', {}))
        else:
            self.awardTitle = None
        if kwargs.get('details'):
            self.details = LocalizedString(**kwargs.get('details', {}))
        else:
            self.details = None
        if kwargs.get('event'):
            self.event = LocalizedString(**kwargs.get('event', {}))
        else:
            self.event = None
        self.id = kwargs.get('id', "")
        self.year = kwargs.get('year', 0)
    def __eq__(self, other):
        if not isinstance(other, SelfVerifiedAward):
            return False
        return self.id == other.id


class SelfVerifiedAwardConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(SelfVerifiedAward(**node.get("node", {})))

class SelfVerifiedEducation:
    def __init__(self, **kwargs):
        if kwargs.get('degree'):
            self.degree = LocalizedString(**kwargs.get('degree', {}))
        else:
            self.degree = None
        if kwargs.get('details'):
            self.details = LocalizedString(**kwargs.get('details', {}))
        else:
            self.details = None
        self.id = kwargs.get('id', "")
        if kwargs.get('location'):
            self.location = LocalizedString(**kwargs.get('location', {}))
        else:
            self.location = None
        if kwargs.get('school'):
            self.school = LocalizedString(**kwargs.get('school', {}))
        else:
            self.school = None
        self.year = kwargs.get('year', 0)
    def __eq__(self, other):
        if not isinstance(other, SelfVerifiedEducation):
            return False
        return self.id == other.id


class SelfVerifiedEducationConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(SelfVerifiedEducation(**node.get("node", {})))

class SelfVerifiedNameAttribute:
    def __init__(self, **kwargs):
        self.total = kwargs.get('total', 0)
        if kwargs.get('values'):
            self.values = SelfVerifiedNameAttributeValue(**kwargs.get('values', {}))
        else:
            self.values = None
    def __eq__(self, other):
        if not isinstance(other, SelfVerifiedNameAttribute):
            return False
        return (self.total == other.total and self.values == other.values)

class SelfVerifiedNameAttributeMetadata:
    def __init__(self, **kwargs):
        self.allowFreeFormText = kwargs.get('allowFreeFormText', False)
        self.limit = kwargs.get('limit', 0)
        if kwargs.get('validValues'):
            self.validValues = SelfVerifiedNameAttributeValue(**kwargs.get('validValues', {}))
        else:
            self.validValues = None
    def __eq__(self, other):
        if not isinstance(other, SelfVerifiedNameAttributeMetadata):
            return False
        return (self.allowFreeFormText == other.allowFreeFormText and self.limit == other.limit and self.validValues == other.validValues)

class SelfVerifiedNameAttributeValue:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, SelfVerifiedNameAttributeValue):
            return False
        return self.id == other.id

class SelfVerifiedNameAward:
    def __init__(self, **kwargs):
        if kwargs.get('details'):
            self.details = SelfVerifiedNameAttributeValue(**kwargs.get('details', {}))
        else:
            self.details = None
        if kwargs.get('event'):
            self.event = SelfVerifiedNameAttributeValue(**kwargs.get('event', {}))
        else:
            self.event = None
        self.id = kwargs.get('id', "")
        if kwargs.get('name'):
            self.name = SelfVerifiedNameAttributeValue(**kwargs.get('name', {}))
        else:
            self.name = None
        self.year = kwargs.get('year', 0)
    def __eq__(self, other):
        if not isinstance(other, SelfVerifiedNameAward):
            return False
        return self.id == other.id


class SelfVerifiedNameAwardConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(SelfVerifiedNameAward(**node.get("node", {})))

class SelfVerifiedNameCredit:
    def __init__(self, **kwargs):
        if kwargs.get('companyOrDirector'):
            self.companyOrDirector = SelfVerifiedNameAttributeValue(**kwargs.get('companyOrDirector', {}))
        else:
            self.companyOrDirector = None
        self.id = kwargs.get('id', "")
        if kwargs.get('projectTitle'):
            self.projectTitle = SelfVerifiedNameAttributeValue(**kwargs.get('projectTitle', {}))
        else:
            self.projectTitle = None
        if kwargs.get('roleOrPosition'):
            self.roleOrPosition = SelfVerifiedNameAttributeValue(**kwargs.get('roleOrPosition', {}))
        else:
            self.roleOrPosition = None
        if kwargs.get('type'):
            self.type = SelfVerifiedNameCreditType(**kwargs.get('type', {}))
        else:
            self.type = None
    def __eq__(self, other):
        if not isinstance(other, SelfVerifiedNameCredit):
            return False
        return self.id == other.id


class SelfVerifiedNameCreditConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(SelfVerifiedNameCredit(**node.get("node", {})))

class SelfVerifiedNameCreditMetadata:
    def __init__(self, **kwargs):
        if kwargs.get('creditTypes'):
            self.creditTypes = SelfVerifiedNameCreditType(**kwargs.get('creditTypes', {}))
        else:
            self.creditTypes = None
        self.limit = kwargs.get('limit', 0)
    def __eq__(self, other):
        if not isinstance(other, SelfVerifiedNameCreditMetadata):
            return False
        return (self.creditTypes == other.creditTypes and self.limit == other.limit)

class SelfVerifiedNameCreditType:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, SelfVerifiedNameCreditType):
            return False
        return self.id == other.id

class SelfVerifiedNameCreditTypeWithCredits:
    def __init__(self, **kwargs):
        if kwargs.get('credits'):
            self.credits = SelfVerifiedNameCreditConnection(**kwargs.get('credits', {}))
        else:
            self.credits = None
        if kwargs.get('creditType'):
            self.creditType = SelfVerifiedNameCreditType(**kwargs.get('creditType', {}))
        else:
            self.creditType = None
    def __eq__(self, other):
        if not isinstance(other, SelfVerifiedNameCreditTypeWithCredits):
            return False
        return (self.credits == other.credits and self.creditType == other.creditType)

class SelfVerifiedNameData:
    def __init__(self, **kwargs):
        if kwargs.get('accents'):
            self.accents = SelfVerifiedNameAttribute(**kwargs.get('accents', {}))
        else:
            self.accents = None
        if kwargs.get('agePlayingRange'):
            self.agePlayingRange = AgePlayingRange(**kwargs.get('agePlayingRange', {}))
        else:
            self.agePlayingRange = None
        if kwargs.get('athleticSkills'):
            self.athleticSkills = SelfVerifiedNameAttribute(**kwargs.get('athleticSkills', {}))
        else:
            self.athleticSkills = None
        if kwargs.get('awards'):
            self.awards = SelfVerifiedNameAwardConnection(**kwargs.get('awards', {}))
        else:
            self.awards = None
        if kwargs.get('blog'):
            self.blog = BlogLink(**kwargs.get('blog', {}))
        else:
            self.blog = None
        if kwargs.get('creditTypes'):
            self.creditTypes = SelfVerifiedNameCreditTypeWithCredits(**kwargs.get('creditTypes', {}))
        else:
            self.creditTypes = None
        if kwargs.get('danceSkills'):
            self.danceSkills = SelfVerifiedNameAttribute(**kwargs.get('danceSkills', {}))
        else:
            self.danceSkills = None
        if kwargs.get('educationalHistory'):
            self.educationalHistory = SelfVerifiedNameEducationConnection(**kwargs.get('educationalHistory', {}))
        else:
            self.educationalHistory = None
        if kwargs.get('ethnicAppearances'):
            self.ethnicAppearances = SelfVerifiedNameAttribute(**kwargs.get('ethnicAppearances', {}))
        else:
            self.ethnicAppearances = None
        if kwargs.get('eyeColor'):
            self.eyeColor = SelfVerifiedNameAttributeValue(**kwargs.get('eyeColor', {}))
        else:
            self.eyeColor = None
        if kwargs.get('guildAffiliations'):
            self.guildAffiliations = GuildAffiliationVerificationStatusConnection(**kwargs.get('guildAffiliations', {}))
        else:
            self.guildAffiliations = None
        if kwargs.get('guildAffiliationVisibilities'):
            self.guildAffiliationVisibilities = GuildAffiliationVisibilityStatusConnection(**kwargs.get('guildAffiliationVisibilities', {}))
        else:
            self.guildAffiliationVisibilities = None
        if kwargs.get('guildStatus'):
            self.guildStatus = GuildStatus(**kwargs.get('guildStatus', {}))
        else:
            self.guildStatus = None
        if kwargs.get('hairColor'):
            self.hairColor = SelfVerifiedNameAttributeValue(**kwargs.get('hairColor', {}))
        else:
            self.hairColor = None
        if kwargs.get('hairLength'):
            self.hairLength = SelfVerifiedNameAttributeValue(**kwargs.get('hairLength', {}))
        else:
            self.hairLength = None
        self.hasValidPassport = kwargs.get('hasValidPassport', False)
        self.isWillingToWorkUnpaid = kwargs.get('isWillingToWorkUnpaid', False)
        if kwargs.get('jobCategories'):
            self.jobCategories = SelfVerifiedNameAttribute(**kwargs.get('jobCategories', {}))
        else:
            self.jobCategories = None
        if kwargs.get('jobTitles'):
            self.jobTitles = SelfVerifiedNameAttribute(**kwargs.get('jobTitles', {}))
        else:
            self.jobTitles = None
        if kwargs.get('musicalInstruments'):
            self.musicalInstruments = SelfVerifiedNameAttribute(**kwargs.get('musicalInstruments', {}))
        else:
            self.musicalInstruments = None
        if kwargs.get('performerSkills'):
            self.performerSkills = SelfVerifiedNameAttribute(**kwargs.get('performerSkills', {}))
        else:
            self.performerSkills = None
        if kwargs.get('personalLocations'):
            self.personalLocations = NamePersonalLocations(**kwargs.get('personalLocations', {}))
        else:
            self.personalLocations = None
        if kwargs.get('physique'):
            self.physique = SelfVerifiedNameAttributeValue(**kwargs.get('physique', {}))
        else:
            self.physique = None
        if kwargs.get('primaryCitizenship'):
            self.primaryCitizenship = LocalizedDisplayableCountry(**kwargs.get('primaryCitizenship', {}))
        else:
            self.primaryCitizenship = None
        if kwargs.get('references'):
            self.references = SelfVerifiedNameReferenceConnection(**kwargs.get('references', {}))
        else:
            self.references = None
        if kwargs.get('resumeCustomSections'):
            self.resumeCustomSections = SelfVerifiedResumeCustomSectionConnection(**kwargs.get('resumeCustomSections', {}))
        else:
            self.resumeCustomSections = None
        if kwargs.get('resumeDetails'):
            self.resumeDetails = SelfVerifiedNameAttributeValue(**kwargs.get('resumeDetails', {}))
        else:
            self.resumeDetails = None
        if kwargs.get('spokenLanguages'):
            self.spokenLanguages = SelfVerifiedNameAttribute(**kwargs.get('spokenLanguages', {}))
        else:
            self.spokenLanguages = None
        if kwargs.get('trainings'):
            self.trainings = SelfVerifiedNameTrainingConnection(**kwargs.get('trainings', {}))
        else:
            self.trainings = None
        if kwargs.get('twitter'):
            self.twitter = TwitterLink(**kwargs.get('twitter', {}))
        else:
            self.twitter = None
        if kwargs.get('uniqueTraits'):
            self.uniqueTraits = SelfVerifiedNameAttribute(**kwargs.get('uniqueTraits', {}))
        else:
            self.uniqueTraits = None
        if kwargs.get('voiceTypes'):
            self.voiceTypes = SelfVerifiedNameAttribute(**kwargs.get('voiceTypes', {}))
        else:
            self.voiceTypes = None
        if kwargs.get('weight'):
            self.weight = NameWeight(**kwargs.get('weight', {}))
        else:
            self.weight = None
        if kwargs.get('workAuthorizationCountries'):
            self.workAuthorizationCountries = WorkAuthorizationCountries(**kwargs.get('workAuthorizationCountries', {}))
        else:
            self.workAuthorizationCountries = None
        if kwargs.get('workHistoryCreditTypes'):
            self.workHistoryCreditTypes = SelfVerifiedNameAttribute(**kwargs.get('workHistoryCreditTypes', {}))
        else:
            self.workHistoryCreditTypes = None
    def __eq__(self, other):
        if not isinstance(other, SelfVerifiedNameData):
            return False
        return (self.accents == other.accents and self.agePlayingRange == other.agePlayingRange and self.athleticSkills == other.athleticSkills and self.awards == other.awards and self.blog == other.blog and self.creditTypes == other.creditTypes and self.danceSkills == other.danceSkills and self.educationalHistory == other.educationalHistory and self.ethnicAppearances == other.ethnicAppearances and self.eyeColor == other.eyeColor and self.guildAffiliations == other.guildAffiliations and self.guildAffiliationVisibilities == other.guildAffiliationVisibilities and self.guildStatus == other.guildStatus and self.hairColor == other.hairColor and self.hairLength == other.hairLength and self.hasValidPassport == other.hasValidPassport and self.isWillingToWorkUnpaid == other.isWillingToWorkUnpaid and self.jobCategories == other.jobCategories and self.jobTitles == other.jobTitles and self.musicalInstruments == other.musicalInstruments and self.performerSkills == other.performerSkills and self.personalLocations == other.personalLocations and self.physique == other.physique and self.primaryCitizenship == other.primaryCitizenship and self.references == other.references and self.resumeCustomSections == other.resumeCustomSections and self.resumeDetails == other.resumeDetails and self.spokenLanguages == other.spokenLanguages and self.trainings == other.trainings and self.twitter == other.twitter and self.uniqueTraits == other.uniqueTraits and self.voiceTypes == other.voiceTypes and self.weight == other.weight and self.workAuthorizationCountries == other.workAuthorizationCountries and self.workHistoryCreditTypes == other.workHistoryCreditTypes)

class SelfVerifiedNameEducation:
    def __init__(self, **kwargs):
        if kwargs.get('degree'):
            self.degree = SelfVerifiedNameAttributeValue(**kwargs.get('degree', {}))
        else:
            self.degree = None
        if kwargs.get('details'):
            self.details = SelfVerifiedNameAttributeValue(**kwargs.get('details', {}))
        else:
            self.details = None
        self.id = kwargs.get('id', "")
        if kwargs.get('location'):
            self.location = SelfVerifiedNameAttributeValue(**kwargs.get('location', {}))
        else:
            self.location = None
        if kwargs.get('school'):
            self.school = SelfVerifiedNameAttributeValue(**kwargs.get('school', {}))
        else:
            self.school = None
        self.year = kwargs.get('year', 0)
    def __eq__(self, other):
        if not isinstance(other, SelfVerifiedNameEducation):
            return False
        return self.id == other.id


class SelfVerifiedNameEducationConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(SelfVerifiedNameEducation(**node.get("node", {})))

class SelfVerifiedNameMetadata:
    def __init__(self, **kwargs):
        if kwargs.get('accent'):
            self.accent = SelfVerifiedNameAttributeMetadata(**kwargs.get('accent', {}))
        else:
            self.accent = None
        if kwargs.get('athleticSkill'):
            self.athleticSkill = SelfVerifiedNameAttributeMetadata(**kwargs.get('athleticSkill', {}))
        else:
            self.athleticSkill = None
        if kwargs.get('award'):
            self.award = SelfVerifiedNameAttributeMetadata(**kwargs.get('award', {}))
        else:
            self.award = None
        if kwargs.get('credit'):
            self.credit = SelfVerifiedNameCreditMetadata(**kwargs.get('credit', {}))
        else:
            self.credit = None
        if kwargs.get('danceSkill'):
            self.danceSkill = SelfVerifiedNameAttributeMetadata(**kwargs.get('danceSkill', {}))
        else:
            self.danceSkill = None
        if kwargs.get('educationalHistory'):
            self.educationalHistory = SelfVerifiedNameAttributeMetadata(**kwargs.get('educationalHistory', {}))
        else:
            self.educationalHistory = None
        if kwargs.get('ethnicAppearance'):
            self.ethnicAppearance = SelfVerifiedNameAttributeMetadata(**kwargs.get('ethnicAppearance', {}))
        else:
            self.ethnicAppearance = None
        if kwargs.get('eyeColor'):
            self.eyeColor = SelfVerifiedNameAttributeMetadata(**kwargs.get('eyeColor', {}))
        else:
            self.eyeColor = None
        if kwargs.get('guildAffiliation'):
            self.guildAffiliation = SelfVerifiedNameAttributeMetadata(**kwargs.get('guildAffiliation', {}))
        else:
            self.guildAffiliation = None
        if kwargs.get('hairColor'):
            self.hairColor = SelfVerifiedNameAttributeMetadata(**kwargs.get('hairColor', {}))
        else:
            self.hairColor = None
        if kwargs.get('hairLength'):
            self.hairLength = SelfVerifiedNameAttributeMetadata(**kwargs.get('hairLength', {}))
        else:
            self.hairLength = None
        if kwargs.get('jobCategory'):
            self.jobCategory = SelfVerifiedNameAttributeMetadata(**kwargs.get('jobCategory', {}))
        else:
            self.jobCategory = None
        if kwargs.get('jobTitle'):
            self.jobTitle = SelfVerifiedNameAttributeMetadata(**kwargs.get('jobTitle', {}))
        else:
            self.jobTitle = None
        if kwargs.get('musicalInstrument'):
            self.musicalInstrument = SelfVerifiedNameAttributeMetadata(**kwargs.get('musicalInstrument', {}))
        else:
            self.musicalInstrument = None
        if kwargs.get('performerSkill'):
            self.performerSkill = SelfVerifiedNameAttributeMetadata(**kwargs.get('performerSkill', {}))
        else:
            self.performerSkill = None
        if kwargs.get('personalLocation'):
            self.personalLocation = NamePersonalLocationMetadata(**kwargs.get('personalLocation', {}))
        else:
            self.personalLocation = None
        if kwargs.get('physique'):
            self.physique = SelfVerifiedNameAttributeMetadata(**kwargs.get('physique', {}))
        else:
            self.physique = None
        if kwargs.get('primaryCitizenship'):
            self.primaryCitizenship = CountryAttributeMetadata(**kwargs.get('primaryCitizenship', {}))
        else:
            self.primaryCitizenship = None
        if kwargs.get('reference'):
            self.reference = SelfVerifiedNameAttributeMetadata(**kwargs.get('reference', {}))
        else:
            self.reference = None
        if kwargs.get('resumeCustomSection'):
            self.resumeCustomSection = SelfVerifiedNameAttributeMetadata(**kwargs.get('resumeCustomSection', {}))
        else:
            self.resumeCustomSection = None
        if kwargs.get('spokenLanguage'):
            self.spokenLanguage = SelfVerifiedNameAttributeMetadata(**kwargs.get('spokenLanguage', {}))
        else:
            self.spokenLanguage = None
        if kwargs.get('training'):
            self.training = SelfVerifiedNameAttributeMetadata(**kwargs.get('training', {}))
        else:
            self.training = None
        if kwargs.get('uniqueTrait'):
            self.uniqueTrait = SelfVerifiedNameAttributeMetadata(**kwargs.get('uniqueTrait', {}))
        else:
            self.uniqueTrait = None
        if kwargs.get('voiceType'):
            self.voiceType = SelfVerifiedNameAttributeMetadata(**kwargs.get('voiceType', {}))
        else:
            self.voiceType = None
        if kwargs.get('workAuthorizationCountry'):
            self.workAuthorizationCountry = CountryAttributeMetadata(**kwargs.get('workAuthorizationCountry', {}))
        else:
            self.workAuthorizationCountry = None
        if kwargs.get('workHistoryCreditType'):
            self.workHistoryCreditType = SelfVerifiedNameAttributeMetadata(**kwargs.get('workHistoryCreditType', {}))
        else:
            self.workHistoryCreditType = None
    def __eq__(self, other):
        if not isinstance(other, SelfVerifiedNameMetadata):
            return False
        return (self.accent == other.accent and self.athleticSkill == other.athleticSkill and self.award == other.award and self.credit == other.credit and self.danceSkill == other.danceSkill and self.educationalHistory == other.educationalHistory and self.ethnicAppearance == other.ethnicAppearance and self.eyeColor == other.eyeColor and self.guildAffiliation == other.guildAffiliation and self.hairColor == other.hairColor and self.hairLength == other.hairLength and self.jobCategory == other.jobCategory and self.jobTitle == other.jobTitle and self.musicalInstrument == other.musicalInstrument and self.performerSkill == other.performerSkill and self.personalLocation == other.personalLocation and self.physique == other.physique and self.primaryCitizenship == other.primaryCitizenship and self.reference == other.reference and self.resumeCustomSection == other.resumeCustomSection and self.spokenLanguage == other.spokenLanguage and self.training == other.training and self.uniqueTrait == other.uniqueTrait and self.voiceType == other.voiceType and self.workAuthorizationCountry == other.workAuthorizationCountry and self.workHistoryCreditType == other.workHistoryCreditType)

class SelfVerifiedNameReference:
    def __init__(self, **kwargs):
        if kwargs.get('contactInfo'):
            self.contactInfo = SelfVerifiedNameAttributeValue(**kwargs.get('contactInfo', {}))
        else:
            self.contactInfo = None
        self.id = kwargs.get('id', "")
        if kwargs.get('name'):
            self.name = SelfVerifiedNameAttributeValue(**kwargs.get('name', {}))
        else:
            self.name = None
        if kwargs.get('relationship'):
            self.relationship = SelfVerifiedNameAttributeValue(**kwargs.get('relationship', {}))
        else:
            self.relationship = None
    def __eq__(self, other):
        if not isinstance(other, SelfVerifiedNameReference):
            return False
        return self.id == other.id


class SelfVerifiedNameReferenceConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(SelfVerifiedNameReference(**node.get("node", {})))

class SelfVerifiedNameTraining:
    def __init__(self, **kwargs):
        if kwargs.get('details'):
            self.details = SelfVerifiedNameAttributeValue(**kwargs.get('details', {}))
        else:
            self.details = None
        self.id = kwargs.get('id', "")
        if kwargs.get('instructor'):
            self.instructor = SelfVerifiedNameAttributeValue(**kwargs.get('instructor', {}))
        else:
            self.instructor = None
        if kwargs.get('location'):
            self.location = SelfVerifiedNameAttributeValue(**kwargs.get('location', {}))
        else:
            self.location = None
        if kwargs.get('school'):
            self.school = SelfVerifiedNameAttributeValue(**kwargs.get('school', {}))
        else:
            self.school = None
        if kwargs.get('type'):
            self.type = SelfVerifiedNameAttributeValue(**kwargs.get('type', {}))
        else:
            self.type = None
        self.year = kwargs.get('year', 0)
    def __eq__(self, other):
        if not isinstance(other, SelfVerifiedNameTraining):
            return False
        return self.id == other.id


class SelfVerifiedNameTrainingConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(SelfVerifiedNameTraining(**node.get("node", {})))

class SelfVerifiedReference:
    def __init__(self, **kwargs):
        if kwargs.get('contact'):
            self.contact = LocalizedString(**kwargs.get('contact', {}))
        else:
            self.contact = None
        self.id = kwargs.get('id', "")
        if kwargs.get('name'):
            self.name = LocalizedString(**kwargs.get('name', {}))
        else:
            self.name = None
        if kwargs.get('relationship'):
            self.relationship = LocalizedString(**kwargs.get('relationship', {}))
        else:
            self.relationship = None
    def __eq__(self, other):
        if not isinstance(other, SelfVerifiedReference):
            return False
        return self.id == other.id


class SelfVerifiedReferenceConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(SelfVerifiedReference(**node.get("node", {})))

class SelfVerifiedResumeCustomSection:
    def __init__(self, **kwargs):
        if kwargs.get('body'):
            self.body = SelfVerifiedNameAttributeValue(**kwargs.get('body', {}))
        else:
            self.body = None
        self.id = kwargs.get('id', "")
        if kwargs.get('title'):
            self.title = SelfVerifiedNameAttributeValue(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, SelfVerifiedResumeCustomSection):
            return False
        return self.id == other.id


class SelfVerifiedResumeCustomSectionConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(SelfVerifiedResumeCustomSection(**node.get("node", {})))

class SelfVerifiedTraining:
    def __init__(self, **kwargs):
        if kwargs.get('details'):
            self.details = LocalizedString(**kwargs.get('details', {}))
        else:
            self.details = None
        self.id = kwargs.get('id', "")
        if kwargs.get('instructor'):
            self.instructor = LocalizedString(**kwargs.get('instructor', {}))
        else:
            self.instructor = None
        if kwargs.get('location'):
            self.location = LocalizedString(**kwargs.get('location', {}))
        else:
            self.location = None
        if kwargs.get('school'):
            self.school = LocalizedString(**kwargs.get('school', {}))
        else:
            self.school = None
        if kwargs.get('training'):
            self.training = LocalizedString(**kwargs.get('training', {}))
        else:
            self.training = None
        self.year = kwargs.get('year', 0)
    def __eq__(self, other):
        if not isinstance(other, SelfVerifiedTraining):
            return False
        return self.id == other.id


class SelfVerifiedTrainingConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(SelfVerifiedTraining(**node.get("node", {})))

class Series:
    def __init__(self, **kwargs):
        if kwargs.get('displayableEpisodeNumber'):
            self.displayableEpisodeNumber = DisplayableEpisodeNumber(**kwargs.get('displayableEpisodeNumber', {}))
        else:
            self.displayableEpisodeNumber = None
        if kwargs.get('nextEpisode'):
            self.nextEpisode = Title(**kwargs.get('nextEpisode', {}))
        else:
            self.nextEpisode = None
        if kwargs.get('previousEpisode'):
            self.previousEpisode = Title(**kwargs.get('previousEpisode', {}))
        else:
            self.previousEpisode = None
        if kwargs.get('series'):
            self.series = Title(**kwargs.get('series', {}))
        else:
            self.series = None
    def __eq__(self, other):
        if not isinstance(other, Series):
            return False
        return (self.displayableEpisodeNumber == other.displayableEpisodeNumber and self.nextEpisode == other.nextEpisode and self.previousEpisode == other.previousEpisode and self.series == other.series)

class SeriesCreditAttribute:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.total = kwargs.get('total', 0)
        self.text = kwargs.get('text', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
    def __eq__(self, other):
        if not isinstance(other, SeriesCreditAttribute):
            return False
        return self.id == other.id

class SeverityLevel:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
        self.votedFor = kwargs.get('votedFor', 0)
        self.voteType = kwargs.get('voteType', "")
    def __eq__(self, other):
        if not isinstance(other, SeverityLevel):
            return False
        return self.id == other.id

class SharedCreditCategorySummary:
    def __init__(self, **kwargs):
        if kwargs.get('creditCategory'):
            self.creditCategory = CreditCategory(**kwargs.get('creditCategory', {}))
        else:
            self.creditCategory = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, SharedCreditCategorySummary):
            return False
        return (self.creditCategory == other.creditCategory and self.total == other.total)

class SharedNameItem:
    def __init__(self, **kwargs):
        if kwargs.get('mutualName'):
            self.mutualName = Name(**kwargs.get('mutualName', {}))
        else:
            self.mutualName = None
        if kwargs.get('sharedTitlesWithNameInput'):
            self.sharedTitlesWithNameInput = SharedTitle(**kwargs.get('sharedTitlesWithNameInput', {}))
        else:
            self.sharedTitlesWithNameInput = None
        if kwargs.get('sharedTitlesWithNamePage'):
            self.sharedTitlesWithNamePage = SharedTitle(**kwargs.get('sharedTitlesWithNamePage', {}))
        else:
            self.sharedTitlesWithNamePage = None
        self.totalSharedTitlesWithNameInput = kwargs.get('totalSharedTitlesWithNameInput', 0)
        self.totalSharedTitlesWithNamePage = kwargs.get('totalSharedTitlesWithNamePage', 0)
    def __eq__(self, other):
        if not isinstance(other, SharedNameItem):
            return False
        return (self.mutualName == other.mutualName and self.sharedTitlesWithNameInput == other.sharedTitlesWithNameInput and self.sharedTitlesWithNamePage == other.sharedTitlesWithNamePage and self.totalSharedTitlesWithNameInput == other.totalSharedTitlesWithNameInput and self.totalSharedTitlesWithNamePage == other.totalSharedTitlesWithNamePage)


class SharedNameItemConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(SharedNameItem(**node.get("node", {})))

class SharedNamesResult:
    def __init__(self, **kwargs):
        if kwargs.get('sharedCreditCategorySummary'):
            self.sharedCreditCategorySummary = SharedCreditCategorySummary(**kwargs.get('sharedCreditCategorySummary', {}))
        else:
            self.sharedCreditCategorySummary = None
        if kwargs.get('sharedNames'):
            self.sharedNames = SharedNameItemConnection(**kwargs.get('sharedNames', {}))
        else:
            self.sharedNames = None
        if kwargs.get('statusMessage'):
            self.statusMessage = LocalizedMarkdown(**kwargs.get('statusMessage', {}))
        else:
            self.statusMessage = None
    def __eq__(self, other):
        if not isinstance(other, SharedNamesResult):
            return False
        return (self.sharedCreditCategorySummary == other.sharedCreditCategorySummary and self.sharedNames == other.sharedNames and self.statusMessage == other.statusMessage)

class SharedNamesSummary:
    def __init__(self, **kwargs):
        self.inNetwork = kwargs.get('inNetwork', False)
        if kwargs.get('summaryText'):
            self.summaryText = LocalizedString(**kwargs.get('summaryText', {}))
        else:
            self.summaryText = None
        self.totalSharedConnections = kwargs.get('totalSharedConnections', 0)
    def __eq__(self, other):
        if not isinstance(other, SharedNamesSummary):
            return False
        return (self.inNetwork == other.inNetwork and self.summaryText == other.summaryText and self.totalSharedConnections == other.totalSharedConnections)

class SharedTitle:
    def __init__(self, **kwargs):
        if kwargs.get('nameInputCreditedJobCategories'):
            self.nameInputCreditedJobCategories = CreditCategory(**kwargs.get('nameInputCreditedJobCategories', {}))
        else:
            self.nameInputCreditedJobCategories = None
        if kwargs.get('namePageCreditedJobCategories'):
            self.namePageCreditedJobCategories = CreditCategory(**kwargs.get('namePageCreditedJobCategories', {}))
        else:
            self.namePageCreditedJobCategories = None
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, SharedTitle):
            return False
        return (self.nameInputCreditedJobCategories == other.nameInputCreditedJobCategories and self.namePageCreditedJobCategories == other.namePageCreditedJobCategories and self.title == other.title)


class SharedTitlesConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(SharedTitle(**node.get("node", {})))

class Showtime:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('primaryTicketing'):
            self.primaryTicketing = ShowtimeTicketing(**kwargs.get('primaryTicketing', {}))
        else:
            self.primaryTicketing = None
        if kwargs.get('screeningStart'):
            self.screeningStart = ScreeningDateTime(**kwargs.get('screeningStart', {}))
        else:
            self.screeningStart = None
        if kwargs.get('screeningType'):
            self.screeningType = ShowtimeScreeningType(**kwargs.get('screeningType', {}))
        else:
            self.screeningType = None
    def __eq__(self, other):
        if not isinstance(other, Showtime):
            return False
        return self.id == other.id

class ShowtimeScreeningType:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, ShowtimeScreeningType):
            return False
        return self.id == other.id

class ShowtimeTicketing:
    def __init__(self, **kwargs):
        self.link = kwargs.get('link', "")
    def __eq__(self, other):
        if not isinstance(other, ShowtimeTicketing):
            return False
        return (self.link == other.link)

class ShowtimesByScreeningType:
    def __init__(self, **kwargs):
        if kwargs.get('screeningType'):
            self.screeningType = ShowtimeScreeningType(**kwargs.get('screeningType', {}))
        else:
            self.screeningType = None
        if kwargs.get('showtimes'):
            self.showtimes = Showtime(**kwargs.get('showtimes', {}))
        else:
            self.showtimes = None
    def __eq__(self, other):
        if not isinstance(other, ShowtimesByScreeningType):
            return False
        return (self.screeningType == other.screeningType and self.showtimes == other.showtimes)

class SignInOption:
    def __init__(self, **kwargs):
        self.redirectURL = kwargs.get('redirectURL', "")
        self.type = kwargs.get('type', "")
    def __eq__(self, other):
        if not isinstance(other, SignInOption):
            return False
        return (self.redirectURL == other.redirectURL and self.type == other.type)

class SignInOptionRedirectURLOutput:
    def __init__(self, **kwargs):
        if kwargs.get('signInOption'):
            self.signInOption = SignInOption(**kwargs.get('signInOption', {}))
        else:
            self.signInOption = None
    def __eq__(self, other):
        if not isinstance(other, SignInOptionRedirectURLOutput):
            return False
        return (self.signInOption == other.signInOption)

class SignInOptionsRedirectURLsOutput:
    def __init__(self, **kwargs):
        if kwargs.get('signInOptions'):
            self.signInOptions = SignInOption(**kwargs.get('signInOptions', {}))
        else:
            self.signInOptions = None
    def __eq__(self, other):
        if not isinstance(other, SignInOptionsRedirectURLsOutput):
            return False
        return (self.signInOptions == other.signInOptions)

class SoundMix:
    def __init__(self, **kwargs):
        if kwargs.get('attributes'):
            self.attributes = [DisplayableAttribute(**attr) for attr in kwargs.get('attributes', [])]
        else:
            self.attributes = None
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableTechnicalSpecificationProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.id = kwargs.get('id', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, SoundMix):
            return False
        return self.id == other.id

class SoundMixes:
    def __init__(self, **kwargs):
        if kwargs.get('items'):
            self.items = SoundMix(**kwargs.get('items', {}))
        else:
            self.items = None
        if kwargs.get('restriction'):
            self.restriction = TechnicalSpecificationsRestriction(**kwargs.get('restriction', {}))
        else:
            self.restriction = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, SoundMixes):
            return False
        return (self.items == other.items and self.restriction == other.restriction and self.total == other.total)

class SoundtrackRestriction:
    def __init__(self, **kwargs):
        if kwargs.get('explanations'):
            self.explanations = RestrictionExplanation(**kwargs.get('explanations', {}))
        else:
            self.explanations = None
        self.reasons = kwargs.get('reasons', "")
        self.restrictionReason = kwargs.get('restrictionReason', "")
        self.unrestrictedTotal = kwargs.get('unrestrictedTotal', 0)
    def __eq__(self, other):
        if not isinstance(other, SoundtrackRestriction):
            return False
        return (self.explanations == other.explanations and self.reasons == other.reasons and self.restrictionReason == other.restrictionReason and self.unrestrictedTotal == other.unrestrictedTotal)

class Source:
    def __init__(self, **kwargs):
        self.attributionUrl = kwargs.get('attributionUrl', "")
        if kwargs.get('banner'):
            self.banner = Banner(**kwargs.get('banner', {}))
        else:
            self.banner = None
        self.id = kwargs.get('id', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, Source):
            return False
        return self.id == other.id

class SpokenLanguage:
    def __init__(self, **kwargs):
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableTitleSpokenLanguageProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, SpokenLanguage):
            return False
        return self.id == other.id

class SpokenLanguages:
    def __init__(self, **kwargs):
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('spokenLanguages'):
            self.spokenLanguages = SpokenLanguage(**kwargs.get('spokenLanguages', {}))
        else:
            self.spokenLanguages = None
    def __eq__(self, other):
        if not isinstance(other, SpokenLanguages):
            return False
        return (self.language == other.language and self.spokenLanguages == other.spokenLanguages)

class SpouseAttributes:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, SpouseAttributes):
            return False
        return self.id == other.id

class SpouseName:
    def __init__(self, **kwargs):
        if kwargs.get('asMarkdown'):
            self.asMarkdown = Markdown(**kwargs.get('asMarkdown', {}))
        else:
            self.asMarkdown = None
        if kwargs.get('name'):
            self.name = Name(**kwargs.get('name', {}))
        else:
            self.name = None
    def __eq__(self, other):
        if not isinstance(other, SpouseName):
            return False
        return (self.asMarkdown == other.asMarkdown and self.name == other.name)

class StaffStatus:
    def __init__(self, **kwargs):
        self.category = kwargs.get('category', "")
    def __eq__(self, other):
        if not isinstance(other, StaffStatus):
            return False
        return (self.category == other.category)

class StreamingTitle:
    def __init__(self, **kwargs):
        self.refTag = kwargs.get('refTag', "")
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, StreamingTitle):
            return False
        return (self.refTag == other.refTag and self.title == other.title)


class StreamingTitleConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(StreamingTitle(**node.get("node", {})))

class StreamingTitles:
    def __init__(self, **kwargs):
        if kwargs.get('provider'):
            self.provider = WatchProvider(**kwargs.get('provider', {}))
        else:
            self.provider = None
        if kwargs.get('titles'):
            self.titles = StreamingTitleConnection(**kwargs.get('titles', {}))
        else:
            self.titles = None
    def __eq__(self, other):
        if not isinstance(other, StreamingTitles):
            return False
        return (self.provider == other.provider and self.titles == other.titles)

class SuggestionSearchItem:
    def __init__(self, **kwargs):
        self.constId = kwargs.get('constId', "")
        if kwargs.get('displayLabels'):
            self.displayLabels = DisplayLabels(**kwargs.get('displayLabels', {}))
        else:
            self.displayLabels = None
        self.id = kwargs.get('id', "")
        if kwargs.get('image'):
            self.image = MediaServiceImage(**kwargs.get('image', {}))
        else:
            self.image = None
        self.rank = kwargs.get('rank', 0)
        self.refTagFragment = kwargs.get('refTagFragment', "")
        if kwargs.get('releaseYear'):
            self.releaseYear = YearRange(**kwargs.get('releaseYear', {}))
        else:
            self.releaseYear = None
        self.titleTypeId = kwargs.get('titleTypeId', "")
        if kwargs.get('topVideos'):
            self.topVideos = VideoMedia(**kwargs.get('topVideos', {}))
        else:
            self.topVideos = None
        self.url = kwargs.get('url', "")
        self.videoCount = kwargs.get('videoCount', 0)
    def __eq__(self, other):
        if not isinstance(other, SuggestionSearchItem):
            return False
        return self.id == other.id

class SupportedQuestionFilters:
    def __init__(self, **kwargs):
        self.countries = kwargs.get('countries', "")
        self.dataTypes = kwargs.get('dataTypes', "")
        self.languages = kwargs.get('languages', "")
    def __eq__(self, other):
        if not isinstance(other, SupportedQuestionFilters):
            return False
        return (self.countries == other.countries and self.dataTypes == other.dataTypes and self.languages == other.languages)

class SymphonyArgument:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', "")
        self.value = kwargs.get('value', "")
    def __eq__(self, other):
        if not isinstance(other, SymphonyArgument):
            return False
        return (self.name == other.name and self.value == other.value)

class SymphonyMetadata:
    def __init__(self, **kwargs):
        self.contentId = kwargs.get('contentId', "")
        self.creativeId = kwargs.get('creativeId', "")
        self.multiSlotGroupName = kwargs.get('multiSlotGroupName', "")
        self.multiSlotOrder = kwargs.get('multiSlotOrder', 0)
        self.placementId = kwargs.get('placementId', "")
    def __eq__(self, other):
        if not isinstance(other, SymphonyMetadata):
            return False
        return (self.contentId == other.contentId and self.creativeId == other.creativeId and self.multiSlotGroupName == other.multiSlotGroupName and self.multiSlotOrder == other.multiSlotOrder and self.placementId == other.placementId)

class SymphonyPlacement:
    def __init__(self, **kwargs):
        if kwargs.get('componentArguments'):
            self.componentArguments = SymphonyArgument(**kwargs.get('componentArguments', {}))
        else:
            self.componentArguments = None
        if kwargs.get('componentMetadata'):
            self.componentMetadata = SymphonyMetadata(**kwargs.get('componentMetadata', {}))
        else:
            self.componentMetadata = None
        self.componentName = kwargs.get('componentName', "")
        self.slot = kwargs.get('slot', "")
    def __eq__(self, other):
        if not isinstance(other, SymphonyPlacement):
            return False
        return (self.componentArguments == other.componentArguments and self.componentMetadata == other.componentMetadata and self.componentName == other.componentName and self.slot == other.slot)

class Tagline:
    def __init__(self, **kwargs):
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableTitleTaglineProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, Tagline):
            return False
        return (self.displayableProperty == other.displayableProperty and self.text == other.text)


class TaglineConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Tagline(**node.get("node", {})))

class TechnicalSpecifications:
    def __init__(self, **kwargs):
        if kwargs.get('aspectRatios'):
            self.aspectRatios = AspectRatios(**kwargs.get('aspectRatios', {}))
        else:
            self.aspectRatios = None
        if kwargs.get('cameras'):
            self.cameras = Cameras(**kwargs.get('cameras', {}))
        else:
            self.cameras = None
        if kwargs.get('colorations'):
            self.colorations = Colorations(**kwargs.get('colorations', {}))
        else:
            self.colorations = None
        if kwargs.get('filmLengths'):
            self.filmLengths = FilmLengths(**kwargs.get('filmLengths', {}))
        else:
            self.filmLengths = None
        if kwargs.get('laboratories'):
            self.laboratories = Laboratories(**kwargs.get('laboratories', {}))
        else:
            self.laboratories = None
        if kwargs.get('negativeFormats'):
            self.negativeFormats = NegativeFormats(**kwargs.get('negativeFormats', {}))
        else:
            self.negativeFormats = None
        if kwargs.get('printedFormats'):
            self.printedFormats = PrintedFormats(**kwargs.get('printedFormats', {}))
        else:
            self.printedFormats = None
        if kwargs.get('processes'):
            self.processes = Processes(**kwargs.get('processes', {}))
        else:
            self.processes = None
        if kwargs.get('soundMixes'):
            self.soundMixes = SoundMixes(**kwargs.get('soundMixes', {}))
        else:
            self.soundMixes = None
    def __eq__(self, other):
        if not isinstance(other, TechnicalSpecifications):
            return False
        return (self.aspectRatios == other.aspectRatios and self.cameras == other.cameras and self.colorations == other.colorations and self.filmLengths == other.filmLengths and self.laboratories == other.laboratories and self.negativeFormats == other.negativeFormats and self.printedFormats == other.printedFormats and self.processes == other.processes and self.soundMixes == other.soundMixes)

class TechnicalSpecificationsRestriction:
    def __init__(self, **kwargs):
        if kwargs.get('explanations'):
            self.explanations = RestrictionExplanation(**kwargs.get('explanations', {}))
        else:
            self.explanations = None
        self.reasons = kwargs.get('reasons', "")
        self.restrictionReason = kwargs.get('restrictionReason', "")
        self.unrestrictedTotal = kwargs.get('unrestrictedTotal', 0)
    def __eq__(self, other):
        if not isinstance(other, TechnicalSpecificationsRestriction):
            return False
        return (self.explanations == other.explanations and self.reasons == other.reasons and self.restrictionReason == other.restrictionReason and self.unrestrictedTotal == other.unrestrictedTotal)

class Test:
    def __init__(self, **kwargs):
        self.error = kwargs.get('error', "")
        self.experimental = kwargs.get('experimental', "")
        self.result = kwargs.get('result', "")
        if kwargs.get('testItems'):
            self.testItems = TestItem(**kwargs.get('testItems', {}))
        else:
            self.testItems = None
    def __eq__(self, other):
        if not isinstance(other, Test):
            return False
        return (self.error == other.error and self.experimental == other.experimental and self.result == other.result and self.testItems == other.testItems)

class TestAuth:
    def __init__(self, **kwargs):
        self.cacheableResult = kwargs.get('cacheableResult', "")
        self.cacheableResultWithNoCacheCustomerId = kwargs.get('cacheableResultWithNoCacheCustomerId', "")
        self.cacheableResultWithNoCacheUserId = kwargs.get('cacheableResultWithNoCacheUserId', "")
        self.clientIp = kwargs.get('clientIp', "")
        self.detectedCountry = kwargs.get('detectedCountry', "")
        self.hasAuthenticationHeaders = kwargs.get('hasAuthenticationHeaders', False)
        self.hasGatewayName = kwargs.get('hasGatewayName', False)
        self.hasTransitiveAuthenticationHeaders = kwargs.get('hasTransitiveAuthenticationHeaders', False)
        self.isInternalClient = kwargs.get('isInternalClient', False)
        self.isNon1PInternalClient = kwargs.get('isNon1PInternalClient', False)
        self.nonCacheableResult = kwargs.get('nonCacheableResult', "")
        self.operationName = kwargs.get('operationName', "")
        self.result = kwargs.get('result', "")
    def __eq__(self, other):
        if not isinstance(other, TestAuth):
            return False
        return (self.cacheableResult == other.cacheableResult and self.cacheableResultWithNoCacheCustomerId == other.cacheableResultWithNoCacheCustomerId and self.cacheableResultWithNoCacheUserId == other.cacheableResultWithNoCacheUserId and self.clientIp == other.clientIp and self.detectedCountry == other.detectedCountry and self.hasAuthenticationHeaders == other.hasAuthenticationHeaders and self.hasGatewayName == other.hasGatewayName and self.hasTransitiveAuthenticationHeaders == other.hasTransitiveAuthenticationHeaders and self.isInternalClient == other.isInternalClient and self.isNon1PInternalClient == other.isNon1PInternalClient and self.nonCacheableResult == other.nonCacheableResult and self.operationName == other.operationName and self.result == other.result)

class TestAuthTimer:
    def __init__(self, **kwargs):
        self.authTimer = kwargs.get('authTimer', "")
    def __eq__(self, other):
        if not isinstance(other, TestAuthTimer):
            return False
        return (self.authTimer == other.authTimer)

class TestEntitlement:
    def __init__(self, **kwargs):
        self.entitlement = kwargs.get('entitlement', "")
        self.result = kwargs.get('result', "")
    def __eq__(self, other):
        if not isinstance(other, TestEntitlement):
            return False
        return (self.entitlement == other.entitlement and self.result == other.result)

class TestItem:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
    def __eq__(self, other):
        if not isinstance(other, TestItem):
            return False
        return self.id == other.id

class ThirdPartyTrackers:
    def __init__(self, **kwargs):
        self.impressionTrackers = kwargs.get('impressionTrackers', "")
        self.titlePosterClickTrackers = kwargs.get('titlePosterClickTrackers', "")
        self.videoCompleteTrackers = kwargs.get('videoCompleteTrackers', "")
        self.videoFirstQuartileTrackers = kwargs.get('videoFirstQuartileTrackers', "")
        self.videoMidpointTrackers = kwargs.get('videoMidpointTrackers', "")
        self.videoStartTrackers = kwargs.get('videoStartTrackers', "")
        self.videoThirdQuartileTrackers = kwargs.get('videoThirdQuartileTrackers', "")
    def __eq__(self, other):
        if not isinstance(other, ThirdPartyTrackers):
            return False
        return (self.impressionTrackers == other.impressionTrackers and self.titlePosterClickTrackers == other.titlePosterClickTrackers and self.videoCompleteTrackers == other.videoCompleteTrackers and self.videoFirstQuartileTrackers == other.videoFirstQuartileTrackers and self.videoMidpointTrackers == other.videoMidpointTrackers and self.videoStartTrackers == other.videoStartTrackers and self.videoThirdQuartileTrackers == other.videoThirdQuartileTrackers)

class Thumbnail:
    def __init__(self, **kwargs):
        self.height = kwargs.get('height', 0)
        self.url = kwargs.get('url', "")
        self.width = kwargs.get('width', 0)
    def __eq__(self, other):
        if not isinstance(other, Thumbnail):
            return False
        return (self.height == other.height and self.url == other.url and self.width == other.width)

class Title:
    def __init__(self, **kwargs):
        if kwargs.get('aggregateRatingsBreakdown'):
            self.aggregateRatingsBreakdown = AggregateRatingsBreakdown(**kwargs.get('aggregateRatingsBreakdown', {}))
        else:
            self.aggregateRatingsBreakdown = None
        if kwargs.get('akas'):
            self.akas = AkaConnection(**kwargs.get('akas', {}))
        else:
            self.akas = None
        if kwargs.get('alexaTopQuestions'):
            self.alexaTopQuestions = AlexaQuestionConnection(**kwargs.get('alexaTopQuestions', {}))
        else:
            self.alexaTopQuestions = None
        if kwargs.get('alternateVersions'):
            self.alternateVersions = AlternateVersionConnection(**kwargs.get('alternateVersions', {}))
        else:
            self.alternateVersions = None
        if kwargs.get('amazonMusicAlbums'):
            self.amazonMusicAlbums = AmazonMusicProduct(**kwargs.get('amazonMusicAlbums', {}))
        else:
            self.amazonMusicAlbums = None
        if kwargs.get('awardNominations'):
            self.awardNominations = AwardNominationConnection(**kwargs.get('awardNominations', {}))
        else:
            self.awardNominations = None
        self.canonicalUrl = kwargs.get('canonicalUrl', "")
        self.canHaveEpisodes = kwargs.get('canHaveEpisodes', False)
        if kwargs.get('canRate'):
            self.canRate = CanRate(**kwargs.get('canRate', {}))
        else:
            self.canRate = None
        if kwargs.get('certificate'):
            self.certificate = Certificate(**kwargs.get('certificate', {}))
        else:
            self.certificate = None
        if kwargs.get('certificates'):
            self.certificates = CertificatesConnection(**kwargs.get('certificates', {}))
        else:
            self.certificates = None
        if kwargs.get('cinemaShowtimesByScreeningType'):
            self.cinemaShowtimesByScreeningType = TitleCinemaShowtimesByScreeningTypeConnection(**kwargs.get('cinemaShowtimesByScreeningType', {}))
        else:
            self.cinemaShowtimesByScreeningType = None
        if kwargs.get('companyCreditCategories'):
            self.companyCreditCategories = CompanyCreditCategoryWithCompanyCredits(**kwargs.get('companyCreditCategories', {}))
        else:
            self.companyCreditCategories = None
        if kwargs.get('companyCredits'):
            self.companyCredits = CompanyCreditConnection(**kwargs.get('companyCredits', {}))
        else:
            self.companyCredits = None
        if kwargs.get('connectionCategories'):
            self.connectionCategories = ConnectionCategoryWithConnections(**kwargs.get('connectionCategories', {}))
        else:
            self.connectionCategories = None
        if kwargs.get('connections'):
            self.connections = TitleConnectionConnection(**kwargs.get('connections', {}))
        else:
            self.connections = None
        if kwargs.get('contributionQuestions'):
            self.contributionQuestions = QuestionConnection(**kwargs.get('contributionQuestions', {}))
        else:
            self.contributionQuestions = None
        if kwargs.get('countriesOfOrigin'):
            self.countriesOfOrigin = CountriesOfOrigin(**kwargs.get('countriesOfOrigin', {}))
        else:
            self.countriesOfOrigin = None
        if kwargs.get('crazyCredits'):
            self.crazyCredits = CrazyCreditConnection(**kwargs.get('crazyCredits', {}))
        else:
            self.crazyCredits = None
        if kwargs.get('creditCategories'):
            self.creditCategories = TitleCreditCategoryWithCredits(**kwargs.get('creditCategories', {}))
        else:
            self.creditCategories = None
        if kwargs.get('creditGroupings'):
            self.creditGroupings = CreditGroupingConnection(**kwargs.get('creditGroupings', {}))
        else:
            self.creditGroupings = None
        if kwargs.get('credits'):
            self.credits = CreditConnection(**kwargs.get('credits', {}))
        else:
            self.credits = None
        if kwargs.get('creditsV2'):
            self.creditsV2 = CreditV2Connection(**kwargs.get('creditsV2', {}))
        else:
            self.creditsV2 = None
        if kwargs.get('engagementStatistics'):
            self.engagementStatistics = EngagementStatistics(**kwargs.get('engagementStatistics', {}))
        else:
            self.engagementStatistics = None
        if kwargs.get('episodeCredits'):
            self.episodeCredits = CreditV2Connection(**kwargs.get('episodeCredits', {}))
        else:
            self.episodeCredits = None
        if kwargs.get('episodes'):
            self.episodes = Episodes(**kwargs.get('episodes', {}))
        else:
            self.episodes = None
        if kwargs.get('experimental_credits'):
            self.experimental_credits = ExperimentalCreditConnection(**kwargs.get('experimental_credits', {}))
        else:
            self.experimental_credits = None
        if kwargs.get('experimental_trackNotificationPreferences'):
            self.experimental_trackNotificationPreferences = Experimental_TrackNotificationPreferences(**kwargs.get('experimental_trackNotificationPreferences', {}))
        else:
            self.experimental_trackNotificationPreferences = None
        if kwargs.get('externalLinkCategories'):
            self.externalLinkCategories = ExternalLinkCategoryWithExternalLinks(**kwargs.get('externalLinkCategories', {}))
        else:
            self.externalLinkCategories = None
        if kwargs.get('externalLinks'):
            self.externalLinks = ExternalLinkConnection(**kwargs.get('externalLinks', {}))
        else:
            self.externalLinks = None
        if kwargs.get('faqs'):
            self.faqs = FaqConnection(**kwargs.get('faqs', {}))
        else:
            self.faqs = None
        if kwargs.get('featuredPolls'):
            self.featuredPolls = PollsConnection(**kwargs.get('featuredPolls', {}))
        else:
            self.featuredPolls = None
        if kwargs.get('featuredReviews'):
            self.featuredReviews = ReviewsConnection(**kwargs.get('featuredReviews', {}))
        else:
            self.featuredReviews = None
        if kwargs.get('filmingDates'):
            self.filmingDates = FilmingDatesConnection(**kwargs.get('filmingDates', {}))
        else:
            self.filmingDates = None
        if kwargs.get('filmingLocations'):
            self.filmingLocations = FilmingLocationConnection(**kwargs.get('filmingLocations', {}))
        else:
            self.filmingLocations = None
        if kwargs.get('genres'):
            self.genres = Genres(**kwargs.get('genres', {}))
        else:
            self.genres = None
        if kwargs.get('goofCategories'):
            self.goofCategories = GoofCategoryWithGoofs(**kwargs.get('goofCategories', {}))
        else:
            self.goofCategories = None
        if kwargs.get('goofs'):
            self.goofs = GoofConnection(**kwargs.get('goofs', {}))
        else:
            self.goofs = None
        self.id = kwargs.get('id', "")
        if kwargs.get('images'):
            self.images = ImageConnection(**kwargs.get('images', {}))
        else:
            self.images = None
        if kwargs.get('imageTypes'):
            self.imageTypes = ImageTypeWithImages(**kwargs.get('imageTypes', {}))
        else:
            self.imageTypes = None
        if kwargs.get('_imageUploadLink'):
            self._imageUploadLink = ContributionLink(**kwargs.get('_imageUploadLink', {}))
        else:
            self._imageUploadLink = None
        if kwargs.get('interests'):
            self.interests = InterestConnection(**kwargs.get('interests', {}))
        else:
            self.interests = None
        self.isAdult = kwargs.get('isAdult', False)
        self.isWGAVerified = kwargs.get('isWGAVerified', False)
        if kwargs.get('keywordItemCategories'):
            self.keywordItemCategories = TitleKeywordItemCategoryWithKeywords(**kwargs.get('keywordItemCategories', {}))
        else:
            self.keywordItemCategories = None
        if kwargs.get('keywords'):
            self.keywords = TitleKeywordConnection(**kwargs.get('keywords', {}))
        else:
            self.keywords = None
        if kwargs.get('latestTrailer'):
            self.latestTrailer = Video(**kwargs.get('latestTrailer', {}))
        else:
            self.latestTrailer = None
        if kwargs.get('latestTrailerWebviewPlayer'):
            self.latestTrailerWebviewPlayer = WebviewVideoPlayer(**kwargs.get('latestTrailerWebviewPlayer', {}))
        else:
            self.latestTrailerWebviewPlayer = None
        if kwargs.get('lifetimeGross'):
            self.lifetimeGross = BoxOfficeGross(**kwargs.get('lifetimeGross', {}))
        else:
            self.lifetimeGross = None
        if kwargs.get('meta'):
            self.meta = TitleMeta(**kwargs.get('meta', {}))
        else:
            self.meta = None
        if kwargs.get('metacritic'):
            self.metacritic = Metacritic(**kwargs.get('metacritic', {}))
        else:
            self.metacritic = None
        if kwargs.get('meterRank'):
            self.meterRank = TitleMeterRanking(**kwargs.get('meterRank', {}))
        else:
            self.meterRank = None
        if kwargs.get('meterRankingHistory'):
            self.meterRankingHistory = TitleMeterRankingHistory(**kwargs.get('meterRankingHistory', {}))
        else:
            self.meterRankingHistory = None
        if kwargs.get('moreLikeThisTitles'):
            self.moreLikeThisTitles = TitleConnection(**kwargs.get('moreLikeThisTitles', {}))
        else:
            self.moreLikeThisTitles = None
        if kwargs.get('news'):
            self.news = NewsConnection(**kwargs.get('news', {}))
        else:
            self.news = None
        if kwargs.get('nominations'):
            self.nominations = NominationConnection(**kwargs.get('nominations', {}))
        else:
            self.nominations = None
        if kwargs.get('openingWeekendGross'):
            self.openingWeekendGross = OpeningWeekendGross(**kwargs.get('openingWeekendGross', {}))
        else:
            self.openingWeekendGross = None
        if kwargs.get('openingWeekendGrosses'):
            self.openingWeekendGrosses = OpeningWeekendGrossConnection(**kwargs.get('openingWeekendGrosses', {}))
        else:
            self.openingWeekendGrosses = None
        if kwargs.get('originalTitleText'):
            self.originalTitleText = TitleText(**kwargs.get('originalTitleText', {}))
        else:
            self.originalTitleText = None
        if kwargs.get('parentsGuide'):
            self.parentsGuide = ParentsGuide(**kwargs.get('parentsGuide', {}))
        else:
            self.parentsGuide = None
        if kwargs.get('_parentsGuideContributionLink'):
            self._parentsGuideContributionLink = ContributionLink(**kwargs.get('_parentsGuideContributionLink', {}))
        else:
            self._parentsGuideContributionLink = None
        if kwargs.get('plot'):
            self.plot = Plot(**kwargs.get('plot', {}))
        else:
            self.plot = None
        if kwargs.get('_plotContributionLink'):
            self._plotContributionLink = ContributionLink(**kwargs.get('_plotContributionLink', {}))
        else:
            self._plotContributionLink = None
        if kwargs.get('plots'):
            self.plots = PlotConnection(**kwargs.get('plots', {}))
        else:
            self.plots = None
        if kwargs.get('prestigiousAwardSummary'):
            self.prestigiousAwardSummary = PrestigiousAwardSummary(**kwargs.get('prestigiousAwardSummary', {}))
        else:
            self.prestigiousAwardSummary = None
        if kwargs.get('primaryImage'):
            self.primaryImage = Image(**kwargs.get('primaryImage', {}))
        else:
            self.primaryImage = None
        if kwargs.get('primaryVideos'):
            self.primaryVideos = VideoConnection(**kwargs.get('primaryVideos', {}))
        else:
            self.primaryVideos = None
        if kwargs.get('primaryWatchOption'):
            self.primaryWatchOption = PrimaryWatchOption(**kwargs.get('primaryWatchOption', {}))
        else:
            self.primaryWatchOption = None
        if kwargs.get('principalCredits'):
            self.principalCredits = PrincipalCreditsForCategory(**kwargs.get('principalCredits', {}))
        else:
            self.principalCredits = None
        if kwargs.get('principalCreditsV2'):
            self.principalCreditsV2 = PrincipalCreditsForGrouping(**kwargs.get('principalCreditsV2', {}))
        else:
            self.principalCreditsV2 = None
        if kwargs.get('productionBudget'):
            self.productionBudget = ProductionBudget(**kwargs.get('productionBudget', {}))
        else:
            self.productionBudget = None
        if kwargs.get('productionDates'):
            self.productionDates = ProductionDatesConnection(**kwargs.get('productionDates', {}))
        else:
            self.productionDates = None
        if kwargs.get('productionStatus'):
            self.productionStatus = ProductionStatusDetails(**kwargs.get('productionStatus', {}))
        else:
            self.productionStatus = None
        if kwargs.get('quotes'):
            self.quotes = TitleQuoteConnection(**kwargs.get('quotes', {}))
        else:
            self.quotes = None
        if kwargs.get('rankedLifetimeGross'):
            self.rankedLifetimeGross = RankedLifetimeBoxOfficeGross(**kwargs.get('rankedLifetimeGross', {}))
        else:
            self.rankedLifetimeGross = None
        if kwargs.get('rankedLifetimeGrosses'):
            self.rankedLifetimeGrosses = RankedLifetimeBoxOfficeGrossConnection(**kwargs.get('rankedLifetimeGrosses', {}))
        else:
            self.rankedLifetimeGrosses = None
        if kwargs.get('ratingsSummary'):
            self.ratingsSummary = RatingsSummary(**kwargs.get('ratingsSummary', {}))
        else:
            self.ratingsSummary = None
        if kwargs.get('relatedInterests'):
            self.relatedInterests = InterestConnection(**kwargs.get('relatedInterests', {}))
        else:
            self.relatedInterests = None
        if kwargs.get('relatedLists'):
            self.relatedLists = ListConnection(**kwargs.get('relatedLists', {}))
        else:
            self.relatedLists = None
        if kwargs.get('releaseDate'):
            self.releaseDate = ReleaseDate(**kwargs.get('releaseDate', {}))
        else:
            self.releaseDate = None
        if kwargs.get('releaseDates'):
            self.releaseDates = ReleaseDateConnection(**kwargs.get('releaseDates', {}))
        else:
            self.releaseDates = None
        if kwargs.get('releaseYear'):
            self.releaseYear = YearRange(**kwargs.get('releaseYear', {}))
        else:
            self.releaseYear = None
        if kwargs.get('_reviewContributionLink'):
            self._reviewContributionLink = ContributionLink(**kwargs.get('_reviewContributionLink', {}))
        else:
            self._reviewContributionLink = None
        if kwargs.get('reviews'):
            self.reviews = ReviewsConnection(**kwargs.get('reviews', {}))
        else:
            self.reviews = None
        if kwargs.get('reviewSummary'):
            self.reviewSummary = TitleReviewSummary(**kwargs.get('reviewSummary', {}))
        else:
            self.reviewSummary = None
        if kwargs.get('runtime'):
            self.runtime = Runtime(**kwargs.get('runtime', {}))
        else:
            self.runtime = None
        if kwargs.get('runtimes'):
            self.runtimes = RuntimeConnection(**kwargs.get('runtimes', {}))
        else:
            self.runtimes = None
        if kwargs.get('series'):
            self.series = Series(**kwargs.get('series', {}))
        else:
            self.series = None
        if kwargs.get('soundtrack'):
            self.soundtrack = TrackConnection(**kwargs.get('soundtrack', {}))
        else:
            self.soundtrack = None
        if kwargs.get('spokenLanguages'):
            self.spokenLanguages = SpokenLanguages(**kwargs.get('spokenLanguages', {}))
        else:
            self.spokenLanguages = None
        if kwargs.get('taglines'):
            self.taglines = TaglineConnection(**kwargs.get('taglines', {}))
        else:
            self.taglines = None
        if kwargs.get('technicalSpecifications'):
            self.technicalSpecifications = TechnicalSpecifications(**kwargs.get('technicalSpecifications', {}))
        else:
            self.technicalSpecifications = None
        if kwargs.get('titleGenres'):
            self.titleGenres = TitleGenres(**kwargs.get('titleGenres', {}))
        else:
            self.titleGenres = None
        if kwargs.get('titleText'):
            self.titleText = TitleText(**kwargs.get('titleText', {}))
        else:
            self.titleText = None
        if kwargs.get('titleType'):
            self.titleType = TitleType(**kwargs.get('titleType', {}))
        else:
            self.titleType = None
        if kwargs.get('trackNotificationPreferences'):
            self.trackNotificationPreferences = TrackNotificationPreferences(**kwargs.get('trackNotificationPreferences', {}))
        else:
            self.trackNotificationPreferences = None
        if kwargs.get('trivia'):
            self.trivia = TitleTriviaConnection(**kwargs.get('trivia', {}))
        else:
            self.trivia = None
        if kwargs.get('triviaCategories'):
            self.triviaCategories = TriviaCategoryWithTrivia(**kwargs.get('triviaCategories', {}))
        else:
            self.triviaCategories = None
        if kwargs.get('_triviaContributionLink'):
            self._triviaContributionLink = ContributionLink(**kwargs.get('_triviaContributionLink', {}))
        else:
            self._triviaContributionLink = None
        if kwargs.get('userRating'):
            self.userRating = Rating(**kwargs.get('userRating', {}))
        else:
            self.userRating = None
        if kwargs.get('userWatchedStatus'):
            self.userWatchedStatus = WatchedStatus(**kwargs.get('userWatchedStatus', {}))
        else:
            self.userWatchedStatus = None
        if kwargs.get('videos'):
            self.videos = TitleRelatedVideos(**kwargs.get('videos', {}))
        else:
            self.videos = None
        if kwargs.get('videoStrip'):
            self.videoStrip = VideoConnection(**kwargs.get('videoStrip', {}))
        else:
            self.videoStrip = None
        if kwargs.get('videoTypes'):
            self.videoTypes = VideoTypeWithVideos(**kwargs.get('videoTypes', {}))
        else:
            self.videoTypes = None
        if kwargs.get('watchOption'):
            self.watchOption = WatchOption(**kwargs.get('watchOption', {}))
        else:
            self.watchOption = None
        if kwargs.get('watchOptionsByCategory'):
            self.watchOptionsByCategory = CategorizedWatchOptionsList(**kwargs.get('watchOptionsByCategory', {}))
        else:
            self.watchOptionsByCategory = None
    def __str__(self):
        if self.releaseYear:
            return f"{self.titleText} ({self.releaseYear})"
        return f"{self.titleText}"
    def __repr__(self):
        repr_str = f"{self.id}"
        if self.titleText and self.releaseYear:
            repr_str = f"{repr_str}: {self.titleText} ({self.releaseYear})"
        elif self.titleText:
            repr_str = f"{repr_str}: {self.titleText}"
        repr_str = f"<--- {repr_str} --->"
        return repr_str
    def __eq__(self, other):
        if not isinstance(other, Title):
            return False
        return self.id == other.id

class TitleChartMetadata:
    def __init__(self, **kwargs):
        if kwargs.get('chartDescription'):
            self.chartDescription = LocalizedString(**kwargs.get('chartDescription', {}))
        else:
            self.chartDescription = None
        if kwargs.get('chartName'):
            self.chartName = LocalizedString(**kwargs.get('chartName', {}))
        else:
            self.chartName = None
    def __eq__(self, other):
        if not isinstance(other, TitleChartMetadata):
            return False
        return (self.chartDescription == other.chartDescription and self.chartName == other.chartName)

class TitleChartRankingsNode:
    def __init__(self, **kwargs):
        self.chartRating = kwargs.get('chartRating', 0.0)
        self.chartVoteCount = kwargs.get('chartVoteCount', 0)
        if kwargs.get('item'):
            self.item = Title(**kwargs.get('item', {}))
        else:
            self.item = None
    def __eq__(self, other):
        if not isinstance(other, TitleChartRankingsNode):
            return False
        return (self.chartRating == other.chartRating and self.chartVoteCount == other.chartVoteCount and self.item == other.item)

class TitleCinemaShowtimesByScreeningType:
    def __init__(self, **kwargs):
        if kwargs.get('cinema'):
            self.cinema = Cinema(**kwargs.get('cinema', {}))
        else:
            self.cinema = None
        if kwargs.get('distanceToCinema'):
            self.distanceToCinema = DistanceToCinema(**kwargs.get('distanceToCinema', {}))
        else:
            self.distanceToCinema = None
        self.id = kwargs.get('id', "")
        if kwargs.get('showtimesByScreeningType'):
            self.showtimesByScreeningType = ShowtimesByScreeningType(**kwargs.get('showtimesByScreeningType', {}))
        else:
            self.showtimesByScreeningType = None
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, TitleCinemaShowtimesByScreeningType):
            return False
        return self.id == other.id


class TitleCinemaShowtimesByScreeningTypeConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(TitleCinemaShowtimesByScreeningType(**node.get("node", {})))

class TitleCinemaShowtimesFallbackResult:
    def __init__(self, **kwargs):
        self.fallbackDate = kwargs.get('fallbackDate', "")
    def __eq__(self, other):
        if not isinstance(other, TitleCinemaShowtimesFallbackResult):
            return False
        return (self.fallbackDate == other.fallbackDate)

class TitleConnectionCategory:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, TitleConnectionCategory):
            return False
        return self.id == other.id


class TitleConnectionConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(TitleConnection(**node.get("node", {})))

class TitleCreditCategoryWithCredits:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = CreditCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('credits'):
            self.credits = CreditConnection(**kwargs.get('credits', {}))
        else:
            self.credits = None
    def __eq__(self, other):
        if not isinstance(other, TitleCreditCategoryWithCredits):
            return False
        return (self.category == other.category and self.credits == other.credits)

class TitleDisplayOutput:
    def __init__(self, **kwargs):
        self.country = kwargs.get('country', "")
        self.language = kwargs.get('language', "")
        self.prefersReferenceView = kwargs.get('prefersReferenceView', False)
    def __eq__(self, other):
        if not isinstance(other, TitleDisplayOutput):
            return False
        return (self.country == other.country and self.language == other.language and self.prefersReferenceView == other.prefersReferenceView)

class TitleGenre:
    def __init__(self, **kwargs):
        if kwargs.get('genre'):
            self.genre = GenreItem(**kwargs.get('genre', {}))
        else:
            self.genre = None
        self.relevanceRanking = kwargs.get('relevanceRanking', 0)
        if kwargs.get('subGenres'):
            self.subGenres = [TitleKeyword(**subgenre) for subgenre in kwargs.get('subGenres', [])]
        else:
            self.subGenres = None
    def __eq__(self, other):
        if not isinstance(other, TitleGenre):
            return False
        return (self.genre == other.genre and self.relevanceRanking == other.relevanceRanking and self.subGenres == other.subGenres)

class TitleGenreRecommendation:
    def __init__(self, **kwargs):
        if kwargs.get('explanation'):
            self.explanation = LocalizedMarkdown(**kwargs.get('explanation', {}))
        else:
            self.explanation = None
        if kwargs.get('label'):
            self.label = LocalizedString(**kwargs.get('label', {}))
        else:
            self.label = None
        self.refTag = kwargs.get('refTag', "")
        if kwargs.get('titles'):
            self.titles = TitleGenreRecommendationConnection(**kwargs.get('titles', {}))
        else:
            self.titles = None
    def __eq__(self, other):
        if not isinstance(other, TitleGenreRecommendation):
            return False
        return (self.explanation == other.explanation and self.label == other.label and self.refTag == other.refTag and self.titles == other.titles)


class TitleGenreRecommendationConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(TitleGenreRecommendation(**node.get("node", {})))

class TitleGenres:
    def __init__(self, **kwargs):
        if kwargs.get('genres'):
            self.genres = TitleGenre(**kwargs.get('genres', {}))
        else:
            self.genres = None
    def __eq__(self, other):
        if not isinstance(other, TitleGenres):
            return False
        return (self.genres == other.genres)

class TitleKeyword:
    def __init__(self, **kwargs):
        if kwargs.get('interestScore'):
            self.interestScore = InterestScore(**kwargs.get('interestScore', {}))
        else:
            self.interestScore = None
        if kwargs.get('itemCategory'):
            self.itemCategory = TitleKeywordItemCategory(**kwargs.get('itemCategory', {}))
        else:
            self.itemCategory = None
        if kwargs.get('keyword'):
            self.keyword = Keyword(**kwargs.get('keyword', {}))
        else:
            self.keyword = None
        self.legacyId = kwargs.get('legacyId', "")
    def __eq__(self, other):
        if not isinstance(other, TitleKeyword):
            return False
        return (self.interestScore == other.interestScore and self.itemCategory == other.itemCategory and self.keyword == other.keyword and self.legacyId == other.legacyId)


class TitleKeywordConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(TitleKeyword(**node.get("node", {})))

class TitleKeywordItemCategory:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.itemCategoryId = kwargs.get('itemCategoryId', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, TitleKeywordItemCategory):
            return False
        return self.id == other.id

class TitleKeywordItemCategoryWithKeywords:
    def __init__(self, **kwargs):
        if kwargs.get('itemCategory'):
            self.itemCategory = TitleKeywordItemCategory(**kwargs.get('itemCategory', {}))
        else:
            self.itemCategory = None
        if kwargs.get('keywords'):
            self.keywords = TitleKeywordConnection(**kwargs.get('keywords', {}))
        else:
            self.keywords = None
    def __eq__(self, other):
        if not isinstance(other, TitleKeywordItemCategoryWithKeywords):
            return False
        return (self.itemCategory == other.itemCategory and self.keywords == other.keywords)


class TitleConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Title(**node.get("node", {})))

class TitleMeta:
    def __init__(self, **kwargs):
        self.canonicalId = kwargs.get('canonicalId', "")
        self.publicationStatus = kwargs.get('publicationStatus', "")
        if kwargs.get('restrictions'):
            self.restrictions = TitleMetaRestrictions(**kwargs.get('restrictions', {}))
        else:
            self.restrictions = None
    def __eq__(self, other):
        if not isinstance(other, TitleMeta):
            return False
        return (self.canonicalId == other.canonicalId and self.publicationStatus == other.publicationStatus and self.restrictions == other.restrictions)

class TitleMetaRestrictions:
    def __init__(self, **kwargs):
        if kwargs.get('explanations'):
            self.explanations = RestrictionExplanation(**kwargs.get('explanations', {}))
        else:
            self.explanations = None
        self.reasons = kwargs.get('reasons', "")
        self.restrictionReason = kwargs.get('restrictionReason', "")
    def __eq__(self, other):
        if not isinstance(other, TitleMetaRestrictions):
            return False
        return (self.explanations == other.explanations and self.reasons == other.reasons and self.restrictionReason == other.restrictionReason)

class TitleMetadata:
    def __init__(self, **kwargs):
        if kwargs.get('externalLinkCategories'):
            self.externalLinkCategories = ExternalLinkCategory(**kwargs.get('externalLinkCategories', {}))
        else:
            self.externalLinkCategories = None
        if kwargs.get('goofCategories'):
            self.goofCategories = GoofCategory(**kwargs.get('goofCategories', {}))
        else:
            self.goofCategories = None
        if kwargs.get('titleConnectionCategories'):
            self.titleConnectionCategories = TitleConnectionCategory(**kwargs.get('titleConnectionCategories', {}))
        else:
            self.titleConnectionCategories = None
        if kwargs.get('titleGenres'):
            self.titleGenres = GenreItem(**kwargs.get('titleGenres', {}))
        else:
            self.titleGenres = None
        if kwargs.get('titleTypeCategories'):
            self.titleTypeCategories = TitleTypeCategoryWithTitleTypes(**kwargs.get('titleTypeCategories', {}))
        else:
            self.titleTypeCategories = None
        if kwargs.get('titleTypes'):
            self.titleTypes = TitleType(**kwargs.get('titleTypes', {}))
        else:
            self.titleTypes = None
    def __eq__(self, other):
        if not isinstance(other, TitleMetadata):
            return False
        return (self.externalLinkCategories == other.externalLinkCategories and self.goofCategories == other.goofCategories and self.titleConnectionCategories == other.titleConnectionCategories and self.titleGenres == other.titleGenres and self.titleTypeCategories == other.titleTypeCategories and self.titleTypes == other.titleTypes)

class TitleMeterRanking:
    def __init__(self, **kwargs):
        self.currentRank = kwargs.get('currentRank', 0)
        self.meterType = kwargs.get('meterType', "")
        if kwargs.get('rankChange'):
            self.rankChange = MeterRankChange(**kwargs.get('rankChange', {}))
        else:
            self.rankChange = None
    def __eq__(self, other):
        if not isinstance(other, TitleMeterRanking):
            return False
        return (self.currentRank == other.currentRank and self.meterType == other.meterType and self.rankChange == other.rankChange)

class TitleMeterRankingHistory:
    def __init__(self, **kwargs):
        if kwargs.get('bestRank'):
            self.bestRank = MeterRankingHistoryEntry(**kwargs.get('bestRank', {}))
        else:
            self.bestRank = None
        if kwargs.get('ranks'):
            self.ranks = MeterRankingHistoryEntry(**kwargs.get('ranks', {}))
        else:
            self.ranks = None
        if kwargs.get('restriction'):
            self.restriction = MeterRestriction(**kwargs.get('restriction', {}))
        else:
            self.restriction = None
    def __eq__(self, other):
        if not isinstance(other, TitleMeterRankingHistory):
            return False
        return (self.bestRank == other.bestRank and self.ranks == other.ranks and self.restriction == other.restriction)

class TitleQuote:
    def __init__(self, **kwargs):
        if kwargs.get('displayableArticle'):
            self.displayableArticle = DisplayableArticle(**kwargs.get('displayableArticle', {}))
        else:
            self.displayableArticle = None
        self.id = kwargs.get('id', "")
        if kwargs.get('interestScore'):
            self.interestScore = InterestScore(**kwargs.get('interestScore', {}))
        else:
            self.interestScore = None
        self.isSpoiler = kwargs.get('isSpoiler', False)
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        if kwargs.get('lines'):
            self.lines = TitleQuoteLine(**kwargs.get('lines', {}))
        else:
            self.lines = None
    def __eq__(self, other):
        if not isinstance(other, TitleQuote):
            return False
        return self.id == other.id

class TitleQuoteCharacter:
    def __init__(self, **kwargs):
        self.character = kwargs.get('character', "")
        if kwargs.get('name'):
            self.name = Name(**kwargs.get('name', {}))
        else:
            self.name = None
    def __eq__(self, other):
        if not isinstance(other, TitleQuoteCharacter):
            return False
        return (self.character == other.character and self.name == other.name)


class TitleQuoteConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(TitleQuote(**node.get("node", {})))

class TitleQuoteLine:
    def __init__(self, **kwargs):
        if kwargs.get('characters'):
            self.characters = TitleQuoteCharacter(**kwargs.get('characters', {}))
        else:
            self.characters = None
        self.stageDirection = kwargs.get('stageDirection', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, TitleQuoteLine):
            return False
        return (self.characters == other.characters and self.stageDirection == other.stageDirection and self.text == other.text)

class TitleRecommendation:
    def __init__(self, **kwargs):
        if kwargs.get('explanations'):
            self.explanations = RecommendationExplanation(**kwargs.get('explanations', {}))
        else:
            self.explanations = None
        self.refTag = kwargs.get('refTag', "")
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, TitleRecommendation):
            return False
        return (self.explanations == other.explanations and self.refTag == other.refTag and self.title == other.title)

class TitleRelatedVideos:
    def __init__(self, **kwargs):
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, TitleRelatedVideos):
            return False
        return (self.total == other.total)

class TitleReviewExcerpt:
    def __init__(self, **kwargs):
        if kwargs.get('excerpt'):
            self.excerpt = LocalizedMarkdown(**kwargs.get('excerpt', {}))
        else:
            self.excerpt = None
        if kwargs.get('review'):
            self.review = Review(**kwargs.get('review', {}))
        else:
            self.review = None
    def __eq__(self, other):
        if not isinstance(other, TitleReviewExcerpt):
            return False
        return (self.excerpt == other.excerpt and self.review == other.review)

class TitleReviewSentimentSection:
    def __init__(self, **kwargs):
        if kwargs.get('long'):
            self.long = LocalizedMarkdown(**kwargs.get('long', {}))
        else:
            self.long = None
        if kwargs.get('medium'):
            self.medium = LocalizedMarkdown(**kwargs.get('medium', {}))
        else:
            self.medium = None
        if kwargs.get('short'):
            self.short = LocalizedMarkdown(**kwargs.get('short', {}))
        else:
            self.short = None
    def __eq__(self, other):
        if not isinstance(other, TitleReviewSentimentSection):
            return False
        return (self.long == other.long and self.medium == other.medium and self.short == other.short)

class TitleReviewSummary:
    def __init__(self, **kwargs):
        if kwargs.get('negative'):
            self.negative = TitleReviewSentimentSection(**kwargs.get('negative', {}))
        else:
            self.negative = None
        if kwargs.get('overall'):
            self.overall = TitleReviewSentimentSection(**kwargs.get('overall', {}))
        else:
            self.overall = None
        if kwargs.get('positive'):
            self.positive = TitleReviewSentimentSection(**kwargs.get('positive', {}))
        else:
            self.positive = None
        if kwargs.get('themes'):
            self.themes = TitleReviewTheme(**kwargs.get('themes', {}))
        else:
            self.themes = None
    def __eq__(self, other):
        if not isinstance(other, TitleReviewSummary):
            return False
        return (self.negative == other.negative and self.overall == other.overall and self.positive == other.positive and self.themes == other.themes)

class TitleReviewTheme:
    def __init__(self, **kwargs):
        if kwargs.get('label'):
            self.label = LocalizedString(**kwargs.get('label', {}))
        else:
            self.label = None
        if kwargs.get('reviews'):
            self.reviews = TitleReviewExcerpt(**kwargs.get('reviews', {}))
        else:
            self.reviews = None
        self.sentiment = kwargs.get('sentiment', "")
        if kwargs.get('summary'):
            self.summary = LocalizedMarkdown(**kwargs.get('summary', {}))
        else:
            self.summary = None
        self.themeId = kwargs.get('themeId', "")
    def __eq__(self, other):
        if not isinstance(other, TitleReviewTheme):
            return False
        return (self.label == other.label and self.reviews == other.reviews and self.sentiment == other.sentiment and self.summary == other.summary and self.themeId == other.themeId)

class TitleText:
    def __init__(self, **kwargs):
        if kwargs.get('country'):
            self.country = DisplayableCountry(**kwargs.get('country', {}))
        else:
            self.country = None
        self.isOriginalTitle = kwargs.get('isOriginalTitle', False)
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __str__(self):
        return self.text
    def __repr__(self):
        return f"TitleText(country={self.country}, isOriginalTitle={self.isOriginalTitle}, language={self.language}, text={self.text})"
    def __eq__(self, other):
        if not isinstance(other, TitleText):
            return False
        return (self.country == other.country and self.isOriginalTitle == other.isOriginalTitle and self.language == other.language and self.text == other.text)

class TitleTrivia:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = TriviaCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('_correctionLink'):
            self._correctionLink = ContributionLink(**kwargs.get('_correctionLink', {}))
        else:
            self._correctionLink = None
        if kwargs.get('displayableArticle'):
            self.displayableArticle = DisplayableArticle(**kwargs.get('displayableArticle', {}))
        else:
            self.displayableArticle = None
        self.id = kwargs.get('id', "")
        if kwargs.get('interestScore'):
            self.interestScore = InterestScore(**kwargs.get('interestScore', {}))
        else:
            self.interestScore = None
        self.isSpoiler = kwargs.get('isSpoiler', False)
        if kwargs.get('relatedNames'):
            self.relatedNames = Name(**kwargs.get('relatedNames', {}))
        else:
            self.relatedNames = None
        if kwargs.get('_reportingLink'):
            self._reportingLink = ContributionLink(**kwargs.get('_reportingLink', {}))
        else:
            self._reportingLink = None
        if kwargs.get('text'):
            self.text = Markdown(**kwargs.get('text', {}))
        else:
            self.text = None
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
        if kwargs.get('trademark'):
            self.trademark = Markdown(**kwargs.get('trademark', {}))
        else:
            self.trademark = None
    def __eq__(self, other):
        if not isinstance(other, TitleTrivia):
            return False
        return self.id == other.id


class TitleTriviaConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(TitleTrivia(**node.get("node", {})))

class TitleType:
    def __init__(self, **kwargs):
        self.canHaveEpisodes = kwargs.get('canHaveEpisodes', False)
        if kwargs.get('categories'):
            self.categories = [TitleTypeCategory(**category) for category in kwargs.get('categories', [])]
        else:
            self.categories = None
        if kwargs.get('displayableProperty'):
            self.displayableProperty = DisplayableTitleTypeProperty(**kwargs.get('displayableProperty', {}))
        else:
            self.displayableProperty = None
        self.id = kwargs.get('id', "")
        self.isEpisode = kwargs.get('isEpisode', False)
        self.isSeries = kwargs.get('isSeries', False)
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, TitleType):
            return False
        return self.id == other.id

class TitleTypeCategory:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
        self.value = kwargs.get('value', [])
    def __eq__(self, other):
        if not isinstance(other, TitleTypeCategory):
            return False
        return self.id == other.id

class TitleTypeCategorySummary:
    def __init__(self, **kwargs):
        if kwargs.get('titleTypeCategory'):
            self.titleTypeCategory = TitleTypeCategory(**kwargs.get('titleTypeCategory', {}))
        else:
            self.titleTypeCategory = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, TitleTypeCategorySummary):
            return False
        return (self.titleTypeCategory == other.titleTypeCategory and self.total == other.total)

class TitleTypeCategoryWithTitleTypes:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = TitleTypeCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('titleTypes'):
            self.titleTypes = TitleType(**kwargs.get('titleTypes', {}))
        else:
            self.titleTypes = None
    def __eq__(self, other):
        if not isinstance(other, TitleTypeCategoryWithTitleTypes):
            return False
        return (self.category == other.category and self.titleTypes == other.titleTypes)

class TitleTypeSummary:
    def __init__(self, **kwargs):
        if kwargs.get('titleType'):
            self.titleType = TitleType(**kwargs.get('titleType', {}))
        else:
            self.titleType = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, TitleTypeSummary):
            return False
        return (self.titleType == other.titleType and self.total == other.total)

class TitleWatchedStatus:
    def __init__(self, **kwargs):
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
        if kwargs.get('watchedStatus'):
            self.watchedStatus = WatchedStatus(**kwargs.get('watchedStatus', {}))
        else:
            self.watchedStatus = None
    def __eq__(self, other):
        if not isinstance(other, TitleWatchedStatus):
            return False
        return (self.title == other.title and self.watchedStatus == other.watchedStatus)

class TitleWatchlistRecommendation:
    def __init__(self, **kwargs):
        if kwargs.get('explanation'):
            self.explanation = LocalizedMarkdown(**kwargs.get('explanation', {}))
        else:
            self.explanation = None
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, TitleWatchlistRecommendation):
            return False
        return (self.explanation == other.explanation and self.title == other.title)

class TopGrossingReleasesNode:
    def __init__(self, **kwargs):
        if kwargs.get('gross'):
            self.gross = BoxOfficeGross(**kwargs.get('gross', {}))
        else:
            self.gross = None
        if kwargs.get('release'):
            self.release = BoxOfficeRelease(**kwargs.get('release', {}))
        else:
            self.release = None
    def __eq__(self, other):
        if not isinstance(other, TopGrossingReleasesNode):
            return False
        return (self.gross == other.gross and self.release == other.release)

class TopRanking:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.rank = kwargs.get('rank', 0)
        if kwargs.get('text'):
            self.text = LocalizedString(**kwargs.get('text', {}))
        else:
            self.text = None
    def __eq__(self, other):
        if not isinstance(other, TopRanking):
            return False
        return self.id == other.id

class TotalCredits:
    def __init__(self, **kwargs):
        if kwargs.get('restriction'):
            self.restriction = CreditRestriction(**kwargs.get('restriction', {}))
        else:
            self.restriction = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, TotalCredits):
            return False
        return (self.restriction == other.restriction and self.total == other.total)

class Track:
    def __init__(self, **kwargs):
        if kwargs.get('amazonMusicProducts'):
            self.amazonMusicProducts = AmazonMusicProduct(**kwargs.get('amazonMusicProducts', {}))
        else:
            self.amazonMusicProducts = None
        if kwargs.get('comments'):
            self.comments = Markdown(**kwargs.get('comments', {}))
        else:
            self.comments = None
        if kwargs.get('displayableArticle'):
            self.displayableArticle = DisplayableArticle(**kwargs.get('displayableArticle', {}))
        else:
            self.displayableArticle = None
        self.id = kwargs.get('id', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, Track):
            return False
        return self.id == other.id


class TrackConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Track(**node.get("node", {})))

class TrackNotificationPreference:
    def __init__(self, **kwargs):
        self.interested = kwargs.get('interested', False)
        if kwargs.get('type'):
            self.type = TrackNotificationPreferenceType(**kwargs.get('type', {}))
        else:
            self.type = None
    def __eq__(self, other):
        if not isinstance(other, TrackNotificationPreference):
            return False
        return (self.interested == other.interested and self.type == other.type)

class TrackNotificationPreferenceType:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('language'):
            self.language = DisplayableLanguage(**kwargs.get('language', {}))
        else:
            self.language = None
        self.text = kwargs.get('text', "")
        self.typeId = kwargs.get('typeId', "")
    def __eq__(self, other):
        if not isinstance(other, TrackNotificationPreferenceType):
            return False
        return self.id == other.id

class TrackNotificationPreferences:
    def __init__(self, **kwargs):
        self.isTracking = kwargs.get('isTracking', False)
        if kwargs.get('notificationPreferences'):
            self.notificationPreferences = TrackNotificationPreference(**kwargs.get('notificationPreferences', {}))
        else:
            self.notificationPreferences = None
    def __eq__(self, other):
        if not isinstance(other, TrackNotificationPreferences):
            return False
        return (self.isTracking == other.isTracking and self.notificationPreferences == other.notificationPreferences)

class Trademark:
    def __init__(self, **kwargs):
        if kwargs.get('displayableArticle'):
            self.displayableArticle = DisplayableArticle(**kwargs.get('displayableArticle', {}))
        else:
            self.displayableArticle = None
        if kwargs.get('text'):
            self.text = Markdown(**kwargs.get('text', {}))
        else:
            self.text = None
    def __eq__(self, other):
        if not isinstance(other, Trademark):
            return False
        return (self.displayableArticle == other.displayableArticle and self.text == other.text)


class TrademarkConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Trademark(**node.get("node", {})))

class TrendingCollectionOption:
    def __init__(self, **kwargs):
        if kwargs.get('country'):
            self.country = DisplayableCountry(**kwargs.get('country', {}))
        else:
            self.country = None
        self.dataWindow = kwargs.get('dataWindow', "")
        self.trafficSource = kwargs.get('trafficSource', "")
    def __eq__(self, other):
        if not isinstance(other, TrendingCollectionOption):
            return False
        return (self.country == other.country and self.dataWindow == other.dataWindow and self.trafficSource == other.trafficSource)

class TrendingNameCollection:
    def __init__(self, **kwargs):
        if kwargs.get('items'):
            self.items = TrendingNameNodeConnection(**kwargs.get('items', {}))
        else:
            self.items = None
        if kwargs.get('option'):
            self.option = TrendingCollectionOption(**kwargs.get('option', {}))
        else:
            self.option = None
    def __eq__(self, other):
        if not isinstance(other, TrendingNameCollection):
            return False
        return (self.items == other.items and self.option == other.option)

class TrendingNameCollectionOptions:
    def __init__(self, **kwargs):
        if kwargs.get('options'):
            self.options = TrendingCollectionOption(**kwargs.get('options', {}))
        else:
            self.options = None
        if kwargs.get('selectedItem'):
            self.selectedItem = TrendingNameCollection(**kwargs.get('selectedItem', {}))
        else:
            self.selectedItem = None
    def __eq__(self, other):
        if not isinstance(other, TrendingNameCollectionOptions):
            return False
        return (self.options == other.options and self.selectedItem == other.selectedItem)

class TrendingNameNode:
    def __init__(self, **kwargs):
        if kwargs.get('item'):
            self.item = Name(**kwargs.get('item', {}))
        else:
            self.item = None
        self.rank = kwargs.get('rank', 0)
        self.weightRank = kwargs.get('weightRank', 0)
    def __eq__(self, other):
        if not isinstance(other, TrendingNameNode):
            return False
        return (self.item == other.item and self.rank == other.rank and self.weightRank == other.weightRank)


class TrendingNameNodeConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(TrendingNameNode(**node.get("node", {})))

class TrendingTitleCollection:
    def __init__(self, **kwargs):
        if kwargs.get('items'):
            self.items = TrendingTitleNodeConnection(**kwargs.get('items', {}))
        else:
            self.items = None
        if kwargs.get('option'):
            self.option = TrendingCollectionOption(**kwargs.get('option', {}))
        else:
            self.option = None
    def __eq__(self, other):
        if not isinstance(other, TrendingTitleCollection):
            return False
        return (self.items == other.items and self.option == other.option)

class TrendingTitleCollectionOptions:
    def __init__(self, **kwargs):
        if kwargs.get('options'):
            self.options = TrendingCollectionOption(**kwargs.get('options', {}))
        else:
            self.options = None
        if kwargs.get('selectedItem'):
            self.selectedItem = TrendingTitleCollection(**kwargs.get('selectedItem', {}))
        else:
            self.selectedItem = None
    def __eq__(self, other):
        if not isinstance(other, TrendingTitleCollectionOptions):
            return False
        return (self.options == other.options and self.selectedItem == other.selectedItem)

class TrendingTitleNode:
    def __init__(self, **kwargs):
        if kwargs.get('item'):
            self.item = Title(**kwargs.get('item', {}))
        else:
            self.item = None
        self.rank = kwargs.get('rank', 0)
        self.weightRank = kwargs.get('weightRank', 0)
    def __eq__(self, other):
        if not isinstance(other, TrendingTitleNode):
            return False
        return (self.item == other.item and self.rank == other.rank and self.weightRank == other.weightRank)


class TrendingTitleNodeConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(TrendingTitleNode(**node.get("node", {})))

class TrendingVideoNode:
    def __init__(self, **kwargs):
        if kwargs.get('item'):
            self.item = Video(**kwargs.get('item', {}))
        else:
            self.item = None
        self.rank = kwargs.get('rank', 0)
        self.weightRank = kwargs.get('weightRank', 0)
    def __eq__(self, other):
        if not isinstance(other, TrendingVideoNode):
            return False
        return (self.item == other.item and self.rank == other.rank and self.weightRank == other.weightRank)

class TriviaCategory:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, TriviaCategory):
            return False
        return self.id == other.id

class TriviaCategoryWithTrivia:
    def __init__(self, **kwargs):
        if kwargs.get('category'):
            self.category = TriviaCategory(**kwargs.get('category', {}))
        else:
            self.category = None
        if kwargs.get('restriction'):
            self.restriction = TriviaRestriction(**kwargs.get('restriction', {}))
        else:
            self.restriction = None
        if kwargs.get('trivia'):
            self.trivia = TitleTriviaConnection(**kwargs.get('trivia', {}))
        else:
            self.trivia = None
    def __eq__(self, other):
        if not isinstance(other, TriviaCategoryWithTrivia):
            return False
        return (self.category == other.category and self.restriction == other.restriction and self.trivia == other.trivia)

class TriviaRestriction:
    def __init__(self, **kwargs):
        if kwargs.get('explanations'):
            self.explanations = RestrictionExplanation(**kwargs.get('explanations', {}))
        else:
            self.explanations = None
        self.reasons = kwargs.get('reasons', "")
        self.restrictionReason = kwargs.get('restrictionReason', "")
        self.unrestrictedTotal = kwargs.get('unrestrictedTotal', 0)
    def __eq__(self, other):
        if not isinstance(other, TriviaRestriction):
            return False
        return (self.explanations == other.explanations and self.reasons == other.reasons and self.restrictionReason == other.restrictionReason and self.unrestrictedTotal == other.unrestrictedTotal)

class TwitterLink:
    def __init__(self, **kwargs):
        self.label = kwargs.get('label', "")
        self.url = kwargs.get('url', "")
        self.username = kwargs.get('username', "")
    def __eq__(self, other):
        if not isinstance(other, TwitterLink):
            return False
        return (self.label == other.label and self.url == other.url and self.username == other.username)

class UIWorkflow:
    def __init__(self, **kwargs):
        if kwargs.get('actionTray'):
            self.actionTray = UIWorkflowActionTray(**kwargs.get('actionTray', {}))
        else:
            self.actionTray = None
        if kwargs.get('contentHeader'):
            self.contentHeader = UIWorkflowContentHeader(**kwargs.get('contentHeader', {}))
        else:
            self.contentHeader = None
        if kwargs.get('contextHeader'):
            self.contextHeader = UIWorkflowContextHeader(**kwargs.get('contextHeader', {}))
        else:
            self.contextHeader = None
        if kwargs.get('workflowState'):
            self.workflowState = UIWorkflowExecutionState(**kwargs.get('workflowState', {}))
        else:
            self.workflowState = None
        self.workflowType = kwargs.get('workflowType', "")
    def __eq__(self, other):
        if not isinstance(other, UIWorkflow):
            return False
        return (self.actionTray == other.actionTray and self.contentHeader == other.contentHeader and self.contextHeader == other.contextHeader and self.workflowState == other.workflowState and self.workflowType == other.workflowType)

class UIWorkflowAction:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('label'):
            self.label = LocalizedString(**kwargs.get('label', {}))
        else:
            self.label = None
        self.navigationDirection = kwargs.get('navigationDirection', "")
        self.requiresFormData = kwargs.get('requiresFormData', False)
        self.type = kwargs.get('type', "")
    def __eq__(self, other):
        if not isinstance(other, UIWorkflowAction):
            return False
        return self.id == other.id

class UIWorkflowActionTray:
    def __init__(self, **kwargs):
        if kwargs.get('actions'):
            self.actions = UIWorkflowAction(**kwargs.get('actions', {}))
        else:
            self.actions = None
    def __eq__(self, other):
        if not isinstance(other, UIWorkflowActionTray):
            return False
        return (self.actions == other.actions)

class UIWorkflowBody:
    def __init__(self, **kwargs):
        pass
    def __eq__(self, other):
        if not isinstance(other, UIWorkflowBody):
            return False
        return True

class UIWorkflowContentHeader:
    def __init__(self, **kwargs):
        if kwargs.get('heading'):
            self.heading = LocalizedMarkdown(**kwargs.get('heading', {}))
        else:
            self.heading = None
        if kwargs.get('helpLink'):
            self.helpLink = HelpLink(**kwargs.get('helpLink', {}))
        else:
            self.helpLink = None
    def __eq__(self, other):
        if not isinstance(other, UIWorkflowContentHeader):
            return False
        return (self.heading == other.heading and self.helpLink == other.helpLink)

class UIWorkflowContextHeader:
    def __init__(self, **kwargs):
        if kwargs.get('heading'):
            self.heading = LocalizedMarkdown(**kwargs.get('heading', {}))
        else:
            self.heading = None
    def __eq__(self, other):
        if not isinstance(other, UIWorkflowContextHeader):
            return False
        return (self.heading == other.heading)

class UIWorkflowExecutionState:
    def __init__(self, **kwargs):
        self.executionId = kwargs.get('executionId', "")
        self.interactionId = kwargs.get('interactionId', "")
        self.status = kwargs.get('status', "")
        self.workflowId = kwargs.get('workflowId', "")
    def __eq__(self, other):
        if not isinstance(other, UIWorkflowExecutionState):
            return False
        return (self.executionId == other.executionId and self.interactionId == other.interactionId and self.status == other.status and self.workflowId == other.workflowId)

class UIWorkflowGlobalMenu:
    def __init__(self, **kwargs):
        pass
    def __eq__(self, other):
        if not isinstance(other, UIWorkflowGlobalMenu):
            return False
        return True

class UpdateUserProfileFeedback:
    def __init__(self, **kwargs):
        if kwargs.get('validationFeedback'):
            self.validationFeedback = ValidationFeedback(**kwargs.get('validationFeedback', {}))
        else:
            self.validationFeedback = None
    def __eq__(self, other):
        if not isinstance(other, UpdateUserProfileFeedback):
            return False
        return (self.validationFeedback == other.validationFeedback)

class User:
    def __init__(self, **kwargs):
        self.displayName = kwargs.get('displayName', "")
        if kwargs.get('feedbackGiven'):
            self.feedbackGiven = FeedbackGiven(**kwargs.get('feedbackGiven', {}))
        else:
            self.feedbackGiven = None
        self.fullName = kwargs.get('fullName', "")
        if kwargs.get('interests'):
            self.interests = InterestConnection(**kwargs.get('interests', {}))
        else:
            self.interests = None
        if kwargs.get('linkedAuthProviders'):
            self.linkedAuthProviders = LinkedAuthProvider(**kwargs.get('linkedAuthProviders', {}))
        else:
            self.linkedAuthProviders = None
        self.preferredLanguage = kwargs.get('preferredLanguage', "")
        if kwargs.get('preferredStreamingProviders'):
            self.preferredStreamingProviders = UserPreferredStreamingProvidersOutput(**kwargs.get('preferredStreamingProviders', {}))
        else:
            self.preferredStreamingProviders = None
        if kwargs.get('profile'):
            self.profile = UserProfile(**kwargs.get('profile', {}))
        else:
            self.profile = None
        if kwargs.get('proStatus'):
            self.proStatus = ProStatus(**kwargs.get('proStatus', {}))
        else:
            self.proStatus = None
        if kwargs.get('ratingsPrivacy'):
            self.ratingsPrivacy = RatingsPrivacy(**kwargs.get('ratingsPrivacy', {}))
        else:
            self.ratingsPrivacy = None
        if kwargs.get('staffStatus'):
            self.staffStatus = StaffStatus(**kwargs.get('staffStatus', {}))
        else:
            self.staffStatus = None
        if kwargs.get('titleDisplay'):
            self.titleDisplay = TitleDisplayOutput(**kwargs.get('titleDisplay', {}))
        else:
            self.titleDisplay = None
    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return (self.displayName == other.displayName and self.feedbackGiven == other.feedbackGiven and self.fullName == other.fullName and self.interests == other.interests and self.linkedAuthProviders == other.linkedAuthProviders and self.preferredLanguage == other.preferredLanguage and self.preferredStreamingProviders == other.preferredStreamingProviders and self.profile == other.profile and self.proStatus == other.proStatus and self.ratingsPrivacy == other.ratingsPrivacy and self.staffStatus == other.staffStatus and self.titleDisplay == other.titleDisplay)

class UserConsentOutput:
    def __init__(self, **kwargs):
        if kwargs.get('consent'):
            self.consent = Consent(**kwargs.get('consent', {}))
        else:
            self.consent = None
        self.consentOperation = kwargs.get('consentOperation', "")
        self.consentType = kwargs.get('consentType', "")
    def __eq__(self, other):
        if not isinstance(other, UserConsentOutput):
            return False
        return (self.consent == other.consent and self.consentOperation == other.consentOperation and self.consentType == other.consentType)

class UserLinkedAuthProviderStatusesOutput:
    def __init__(self, **kwargs):
        if kwargs.get('providers'):
            self.providers = AuthProviderStatus(**kwargs.get('providers', {}))
        else:
            self.providers = None
    def __eq__(self, other):
        if not isinstance(other, UserLinkedAuthProviderStatusesOutput):
            return False
        return (self.providers == other.providers)

class UserNotification:
    def __init__(self, **kwargs):
        if kwargs.get('header'):
            self.header = LocalizedString(**kwargs.get('header', {}))
        else:
            self.header = None
        self.id = kwargs.get('id', "")
        if kwargs.get('image'):
            self.image = MediaServiceImage(**kwargs.get('image', {}))
        else:
            self.image = None
        self.lastUpdated = kwargs.get('lastUpdated', "")
        if kwargs.get('primaryContent'):
            self.primaryContent = LocalizedMarkdown(**kwargs.get('primaryContent', {}))
        else:
            self.primaryContent = None
        if kwargs.get('secondaryContent'):
            self.secondaryContent = LocalizedString(**kwargs.get('secondaryContent', {}))
        else:
            self.secondaryContent = None
        self.url = kwargs.get('url', "")
    def __eq__(self, other):
        if not isinstance(other, UserNotification):
            return False
        return self.id == other.id

class UserPreferredStreamingProvidersOutput:
    def __init__(self, **kwargs):
        if kwargs.get('streamingProviders'):
            self.streamingProviders = WatchProviderConnection(**kwargs.get('streamingProviders', {}))
        else:
            self.streamingProviders = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, UserPreferredStreamingProvidersOutput):
            return False
        return (self.streamingProviders == other.streamingProviders and self.total == other.total)

class UserProfile:
    def __init__(self, **kwargs):
        if kwargs.get('bio'):
            self.bio = UserProfileBio(**kwargs.get('bio', {}))
        else:
            self.bio = None
        self.creationDate = kwargs.get('creationDate', "")
        if kwargs.get('primaryImage'):
            self.primaryImage = UserProfileImage(**kwargs.get('primaryImage', {}))
        else:
            self.primaryImage = None
        self.userId = kwargs.get('userId', "")
        if kwargs.get('username'):
            self.username = UserProfileUsername(**kwargs.get('username', {}))
        else:
            self.username = None
    def __eq__(self, other):
        if not isinstance(other, UserProfile):
            return False
        return (self.bio == other.bio and self.creationDate == other.creationDate and self.primaryImage == other.primaryImage and self.userId == other.userId and self.username == other.username)

class UserProfileBio:
    def __init__(self, **kwargs):
        if kwargs.get('status'):
            self.status = UserProfileBioUpdateStatus(**kwargs.get('status', {}))
        else:
            self.status = None
        if kwargs.get('text'):
            self.text = Markdown(**kwargs.get('text', {}))
        else:
            self.text = None
    def __eq__(self, other):
        if not isinstance(other, UserProfileBio):
            return False
        return (self.status == other.status and self.text == other.text)

class UserProfileBioUpdateStatus:
    def __init__(self, **kwargs):
        self.lastUpdated = kwargs.get('lastUpdated', "")
        if kwargs.get('modifiedItem'):
            self.modifiedItem = Markdown(**kwargs.get('modifiedItem', {}))
        else:
            self.modifiedItem = None
        if kwargs.get('updateFeedback'):
            self.updateFeedback = UpdateUserProfileFeedback(**kwargs.get('updateFeedback', {}))
        else:
            self.updateFeedback = None
        self.updateStatus = kwargs.get('updateStatus', "")
    def __eq__(self, other):
        if not isinstance(other, UserProfileBioUpdateStatus):
            return False
        return (self.lastUpdated == other.lastUpdated and self.modifiedItem == other.modifiedItem and self.updateFeedback == other.updateFeedback and self.updateStatus == other.updateStatus)

class UserProfileImage:
    def __init__(self, **kwargs):
        if kwargs.get('image'):
            self.image = Image(**kwargs.get('image', {}))
        else:
            self.image = None
        if kwargs.get('status'):
            self.status = UserProfileImageUpdateStatus(**kwargs.get('status', {}))
        else:
            self.status = None
    def __eq__(self, other):
        if not isinstance(other, UserProfileImage):
            return False
        return (self.image == other.image and self.status == other.status)

class UserProfileImageUpdateStatus:
    def __init__(self, **kwargs):
        self.lastUpdated = kwargs.get('lastUpdated', "")
        if kwargs.get('modifiedItem'):
            self.modifiedItem = Image(**kwargs.get('modifiedItem', {}))
        else:
            self.modifiedItem = None
        if kwargs.get('updateFeedback'):
            self.updateFeedback = UpdateUserProfileFeedback(**kwargs.get('updateFeedback', {}))
        else:
            self.updateFeedback = None
        self.updateStatus = kwargs.get('updateStatus', "")
    def __eq__(self, other):
        if not isinstance(other, UserProfileImageUpdateStatus):
            return False
        return (self.lastUpdated == other.lastUpdated and self.modifiedItem == other.modifiedItem and self.updateFeedback == other.updateFeedback and self.updateStatus == other.updateStatus)

class UserProfileUsername:
    def __init__(self, **kwargs):
        if kwargs.get('status'):
            self.status = UserProfileUsernameUpdateStatus(**kwargs.get('status', {}))
        else:
            self.status = None
        self.text = kwargs.get('text', "")
    def __eq__(self, other):
        if not isinstance(other, UserProfileUsername):
            return False
        return (self.status == other.status and self.text == other.text)

class UserProfileUsernameUpdateStatus:
    def __init__(self, **kwargs):
        self.lastUpdated = kwargs.get('lastUpdated', "")
        self.modifiedItem = kwargs.get('modifiedItem', "")
        if kwargs.get('updateFeedback'):
            self.updateFeedback = UpdateUserProfileFeedback(**kwargs.get('updateFeedback', {}))
        else:
            self.updateFeedback = None
        self.updateStatus = kwargs.get('updateStatus', "")
    def __eq__(self, other):
        if not isinstance(other, UserProfileUsernameUpdateStatus):
            return False
        return (self.lastUpdated == other.lastUpdated and self.modifiedItem == other.modifiedItem and self.updateFeedback == other.updateFeedback and self.updateStatus == other.updateStatus)

class UserReaction:
    def __init__(self, **kwargs):
        self.entityId = kwargs.get('entityId', "")
        self.lastUpdated = kwargs.get('lastUpdated', "")
        if kwargs.get('reaction'):
            self.reaction = Reaction(**kwargs.get('reaction', {}))
        else:
            self.reaction = None
    def __eq__(self, other):
        if not isinstance(other, UserReaction):
            return False
        return (self.entityId == other.entityId and self.lastUpdated == other.lastUpdated and self.reaction == other.reaction)

class ValidationFeedback:
    def __init__(self, **kwargs):
        if kwargs.get('message'):
            self.message = LocalizedMarkdown(**kwargs.get('message', {}))
        else:
            self.message = None
        self.status = kwargs.get('status', "")
        if kwargs.get('title'):
            self.title = LocalizedMarkdown(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, ValidationFeedback):
            return False
        return (self.message == other.message and self.status == other.status and self.title == other.title)

class VanityUrl:
    def __init__(self, **kwargs):
        self.label = kwargs.get('label', "")
        if kwargs.get('name'):
            self.name = Name(**kwargs.get('name', {}))
        else:
            self.name = None
        self.url = kwargs.get('url', "")
        self.urlPath = kwargs.get('urlPath', "")
    def __eq__(self, other):
        if not isinstance(other, VanityUrl):
            return False
        return (self.label == other.label and self.name == other.name and self.url == other.url and self.urlPath == other.urlPath)

class Video:
    def __init__(self, **kwargs):
        self.appAdURL = kwargs.get('appAdURL', "")
        self.appAdURLV2 = kwargs.get('appAdURLV2', "")
        if kwargs.get('contentType'):
            self.contentType = VideoContentType(**kwargs.get('contentType', {}))
        else:
            self.contentType = None
        self.createdDate = kwargs.get('createdDate', "")
        if kwargs.get('description'):
            self.description = LocalizedString(**kwargs.get('description', {}))
        else:
            self.description = None
        self.id = kwargs.get('id', "")
        self.isMature = kwargs.get('isMature', False)
        if kwargs.get('name'):
            self.name = LocalizedString(**kwargs.get('name', {}))
        else:
            self.name = None
        if kwargs.get('personalizedSuggestedVideos'):
            self.personalizedSuggestedVideos = VideoConnection(**kwargs.get('personalizedSuggestedVideos', {}))
        else:
            self.personalizedSuggestedVideos = None
        if kwargs.get('playbackURLs'):
            self.playbackURLs = PlaybackURL(**kwargs.get('playbackURLs', {}))
        else:
            self.playbackURLs = None
        if kwargs.get('previewURLs'):
            self.previewURLs = PlaybackURL(**kwargs.get('previewURLs', {}))
        else:
            self.previewURLs = None
        if kwargs.get('primaryTitle'):
            self.primaryTitle = Title(**kwargs.get('primaryTitle', {}))
        else:
            self.primaryTitle = None
        if kwargs.get('providerType'):
            self.providerType = VideoProviderType(**kwargs.get('providerType', {}))
        else:
            self.providerType = None
        if kwargs.get('reactionsSummary'):
            self.reactionsSummary = ReactionsSummary(**kwargs.get('reactionsSummary', {}))
        else:
            self.reactionsSummary = None
        if kwargs.get('recommendedTimedTextTrack'):
            self.recommendedTimedTextTrack = VideoTimedTextTrack(**kwargs.get('recommendedTimedTextTrack', {}))
        else:
            self.recommendedTimedTextTrack = None
        if kwargs.get('relatedNames'):
            self.relatedNames = VideoNameRelationConnection(**kwargs.get('relatedNames', {}))
        else:
            self.relatedNames = None
        if kwargs.get('relatedTitles'):
            self.relatedTitles = VideoTitleRelationConnection(**kwargs.get('relatedTitles', {}))
        else:
            self.relatedTitles = None
        if kwargs.get('relatedVideos'):
            self.relatedVideos = VideoConnection(**kwargs.get('relatedVideos', {}))
        else:
            self.relatedVideos = None
        if kwargs.get('runtime'):
            self.runtime = VideoRuntime(**kwargs.get('runtime', {}))
        else:
            self.runtime = None
        if kwargs.get('thumbnail'):
            self.thumbnail = Thumbnail(**kwargs.get('thumbnail', {}))
        else:
            self.thumbnail = None
        if kwargs.get('timedTextTracks'):
            self.timedTextTracks = VideoTimedTextTrack(**kwargs.get('timedTextTracks', {}))
        else:
            self.timedTextTracks = None
        if kwargs.get('userReactions'):
            self.userReactions = UserReaction(**kwargs.get('userReactions', {}))
        else:
            self.userReactions = None
        if kwargs.get('videoDimensions'):
            self.videoDimensions = VideoDimensions(**kwargs.get('videoDimensions', {}))
        else:
            self.videoDimensions = None
        self.webAdURL = kwargs.get('webAdURL', "")
        self.webAdURLV2 = kwargs.get('webAdURLV2', "")
    def __eq__(self, other):
        if not isinstance(other, Video):
            return False
        return self.id == other.id

class VideoContentType:
    def __init__(self, **kwargs):
        if kwargs.get('displayName'):
            self.displayName = LocalizedString(**kwargs.get('displayName', {}))
        else:
            self.displayName = None
        self.id = kwargs.get('id', "")
    def __eq__(self, other):
        if not isinstance(other, VideoContentType):
            return False
        return self.id == other.id

class VideoDimensions:
    def __init__(self, **kwargs):
        self.appearance = kwargs.get('appearance', "")
        self.aspectRatio = kwargs.get('aspectRatio', 0.0)
        self.height = kwargs.get('height', 0)
        self.width = kwargs.get('width', 0)
    def __eq__(self, other):
        if not isinstance(other, VideoDimensions):
            return False
        return (self.appearance == other.appearance and self.aspectRatio == other.aspectRatio and self.height == other.height and self.width == other.width)

class VideoFacets:
    def __init__(self, **kwargs):
        if kwargs.get('names'):
            self.names = VideoNameFacet(**kwargs.get('names', {}))
        else:
            self.names = None
        if kwargs.get('titles'):
            self.titles = VideoTitleFacet(**kwargs.get('titles', {}))
        else:
            self.titles = None
        if kwargs.get('types'):
            self.types = VideoTypeFacet(**kwargs.get('types', {}))
        else:
            self.types = None
    def __eq__(self, other):
        if not isinstance(other, VideoFacets):
            return False
        return (self.names == other.names and self.titles == other.titles and self.types == other.types)


class VideoConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(Video(**node.get("node", {})))

class VideoMedia:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
        if kwargs.get('name'):
            self.name = LocalizedString(**kwargs.get('name', {}))
        else:
            self.name = None
        if kwargs.get('primaryImage'):
            self.primaryImage = MediaServiceImage(**kwargs.get('primaryImage', {}))
        else:
            self.primaryImage = None
        if kwargs.get('runtime'):
            self.runtime = VideoRuntime(**kwargs.get('runtime', {}))
        else:
            self.runtime = None
    def __eq__(self, other):
        if not isinstance(other, VideoMedia):
            return False
        return self.id == other.id

class VideoNameFacet:
    def __init__(self, **kwargs):
        if kwargs.get('name'):
            self.name = Name(**kwargs.get('name', {}))
        else:
            self.name = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, VideoNameFacet):
            return False
        return (self.name == other.name and self.total == other.total)

class VideoNameRelation:
    def __init__(self, **kwargs):
        if kwargs.get('name'):
            self.name = Name(**kwargs.get('name', {}))
        else:
            self.name = None
    def __eq__(self, other):
        if not isinstance(other, VideoNameRelation):
            return False
        return (self.name == other.name)


class VideoNameRelationConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(VideoNameRelation(**node.get("node", {})))

class VideoProviderType:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', "")
    def __eq__(self, other):
        if not isinstance(other, VideoProviderType):
            return False
        return self.id == other.id

class VideoRuntime:
    def __init__(self, **kwargs):
        self.unit = kwargs.get('unit', "")
        self.value = kwargs.get('value', 0)
    def __eq__(self, other):
        if not isinstance(other, VideoRuntime):
            return False
        return (self.unit == other.unit and self.value == other.value)

class VideoTimedTextTrack:
    def __init__(self, **kwargs):
        if kwargs.get('displayName'):
            self.displayName = LocalizedString(**kwargs.get('displayName', {}))
        else:
            self.displayName = None
        self.language = kwargs.get('language', "")
        self.refTagFragment = kwargs.get('refTagFragment', "")
        self.type = kwargs.get('type', "")
        self.url = kwargs.get('url', "")
    def __eq__(self, other):
        if not isinstance(other, VideoTimedTextTrack):
            return False
        return (self.displayName == other.displayName and self.language == other.language and self.refTagFragment == other.refTagFragment and self.type == other.type and self.url == other.url)

class VideoTitleFacet:
    def __init__(self, **kwargs):
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
        self.total = kwargs.get('total', 0)
    def __eq__(self, other):
        if not isinstance(other, VideoTitleFacet):
            return False
        return (self.title == other.title and self.total == other.total)

class VideoTitleRelation:
    def __init__(self, **kwargs):
        if kwargs.get('title'):
            self.title = Title(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, VideoTitleRelation):
            return False
        return (self.title == other.title)


class VideoTitleRelationConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(VideoTitleRelation(**node.get("node", {})))

class VideoTypeFacet:
    def __init__(self, **kwargs):
        self.total = kwargs.get('total', 0)
        if kwargs.get('type'):
            self.type = VideoContentType(**kwargs.get('type', {}))
        else:
            self.type = None
    def __eq__(self, other):
        if not isinstance(other, VideoTypeFacet):
            return False
        return (self.total == other.total and self.type == other.type)

class VideoTypeWithVideos:
    def __init__(self, **kwargs):
        if kwargs.get('videos'):
            self.videos = VideoConnection(**kwargs.get('videos', {}))
        else:
            self.videos = None
        if kwargs.get('videoType'):
            self.videoType = VideoContentType(**kwargs.get('videoType', {}))
        else:
            self.videoType = None
    def __eq__(self, other):
        if not isinstance(other, VideoTypeWithVideos):
            return False
        return (self.videos == other.videos and self.videoType == other.videoType)

class WatchOption:
    def __init__(self, **kwargs):
        if kwargs.get('description'):
            self.description = LocalizedString(**kwargs.get('description', {}))
        else:
            self.description = None
        self.link = kwargs.get('link', "")
        self.promoted = kwargs.get('promoted', False)
        if kwargs.get('provider'):
            self.provider = WatchProvider(**kwargs.get('provider', {}))
        else:
            self.provider = None
        if kwargs.get('providerName'):
            self.providerName = LocalizedString(**kwargs.get('providerName', {}))
        else:
            self.providerName = None
        self.providerRefTagFragment = kwargs.get('providerRefTagFragment', "")
        if kwargs.get('shortDescription'):
            self.shortDescription = LocalizedString(**kwargs.get('shortDescription', {}))
        else:
            self.shortDescription = None
        if kwargs.get('shortTitle'):
            self.shortTitle = LocalizedString(**kwargs.get('shortTitle', {}))
        else:
            self.shortTitle = None
        if kwargs.get('title'):
            self.title = LocalizedString(**kwargs.get('title', {}))
        else:
            self.title = None
    def __eq__(self, other):
        if not isinstance(other, WatchOption):
            return False
        return (self.description == other.description and self.link == other.link and self.promoted == other.promoted and self.provider == other.provider and self.providerName == other.providerName and self.providerRefTagFragment == other.providerRefTagFragment and self.shortDescription == other.shortDescription and self.shortTitle == other.shortTitle and self.title == other.title)

class WatchProvider:
    def __init__(self, **kwargs):
        if kwargs.get('description'):
            self.description = LocalizedString(**kwargs.get('description', {}))
        else:
            self.description = None
        self.id = kwargs.get('id', "")
        self.isPopular = kwargs.get('isPopular', False)
        self.isSupported = kwargs.get('isSupported', False)
        if kwargs.get('logos'):
            self.logos = WatchProviderLogos(**kwargs.get('logos', {}))
        else:
            self.logos = None
        if kwargs.get('name'):
            self.name = LocalizedString(**kwargs.get('name', {}))
        else:
            self.name = None
        self.refTagFragment = kwargs.get('refTagFragment', "")
        self.watchOptionCategoryType = kwargs.get('watchOptionCategoryType', "")
    def __eq__(self, other):
        if not isinstance(other, WatchProvider):
            return False
        return self.id == other.id


class WatchProviderConnection(Edge):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edges = []
        for node in kwargs.get("edges", []):
            if not isinstance(node, dict):
                raise TypeError(f"Expected dict for node, got {type(node)}")
            self.edges.append(WatchProvider(**node.get("node", {})))

class WatchProviderLogos:
    def __init__(self, **kwargs):
        if kwargs.get('icon'):
            self.icon = MediaServiceImage(**kwargs.get('icon', {}))
        else:
            self.icon = None
        if kwargs.get('slate'):
            self.slate = MediaServiceImage(**kwargs.get('slate', {}))
        else:
            self.slate = None
    def __eq__(self, other):
        if not isinstance(other, WatchProviderLogos):
            return False
        return (self.icon == other.icon and self.slate == other.slate)

class WatchedStatus:
    def __init__(self, **kwargs):
        self.firstWatched = kwargs.get('firstWatched', "")
        self.isWatched = kwargs.get('isWatched', False)
        self.remainingWatchedSourceTypes = kwargs.get('remainingWatchedSourceTypes', "")
    def __eq__(self, other):
        if not isinstance(other, WatchedStatus):
            return False
        return (self.firstWatched == other.firstWatched and self.isWatched == other.isWatched and self.remainingWatchedSourceTypes == other.remainingWatchedSourceTypes)

class WatchlistStatistics:
    def __init__(self, **kwargs):
        if kwargs.get('displayableCount'):
            self.displayableCount = LocalizedDisplayableCount(**kwargs.get('displayableCount', {}))
        else:
            self.displayableCount = None
        self.totalCount = kwargs.get('totalCount', 0)
    def __eq__(self, other):
        if not isinstance(other, WatchlistStatistics):
            return False
        return (self.displayableCount == other.displayableCount and self.totalCount == other.totalCount)

class WebsiteLink:
    def __init__(self, **kwargs):
        self.label = kwargs.get('label', "")
        self.url = kwargs.get('url', "")
    def __eq__(self, other):
        if not isinstance(other, WebsiteLink):
            return False
        return (self.label == other.label and self.url == other.url)

class WebviewVideoPlayer:
    def __init__(self, **kwargs):
        self.audioLanguage = kwargs.get('audioLanguage', "")
        self.burnedInCaptionsLanguage = kwargs.get('burnedInCaptionsLanguage', "")
        if kwargs.get('description'):
            self.description = LocalizedString(**kwargs.get('description', {}))
        else:
            self.description = None
        self.webviewUrl = kwargs.get('webviewUrl', "")
    def __eq__(self, other):
        if not isinstance(other, WebviewVideoPlayer):
            return False
        return (self.audioLanguage == other.audioLanguage and self.burnedInCaptionsLanguage == other.burnedInCaptionsLanguage and self.description == other.description and self.webviewUrl == other.webviewUrl)

class WorkAuthorizationCountries:
    def __init__(self, **kwargs):
        self.total = kwargs.get('total', 0)
        if kwargs.get('workAuthorizations'):
            self.workAuthorizations = WorkAuthorizationInCountry(**kwargs.get('workAuthorizations', {}))
        else:
            self.workAuthorizations = None
    def __eq__(self, other):
        if not isinstance(other, WorkAuthorizationCountries):
            return False
        return (self.total == other.total and self.workAuthorizations == other.workAuthorizations)

class WorkAuthorizationInCountry:
    def __init__(self, **kwargs):
        if kwargs.get('country'):
            self.country = LocalizedDisplayableCountry(**kwargs.get('country', {}))
        else:
            self.country = None
        self.isAuthorized = kwargs.get('isAuthorized', False)
    def __eq__(self, other):
        if not isinstance(other, WorkAuthorizationInCountry):
            return False
        return (self.country == other.country and self.isAuthorized == other.isAuthorized)

class YearDisplayableProperty:
    def __init__(self, **kwargs):
        if kwargs.get('value'):
            self.value = Markdown(**kwargs.get('value', {}))
        else:
            self.value = None
    def __eq__(self, other):
        if not isinstance(other, YearDisplayableProperty):
            return False
        return (self.value == other.value)
    def __str__(self):
        return str(self.value) if self.value else ""
    def __repr__(self):
        return f"YearDisplayableProperty(value={self.value})"

class YearRange:
    def __init__(self, **kwargs):
        self.endYear = kwargs.get('endYear', 0)
        self.year = kwargs.get('year', 0)
    def __str__(self):
        if self.year and self.endYear:
            return f"{self.year}-{self.endYear}"
        elif self.year:
            return str(self.year)
        return ""
    def __repr__(self):
        return f"YearRange(year={self.year}, endYear={self.endYear})"
    def __eq__(self, other):
        if not isinstance(other, YearRange):
            return False
        return (self.endYear == other.endYear and self.year == other.year)
# fmt: on
