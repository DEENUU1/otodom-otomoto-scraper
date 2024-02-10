from typing import List, Optional

from bs4 import BeautifulSoup

from .parser import ParserStrategy, ResultBase


class OtoBaseParser(ParserStrategy):

    def get_soup(self, data: str):
        return BeautifulSoup(data, 'html.parser')

    def parse(self, data: List[Optional[str]]) -> List[Optional[ResultBase]]:
        result = []

        for page in data:
            soup = self.get_soup(page)

            offers = self.get_offers(soup)
            for offer in offers:
                if not offer:
                    continue

                parsed_offer = self.get_offer(offer)
                if parsed_offer:
                    result.append(parsed_offer)

        return result

    def get_offers(self, soup) -> List[Optional[str]]:
        raise NotImplementedError

    def get_offer(self, offer) -> Optional[ResultBase]:
        raise NotImplementedError
