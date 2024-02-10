from typing import Any

from .oto_base import OtoBaseScraper


class OtoDomScraper(OtoBaseScraper):

    def get_next_button(self, soup: Any) -> Any:
        try:
            next_page_button = soup.find("button", {"data-cy": "pagination.next-page"})
            if next_page_button:
                return next_page_button

        except Exception as e:
            print(e)
            raise e

        return None

    def update_url(self, url: str, current_page: int) -> str:
        return f"{url}&page={current_page}"
