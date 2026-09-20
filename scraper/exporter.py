import csv
from pathlib import Path


def save_to_csv(products: list[dict], filename: str):
    """Save products to a CSV file."""

    output_path = Path(filename)

    with output_path.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "title",
                "price",
                "availability",
                "rating",
            ],
        )

        writer.writeheader()
        writer.writerows(products)