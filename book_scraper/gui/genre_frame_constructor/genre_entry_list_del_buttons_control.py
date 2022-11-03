from Tkconstants import END


class GenresEntryListDelButtonsControl(object):

    def __init__(self, genres_list_from, genres_list_to):
        self.genres_list_const = genres_list_from
        self.genres_list_new = genres_list_to

    def _del_item_list_genres(self):
        selection = self.genres_list_new.curselection()
        if selection:
            self.genres_list_const.insert(self.genres_list_new.size(), self.genres_list_new.get(selection))
            self.genres_list_new.delete(selection)

    def _del_all_list_genres(self):
        self.genres_list_const.insert(0, *self.genres_list_new.get(0, END))
        self.genres_list_new.delete(0, END)

