from scraper import scrape_category_links , scrape_vendor_info
from manager import load_csv_column_as_list, split_csv_into_three_files
from config import settings

def main():
    CATEGORY_LINKS_FILE = settings.CATEGORY_LINKS_FILE
    ACTIVE_FILE_INDEX = settings.ACTIVE_FILE_INDEX
    CATEGORY_SITEMAP_URLS = settings.CATEGORY_SITEMAP_URLS
    category_links_future = scrape_category_links(CATEGORY_SITEMAP_URLS)
    category_links_future.get()

    split_files = split_csv_into_three_files(csv_file=CATEGORY_LINKS_FILE)

    if split_files:
        active_file = split_files[ACTIVE_FILE_INDEX]
        all_urls = load_csv_column_as_list("url", csv_file=active_file)
        vendor_info_future = scrape_vendor_info(all_urls)
        vendor_info_future.get()


if __name__ == "__main__":
    main()
