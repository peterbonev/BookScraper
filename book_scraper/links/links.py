class Links(object):
    """
    Interface class, that maintans transfer of the data between BookLinksParser and BookContentParser.
    Stores data(links to resources) as dictionary and could be used as key(ganres categories), values(links to them)
    """

    def __init__(self):
        self.__link_buffer = {}

    def add(self, key, value):
        self.__link_buffer[key] = value

    def content(self):
        return self.__link_buffer

    def reset(self):
        self.__link_buffer.clear()

    def __dict__(self):
        return self.__link_buffer
