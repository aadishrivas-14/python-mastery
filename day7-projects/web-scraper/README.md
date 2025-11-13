# Project 2: Web Scraper

Build a web scraper to extract data from websites.

## Features
- Scrape product listings
- Extract titles, prices, ratings
- Handle pagination
- Export to CSV/JSON
- Rate limiting

## Usage
```bash
python scraper.py --url "https://example.com/products" --output products.csv
```

## Implementation
- BeautifulSoup for parsing
- requests for HTTP
- CSV/JSON export
- Error handling
- Respect robots.txt

## Run
```bash
pip install -r requirements.txt
python src/scraper.py --help
pytest tests/ -v
```
