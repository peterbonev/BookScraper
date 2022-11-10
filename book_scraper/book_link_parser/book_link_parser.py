from book_scraper.book_link_parser.book_link_all_books_parser import (
    BookLinkAllBooksParser,
)
from book_scraper.links.links import Links


class BookLinkParser(object):
    """
    Class, parses links of books from given genre or list of genres of the site and could be limited to certain number
    """

    def __init__(self, genres_object_instance):
        self.__genre_parser = genres_object_instance
        self.__book_parser = BookLinkAllBooksParser()
        self._genres = self.__genre_parser.genres()

    def collect(self, list_genres=None, num_books=None):
        """
        Method for collecting book links
        param:list_genres (could be all genres)
        param: num_books - limit of books to search
        """
        result = Links()
        if (num_books and not list_genres) or (
            len(list_genres) == len(self.__genre_parser._parse_genres().content())
        ):
            result = self.__book_parser._parse_all_urls(num_books)
        else:
            result = self.__genre_parser._parse_by_genre(
                list_genres, self.__genre_parser._parse_genres(), num_books
            )

        return result
