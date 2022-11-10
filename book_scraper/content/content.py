# -*- coding: utf-8 -*-
from book_scraper.database.database import DataBase


class Content(object):
    """
    Interafce class to collect parsed data from BookContentParser and DataBase.
    Provides loosly coupling between BookContentParser and DataBase and could be used for maangement of
    multiple scraping items
    """

    def __init__(self):
        self._content = {}

    def add(self, genre, title, price, rating, available, description, upc):
        self._content[upc] = [title, genre, price, rating, available, description]

    def export_to_db(self):
        database = DataBase()
        for key, value in self._content.items():
            title, genre, price, rating, available, description = value
            database.add_item(title, genre, price, rating, available, description, key)

    def reset(self):
        self._content.clear()

    def view(self):
        for k, v in self._content.items():
            print("{} {}".format(k, v))
