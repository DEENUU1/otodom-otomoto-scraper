from typing import Optional, Type

from strategy.scraper import ScrapeStrategy
from .params import OtoDomParams


class OtoDomScraper(ScrapeStrategy):
    BASE_URL: str = "https://www.otodom.pl/"

    @staticmethod
    def _get_url(params: Type[OtoDomParams] = None) -> str:
        raise NotImplementedError

    def scrape(self, params: Optional[OtoDomParams] = None, url: Optional[str] = None):
        if not url:
            url = self._get_url(params)
            print(f"Build url: {url}")
        print(f"Passed url: {url}")

