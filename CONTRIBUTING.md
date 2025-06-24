# Pull Requests
https://github.com/MiM-MiM/SimpleIMDbDevPy/pulls

Don't hesitate to make one, even if you make mistakes help is appreciated.

# Issues
https://github.com/MiM-MiM/SimpleIMDbDevPy/issues

If you think you've found a bug open an issue. Including if something is missing and/or not returned as you expected. This can also be used to request a feature, please use a discussion if the feature is still in an idea phase and issues if you have an example of what you'd like and why.

Always be sure you are on the latest version under the `master` branch. If you have an issue with an older `MAJOR` version, consider if updating is reasonable and solves the issue or if it is still present.

# Discussions
https://github.com/MiM-MiM/SimpleIMDbDevPy/discussions

Discussions can be used to discuss possible features before they made it to the stage of an official issue. You may also discuss here for how to integrate it into existing scripts.

# Guidelines
## Versioning
https://semver.org/
- Semantic versioning is used, `MAJOR`.`MINOR`.`PATCH`-`TAG`
- A `PATCH` can contain multiple or single bugfixes, depending on what all needs fixed.
  - If there are 9 or more patches, consider if a `MINOR` version increase to encompase all of the fixes.
- A `MINOR` version increase cannot break any backwards compatibility issues.
- A `MAJOR` version increase results in backwards compatibility issues or bigger features being added.
- A `TAG` is to be used when working on a version not fully ready to publish. Typically `alpha`, `beta`, or `rc`. A number can be appended to signify different versions of that tag.

#### `MAJOR` version release method.
All major versions need to have their own branch, the current stable version should remain the `master` branch. Feature branches to be merged should be under a name describing the feature. If a new major version is released and there isn't a branch for that version, create one.

#### Updates to versions of previous `MAJOR` versions
Updates to the non-latest version will be considered on the bug and reason. Security updates will always be a priority.

## Caching
All API calls should be cached for the same input. If you need to alter more values based on that API call, move the API call to a standalone method so it can be cached and the other code make that call. If the point of a method is only to be used as a middleman API call that is cached, consider prefixing the name with an underscore to indicate it is a private method to be used at the caller's own risk.

## Tests
Each method called needs at least one test that covers it. Directly is preferred, indirect will suffice until a standalone test is added.
All network calls must be spoofed, including any expected data being passed. Headers are optional to spoof, only needed if the API call otherwise requires it for validation, i.e. if there was a needed `API_KEY`. The `responses` package is being used to spoof these requests.

## Formatted with black
Black is a simple linting tool that keeps code a consistent design.

<center><a href="https://black.readthedocs.io/en/stable/"><img src="images/black.webp" alt="Black: Any color you like" title="Black" height="75"/></a></center>

Exceptions can be made to the max line width, use `# fmt: ign` for single lines or `# fmt: off/on` for longer sections. These sections should be ones where the potential data being longer than expected does not impact the understanding of the code.

Forgetting to run black and look if exceptions need made will not result in a denied pull request. You are however expected to run `black` every once in a while.

#### Line Endings
`LF` is the only ending to be used, configured by the `.gitattributes` file.

## Naming
Nothing too strict on naming, just make it reasonably consistent.
- If a non-local variable/method is to be considered private, prefix the name with an underscore, `_`.

## Typing
It is required to type everything within reason.
#### Methods
- All input and output must be typed.
- `None` is generally not to be used, consider the falsy form of the wanted type to avoid this.

#### General code
- Variables should remain a static type within reason.
  - An ID that goes from `int` to the prefixed `int` as a string is a valid exception.
- If a type is not able to be auto checked based on the call returning possible multiple, you may use `# type: ignore` if required and type is known still.
  - If the type is not guaranteed, you must do an `isinstance` check and convert as needed or raise the appropiate error.

#### Static variables/meaning
- If there is some static meanign to the design of objects, consider using static global variables to define them.
  - Example is found in the GraphQL schema, using `not REQUIRED` and `REQUIRED` provide the meaning to that boolean, allowing code to be understood without memorizing the structure of that tuple.
- Global variables should be in caps.

## GraphQL
Any generated `GraphQL` request must be generated dynamically, if it is impossible to dynamically generate consider other edits to allow for selection and generation of the desired request.

## Docstrings
Every method is required to have a docstring following the format below, or a similar one that works with IDEs.
```
Base description at the start.

Notes: Any notes that may be good to include.

Examples: Any examples that may help.

Args:
   arg_name (type): Description
   arg_name (type, optional): Description
   ...

Returns:
   type: Description

Raises:
   ValueError: When it is expected to raise one
   ...
```
