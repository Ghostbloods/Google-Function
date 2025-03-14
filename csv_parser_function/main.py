import functions_framework
import csv
import json
from google.cloud import storage, firestore

# Initialize Cloud Storage and Firestore clients
storage_client = storage.Client()
firestore_client = firestore.Client()

@functions_framework.cloud_event
def parse_csv(cloud_event):
    """
    Cloud function that triggers when a CSV file is uploaded to a Cloud Storage bucket.
    Reads the CSV file, parses it, and stores the data in Firestore.
    """

    try:
        # Extract event data
        event_data = cloud_event.data
        bucket_name = event_data["bucket"]
        file_name = event_data["name"]

        # Only process if it is a CSV file
        if not file_name.endswith(".csv"):
            print(f"File {file_name} is not a CSV file. Skipping processing.")
            return "Not a CSV file"

        print(f"Processing file {file_name} from bucket {bucket_name}")

        # Get the file from the Cloud Storage bucket
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_name)

        # Open the file as a stream
        with blob.open("r") as file:
            reader = csv.reader(file)
            headers = next(reader, None)  # Get column headers

            if not headers:
                print(f"File {file_name} is empty. Skipping processing.")
                return "Empty CSV file"

            collection_name = "csv_data"  # Firestore collection name
            batch = firestore_client.batch()
            batch_size = 0
            max_batch_size = 500  # Firestore batch limit

            for row in reader:
                data_dict = dict(zip(headers, row))

                # Ensure the row isn't empty
                if not any(data_dict.values()):
                    continue

                doc_ref = firestore_client.collection(collection_name).document()
                batch.set(doc_ref, data_dict)
                batch_size += 1

                # Commit batch when limit is reached
                if batch_size >= max_batch_size:
                    batch.commit()
                    print(f"Committed {batch_size} records to Firestore.")
                    batch = firestore_client.batch()  # Start a new batch
                    batch_size = 0

            # Commit any remaining records
            if batch_size > 0:
                batch.commit()
                print(f"Committed {batch_size} remaining records to Firestore.")

            print(f"Successfully stored data from {file_name} in Firestore.")
            return "Success"

    except Exception as e:
        print(f"Error processing file {file_name}: {str(e)}")
        return f"Error: {str(e)}"
