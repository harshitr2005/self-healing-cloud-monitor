import requests
import json

try:
    response = requests.get("https://status.aws.amazon.com/data.json", timeout=10)
    data = response.json()
    with open("/var/www/html/status.json", "w") as f:
        json.dump(data, f)
except Exception as e:
    with open("/var/www/html/status.json", "w") as f:
        json.dump({"error": str(e)}, f)
