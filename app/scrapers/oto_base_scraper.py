from typing import Optional, List, Any

import requests
from bs4 import BeautifulSoup

from .scraper import ScrapeStrategy


class OtoBaseScraper(ScrapeStrategy):
    def scrape(self, url: Optional[str] = None, page_limit: Optional[int] = None) -> List[Optional[str]]:
        result = []
        current_page: int = 1
        temp_url = url

        while True:
            page_content = self.get_page_content(temp_url)
            result.append(page_content)
            next_page = self.is_next_page(page_content)

            if not next_page or (page_limit is not None and current_page >= page_limit):
                break

            current_page += 1
            page_url = self.update_url(url, current_page)
            print(f"Next page: {page_url}")

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

    def is_next_page(self, page_content: Optional[str]) -> bool:
        if not page_content:
            return False

        soup = BeautifulSoup(page_content, "html.parser")
        try:
            next_page_button = self.get_next_button(soup)
            if next_page_button:
                return True

        except Exception as e:
            print(e)
            raise e

        return False

    def get_next_button(self, soup: Any) -> Any:
        raise NotImplementedError

    def update_url(self, url: str, current_page: int) -> str:
        pass
