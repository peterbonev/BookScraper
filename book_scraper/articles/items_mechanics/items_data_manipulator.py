# -*- coding: utf-8 -*-
from book_scraper.articles.items_mechanics.items_link_data import ItemsLinkData

class ItemsDataManipulator(ItemsLinkData):
    def __init__(self):
        ItemsLinkData.__init__(self)
        self.default_key = "title"
    
    def sort_data(self, key, order=False):
        """
            Sort data by given argument and order by ascending or descending 
            param: by_arg,
            param: order,
            return: list of items
        """
        if self.is_search_items_empty() or not self.is_key_valid(self.searched_items[0], key):
            return
        lists = sorted(self.gen_values_searched_items(), key=lambda k: (k[key], k[self.default_key]) ,reverse=order)
        self.searched_items = lists
    
    def filter(self, key= None, value= None):
        """
            Filter searched_items by key and value
            param: key,
            param: value,
        """
        if self.is_search_items_empty() or not self.is_key_valid(self.searched_items[0], key):
            return
        
        self.searched_items = [item for item in self.gen_values_searched_items() if str(value).lower() in str(item[key]).lower()]
