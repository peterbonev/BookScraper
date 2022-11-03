from book_scraper.book_content_parser.data_parse_description import DataParseDescription
from book_scraper.book_content_parser.data_parse_genre import DataParseGenre
from book_scraper.book_content_parser.data_parse_price import DataParsePrice
from book_scraper.book_content_parser.data_parse_rating import DataParseRating
from book_scraper.book_content_parser.data_parse_title import DataParseTitle
from book_scraper.book_content_parser.data_parse_upc import DataParseUPC
from book_scraper.book_content_parser.data_parse_available import DataParseAvailable


class DataParserMixin(DataParseGenre, DataParseDescription, DataParsePrice, DataParseRating, DataParseTitle,
                      DataParseUPC, DataParseAvailable):
    """
        Wrapper class, for scraping certain categories from site
    """
    def data(self, raw_data):
        return self.genre(raw_data), self.price(raw_data), self.title(raw_data), self.rating(raw_data),\
               self.num_available(raw_data),self.description(raw_data), self.upc(raw_data)