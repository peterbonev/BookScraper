from Tkinter import Frame, Button

from genre_entry_list_add_buttons_control import \
    GenresEntryListAddButtonsControl


class BookScraperApplicationGenresAddButtons(object):

    def __init__(self):

        super(BookScraperApplicationGenresAddButtons, self).__init__()
        self.__label_frame_genres = None
        self.genres_list_const = None
        self.genres_list_new = None

    def _add_control(self, frame, genres_list_from, genres_list_to):
        self.__label_frame_genres = frame
        self.genres_list_const = genres_list_from
        self.genres_list_new = genres_list_to

        single_add_control_functions = GenresEntryListAddButtonsControl(self.genres_list_const, self.genres_list_new).\
            _add_item_search_list_genres
        all_add_control_functions = GenresEntryListAddButtonsControl(self.genres_list_const, self.genres_list_new). \
            _add_all_list_genres
        self.__select_genre_buttons = Frame(self.__label_frame_genres)
        self.__select_genre_buttons.grid(row=3, column=2, padx=5, pady=5)
        self.select_genre_button_add = Button(self.__select_genre_buttons, text="ADD",
                                              command=single_add_control_functions)
        self.select_genre_button_add.grid(padx=3, ipadx=13)
        self.select_genre_button_add = Button(self.__select_genre_buttons, text="ADD ALL",
                                              command=all_add_control_functions)
        self.select_genre_button_add.grid(padx=1)

        return self.__select_genre_buttons