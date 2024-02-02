from otodom.scraper import OtoDomScraper
from strategy.scraper import Scraper

otodom_url = "https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/mazowieckie/warszawa/warszawa/warszawa?limit=36&ownerTypeSingleSelect=ALL&by=DEFAULT&direction=DESC&viewType=listing"
scraper = Scraper(OtoDomScraper()).scrape(url=otodom_url)
print(scraper)

