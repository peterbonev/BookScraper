import StringIO
import sys
import unittest
from book_scraper.database.database import DataBase as db
from book_scraper.articles.items import Items as it


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
        expected_result = [{'reviews': 0,
                            'rating': 4,
                            'description': 'WICKED above her hipbone',
                            'title': 'Sharp Objects',
                            'genre': 'Mystery',
                            'price': 47.82,
                            'available': 20,
                            'upc': 'e00eb4fd7b871a48'},
                           {'reviews': 1,
                            'rating': 1,
                            'description': 'description',
                            'title': 'Objects',
                            'genre': 'smt',
                            'price': 40.0,
                            'available': 10,
                            'upc': 'eb871a48'},
                           {'reviews': 0,
                            'rating': 5,
                            'description': 'hipbone',
                            'title': 'title',
                            'genre': 'genre',
                            'price': 50.21,
                            'available': 50,
                            'upc': 'e00eb4fd748'}]
        self.assertEqual(self.searched_items.searched_items, expected_result)

    def test_generic_search_success(self):
        """
            Successfully searched for book with rating 1
        """
        expected_result = [{'reviews': 1,
                            'rating': 1,
                            'description': 'description',
                            'title': 'Objects',
                            'genre': 'smt',
                            'price': 40.0,
                            'available': 10,
                            'upc': 'eb871a48'}]
        self.searched_items.filter('rating', 1, '=')
        self.assertEqual(self.searched_items.searched_items, expected_result)

    def test_generic_search_wrong_key(self):
        """
            If the key for searching is wrong the generic search returns nothing
        """
        self.assertEqual(self.searched_items.filter('raing', 1, '='), None)

    def test_generic_search_non_existing_value(self):
        """
            If the value we are searching is wrong/not existing the generic search returns nothing
        """
        self.assertEqual(self.searched_items.filter('rating', 10, '='), None)

    def test_generic_search_wrong_sign(self):
        """
            If the sign we are searching with is wrong/not existing the generic search returns nothing
        """
        self.assertEqual(self.searched_items.filter('rating', 1, '!='), None)

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
        expected_result = [{'reviews': 1,
                            'rating': 1,
                            'description': 'description',
                            'title': 'Objects',
                            'genre': 'smt',
                            'price': 40.0,
                            'available': 10,
                            'upc': 'eb871a48'}]
        self.searched_items.filter('rating', 1, '=')
        self.assertEqual(list(self.searched_items.gen_values_searched_items()), expected_result)

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
        expected_res = [{'available': 50,
                         'rating': 5,
                         'description': 'hipbone',
                         'title': 'title',
                         'genre': 'genre',
                         'price': 50.21,
                         'reviews': 0,
                         'upc': 'e00eb4fd748'},
                        {'available': 20,
                         'rating': 4,
                         'description': 'WICKED above her hipbone',
                         'title': 'Sharp Objects',
                         'genre': 'Mystery',
                         'price': 47.82,
                         'reviews': 0,
                         'upc': 'e00eb4fd7b871a48'},
                        {'available': 10,
                         'rating': 1,
                         'description': 'description',
                         'title': 'Objects',
                         'genre': 'smt',
                         'price': 40.0,
                         'reviews': 1,
                         'upc': 'eb871a48'}]
        self.assertEqual(self.searched_items.searched_items, expected_res)

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
        expected_res = "{'available': 20, 'rating': 4, 'description': 'WICKED above her hipbone', 'title': 'Sharp " \
                       "Objects', 'genre': 'Mystery', 'price': 47.82, 'reviews': 0, 'upc': 'e00eb4fd7b871a48'}\n{" \
                       "'available': 10, 'rating': 1, 'description': 'description', 'title': 'Objects', " \
                       "'genre': 'smt', 'price': 40.0, 'reviews': 1, 'upc': 'eb871a48'}\n{'available': 50, 'rating': " \
                       "5, " \
                       "'description': 'hipbone', 'title': 'title', 'genre': 'genre', 'price': 50.21, 'reviews': 0, " \
                       "'upc': 'e00eb4fd748'}\n\n"

        self.assertEqual(expected_res, print_items_output.getvalue())


if __name__ == '__main__':
    unittest.main()
