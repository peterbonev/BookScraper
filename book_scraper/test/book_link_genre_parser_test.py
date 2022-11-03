import unittest

from book_scraper.book_link_parser.book_link_genre_parser_mixin import BookLinkGenresParserMixin as link_genre_parser
from book_scraper.links.links import Links


class BookLinkGenresParserMixinTest(unittest.TestCase):

    def SetUp(self):
        self.list_genres_titles = [u'Young Adult', u'Humor', u'Fiction', u'Add a comment', u'Music', u'Historical Fiction',
                            u'Womens Fiction', u'Christian', u'Business', u'Sports and Games', u'Horror', u'Philosophy',
                            u'New Adult', u'Short Stories', u'Thriller', u'Contemporary', u'Mystery', u'Default']
        self.list_genres_links = ['http://books.toscrape.com/catalogue/category/books/autobiography_27/index.html',
                                  'http://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html']
        self.genre_parser = link_genre_parser()
        self.links = link_genre_parser()._parse_genres()

    def test_parse_genres_titles(self):
        self.assertDictContainsSubset(self.list_genres_titles,self.genre_parser._parse_genres().content().keys() )

    def test_parse_by_genre(self):#(self, input_list_genres, links_object, limit=None):  # old: parse_url_genre_cat
        self.assertDictContainsSubset(self.list_genres_links, self.genre_parser._parse_by_genre(self.list_genres_titles, self.links).content().values())