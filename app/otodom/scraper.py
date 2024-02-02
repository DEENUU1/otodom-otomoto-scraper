from typing import Optional, Type, List

import requests
from bs4 import BeautifulSoup

from strategy.scraper import ScrapeStrategy
from .params import OtoDomParams


class OtoDomScraper(ScrapeStrategy):
    BASE_URL: str = "https://www.otodom.pl/"

    def scrape(self, url: Optional[str] = None) -> List[Optional[str]]:
        result = []

        current_page: int = 1

        while True:
            page_content = self.get_page_content(url)
            result.append(page_content)

            next_page = self.is_next_page(page_content)

            if not next_page:
                break

            current_page += 1
            url += f"?page={current_page}"
            print(f"Next page: {url}")

        return result

    @staticmethod
    def get_page_content(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text

        except Exception as e:
            print(e)
            raise e

    @staticmethod
    def is_next_page(page_content: Optional[str]) -> bool:
        if not page_content:
            return False

        soup = BeautifulSoup(page_content, "html.parser")
        try:
            next_page_button = soup.find("button", {"data-cy": "pagination.next-page"})
            if next_page_button:
                return True

        except Exception as e:
            print(e)
            raise e

        return False
