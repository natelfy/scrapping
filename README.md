# Scraping Script Express

Scraping Script Express is a simple utility that helps you scrape a website and generate CSV output in one click. It provides a minimal reference for turning a URL and an HTML tag or CSS selector into a CSV file containing the extracted text. The intent of this repository is to provide a small reference implementation with a minimal CI setup.

## Warning

Web scraping is subject to legal and ethical restrictions. **Always** review and
comply with the terms of service of the websites you target. Ensure you have
permission to scrape and that your use complies with applicable laws.

## Features

- Fetch pages using `requests`
- Parse HTML with `BeautifulSoup`
- Save results to a CSV file

## Requirements

- Python 3.8+

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python scrape.py https://example.com output.csv --selector p
```

Run `python scrape.py` without arguments to be prompted for the URL and output
path. Use `--selector` to choose which elements are scraped. The default is
paragraph tags (`<p>`).

## Development

This repository includes a GitHub Actions workflow that runs unit tests with
`pytest` on every push. Add your tests in the `tests/` directory.

## License

This project is provided under the MIT License. See [LICENSE](LICENSE).