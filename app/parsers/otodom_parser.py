from dataclasses import dataclass
from typing import Optional

from .parser import ResultBase
from .oto_base_parser import OtoBaseParser


@dataclass
class OtoDomOfferDetails:
    total_price: Optional[str] = None
    price_per_meter: Optional[str] = None
    num_of_rooms: Optional[str] = None
    area: Optional[str] = None


@dataclass
class OtoDomResult(ResultBase):
    is_sponsored: bool
    title: Optional[str] = None
    location: Optional[str] = None
    url: Optional[str] = None
    image_url: Optional[str] = None
    details: Optional[OtoDomOfferDetails] = None


class OtoDomParser(OtoBaseParser):

    def get_offer(self, offer) -> Optional[OtoDomResult]:
        try:
            title = offer.find("span", {"data-cy": "listing-item-title"})
            address = offer.find("p", class_="css-19dkezj")
            is_sponsored = offer.find("p", class_="css-1vd92mz")
            url = offer.find("a", {"data-cy": "listing-item-link"})
            image = offer.find("img")

            sponsored = False
            if is_sponsored:
                sponsored = True

            image_url, offer_url = None, None
            if image:
                image_url = image["src"]
            if url:
                offer_url = url["href"]

            result = OtoDomResult(
                is_sponsored=sponsored,
                title=title.text,
                location=address.text,
                url=offer_url,
                image_url=image_url,
                details=self.get_details(offer)
            )

            return result

        except Exception as e:
            raise e

    def get_details(self, offer) -> Optional[OtoDomOfferDetails]:
        try:
            div_container = offer.find("div", class_="e1jyrtvq0")
            if div_container:
                span_elements = div_container.find_all("span")

                total_price = span_elements[0].text.replace("\xa0", "")
                price_per_meter = span_elements[1].text.replace("\xa0", "")
                num_of_rooms = span_elements[2].text
                area = span_elements[3].text

                return OtoDomOfferDetails(
                    total_price=total_price,
                    price_per_meter=price_per_meter,
                    num_of_rooms=num_of_rooms,
                    area=area
                )

        except Exception as e:
            raise e

    def get_offers(self, soup):
        try:
            items = soup.find_all('div', {"data-cy": "listing-item"})
            return items
        except Exception as e:
            print(e)
            raise e
