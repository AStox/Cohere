import cohere
import weaviate
from documents import documents as sales_data
from import_data import import_data
from dotenv import load_dotenv
import json
import os

load_dotenv()

# Initialize Cohere client
cohere_api_key = os.getenv("COHERE_APIKEY")
co = cohere.Client(cohere_api_key)

# Initialize Weaviate client
weaviate_api_key = os.getenv("WEAVIATE_API_KEY")
auth_config = weaviate.AuthApiKey(api_key=weaviate_api_key)
client = weaviate.Client(
    url="https://adcorp-vghi1hv6.weaviate.network",
    auth_client_secret=auth_config,
    additional_headers={"X-Cohere-Api-Key": cohere_api_key},
)

# import_data(client, sales_data)

# Query Weaviate with the embedding vector to find similar items
query_result = (
    client.query.get("Sales", ["title", "snippet"])
    .with_limit(5)
    # .with_near_text({"concepts": ["red sauce spaghetti"]})
    .with_generate(
        grouped_task="generate a recipe that uses ingredients from the sales items. Only list the name of the recipe, the ingredients, and the cost of each ingredient if known. Also calculate the discount on each item if known and show the full sum of money saved at the end",
    )
    .do()
)

# filter results to just show the title, and print them on a new line
print(json.dumps(query_result, indent=4))

print(
    query_result["data"]["Get"]["Sales"][0]["_additional"]["generate"]["groupedResult"]
)
