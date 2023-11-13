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
            ],
        },
    ],
}

# Update the schema in Weaviate
# client.schema.create(schema)
# client.schema.delete_all()
# print(client.schema.get())
