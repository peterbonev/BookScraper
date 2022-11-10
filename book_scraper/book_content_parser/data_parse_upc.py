class DataParseUPC(object):
    def __init__(self):
        pass

    def upc(self, html_raw=None):
        """
        Scrape UPC of the book
        :param html_raw: Beautiful Soup 4 object (bsObj type)
        :return: UPC of the book, data type: unicode
        """
        return html_raw.find("table", class_="table table-striped").find("td").getText()
