import ttk
from Tkinter import StringVar


class BookScraperApplicationExclusionFilterFirstArg(object):

    def __init__(self):
        self._frame = None

    def _args(self, frame):
        self._frame = frame
        self.clicked_filter_list = StringVar(value='Rating')
        self._drop_filters_options = ["Rating", "Price", "Available"]

        self._drop_filters = ttk.Combobox(self._frame, value=self._drop_filters_options)
        self._drop_filters.grid(row=5, column=1, columnspan=1, padx=5, pady=5, ipadx=15, ipady=5)
        self._drop_filters.current(0)

        return self._drop_filters