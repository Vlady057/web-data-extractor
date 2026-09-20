from urllib.parse import urljoin

import requests

from scraper.parser import parse_products, parse_next_page


BASE_URL = "https://books.toscrape.com/"


def fetch_page(url: str) -> str:
    """Download HTML page."""

    response = requests.get(
        url,
        timeout=10,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
    )

    response.raise_for_status()

    response.encoding = response.apparent_encoding

    return response.text


def build_url(base_url: str, path: str) -> str:
    """Build an absolute URL from base URL and relative path."""

    return urljoin(base_url, path)


def scrape_all_pages(start_url: str) -> list[dict]:
    """Scrape products from all pages."""

    all_products = []
    current_url = start_url

    while current_url:
        html = fetch_page(current_url)
        products = parse_products(html)

        all_products.extend(products)

        next_page = parse_next_page(html)

        if next_page:
            current_url = build_url(current_url, next_page)
        else:
            current_url = None

    return all_products

