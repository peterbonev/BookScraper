from Tkconstants import W
from Tkinter import Label


class BookScraperApplicationBooksLabel(object):
    def __init__(self):
        self.__frame = None

    def _label(self, frame):
        """ """
        self.__frame = frame
        self._label_books = Label(
            self.__frame, text="Amount of books to select in search: "
        )
        self._label_books.grid(row=1, column=0, ipadx=50, sticky=W)
