import os

API_URL = os.environ.get("API_URL", "https://jsonplaceholder.typicode.com/posts")
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/Users/niloy/Desktop")
API_RETRY_COUNT = int(os.environ.get("API_RETRY_COUNT", 3))
API_TIME_OUT = int(os.environ.get("API_TIME_OUT", 5))
LOG_DIR = os.environ.get("LOG_DIR", "logs")