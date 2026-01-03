from datetime import datetime
from config.settings import API_URL
from api.client import fetch_posts
from service.excel_service import write_posts_to_excel
from utils.logger import logger

def main():
    logger.info(f"Batch job started on : {datetime.now()}")
    posts = fetch_posts()
    write_posts_to_excel(posts)
    logger.info(f"Batch job ended on : {datetime.now()}")

if __name__ == "__main__":
    main()
