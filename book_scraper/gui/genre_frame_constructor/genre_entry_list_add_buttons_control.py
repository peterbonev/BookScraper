from Tkconstants import END


class GenresEntryListAddButtonsControl(object):

    def __init__(self, genres_list_from, genres_list_to):
        self.genres_list_const = genres_list_from
        self.genres_list_new = genres_list_to

    def _add_item_search_list_genres(self):
        selection = self.genres_list_const.curselection()
        if selection:
            self.genres_list_new.insert(self.genres_list_new.size(), self.genres_list_const.get(selection))
            self.genres_list_const.delete(selection)

    def _add_all_list_genres(self):
        self.genres_list_new.insert(0, *self.genres_list_const.get(0,END))
        self.genres_list_const.delete(0, END)




