import requests
import pprint

url = "https://api.graphql.imdb.com/"
type_name = "Attribute"  # Change this to the desired type name
query = {
    "query": f"""
    {{
        __type(name: "{type_name}") {{
            name
            description
            kind
            fields {{
                name
                description
                type {{
                    name
                    kind
                    ofType {{
                        name
                        kind
                        ofType {{
                            name
                            kind
                            ofType {{
                                name
                                kind
                            }}
                        }}
                    }}
                }}
                args {{
                    name
                    description
                    type {{
                        name
                        kind
                        ofType {{
                            name
                            kind
                        }}
                    }}
                    defaultValue
                }}
            }}
        }}
    }}
    """
}

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

response = requests.post(
    url,
    json=query,
    headers=headers,
    timeout=30
)
pprint.pprint(response.json())