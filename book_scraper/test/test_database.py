import unittest
from types import GeneratorType

from book_scraper.database.database import DataBase as db


class DBTests(unittest.TestCase):
    def setUp(self):
        self.title = 'Sharp Objects'
        self.genre = 'Mystery'
        self.price = 47.82
        self.rating = 4
        self.num_available = 20
        self.description = 'description'
        self.upc = 'e00eb4fd7b871a48'
        self.reviews = 0
        self.new_data_base = db()
        self.test_dict = {'thisIsUpc': {'rating': 4,
                                        'description': 'This is description',
                                        'title': 'This is title',
                                        'genre': 'This is genre',
                                        'price': 10.00,
                                        'available': 10,
                                        'upc': 'thisIsUpc'}}

    def tearDown(self):
        self.new_data_base.reset()

    def test_db_initialising_success(self):
        """
            Test is initializing is correct
        """

        self.assertIsInstance(self.new_data_base, db)

    def test_db_sigleton_is_stored_as_class_instance(self):
        """
            Test if the initialization returns its product as class instance
        """
        self.new_data_base.add_item(self.genre, self.title, self.rating,
                                    self.num_available, self.description)
        assert self.new_data_base._instance is db._instance

    def test_db_instance_taking_arguments_add_item_method_success(self):
        """
            Test to see if add_item method saves the information as intended
        """
        self.new_data_base = db()
        self.new_data_base.add_item('This is genre', 'This is title', 10.00, 4, 10, 'This is description', 'thisIsUpc')
        self.assertEqual(self.new_data_base.data, self.test_dict)

    def test_db_instance_taking_arguments_add_item_method_fail(self):
        """
            Test with different variants of the information added
        """
        self.new_data_base = db()
        self.new_data_base.add_item('genre', 'title', 20.00, 14, 20, 'description', 'thisIsUpc')
        self.assertNotEqual(self.new_data_base.data, self.test_dict)

    def test_try_init_second_db(self):
        """
            class DataBase is singleton so no matter how many instances we create they will hold the same info:
        """
        self.new_data_base2 = db()
        self.new_data_base.add_item(self.genre, self.title, self.rating,
                                    self.num_available, self.description)
        self.assertEqual(self.new_data_base.data, self.new_data_base2.data)

    def test_data(self):
        """
            Test if property function data returns correct type information
        """
        self.assertEqual(type(self.new_data_base.data), dict)

    def test_iterate_through_database(self):
        """
            iterate through database returns generator
        """
        self.assertEqual(type(self.new_data_base.gen_iterate_through_database()), GeneratorType)

    def test_reset(self):
        """
            reset function nullifies the database
        """
        self.assertEqual(self.new_data_base.reset(), None)


if __name__ == '__main__':
    unittest.main()
