from scraper.scraper import build_url, scrape_all_pages


def test_build_url():
    result = build_url(
        "https://books.toscrape.com/",
        "catalogue/page-2.html",
    )

    assert result == "https://books.toscrape.com/catalogue/page-2.html"


def test_scrape_all_pages(monkeypatch):
    pages = {
        "https://books.toscrape.com/": """
            <article class="product_pod">
                <h3><a title="Book 1"></a></h3>
                <p class="price_color">£10.00</p>
                <p class="availability">In stock</p>
                <p class="star-rating One"></p>
            </article>

            <li class="next">
                <a href="catalogue/page-2.html">next</a>
            </li>
        """,

        "https://books.toscrape.com/catalogue/page-2.html": """
            <article class="product_pod">
                <h3><a title="Book 2"></a></h3>
                <p class="price_color">£20.00</p>
                <p class="availability">In stock</p>
                <p class="star-rating Five"></p>
            </article>
        """,
    }

    def fake_fetch_page(url):
        return pages[url]

    monkeypatch.setattr(
        "scraper.scraper.fetch_page",
        fake_fetch_page,
    )

    result = scrape_all_pages("https://books.toscrape.com/")

    assert len(result) == 2
    assert result[0]["title"] == "Book 1"
    assert result[1]["title"] == "Book 2"