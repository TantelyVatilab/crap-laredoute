import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.CATEGORY_LINKS_FILE = os.getenv("CATEGORY_LINKS_FILE", "clean_url.csv")
        self.VENDOR_DATA_OUTPUT_FILE = os.getenv("VENDOR_DATA_OUTPUT_FILE", "final_data.csv")

        self.ACTIVE_FILE_INDEX = int(os.getenv("ACTIVE_FILE_INDEX", 0))
        
        sitemap_urls_str = os.getenv("CATEGORY_SITEMAP_URLS", "")
        self.CATEGORY_SITEMAP_URLS = [url.strip() for url in sitemap_urls_str.split(',') if url.strip()]
        
        self.LIVRABLE_FILE = os.getenv("LIVRABLE_FILE", "livrable.csv")

        files_to_merge_str = os.getenv("FILES_TO_MERGE", "")
        self.FILES_TO_MERGE = [f.strip() for f in files_to_merge_str.split(',') if f.strip()]


settings = Config()