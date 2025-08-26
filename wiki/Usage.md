# Usage
`getByID` and `search` both return a `MyMovie` type. This type can be treated as a dict in most cases. If an item is expected to be a list, i.e. `genres` you can use simple `for itm in lst` format or normal numerical indexing. Every attribute in the `MyMovie` object is either a native type, including `None`, or a `MyMovie` object. Object addition is supported for the same type, however, this is more intended to be used for updates, not normal adition. It works similar to dict addition, `|`. The first object will override the attributes with the second, appending if it is the case of `nodes`. When updating an object you should update minimal at a time, you may run into a `query too complex` error otherwise. If the item you tried to update has no more to fetch, i.e. you are getting all the `AKAs`, it will return `None` when there are no more, indicated by the `hasNextPage` attribute.

## Search examples
TODO, see the functions and the arguments allowed.
Results can be used the same way as the `MyMovie` objects returned by `getByID`.

## getByID examples
```python
from MyMovieGraphQL import GetByID

SuperHeroMovies = GetByID.getByID("in0000008") # Interest
WaltDisney = GetByID.getByID("co0098836") # Company
RandomMovieRoulette = GetByID.getByID("ls091294718") # List
NicolasCage = GetByID.getByID("nm0000115") # Name
TheShawshankRedemption = GetByID.getByID("tt0111161") # Title
TheShawshankRedemptionImage = GetByID.getByID("rm1690056449") # Image
HarryPotter_Wednesday_Similarities = GetByID.getByID("mzERoASQys8") # Poll
theporklion = GetByID.getByID("ur133306497") # User

# You can update multiple at the same time,
# just be sure the resulting query is not too complex.
update = TheShawshankRedemption.update(["akas", "alexaTopQuestions"])
# `update` contains only the updated data,
# the original object was updated
# If it is the item that is a "Connection" (list)
# you can loop/index as if it was a normal list.
for i in range(len(TheShawshankRedemption["alexaTopQuestions"])):
    question = TheShawshankRedemption["alexaTopQuestions"][i]["question"]
    answer = TheShawshankRedemption["alexaTopQuestions"][i]["answer"]
    #print(f"Q: {question}\nA: {answer}")
for aka in TheShawshankRedemption["akas"]:
    print(f"{aka['country']}: {aka}")
# You can even do it manually.
aka = TheShawshankRedemption.get("akas").get("edges")[0].get("node")
print(f"Or manually - {aka['country']}: {aka['text']}")
# If you want to get all the release dates you can do a while loop.
while TheShawshankRedemption.update("releaseDates") is not None:
    pass
releaseDates = TheShawshankRedemption["releaseDates"]
print(f"{TheShawshankRedemption} has {len(releaseDates)} releases")

while TheShawshankRedemption.update("credits") is not None:
    pass
credits = TheShawshankRedemption['credits']
for credit in credits:
    print(f"{credit.ofType} - {credit['name']}: {credit['category']} - {credit.get('attributes', '')}")

```