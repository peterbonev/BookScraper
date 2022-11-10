from book_scraper.book_content_parser.book_content_parser_defines import (
    BOOK_PRICE_CLASS_NAME,
)


class DataParsePrice(object):
    def __init__(self):
        pass

    def price(self, html_raw=None):
        """
        Scrape price of the book
        :param html_raw: Beautiful Soup 4 object (bsObj type)
        :return: Price of the book, data type: float
        """
        return float(
            html_raw.find("p", class_=BOOK_PRICE_CLASS_NAME).getText(strip=True)[1:]
        )
