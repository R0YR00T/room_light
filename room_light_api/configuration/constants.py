import os

auth_token = os.environ.get("NANOLEAF_TOKEN")
ip_address = os.environ.get("NANOLOEAF_IP")
port_number = os.environ.get("NANOLOEAF_PORT")

BASE_URL = f"http://{ip_address}:{port_number}/api/v1/{auth_token}"
