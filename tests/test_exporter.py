from scraper.exporter import save_to_csv


def test_save_to_csv(tmp_path):
    products = [
        {
            "title": "Test Book",
            "price": 19.99,
            "availability": "In stock",
            "rating": "Five",
        }
    ]

    output_file = tmp_path / "books.csv"

    save_to_csv(products, output_file)

    content = output_file.read_text(encoding="utf-8-sig")

    assert "title,price,availability,rating" in content
    assert "Test Book,19.99,In stock,Five" in content