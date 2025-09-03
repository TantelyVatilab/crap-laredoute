from botasaurus.browser import browser, Driver
from botasaurus.soupify import soupify
from utils import simplify_sitemap, extract_info_from_paragraphs
from manager import save_category_links_to_csv, save_vendor_data_to_csv

import xmltodict

@browser(
    reuse_driver=True,
    cache=True,
    run_async=True,
    create_error_logs=False,
    output=None,
    # headless=True,
)
def scrape_category_links(driver: Driver, url: str) -> list[str]:
    print(f"[SCRAPE_CATEGORY_LINKS] Start: {url}")
    
    if driver.config.is_new:
        driver.google_get(url, bypass_cloudflare=True, accept_google_cookies=True)

    driver.sleep(1.3)
    response = driver.requests.get(url)
    response.raise_for_status()

    xml_content = response.text
    xml_parsed = xmltodict.parse(xml_content)

    category_links = simplify_sitemap(xml_parsed)

    save_category_links_to_csv(category_links)
    print(f"[SCRAPE_CATEGORY_LINKS] Done: {url}")
    driver.sleep(1.3)
    return category_links


@browser(
    reuse_driver=True,
    run_async=True,
    create_error_logs=False,
    cache=True,
    output=None,
    # headless=True
)
def scrape_vendor_info(driver: Driver, url: str) -> dict[str, str]:
    print(f"[SCRAPE_VENDOR_INFO] Start: {url}")
    driver.google_get(url, bypass_cloudflare=True, accept_google_cookies=True)
    driver.sleep(1)

    cookie_popup = driver.select("button.pluginPopin")
    if cookie_popup:
        cookie_popup.click()

    consent_button = driver.select("button#didomi-notice-agree-button")
    if consent_button:
        consent_button.click()

    product_list = driver.select("div#productList")
    if product_list:
        first_product_link = product_list.select("a.unified-product-link")
        if first_product_link:
            first_product_link.click()

        vendor_link = driver.select(".hasLink")
        if vendor_link:
            vendor_id = driver.select("#vendorId").get_attribute("value")
            if vendor_id:
                if vendor_id == '0': 
                    return {}
                vendor_url = f"https://www.laredoute.fr/prtngp/vendor-{vendor_id}.aspx"
                driver.sleep(1)
                response = driver.requests.get(vendor_url)
                response.raise_for_status()
                html = response.text
                soup = soupify(html)
                paragraphs = soup.find_all(
                    "p", class_="vendorHeader_informations_popin_dropdown_list"
                )
                vendor_data = extract_info_from_paragraphs(paragraphs)
                save_vendor_data_to_csv(vendor_data)
                print(f"[SCRAPE_VENDOR_INFO] Data found for {url}")
                return vendor_data

    print(f"[SCRAPE_VENDOR_INFO] No data for {url}")
    driver.sleep(1)
    return {}
