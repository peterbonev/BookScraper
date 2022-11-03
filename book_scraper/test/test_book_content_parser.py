import unittest

from book_content_parser.data_parse_description import DataParseDescription
from book_genre_parser.book_link_genre_parser import BookGenresParser
from book_link_parser.book_link_parser import BookLinkParser
from book_scraper.book_content_parser.book_content_parser import BooksContentParser
from book_content_parser.data_parse_available import DataParseAvailable
from book_content_parser.data_parse_price import DataParsePrice
from book_content_parser.data_parse_rating import DataParseRating
from book_content_parser.data_parse_title import DataParseTitle
from book_content_parser.data_parse_upc import DataParseUPC
from book_content_expected import *
from bs4 import BeautifulSoup


class BCPTests(unittest.TestCase):
    def setUp(self):
        self.bcp = BooksContentParser()
        self.new_description = DataParseDescription()

    def test_init(self):
        self.assertIsInstance(self.bcp, BooksContentParser)

    def test_collect_by_price_over(self):
        genres = BookGenresParser()
        lst = ['Science']
        links = BookLinkParser(genres).collect(lst)
        verimp = ['price', '>15']
        result = self.bcp.collect(verimp, links)
        self.assertEqual(price_expected_res, result._content)

    def test_collect_by_rate(self):
        genres = BookGenresParser()
        lst = ['Science']
        links = BookLinkParser(genres).collect(lst)
        verimp = ['rate', '=2']
        result = self.bcp.collect(verimp, links)
        self.assertEqual(rate_expected_res, result._content)

    def test_collect_by_available(self):
        genres = BookGenresParser()
        lst = ['Science']
        links = BookLinkParser(genres).collect(lst)
        verimp = ['available', '<7']
        result = self.bcp.collect(verimp, links)
        self.assertEqual(available_expected_res, result._content)

    def test_data_parse_description_init(self):
        self.assertTrue(isinstance(self.new_description, DataParseDescription))

    def test_description(self):
        file_red = open('expected_res_files/html_content_example.html', 'r')
        html_content = BeautifulSoup(file_red, 'html.parser')
        file_red.close()
        self.assertEqual(description_expected_res, self.new_description.description(html_content))

    def test_no_description(self):
        file_read = open('expected_res_files/star_rate_1.html', 'r')
        test_html = BeautifulSoup(file_read, 'html.parser')
        file_read.close()
        expected_res = 'No description'
        self.assertEqual(expected_res, self.new_description.description(test_html))

    def test_available_init(self):
        new_av = DataParseAvailable()
        self.assertTrue(isinstance(new_av, DataParseAvailable))

    def test_price_init(self):
        new_price = DataParsePrice()
        self.assertTrue(isinstance(new_price, DataParsePrice))

    def test_rate_init(self):
        new_rate = DataParseRating()
        self.assertTrue(isinstance(new_rate, DataParseRating))

    def test_title_init(self):
        new_title = DataParseTitle()
        self.assertTrue(isinstance(new_title, DataParseTitle))

    def test_upc_init(self):
        new_upc = DataParseUPC()
        self.assertTrue(isinstance(new_upc, DataParseUPC))


if __name__ == '__main__':
    unittest.main()
