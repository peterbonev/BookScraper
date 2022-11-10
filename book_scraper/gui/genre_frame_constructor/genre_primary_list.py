from Tkconstants import VERTICAL
from Tkinter import Scrollbar, Listbox


class BookScraperApplicationGenresPriamryList(object):
    def __init__(self, genres):
        self.__label_frame_genres = None
        self.__genres = genres

    def _src_list(self, frame):
        self.__label_frame_genres = frame

        self.__scrollbar_const_list = Scrollbar(
            self.__label_frame_genres, orient=VERTICAL
        )
        self.__genres_list_const = Listbox(
            self.__label_frame_genres, yscrollcommand=self.__scrollbar_const_list.set
        )
        self.__genres_list_const.insert(0, *self.__genres)
        self.__genres_list_const.grid(
            row=3, column=0, padx=10, pady=10, ipadx=20, ipady=5
        )
        self.__scrollbar_const_list.config(command=self.__genres_list_const.yview)
        self.__scrollbar_const_list.grid(row=3, column=1, ipadx=1, ipady=75)

        return self.__genres_list_const
