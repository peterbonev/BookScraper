import argparse

from book_scraper.cli_input_arguments.cli_input_verificator.cli_input_defines import (
    VALIDATION_ARG_RANGE,
)
from cli_input_defines import VALIDATION_SIGN_RANGE


class CLIInputVerificatior(object):
    def _verify_books(self, books):
        """
        Verify, if the books number is always positive number
        """
        if books <= 0:
            message = "Expected positive integer, got value = {}".format(books)
            raise argparse.ArgumentTypeError(message)

        return books

    def _verify_filters(self, filters):
        """
        Verify the content and format of the exclusion filter's input, in order to receive multiple values as a list
        """

        if len(filters) % 2:
            message = "Expected input in {}, got value = {}".format(
                VALIDATION_ARG_RANGE, filters
            )
            raise argparse.ArgumentTypeError(message)
        for filter_index in range(0, len(filters), 2):
            if (filter_index & 1) and (
                filters[filter_index] not in VALIDATION_ARG_RANGE
            ):
                message = "Expected input in {}, got value = {}".format(
                    VALIDATION_ARG_RANGE, not (filter_index & 1)
                )
                raise argparse.ArgumentTypeError(message)
            if (
                not (filter_index & 1)
                and (filters[filter_index + 1][0] not in VALIDATION_SIGN_RANGE)
                and ord(filters[filter_index + 1][1])
            ):
                message = "Expected input in {}, got value = {}".format(
                    VALIDATION_SIGN_RANGE, filters[filter_index + 1][1]
                )
                raise argparse.ArgumentTypeError(message)

        return filters

    def _verify_genres(self, genres, list_genres):
        """
        Verify, whether the input genres are existing ones (parses from sites genre lists, given in list_genres)
        """
        for genre in genres:
            if genre not in list_genres:
                message = "Expected input in {}, got value = {}".format(
                    list_genres, genre
                )
                raise argparse.ArgumentTypeError(message)

        return genres
