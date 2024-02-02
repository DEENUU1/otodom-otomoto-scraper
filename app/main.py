from otodom.scraper import OtoDomScraper
from strategy.scraper import Scraper

# ?page=2
url = "https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/cala-polska"
scraper = Scraper(OtoDomScraper()).scrape(url=url)
print(scraper)

