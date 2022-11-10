from Tkconstants import VERTICAL
from Tkinter import Scrollbar, Listbox


class BookScraperApplicationGenresEntryList(object):
    def __init__(self):
        self.__label_frame_genres = None
        self.__dest_list_genres = None

    def _dest_list(self, frame):
        self.__label_frame_genres = frame

        self.__scrollbar_new_list = Scrollbar(
            self.__label_frame_genres, orient=VERTICAL
        )
        self.__genres_list_new = Listbox(self.__label_frame_genres, yscrollcommand=self.__scrollbar_new_list.set)
        self.__scrollbar_new_list.config(command=self.__genres_list_new.yview)
        self.__scrollbar_new_list.grid(row=3, column=4, ipadx=1, ipady=75)
        self.__genres_list_new.grid(row=3, column=3, padx=5, pady=5, ipadx=20)

        return self.__genres_list_new
