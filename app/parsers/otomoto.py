from dataclasses import dataclass
from typing import Optional

from .otobase import OtoBaseParser
from .parser import ResultBase


@dataclass
class OtoMotoResult(ResultBase):
    title: Optional[str] = None
    url: Optional[str] = None
    image_url: Optional[str] = None
    type_of_seller: Optional[str] = None
    price: Optional[str] = None
    price_currency: Optional[str] = None
    mileage: Optional[str] = None
    fuel_type: Optional[str] = None
    gearbox: Optional[str] = None
    year: Optional[str] = None


class OtoMotoParser(OtoBaseParser):

    def get_offer(self, offer) -> Optional[OtoMotoResult]:
        try:
            title_url_container = offer.find("h1", class_="efpuxbr9 ooa-1ed90th er34gjf0")

            title = title_url_container.find("a")
            url = title["href"]
            image = offer.find("img")
            type_of_seller = offer.find("li", class_="ooa-1y6ajhy ebwza7n5")
            price = offer.find("h3", class_="efpuxbr16 ooa-1n2paoq er34gjf0")
            price_currency = offer.find("p", class_="efpuxbr17 ooa-8vn6i7 er34gjf0")

            mileage = offer.find("dd", {"data-parameter": "mileage"})
            fuel_type = offer.find("dd", {"data-parameter": "fuel_type"})
            gearbox = offer.find("dd", {"data-parameter": "gearbox"})
            year = offer.find("dd", {"data-parameter": "year"})

            result = OtoMotoResult(
                title=title.text if title else None,
                url=url if url else None,
                image_url=image["src"] if image else None,
                type_of_seller=type_of_seller.text if type_of_seller else None,
                price=price.text if price else None,
                price_currency=price_currency.text if price_currency else None,
                mileage=mileage.text if mileage else None,
                fuel_type=fuel_type.text if fuel_type else None,
                gearbox=gearbox.text if gearbox else None,
                year=year.text if year else None,
            )
            return result

        except Exception as e:
            print(e)
            raise e

    def get_offers(self, soup):
        try:
            items = soup.find_all("article", class_="ooa-yca59n efpuxbr0")
            print(f"Find {len(items)} items")
            return items
        except Exception as e:
            print(e)
            raise e
