from Tkconstants import W
from Tkinter import LabelFrame, Checkbutton, IntVar


class BookScraperApplicationExclusionFilterFrame(object):
    def __init__(self):
        self._frame = None

    def _filter_frame(self, main_frame):
        """
        Frame of exclusion filter dialog
        """
        self.__frame = main_frame
        self.label_frame_exc_filter = LabelFrame(
            self.__frame, text="Exclusion filter", padx=5, pady=5
        )
        self.label_frame_exc_filter.grid(row=4, column=0, ipadx=26)

        state = IntVar(value=0)
        self.keywords_frame_check_box = Checkbutton(
            self.label_frame_exc_filter, variable=state
        )
        self.keywords_frame_check_box.grid(
            row=5, column=0, ipadx=10, ipady=10, sticky=W
        )

        return self.label_frame_exc_filter, state
