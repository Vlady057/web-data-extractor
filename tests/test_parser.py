from scraper.parser import parse_next_page, parse_products



def test_parse_products():
    html = """
    <article class="product_pod">
        <h3>
            <a href="book.html" title="Test Book">Test Book</a>
        </h3>

        <p class="price_color">£19.99</p>

        <p class="availability">
            In stock
        </p>

        <p class="star-rating Three">
        </p>
    </article>
    """

    products = parse_products(html)

    assert len(products) == 1
    assert products[0]["title"] == "Test Book"
    assert products[0]["price"] == 19.99
    assert products[0]["availability"] == "In stock"
    assert products[0]["rating"] == "Three"


def test_parse_next_page():
    html = """
    <ul class="pager">
        <li class="next">
            <a href="page-2.html">next</a>
        </li>
    </ul>
    """

    result = parse_next_page(html)

    assert result == "page-2.html"


def test_parse_next_page_when_missing():
    html = """
    <ul class="pager">
    </ul>
    """

    result = parse_next_page(html)

    assert result is None


