import requests
import time
from config.settings import API_URL, API_TIME_OUT, API_RETRY_COUNT
from utils.logger import logger

def fetch_posts() -> list:
    for attempt in range(API_RETRY_COUNT):
        try:
            response = requests.get(API_URL, timeout=API_TIME_OUT)
            response.raise_for_status()
            posts_data = response.json()

            if isinstance(posts_data, list):
                logger.info(f"API - {API_URL} returned {len(posts_data)} records successfully (Attempt {attempt+1})")
                if not posts_data:
                    logger.warning("API returned an empty list")
                return posts_data
            else:
                logger.warning("API returned non-list data")
                return []

        except requests.exceptions.RequestException as e:
            logger.warning(f"API call failed on attempt {attempt+1}: {e}")
            if attempt < API_RETRY_COUNT - 1:
                logger.info(f"Retrying API call (Attempt {attempt + 2}/{API_RETRY_COUNT})")
                time.sleep(2)

    logger.error(f"API failed after {API_RETRY_COUNT} attempts")
    return []
