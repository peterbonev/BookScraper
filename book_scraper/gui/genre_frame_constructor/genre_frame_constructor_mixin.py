from genre_add_buttons import BookScraperApplicationGenresAddButtons
from genre_del_buttons import BookScraperApplicationGenresDelButtons
from genre_entry_list import BookScraperApplicationGenresEntryList
from genre_frame import BookScraperApplicationGenresFrame
from genre_primary_list import BookScraperApplicationGenresPriamryList


class BookScraperApplicationGenreFrameConstructorMixin(BookScraperApplicationGenresFrame,
                                 BookScraperApplicationGenresPriamryList,
                                 BookScraperApplicationGenresEntryList,
                                 BookScraperApplicationGenresAddButtons,
                                BookScraperApplicationGenresDelButtons):

    def construct(self, frame):
        """
            Main method of mixin constructor class of Genres Dialog(as builder of genres GUI dialog,
            from following products: frame, entry list with all genres, dynamically taken from site,
            input list of the chosen genres, controll buttons to add single genre or all genres and delete buttons =
            for single and all genres

        """
        self._top = self._frame(frame)
        list_from = self._src_list(self._top)
        list_to = self._dest_list(self._top)
        button_frame = self._add_control(self._top, list_from, list_to)
        self._del_control(button_frame, list_from, list_to)

        return list_to
