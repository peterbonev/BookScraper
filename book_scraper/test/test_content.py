import sys
import unittest
import StringIO
from book_scraper.content.content import Content as ct
from book_scraper.database.database import DataBase as db


class ContentTest(unittest.TestCase):
    """
        Tests for class Content and its communication with class database
    """

    def setUp(self):
        self.content = ct()
        self.database = db()
        self.content.add('Mystery', 'Sharp Objects', 47.82, 4, 20, 'WICKED above her hipbone', 'e00eb4fd7b871a48')

    def test_init(self):
        self.assertIsInstance(self.content, ct)

    def test_add(self):
        expected_res = {'e00eb4fd7b871a48': ['Sharp Objects',
                                             'Mystery',
                                             47.82,
                                             4,
                                             20,
                                             'WICKED above her hipbone']}
        self.assertEqual(expected_res, self.content._content)

    def test_view(self):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        self.content.view()
        expected_res = "e00eb4fd7b871a48 ['Sharp Objects', 'Mystery', 47.82, 4, 20, 'WICKED above her hipbone']\n"
        self.assertEqual(expected_res, captured_output.getvalue())

    def test_reset(self):
        self.content.reset()
        self.assertEqual({}, self.content._content)

    def test_export_to_db(self):
        self.content.export_to_db()
        upc = 'e00eb4fd7b871a48'
        self.assertTrue(upc in self.database.data)


if __name__ == '__main__':
    unittest.main()
