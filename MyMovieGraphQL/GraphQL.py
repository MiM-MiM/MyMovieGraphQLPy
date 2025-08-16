from MyMovieGraphQL import attributes
from MyMovieGraphQL import arguments


def query_builder(
    data: dict[str, type | str],
    keys: list[str] = [],
    allowPrivate: bool = False,
    keyArgs: dict[str, dict] = {},
    manual: bool = False,
) -> str:
    # keyArgs are used for the args to the selection. The key s which key to pass those args to, attributes.as a dict for the values
    if not isinstance(data, dict):
        raise TypeError(f"The requested data must be a dict, `{type(data)} given.")
    if not isinstance(keys, list):
        raise TypeError(
            f"The requested key selection must be a list of strings, `{type(keys)} given."
        )
    if any([not isinstance(s, str) for s in keys]):
        raise TypeError(
            f"The requested key selection must be a list of strings, one or more is not a string."
        )
    if not isinstance(allowPrivate, bool):
        raise TypeError(
            f"`allowPrivate` must be a boolean value, {type(allowPrivate)} given"
        )
    if not isinstance(keyArgs, dict):
        raise TypeError(f"`keyArgs` must be a boolean value, {type(keyArgs)} given")
    if not keys:
        keys = [str(k) for k in data.keys()]
    sub_attributes: dict[str, str | type] = {}
    query = ""
    all_edges = True
    for k in keys:
        if isinstance(data.get(k), str):
            if not data.get(k, "").endswith("Connection"):  # type: ignore
                all_edges = False
    for k in keys:
        if isinstance(data.get(k), str):
            if data.get(k, "").endswith(".manual"):  # type: ignore
                data[k] = data.get(k, "").removesuffix(".manual")  # type: ignore
                if not manual:
                    continue
        k = k.removeprefix("*").removeprefix("_")
        k_as_on = f"*{k}"
        k_as_private = f"_{k}"
        if k not in data and k_as_on not in data and k_as_private not in data:
            print(data)
            raise ValueError(f"Key `{k}` is not found in the requested data supplied.")
        if k_as_on in data:
            query = f"{query} ... on"
            k = k_as_on
        elif k_as_private in data:
            k = k_as_private
            if not allowPrivate:
                continue
        if isinstance(data[k], str):
            sub_attribute_name = str(data[k])
            k = k.removeprefix("*").removeprefix("_")
            is_edge = sub_attribute_name.endswith("Connection")
            sub_attribute_name = sub_attribute_name.removesuffix("Connection")
            sub_attributes = getattr(attributes, sub_attribute_name)
            if not isinstance(sub_attributes, dict):
                raise TypeError(f"The attribute selected is not a dict, {k}")
            args = ""
            if k not in keyArgs:
                args = "first: 1"
            else:
                queyrArgs = keyArgs.get(k, {})
                args = ", ".join(
                    [f"{argKey}: {queyrArgs[argKey]}" for argKey in queyrArgs.keys()]
                )
            if is_edge:
                sub_query = query_builder(
                    sub_attributes,
                    keys=list(sub_attributes.keys()),
                    allowPrivate=allowPrivate,
                    keyArgs=keyArgs,
                )
                # Connections should get the pagnation.
                pageInfo_data = attributes.PageInfo
                pageInfo_data_keys = list(pageInfo_data.keys())
                pageInfo_sub_query = query_builder(
                    data=pageInfo_data,
                    keys=pageInfo_data_keys,
                    allowPrivate=False,
                )
                # TODO: Find out which fail with `total` added and put it for all except those.
                query = f"{query} {k}({args}) {{ total pageInfo {{ {pageInfo_sub_query} }} edges {{ node {{ {sub_query} }} }} }}"
            else:
                sub_query = query_builder(
                    sub_attributes,
                    keys=list(sub_attributes.keys()),
                    allowPrivate=allowPrivate,
                    keyArgs=keyArgs,
                )
                queyrArgs = keyArgs.get(k, {})
                args = ", ".join(
                    [f"{argKey}: {queyrArgs[argKey]}" for argKey in queyrArgs.keys()]
                )
                if args:
                    query = f"{query} {k}({args}) {{ {sub_query} }}"
                else:
                    query = f"{query} {k} {{ {sub_query} }}"
        else:
            query = f"{query} {k}"
    return query
