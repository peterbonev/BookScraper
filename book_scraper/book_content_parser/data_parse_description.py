from book_scraper.book_content_parser.book_content_parser_defines import BOOK_PRODUCT_DESCRIPTION_ID_NAME, \
    NO_DESCRIPTION


class DataParseDescription(object):

    def __init__(self):
        self.__selection = None

    def description(self, html_raw=None):
        """
        Scrape description of the book
        :param html_raw: Beautiful Soup 4 object (bsObj type)
        :return: Description of the book, data type: unicode
        """
        self.__selection = html_raw.find("div", id=BOOK_PRODUCT_DESCRIPTION_ID_NAME)
        if self.__selection:
            description = self.__selection.findNextSibling("p").get_text(strip=True)
        else:
            description = NO_DESCRIPTION

        return unicode(description)