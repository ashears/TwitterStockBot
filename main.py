import os
from google.cloud import secretmanager

client = secretmanager.SecretManagerServiceClient()
secret_name = "my-secret"
project_id = os.environ["GCP_PROJECT"]
resource_name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
response = client.access_secret_version(resource_name)
secret_string = response.payload.data.decode('UTF-8')

def secret_hello(request):
    return secret_string
