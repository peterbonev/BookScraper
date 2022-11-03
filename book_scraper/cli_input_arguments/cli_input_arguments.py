from book_scraper.cli_input_arguments.cli_argument_parser_module.cli_argument_parser import CLIInputParser
from book_scraper.cli_input_arguments.cli_input_verificator.cli_input_verificatior import CLIInputVerificatior
from book_scraper.verified_input_data.verified_input_data import VerifiedInputData


class InputArguments(CLIInputVerificatior):
    """
        Class, for verification of input data from CLI, according ceratin constraints
    """

    def __init__(self):
        self.__parser = CLIInputParser()

    def get(self, genres_const):
        """"
            Main method of getting parsed and verified data from CLI
        """
        verified_input = VerifiedInputData()
        if self.__parser.parse().genres:
            verified_input.genres = self._verify_genres(self.__parser.parse().genres, genres_const)
        if self.__parser.parse().filter:
            verified_input.filter = self._verify_filters(self.__parser.parse().filter)
        if self.__parser.parse().books:
            verified_input.books = self._verify_books(self.__parser.parse().books)
        verified_input.keywords = self.__parser.parse().keywords
        verified_input.book_title = self.__parser.parse().book_title
        verified_input.file_info = self.__parser.parse().file_info
        verified_input.run_gui = self.__parser.parse().X

        return verified_input

#
# c=InputArguments()
# c.input()

