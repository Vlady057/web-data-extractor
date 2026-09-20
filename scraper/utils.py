import re


def clean_price(price: str) -> float:
    """Extract numeric price from string."""

    match = re.search(r"\d+(?:\.\d+)?", price)

    if not match:
        raise ValueError(f"Invalid price: {price}")

    return float(match.group())