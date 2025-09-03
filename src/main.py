from scraper import scrape_category_links , scrape_vendor_info
from manager import load_csv_column_as_list, split_csv_into_three_files

def main():
    CLEAN_URL = "clean_url.csv"
    ACTIVE_FILE_INDEX = 0
    CATEGORY_SITEMAP_URLS = [
        "https://www.laredoute.fr/sitemap-brndid-001.xml",
        "https://www.laredoute.fr/sitemap-brndid-002.xml",
    ]
    category_links_future = scrape_category_links(CATEGORY_SITEMAP_URLS)
    category_links_future.get()

    split_files = split_csv_into_three_files(csv_file=CLEAN_URL)

    if split_files:
        active_file = split_files[ACTIVE_FILE_INDEX]
        all_urls = load_csv_column_as_list("url", csv_file=active_file)
        vendor_info_future = scrape_vendor_info(all_urls)
        vendor_info_future.get()


if __name__ == "__main__":
    main()
