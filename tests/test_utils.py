import pytest

from scraper.utils import clean_price


def test_clean_price():
    result = clean_price("£51.77")

    assert result == 51.77


def test_clean_price_without_currency():
    result = clean_price("51.77")

    assert result == 51.77


def test_clean_price_invalid():
    with pytest.raises(ValueError):
        clean_price("abc")