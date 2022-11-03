

class DataParseGenre(object):

    def __init__(self):
        pass

    def genre(self, html_raw=None):
        """
        Scrape ganre of book
        :param html_raw: Beautiful Soup 4 object (bsObj type)
        :return: Genre of the book, data type: unicode
        """

        return html_raw.find("li").findNext(class_='active').findPrevious('a', href=True).getText()