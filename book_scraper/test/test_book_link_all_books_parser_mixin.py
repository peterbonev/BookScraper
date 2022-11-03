import unittest
from book_scraper.book_link_parser.book_link_all_books_parser import BookLinkAllBooksParser as blpar
from book_scraper.links.links import Links


class BlpTests(unittest.TestCase):
    def setUp(self):
        self.blpars = blpar()
        self.result = self.blpars._parse_all_urls(3)

    def test_init(self):
        self.assertIsInstance(self.blpars, blpar)

    def test_parse_all_urls_content_returned(self):
        expected_res = "{1: 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html', 2: 'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html', 3: 'http://books.toscrape.com/catalogue/soumission_998/index.html'}"
        result = str(self.result.content())
        self.assertEqual(expected_res, result)

    def test_parse_all_urls_type_returned(self):
        self.assertEqual(Links, type(self.result))


if __name__ == '__main__':
    unittest.main()
