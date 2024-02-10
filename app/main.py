from parsers.otodom_parser import OtoDomParser
from parsers.otomoto_parser import OtoMotoParser
from scrapers.otodom_scraper import OtoDomScraper
from scrapers.otomoto_scraper import OtoMotoScraper
from scrapers.scraper import PageScraper
from parsers.parser import Parser

# otomoto_url = "https://www.otomoto.pl/osobowe"
# otomoto_scraper = OtoMotoScraper()
#
# page_scraper_otomoto = PageScraper(otomoto_scraper)
# otomoto_data = page_scraper_otomoto.scrape(url=otomoto_url)
# otomoto_parser = OtoMotoParser()
# otomoto_page_parser = Parser(otomoto_parser)
# otomoto_parsed_data = otomoto_page_parser.parse(data=otomoto_data)
# for parsed_data in otomoto_parsed_data:
#     print(parsed_data)
#     print("\n\n\n")

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