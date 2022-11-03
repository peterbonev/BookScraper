import StringIO
import sys
import unittest
from book_scraper.database.database import DataBase as db
from book_scraper.articles.items import Items as it
from items_expected import *


class ItemsTests(unittest.TestCase):
    def setUp(self):
        self.new_item = it()
        self.new_db = db()
        self.new_db.add_item('Mystery', 'Sharp Objects', 47.82, 4, 20, 'WICKED above her hipbone', 'e00eb4fd7b871a48',
                             0)
        self.new_db.add_item('smt', 'Objects', 40.00, 1, 10, 'description', 'eb871a48', 1)
        self.new_db.add_item('genre', 'title', 50.21, 5, 50, 'hipbone', 'e00eb4fd748', 0)
        self.searched_items = it()
        self.searched_items.fill_searched_items()

    def tearDown(self):
        pass

    def test_initializing_class_instance(self):
        """
            Test initializing new item
        """
        self.assertIsInstance(self.new_item, it)

    def test_fill_searched_items(self):
        """
            Test for the gathering info from database in searched items instance
        """
        self.assertEqual(fill_searched_items_expected_res, self.searched_items.searched_items)

    def test_filter_success(self):
        """
            Successfully searched for book with rating 1
        """
        self.searched_items.filter('description', 'above')
        self.assertEqual(filter_succs_expected_res, self.searched_items.searched_items)

    def test_filter_wrong_key(self):
        """
            If the key for searching is wrong the filter returns nothing
        """
        self.assertEqual(self.searched_items.filter('raing', 1), None)

    def test_filter_non_existing_value(self):
        """
            If the value we are searching is wrong/not existing the filter returns nothing
        """
        self.assertEqual(self.searched_items.filter('rating', 10), None)

    def test_filter_wrong_sign(self):
        """
            If the sign we are searching with is wrong/not existing the filter returns nothing
        """
        self.assertEqual(self.searched_items.filter('rating', 1), None)

    def test_searched_items_searched_items(self):
        """
            It's not ypo just the names are the same, but it makes sense
            searched items returns list of the searched items
        """
        self.assertEqual(type(self.searched_items.searched_items), list)

    def test_gen_values_searched_items(self):
        """
            After a generic search gen values searched items returns the wanted item/s
        """
        self.searched_items.filter('rating', 1)
        self.assertEqual(gen_value_expected_res, list(self.searched_items.gen_values_searched_items()))

    def test_is_key_valid_success(self):
        """
            is_key_valid returns True if the key exist in the dictionary of the database
            and its case sensitive
        """
        self.assertEqual(self.searched_items.is_key_valid(self.searched_items.searched_items[0], 'rating'), True)

    def test_is_key_valid_fail(self):
        """
            is_key_valid returns False if the key don't exist in the dictionary of the database
        """
        self.assertNotEqual(
            self.searched_items.is_key_valid(self.searched_items.searched_items[0], 'Year of publishing'), True)

    def test_sort_data_success(self):
        """
            Test sorting by right key
        """
        self.searched_items.sort_data('rating', True)
        self.assertEqual(sort_succ_expected_res, self.searched_items.searched_items)

    def test_sort_data_wrong_key(self):
        """
            If the key is wrong the function returns nothing and stops
        """
        self.assertEqual(self.searched_items.sort_data('Rating', True), None)

    def test_print_items(self):
        """
            Test the output of print items
            I have no idea why it wants two blank lines at the end
        """
        print_items_output = StringIO.StringIO()
        sys.stdout = print_items_output
        self.searched_items.print_items()
        self.assertEqual(print_expected_res, print_items_output.getvalue())

    def test_is_search_items_empty_success(self):
        self.assertFalse(self.searched_items.is_search_items_empty())

    def test_is_search_items_empty_fail(self):
        self.new_items = it()
        self.assertTrue(self.new_items.is_search_items_empty())

    def test_return_n_items_success(self):
        self.searched_items.return_n_items(1)
        result = self.searched_items.searched_items
        self.assertEqual(return_n_succ_expected_res, result)

    def test_return_n_items_fail(self):
        self.searched_items.return_n_items(10)
        result = self.searched_items.searched_items
        self.assertEqual(return_n_fail_expected_res, result)

    def test_return_n_items_fail_err_msg(self):
        error_msg = 'There is not so many items: 10\n'
        error_printed = StringIO.StringIO()
        sys.stdout = error_printed
        self.searched_items.return_n_items(10)
        self.assertEqual(error_msg, error_printed.getvalue())


if __name__ == '__main__':
    unittest.main()
