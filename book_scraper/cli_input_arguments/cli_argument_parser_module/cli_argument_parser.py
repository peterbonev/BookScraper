import argparse
import sys


class CLIInputParser(object):
    """
    Parsing the CLI string and convert it to variables
    """

    def __init__(self):

        self._parser = argparse.ArgumentParser(
            description="""The following arguments can be used:\n
                                   b - number of books
                                   g - list of genres to search through    #not working
                                   s - list of sortings (for the output, ascending or descending)  #not working
                                   f - list of priority filters for which books to exclude from the scrape      #not working
                                   d - list of keywords to be searched from the description    #not working
                                   t - title of a book to search for   #not working
                                   F - list of book titles to search for (from given json)     #not working""",
            formatter_class=argparse.RawTextHelpFormatter,
        )

        self._parser.add_argument(
            "-X", dest="X", action="store_const", const=True, default=False
        )
        self._parser.add_argument(
            "-b", type=int, metavar="[0-1000]", default=1000, nargs="?", dest="books"
        )
        self._parser.add_argument("-g", nargs="+", dest="genres")

        self.__group1 = self._parser.add_argument_group()
        self.__group1.add_argument(
            "-s",
            type=str,
            nargs="?",
            choices=[None, "price", "rating", "available", "title"],
            dest="sort",
        )
        self.__group1.add_argument(
            "sort_type", nargs="?", choices=[None, "ascending", "descending"]
        )
        self._parser.add_argument("-f", nargs="+", dest="filter")
        self._parser.add_argument("-d", type=str, nargs="+", dest="keywords")
        self._parser.add_argument("-t", type=str, nargs="+", dest="book_title")
        self._parser.add_argument("-F", nargs="?", dest="file_info")

    def parse(self):
        return self._parser.parse_args()
