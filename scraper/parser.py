from bs4 import BeautifulSoup

from scraper.utils import clean_price


def parse_products(html: str) -> list[dict]:
    """Extract product data from a Books to Scrape page."""

    soup = BeautifulSoup(html, "html.parser")
    products = []

    for product in soup.select("article.product_pod"):
        title = product.select_one("h3 a")
        price = product.select_one(".price_color")
        availability = product.select_one(".availability")
        rating = product.select_one(".star-rating")

        products.append({
            "title": title["title"].strip() if title else None,
            "price": clean_price(price.get_text(strip=True))
            if price else None,
            "availability": availability.get_text(" ", strip=True)
            if availability else None,
            "rating": rating.get("class", [None, None])[-1]
            if rating else None,
        })

    return products


def parse_next_page(html: str) -> str | None:
    """Extract URL of the next page."""

    soup = BeautifulSoup(html, "html.parser")

    next_link = soup.select_one("li.next a")

    if not next_link:
        return None

    return next_link.get("href")