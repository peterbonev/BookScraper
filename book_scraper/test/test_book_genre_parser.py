import unittest
from book_scraper.book_genre_parser.book_link_genre_parser import BookGenresParser as bgp
from genre_parser_expected import *


class BgpTests(unittest.TestCase):
    def setUp(self):
        self.genpars = bgp()

    def test_init(self):
        self.assertIsInstance(self.genpars, bgp)

    def test_genres(self):
        self.assertEqual(all_genres_expected, self.genpars.genres().content())

    def test_parse_by_genre(self):
        links_genres = self.genpars._parse_genres()
        result = self.genpars._parse_by_genre('Travel', links_genres)
        self.assertEqual(expected_pass_by_genre_res, result.content())

    def test_parse_by_genre_with_limit(self):
        links_genres = self.genpars._parse_genres()
        result = self.genpars._parse_by_genre('Travel', links_genres, 5)
        self.assertEqual(expected_pass_by_genre_with_limit_res, result.content())


if __name__ == '__main__':
    unittest.main()
