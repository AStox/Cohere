import cohere
from documents import documents
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("PROD_API_KEY")

co = cohere.Client(api_key)


response = co.chat(
    chat_history=[
        {
            "role": "USER",
            "message": "You have been given a list of their groceries and their pricing information. All these items are on sale. You generate recipes, using this information to generate recipes that maximize the amount of money saved.",
        },
    ],
    message="Generate a recipe and tell me the cost of each ingredient if known",
    documents=documents,
    temperature=0.9,
)

print(response.text)
