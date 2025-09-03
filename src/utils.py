from bs4 import Tag
from model import Vendor
import html

def simplify_sitemap(data_dict: dict) -> list[str]:
    simplified_urls: list[str] = []
    urls = data_dict.get("urlset", {}).get("url", [])

    if not isinstance(urls, list):
        urls = [urls]

    for url in urls:
        loc = url.get("loc")
        if loc:
            simplified_urls.append(loc)

    return simplified_urls

def extract_info_from_paragraphs(paragraphs: list[Tag]) -> dict[str, str]:
    def clean_text(value) -> str:
        if not value:
            return ""
        if hasattr(value, "get_text"):
            value = value.get_text(strip=True)
        return html.unescape(str(value).strip())

    vendor_data: dict[str, str] = {}

    for p in paragraphs:
        strong_tag = p.find("strong")
        if strong_tag:
            key = strong_tag.get_text(strip=True).rstrip(":")
            value = clean_text(strong_tag.next_sibling or strong_tag.find_next(text=True))
            vendor_data[key] = value
        else:
            text = clean_text(p)
            if text:
                vendor_data[f"info_{len(vendor_data)+1}"] = text

    vendor_obj = create_vendor_from_dict(vendor_data).to_dict()
    return vendor_obj


def create_vendor_from_dict(data: dict) -> Vendor:
    return Vendor(
        vendor_name=data.get("Nom du vendeur ", ""),
        legal_name=data.get("Raison sociale ", ""),
        headquarters_address=data.get("Siège social ", ""),
        address=data.get("Adresse ", ""),
        rcs_number=data.get("Numéro de RCS ", ""),
        vat_number=data.get("N° de TVA intracommunautaire ", ""),
        social_capital=data.get("Capital social ", ""),
        eu_contact_name=data.get("Nom du responsable dans l'UE ", ""),
        eu_contact_address=data.get("Adresse postale du responsable dans l'UE ", ""),
        eu_contact_country=data.get("Pays du responsable dans l'UE ", ""),
        eu_contact_email=data.get("Adresse mail du responsable dans l'UE ", "")
    )
