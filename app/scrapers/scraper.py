from abc import ABC, abstractmethod
from typing import Optional, List


class ScrapeStrategy(ABC):

    @abstractmethod
    def scrape(self, url: Optional[str] = None):
        pass


class PageScraper:
    def __init__(self, scraper_strategy: ScrapeStrategy):
        self.scraper_strategy = scraper_strategy

    def scrape(self, url: Optional[str] = None):
        return self.scraper_strategy.scrape(url)
