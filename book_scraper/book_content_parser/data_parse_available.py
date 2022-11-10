import re

from book_content_parser_defines import BOOK_NUM_AVAILABILITY


class DataParseAvailable(object):
    """
    Scrape book's on-stock availability(number of book available)
    :param html_raw: Beautiful Soup 4 object (bsObj type)
    :return: Num of the book, data type: int
    """

    def __init__(self):
        self.__available = None

    def num_available(self, html_raw=None):
        """
        Parse book's available information
        return: Number available books(on-stock)
        """
        self.__available = html_raw.find("p", class_=BOOK_NUM_AVAILABILITY)
        return int("".join(re.findall(r"(\d+)", self.__available.get_text(strip=True))))
