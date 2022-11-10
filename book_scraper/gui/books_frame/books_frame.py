from Tkinter import LabelFrame


class BookScraperApplicationBooksFrame(object):
    def __init__(self):
        self.__frame = None

    def _frame(self, frame):
        """
        Frame object of the book's input
        """
        self.__frame = frame
        self.label_frame_books = LabelFrame(self.__frame, text="BooksScraper")
        self.label_frame_books.grid(padx=10, pady=5, ipadx=100, ipady=5)

        return self.label_frame_books
