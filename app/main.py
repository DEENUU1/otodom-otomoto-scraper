from typing import Optional

import typer

from exporters.export import Export
from exporters.to_json import JsonExport
from parsers.otodom import OtoDomParser
from parsers.otomoto import OtoMotoParser
from parsers.parser import Parser
from scrapers.otodom import OtoDomScraper
from scrapers.otomoto import OtoMotoScraper
from scrapers.scraper import PageScraper

app = typer.Typer()


@app.command()
def main(
        url: str,
        page_limit: Optional[int] = 1,
        export_to: Optional[str] = "json",
) -> None:
    parsed_data = None

    if "otomoto" in url:
        page_scraper_otomoto = PageScraper(scraper_strategy=OtoMotoScraper())
        otomoto_data = page_scraper_otomoto.scrape(url=url, page_limit=page_limit)

        otomoto_page_parser = Parser(parser_strategy=OtoMotoParser())
        parsed_data = otomoto_page_parser.parse(data=otomoto_data)
    elif "otodom" in url:
        page_scraper_otodom = PageScraper(scraper_strategy=OtoDomScraper())
        otodom_data = page_scraper_otodom.scrape(url=url, page_limit=page_limit)

        otodom_page_parser = Parser(parser_strategy=OtoDomParser())
        parsed_data = otodom_page_parser.parse(data=otodom_data)
    else:
        print("Invalid url")

    if export_to == "json":
        if not parsed_data:
            print("No data")

        json_export = JsonExport()
        export = Export(strategy=json_export)
        export.export(parsed_data=parsed_data)

    else:
        print("Invalid export format")


if __name__ == "__main__":
    app()
