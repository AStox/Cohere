import os
import weaviate
from dotenv import load_dotenv

load_dotenv()

cohere_api_key = os.getenv("COHERE_APIKEY")

weaviate_api_key = os.getenv("WEAVIATE_API_KEY")
auth_config = weaviate.AuthApiKey(api_key=weaviate_api_key)
client = weaviate.Client(
    url="https://adcorp-vghi1hv6.weaviate.network",
    auth_client_secret=auth_config,
    additional_headers={"X-Cohere-Api-Key": cohere_api_key},
)

schema = {
    "classes": [
        {
            "class": "Sales",
            "description": "grocery items on sale",
            "vectorizer": "text2vec-cohere",
            "moduleConfig": {"text2vec-cohere": {}, "generative-cohere": {}},
            "properties": [
                {
                    "name": "title",
                    "description": "the name of the item",
                    "dataType": ["string"],
                },
                {
                    "name": "snippet",
                    "description": "A snippet about the sales item and its discount",
                    "dataType": ["string"],
                },
                {
                    "name": "discountedPrice",
                    "description": "The price of the item after the discount",
                    "dataType": ["number"],
                },
                {
                    "name": "regularPrice",
                    "description": "The price of the item before the discount",
                    "dataType": ["number"],
                },
                {
                    "name": "amountSaved",
                    "description": "The amount saved by buying the item on sale",
                    "dataType": ["number"],
                },
            ],
        },
    ],
}

# Update the schema in Weaviate
client.schema.create(schema)
print(client.schema.get())
