#!/usr/bin/python2
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup

from book_scraper.content.content import Content
from book_scraper.book_content_parser.book_content_parser_filter import BookDataParserFilter
from book_scraper.book_content_parser.data_content_mixin import DataParserMixin
from book_scraper.request_parser.request_parser import RequestsParser


class BooksContentParser(DataParserMixin, BookDataParserFilter):

    def __init__(self):
        super(BooksContentParser, self).__init__()
        super(DataParserMixin, self).__init__()

    def collect(self, verified_input=None, args = None, num_books=None):  # previous def scrape_all_info
        """
        Scrape information about a book in following categories:
        title, genrem price, rating, available number, description, UPC
        :param verified_input: VerifiedInputData object
        :param args: Links object
        :param num_books: int
        :return: N/A (all scraped data is put in an instance of class Database)
        """
        self._exclusion_selection = verified_input
        page_responses = RequestsParser(args.content().values()).content()
        results = Content()
        for page in page_responses:

                soup = BeautifulSoup(page.decode('utf-8','ignore'), "lxml")

                genre, price, title, rating, num_available, description, upc = DataParserMixin().data(soup)
                book_info = {'title': title, 'genre': genre, 'price': price, 'available': num_available,
                                 'rating': rating, 'description': description, 'upc': upc}

                if self._exclusion_selection:
                    if self._exclude(self._exclusion_selection, book_info):
                        print(self._exclude(self._exclusion_selection, book_info))
                        continue
                    else:
                        results.add(title, genre, price, rating, num_available, description, upc)
                else:
                    results.add(title, genre, price, rating, num_available, description, upc)

        return results