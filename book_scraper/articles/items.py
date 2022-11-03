# -*- coding: utf-8 -*-
import json

from book_scraper.articles.items_mechanics.items_data_manipulator import ItemsDataManipulator

class Items(ItemsDataManipulator):
    def __init__(self):
        ItemsDataManipulator.__init__(self)
        
    def return_n_items(self, nr_of_items):
        """
            Slice the result list
            param: container,
            param: nr_of_items,
        """
        try:
            self.searched_items[nr_of_items]
            self.searched_items = self.searched_items[:nr_of_items]
        except IndexError:
            print("There is not so many items: %d" %nr_of_items)

    def print_items(self):
        """
            Print all items from database
        """
        for item in self.gen_values_searched_items():
            print(json.dumps(item, indent=4))
