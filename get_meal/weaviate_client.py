import weaviate
import os


def query_weaviate(query_string, result_limit=20):
    # Initialize Cohere client
    cohere_api_key = os.getenv("COHERE_API_KEY")
    # co = cohere.Client(cohere_api_key, "latest")

    # Initialize Weaviate client
    weaviate_api_key = os.getenv("WEAVIATE_API_KEY")
    auth_config = weaviate.AuthApiKey(api_key=weaviate_api_key)
    client = weaviate.Client(
        url="https://adcorp-vghi1hv6.weaviate.network",
        auth_client_secret=auth_config,
        additional_headers={"X-Cohere-Api-Key": cohere_api_key},
    )

    # Query Weaviate with the embedding vector to find similar items
    query_result = (
        client.query.get("Sales", ["title", "discountedPrice", "amountSaved"])
        .with_near_text({"concepts": [query_string]})
        .with_limit(result_limit)
        .do()
    )

    # Return the query result
    processed_documents = []
    for item in query_result["data"]["Get"]["Sales"]:
        processed_documents.append(
            {
                "title": item.get("title", ""),
                # trim prices to 2 decimal places
                "snippet": f"{item['title']} (price: ${item['discountedPrice']}, Savings: ${round(item['amountSaved'],2)})",
            }
        )
    # print the processed documents in a readable format
    return processed_documents
    # return json.dumps(query_result, indent=2)
