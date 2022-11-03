from book_content_parser_defines import MAX_VALUE, VALIDATION_ARG_RANGE


class BookDataParserFilter(object):
    @staticmethod
    def _exclude(value, book=None):
        """
            Exclude, from scraping books, according specific criteria. Multiple criteria could be applied
        :param value: tuple or list with tuples with criteria to be excluded
        :param book: Values of all book's info
        :return: True/False (True=to be excluded; False=in criteria)
        """
        min_limit = 0
        max_limit = 0
        number_limit = 0

        for i in range(0, len(value), 2):
            if value[i] == 'rating':
                number_limit = 6
            else:
                number_limit = MAX_VALUE

            if value[i] in VALIDATION_ARG_RANGE:
                sign, number = value[i + 1][0], int(value[i + 1][1:])
                if sign == '>':
                    min_limit, max_limit = number - 1, number_limit
                elif sign == '<':
                    min_limit, max_limit = 0, number + 1
                elif sign == '=':
                    min_limit, max_limit = number - 1, number + 1
                if min_limit < book[value[i]] < max_limit:
                    return True
                else:
                    continue
            else:
                break
        return False

