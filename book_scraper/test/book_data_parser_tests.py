import unittest
from book_scraper.book_data_parser.book_data_parser import BooksDataParser as bdp
from book_scraper.database.database import DataBase as db

class BookDataParserTests(unittest.TestCase):
    def setUp(self):
        self.bpar = bdp()
        self.new_db = db()

    def test_init(self):
        assert isinstance(self.bpar, bdp)

    def test_scrape_data(self):
        pass

if __name__ == '__main__':
    unittest.main()
