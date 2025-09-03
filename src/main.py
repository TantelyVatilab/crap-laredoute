from scraper import scrape_category_links , scrape_vendor_info
from manager import load_csv_column_as_list

def main():
    category_links_future = scrape_category_links([
        "https://www.laredoute.fr/sitemap-brndid-001.xml",
        "https://www.laredoute.fr/sitemap-brndid-002.xml",
    ])
    category_links_future.get()
    all_urls = load_csv_column_as_list("url")
    vendor_info_future = scrape_vendor_info(all_urls)
    vendor_info_future.get()

if __name__ == "__main__":
    main()
