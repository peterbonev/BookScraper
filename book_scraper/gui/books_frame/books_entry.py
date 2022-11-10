import tkMessageBox
from Tkinter import Entry, IntVar
from tkMessageBox import *


class BookScraperApplicationBooksEntry(object):
    def __init__(self):
        self.__frame = None

    def _entry(self, frame):
        """
        Entry frame for the number of books(GUI input)
        return: Entry object
        """
        self.__frame = frame

        return_value = IntVar(value=1)
        self._entry_books = Entry(self.__frame, width=3, textvariable=return_value)
        self._entry_books.grid(row=1, column=1, rowspan=3, ipadx=10)

        return return_value
