from scraper.scraper import BASE_URL, scrape_all_pages
from scraper.exporter import save_to_csv


def main():
    products = scrape_all_pages(BASE_URL)

    save_to_csv(products, "data/books.csv")

    print(f"Found products: {len(products)}")
    print("Saved to data/books.csv")


if __name__ == "__main__":
    main()