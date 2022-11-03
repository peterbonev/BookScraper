import unittest
from book_scraper.book_link_parser.book_link_all_books_parser_mixin import BookLinkParserAllBooksMixin as parse_all_books
from book_scraper.links.links import Links


class BookLinkGenreParserTest(unittest.TestCase):

    def setUp(self):
        self.num_books = 200
        self.link_parser = parse_all_books()

    def test_result(self):
        result = Links()
        self.assertIsInstance(type(self.link_parser._parse_all_urls(self.num_books), type(result)))

    def test_result_amount(self):
        result = Links().content()
        self.assertEqual(len(self.link_parser._parse_all_urls(self.num_books).content().values()), self.num_books)


if __name__ == '__main__':
    unittest.main()
