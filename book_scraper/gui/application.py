from Tkinter import *
from book_scraper.gui.top_frame import BookScraperApplicationBaseFrame


class BookScraperApplication(object):
    """
    Management class of GUI
    """

    def __init__(self):
        self.window = Tk()
        self.window.wm_title("Book scraper v. 0.1")
        self.window.geometry("640x680")
        self.window.resizable(False, False)
        self._result = None

    def start(self, genres):
        BookScraperApplicationBaseFrame(self._result).construct(self.window, genres)
        self.window.mainloop()
