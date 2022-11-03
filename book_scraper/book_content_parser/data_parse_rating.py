

class DataParseRating(object):

    def __init__(self):
        pass

    def rating(self, html_raw=None):
        """
        Scrape rating of the book
        :param html_raw: Beautiful Soup 4 object (bsObj type)
        :return: Rating of the book, data type: int
        """
        rating = 0
        if html_raw.find('div', class_='col-sm-6 product_main').find("p", class_="star-rating One"):
            rating = 1
        elif html_raw.find('div', class_='col-sm-6 product_main').find("p", class_="star-rating Two"):
            rating = 2
        elif html_raw.find('div', class_='col-sm-6 product_main').find("p", class_="star-rating Three"):
            rating = 3
        elif html_raw.find('div', class_='col-sm-6 product_main').find("p", class_="star-rating Four"):
            rating = 4
        elif html_raw.find('div', class_='col-sm-6 product_main').find("p", class_="star-rating Five"):
            rating = 5

        return rating