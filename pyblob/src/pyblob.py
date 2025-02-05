import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from flask import Flask
import json

app = Flask(__name__)

## Get config from the corresponding environment variables
account_name = os.getenv("BLOB_ACC_NAME")
if not account_name:
    raise ValueError("BLOB_ACC_NAME environment variable not set")
container_name = os.getenv("BLOB_CONTAINER_NAME")
if not container_name:
    raise ValueError("BLOB_CONTAINER_NAME environment variable not set")

@app.route("/")
def home():
    try:
        account_url = "https://" + account_name + ".blob.core.windows.net"
        default_credential = DefaultAzureCredential()

        # Create the BlobServiceClient object
        blob_service_client = BlobServiceClient(account_url, credential=default_credential)

        container_client = blob_service_client.get_container_client(container_name)

        # List the blobs in the container
        blob_list = container_client.list_blobs()

        blob_answer = "<html><body><h2>Container blobs:</h2><ul>"
        for blob in blob_list:
            blob_answer += f"<li>{blob.name}</li>"
        blob_answer += "</ul></body></html>"

        return blob_answer

    except Exception as ex:
        print("Exception:")
        print(ex)
        print("Credentials:")
        print(json.dumps(vars(default_credential), default=str, indent=2))
        return f"<html><body><h2>Exception:</h2><pre>{str(ex)}</pre></body></html>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)