# Flask Blob Storage Application

This project is a Flask web server that connects to Azure Blob Storage. It provides a simple interface to list blobs in a specified container.

## Project Structure

```
pyblob
├── src
│   └── pyblob.py        # Flask application code
├── Dockerfile            # Dockerfile for containerization
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Requirements

To run this application, you need to have the following dependencies:

- Flask
- Azure SDK for Python

These dependencies are listed in the `requirements.txt` file.

## Setup

1. Clone the repository:

   ```
   git clone <repository-url>
   cd pyblob
   ```

2. Build the Docker image:

   ```
   docker build -t pyblob .
   ```

3. Run the Docker container:

   ```
   docker run -p 8000:8000 -e BLOB_ACC_NAME=<your Azure BLOB account name> -e BLOB_CONTAINER_NAME=<the container inside the BLOB storage> pyblob
   ```

4. Access the application:

   Open your web browser and go to `http://localhost:8000` to see the list of blobs in the specified Azure Blob Storage container.

## License

This project is licensed under the MIT License.