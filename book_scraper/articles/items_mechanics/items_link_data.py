from book_scraper.database.database import DataBase

class ItemsLinkData(object):
    def __init__(self):
        """
            Initialize searched_items and fill it with database data
        """
        self.__searched_items = []
    
    @property
    def searched_items(self):
        return self.__searched_items
    
    @searched_items.setter
    def searched_items(self, value):
        self.__searched_items = value
    
    def gen_values_searched_items(self):
        """
            Generator for each item in property search_items
            yeild: item
        """
        for item in self.searched_items:
            yield item

    @staticmethod
    def is_key_valid(container, key):
        """
            Check is key valid for dict
            param: container
            param: key,
            return: boolean
        """
        try:
            container[key]
        except KeyError:
            print("This is invalid input: %s" %key)
            return False
        return True
    
    def is_search_items_empty(self):
        try:
            self.searched_items[0]
        except IndexError:
            print("There are no such items")
            return True
        return False
    
    def fill_searched_items(self):
        """
            Fill searched items(property) with database items
        """
        self.searched_items = [item for item in DataBase().gen_iterate_through_database()]
