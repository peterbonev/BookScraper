import unittest
from book_scraper.book_data_parser.book_data_parser_filter_mixin import BookDataParserFilterMixin as bdpm

class BookMixinTests(unittest.TestCase):
    def setUp(self):
        self.par_mix = bdpm()

    def test_init(self):
        self.assertTrue(isinstance(self.par_mix, bdpm))

    def test_exclude(self):
        pass



if __name__ == '__main__':
    unittest.main()
