import re

from bs4 import BeautifulSoup

from book_scraper.book_link_parser.book_link_parser_defines import DOMAIN_ALL_GENRES, A_TAG, D_TAG, \
    DOMAIN_NAME, HREF_TAG, HTML_LIST_TAG, FROM_END, \
    HTML_BOOK_CLASS, DOMAIN_NAME_STRING, MAX_PAGES, PAGE_SUFFIX

from book_scraper.request_parser import RequestsParser
from book_scraper.links.links import Links

class BookGenresParser(object):

    def __init__(self):
        self.__genres = self._parse_genres()

    def genres(self):
        return self.__genres

    @staticmethod
    def _parse_genres():
        """
            Parse all genres' categories from the web site
        links: class Links instance
        :return: List with genres, data type: list with str
        """
        initial_request = RequestsParser(DOMAIN_NAME).content()
        links = Links()
        soup = BeautifulSoup(initial_request.content, 'lxml')
        selection = soup.find(D_TAG, DOMAIN_ALL_GENRES).get_text(",", strip=True).split(',')[1:]
        all_genres_raw_data = soup.find(D_TAG, DOMAIN_ALL_GENRES).find_all('a', href=True)[1:]

        for index in range(0, len(all_genres_raw_data)):
            links.add(selection[index], '{}{}'.format(DOMAIN_NAME,all_genres_raw_data[index]['href']))     #'{}{}'.format(DOMAIN_NAME, link['href'])

        return links
    @staticmethod
    def _parse_by_genre(input_list_genres, links_object, limit=None): #old: parse_url_genre_cat
        """
        Parse all URLs from given genre
        All results are given in container self.__temp_buffer
        :param target_number_books:int
        :return: list of all books URLs
        """
        result_links = Links()

        for raw_data in links_object.content().keys():
            if not raw_data in input_list_genres:
                links_object.content().pop(raw_data)
            else:
                result_links.add('{}{}'.format(raw_data, 0),
                                 '{}{}{}'.format(links_object.content()[raw_data][:FROM_END], 'index',
                                                   PAGE_SUFFIX))
                for index in range(2, MAX_PAGES):
                    result_links.add('{}{}'.format(raw_data,index), '{}{}{}{}'.format(links_object.content()[raw_data][:FROM_END], 'page-', index, PAGE_SUFFIX))

        requests = RequestsParser(result_links.content().values())
        index = 0
        result_links.reset()
        quit_flag = False
        for request in requests.content():
            # index += 1
            soup = BeautifulSoup(request, 'lxml')
            input_tag = soup.find_all(HTML_LIST_TAG, class_=HTML_BOOK_CLASS)

            for url in input_tag:
                result_links.add(index, '{}{}'.format(DOMAIN_NAME_STRING,re.sub('^(../)+(..)/', '', url.find(A_TAG).get(HREF_TAG))))
                index += 1
                if limit and index >= limit:
                    quit_flag = True
                    return result_links
            if quit_flag:
                break


        return result_links

