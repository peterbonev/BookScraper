from book_scraper.gui.application import BookScraperApplication
from book_scraper.book_genre_parser.book_link_genre_parser import BookGenresParser
from book_scraper.cli_input_arguments.cli_input_arguments import InputArguments
from scraper import BooksScraper


class Manager():
    """
        Orchestration class of the application
    """
    def __init__(self):
        self._genres_parser = BookGenresParser()
        self._genres = self._genres_parser.genres().content().keys()
        self._from_input = InputArguments().get(self._genres)
        self.books = BooksScraper(self._from_input, self._genres_parser)

    
    def start(self):

        if self._from_input.run_gui:
            print(self._from_input.run_gui)
            BookScraperApplication().start(self._genres_parser)
        else:
            self.books.collect()