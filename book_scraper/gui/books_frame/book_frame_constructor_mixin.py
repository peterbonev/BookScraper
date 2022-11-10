from books_entry import BookScraperApplicationBooksEntry
from books_frame import BookScraperApplicationBooksFrame
from books_label import BookScraperApplicationBooksLabel


class BookScraperApplicationBooksFrameMixin(
    BookScraperApplicationBooksEntry,
    BookScraperApplicationBooksFrame,
    BookScraperApplicationBooksLabel,
):
    def construct(self, frame):
        """
        Main method of mixin constructor class of BooksScraper Input Frame(as builder of books GUI dialog, from following prpducts:
        frame, entry and label objects
        """
        self.__frame = self._frame(frame)
        result = self._entry(self.__frame)
        self._label(self.__frame)

        return result
