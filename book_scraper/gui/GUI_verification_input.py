import tkMessageBox
from Tkconstants import END

from book_scraper.verified_input_data.verified_input_data import VerifiedInputData


class GUIInputVerificator(object):

    def __init__(self, books, genres, filter):
        self._books = books
        self._genres = genres
        self._filter = filter

    def verify(self, verified_data):
        """
            Verification of the GUI Inputs(from Entries) - positive integers
            param: VerifiedInputData object
        """
        if int(self._books.get()) > 0:
            verified_data.books = int(self._books.get())

        else:
            tkMessageBox.showinfo('Wrong Input Error', 'Wrong books value. Expected value positive int')
        verified_data.genres = self._genres.get(0, END)

        if int(self._filter[3].get()):
            if int(self._filter[2].get()) > 0:
                verified_data.filter = [self._filter[0].get(), '{}{}'.format(self._filter[1].get(), self._filter[2].get())]
            else:
                tkMessageBox.showinfo('Wrong Input Error', 'Wrong filter value. Expected value positive int')
