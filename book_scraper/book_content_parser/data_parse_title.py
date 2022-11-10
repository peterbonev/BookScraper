from book_scraper.book_content_parser.book_content_parser_defines import (
    BOOK_TITLE_CLASS_NAME,
)


class DataParseTitle(object):
    def __init__(self):
        pass

    def title(self, html_raw=None):
        """
        Scrape title of the book
        :param html_raw: Beautiful Soup 4 object (bsObj type)
        :return: Title of the book, data type: unicode
        """
        return html_raw.find("li", class_=BOOK_TITLE_CLASS_NAME).get_text(strip=True)
