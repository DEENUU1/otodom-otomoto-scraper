from abc import ABC, abstractmethod
from typing import Optional


class ScrapeStrategy(ABC):

    @abstractmethod
    def scrape(self, url: Optional[str] = None, page_limit: Optional[int] = None):
        pass


class PageScraper:
    def __init__(self, scraper_strategy: ScrapeStrategy):
        self.scraper_strategy = scraper_strategy

    def scrape(self, url: Optional[str] = None, page_limit: Optional[int] = None):
        return self.scraper_strategy.scrape(url, page_limit)
