from openpyxl import Workbook
from datetime import datetime
import os
from config.settings import OUTPUT_DIR
from utils.logger import logger

def write_posts_to_excel(posts: list):
    if not posts:
        print("No data to write")
        return
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Posts"

    headers = ["User Id", "Post Id", "Title", "Body"]
    ws.append(headers)

    for post in posts:
        ws.append([post.get("userId"), post.get("id"), post.get("title"), post.get("body")])

    filename = f"posts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    filepath = os.path.join(OUTPUT_DIR, filename)

    wb.save(filepath)
    logger.info(f"Excel file saved: {filepath}")

