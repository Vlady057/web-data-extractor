
# Web Data Extractor

A Python web scraping project that extracts book data from [Books to Scrape](https://books.toscrape.com/) and saves the results to CSV.

## Features

* HTTP requests with `Requests`
* HTML parsing with `BeautifulSoup`
* Price extraction and cleaning with `Regex`
* Automatic pagination
* CSV export
* Unit tests with `pytest`
* Mocked HTTP requests in scraper tests
* Modular project structure

## Extracted Data

The scraper extracts:

* Book title
* Price
* Availability
* Rating

Example output is available in `data/books.csv`.

## Project Structure

```text
web-data-extractor/
├── data/
│   └── books.csv
├── scraper/
│   ├── __init__.py
│   ├── exporter.py
│   ├── parser.py
│   ├── scraper.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_exporter.py
│   ├── test_parser.py
│   ├── test_scraper.py
│   └── test_utils.py
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Vlady057/web-data-extractor.git
cd web-data-extractor
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the scraper:

```bash
python main.py
```

The scraper processes all available pages and saves the extracted data to:

```text
data/books.csv
```

## Testing

Run all tests with:

```bash
pytest
```

Current test suite:

```text
9 passed
```

## Technologies

* Python 3
* Requests
* BeautifulSoup4
* Regex
* CSV
* pytest
* Git / GitHub
