from typing import Optional, Type

from strategy.scraper import ScrapeStrategy
from .params import OtoDomParams
import requests
from bs4 import BeautifulSoup


class OtoDomScraper(ScrapeStrategy):
    BASE_URL: str = "https://www.otodom.pl/"

    @staticmethod
    def _get_url(params: Type[OtoDomParams] = None) -> str:
        raise NotImplementedError

    def scrape(self, params: Optional[OtoDomParams] = None, url: Optional[str] = None):
        current_page: int = 1

        if not url:
            url = self._get_url(params)
            print(f"Build url: {url}")
        print(f"Passed url: {url}")

        page_content = self.get_page_content(url)
        print(page_content)

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

        soup = BeautifulSoup(page_content)
        try:
            next_page_button = soup.find("a", {"data-cy": "pagination.next-page"})
            if next_page_button:
                return True

        except Exception as e:
            print(e)
            raise e

        return False