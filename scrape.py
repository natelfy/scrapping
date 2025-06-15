import argparse
import csv
import requests
from bs4 import BeautifulSoup


def fetch_html(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def extract_elements(html: str, selector: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    return [el.get_text(strip=True) for el in soup.select(selector)]


def save_to_csv(rows: list[str], path: str) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow([row])


def main() -> None:
    parser = argparse.ArgumentParser(description="Scrape HTML elements to CSV")
    parser.add_argument("url", nargs="?", help="Target URL")
    parser.add_argument("output", nargs="?", help="Output CSV path")
    parser.add_argument(
        "--selector",
        default="p",
        help="CSS selector for elements to scrape (default: p)",
    )
    args = parser.parse_args()

    url = args.url or input("URL: ")
    output = args.output or input("Output CSV file path: ")

    html = fetch_html(url)
    elements = extract_elements(html, args.selector)
    save_to_csv(elements, output)


if __name__ == "__main__":
    main()
