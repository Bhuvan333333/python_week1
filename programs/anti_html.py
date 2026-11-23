import argparse
import logging

import requests
from bs4 import BeautifulSoup


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def strip_html(url):
    try:
        response = requests.get(url,timeout=10,headers={"User-Agent": "PythonHTMLTextExtractor/1.0"})

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        for element in soup(["script", "style", "noscript", "template"]):
            element.decompose()

        return soup.get_text(separator=" ", strip=True)

    except requests.RequestException:
        logger.exception("Unable to download webpage")
        raise


def main():
    parser = argparse.ArgumentParser(
        description="Download HTML and print plain text."
    )

    parser.add_argument("url",help="URL of the webpage")

    args = parser.parse_args()

    try:
        text = strip_html(args.url)
        print(text)

    except requests.RequestException:
        logger.error("HTML extraction failed")


if __name__ == "__main__":
    main()