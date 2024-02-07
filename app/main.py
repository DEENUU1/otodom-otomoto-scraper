from scrapers.otodom_scraper import OtoDomScraper
from scrapers.scraper import PageScraper
from scrapers.otomoto_scraper import OtoMotoScraper


otodom_url = "https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/cala-polska"
otodom_scraper = OtoDomScraper()

otomoto_url = "https://www.otomoto.pl/osobowe"
otomoto_scraper = OtoMotoScraper()

page_scraper_otodom = PageScraper(otodom_scraper)
page_scraper_otomoto = PageScraper(otomoto_scraper)


# page_scraper_otodom.scrape(url=otodom_url)
page_scraper_otomoto.scrape(url=otomoto_url)