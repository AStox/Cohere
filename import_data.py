import os
import weaviate
from dotenv import load_dotenv
from documents import documents as sales_data

load_dotenv()

cohere_api_key = os.getenv("COHERE_APIKEY")

weaviate_api_key = os.getenv("WEAVIATE_API_KEY")
auth_config = weaviate.AuthApiKey(api_key=weaviate_api_key)
client = weaviate.Client(
    url="https://adcorp-vghi1hv6.weaviate.network",
    auth_client_secret=auth_config,
    additional_headers={"X-Cohere-Api-Key": cohere_api_key},
)

client.batch.configure(batch_size=100)  # Configure batch
with client.batch as batch:  # Initialize a batch process
    for i, d in enumerate(sales_data):  # Batch import data
        print(f"importing data: {i+1}")
        properties = {
            "title": d["title"],
            "snippet": d["snippet"],
            "discountedPrice": d["discountedPrice"],
            "regularPrice": d["regularPrice"],
            "amountSaved": d["amountSaved"],
        }
        batch.add_data_object(data_object=properties, class_name="Sales")
