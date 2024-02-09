from parsers.otodom_parser import OtoDomParser
from scrapers.otodom_scraper import OtoDomScraper
from scrapers.scraper import PageScraper
from parsers.parser import Parser

otodom_url = "https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/cala-polska"
otodom_scraper = OtoDomScraper()

page_scraper_otodom = PageScraper(otodom_scraper)

otodom_data = page_scraper_otodom.scrape(url=otodom_url)

otodom_parser = OtoDomParser()
otodom_page_parser = Parser(otodom_parser)
otodom_parsed_data = otodom_page_parser.parse(data=otodom_data)
for parsed_data in otodom_parsed_data:
    print(parsed_data)
    print("\n\n\n")