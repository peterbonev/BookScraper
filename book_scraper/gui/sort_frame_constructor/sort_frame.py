from Tkinter import LabelFrame, Checkbutton, IntVar
import ttk
from Tkconstants import W


class BookScraperApplicationSortFrame(object):

    def __init__(self):
        self.__frame = None

    def construct(self, frame):
        """
         Main method of constructor class of Sort Dialog(as builder of
         sort GUI dialog
         If checkbox is checked arguments will be taken as valid input, otherwise they will be discarded
        """
        self.__frame = frame
        self.sort_frame = LabelFrame(self.__frame, text="Sort")
        self.sort_frame.grid(row=9, column=0, padx=5, pady=5, sticky=W)

        selection = IntVar(value=0)
        self.sort_frame_check_box = Checkbutton(self.sort_frame, variable=selection)
        self.sort_frame_check_box.grid(row=10, column=0, ipadx=5)
        self._sort_options = ["Rating", "Price", "Available"]
        self._drop_filters_options = ttk.Combobox(self.sort_frame, value=self._sort_options)
        self._drop_filters_options.current(0)
        self._drop_filters_options.grid(row=10, column=1, padx=5, pady=5, ipadx=15, sticky=W)

        self._sort_type = ["ascending", "descending"]
        self._drop_filters = ttk.Combobox(self.sort_frame, value=self._sort_type)
        self._drop_filters.grid(row=10, column=2, padx=5, pady=5, ipadx=15, sticky=W)
        self._drop_filters.current(0)

        return selection, self._drop_filters_options, self._drop_filters
