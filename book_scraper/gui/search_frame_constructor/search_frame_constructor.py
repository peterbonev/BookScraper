from search_checkbutton import BookScraperApplicationSearchFrameCheckbutton
from search_frame import BookScraperApplicationSearchFrame
from search_radiobuttons import BookScraperApplicationSearchRadiobuttons


class BookScraperApplicationSearchFrameMixin(
    BookScraperApplicationSearchFrame,
    BookScraperApplicationSearchFrameCheckbutton,
    BookScraperApplicationSearchRadiobuttons,
):
    def construct(self, frame):
        """
        Main method of mixin constructor class of Search Dialog (as builder of search GUI dialog, from following parts:
        frame, check button, radiobuttons and text boxes.
        If checkbox is checked arguments will be taken as valid input, otherwise they will be discarded
        """
        frame = self._frame(frame)
        selection = self._checkbutton(frame)
        option_keyword_title, keywords_text, titles_text = self._radiobuttons(frame)

        return selection, option_keyword_title, keywords_text, titles_text
