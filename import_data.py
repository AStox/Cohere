def import_data(client, sales_data):
    client.batch.configure(batch_size=100)  # Configure batch
    with client.batch as batch:  # Initialize a batch process
        for i, d in enumerate(sales_data):  # Batch import data
            print(f"importing data: {i+1}")
            properties = {
                "title": d["title"],
                "snippet": d["snippet"],
            }
            batch.add_data_object(data_object=properties, class_name="Sales")
