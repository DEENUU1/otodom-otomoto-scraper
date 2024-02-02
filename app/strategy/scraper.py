from abc import ABC, abstractmethod
from .params import ParamsBase


class ScrapeStrategy(ABC):
    @abstractmethod
    def scrape(self, params: ParamsBase):
        pass
