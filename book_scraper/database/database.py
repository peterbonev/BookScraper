class DataBase(object):
    _instance = None
    __data = {}
    key = "upc"

    def __new__(cls):
        if cls._instance is not None:
            return cls._instance
        _instance = super(DataBase, cls).__new__(cls)
        return _instance

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data[value[self.key]] = value

    def add_item(
        self,
        genre=None,
        title=None,
        price=None,
        rating=None,
        num_available=None,
        description=None,
        upc=None
    ):
        """
        Add new item to dict
        param: genre,
        param: title,
        param: price,
        param: rating,
        param: availability,
        param: num_available,
        param: description,
        param: UPC,
        param: reviews,
        """
        temp = {
            "title": title,
            "genre": genre,
            "price": price,
            "rating": rating,
            "available": num_available,
            "description": description,
            "upc": upc,
        }

        self.data[temp[self.key]] = temp

    def gen_iterate_through_database(self):
        """
        Generator for each item in database
        yield: item
        """
        for item in DataBase().data.values():
            yield item

    def reset(self):
        """
        Nullify database
        """
        self.__data = {}
