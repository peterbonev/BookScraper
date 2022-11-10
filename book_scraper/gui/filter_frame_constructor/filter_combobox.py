import ttk
from Tkinter import StringVar, OptionMenu, Entry, IntVar


class BookScraperApplicationExclusionFilterCombobox(object):
    def __init__(self):
        self._frame = None

    def _combo(self, frame):
        """
        Comparator dialog for filter exclusion category range
        """
        self._frame = frame
        self.clicked_sign_list = StringVar(value=">")
        self._drop_sign_options = [">", "<", "="]

        self._drop_sign_options = ttk.Combobox(
            self._frame, value=self._drop_sign_options
        )  # OptionMenu(self._frame, self.clicked_sign_list,
        # *self._drop_sign_options)
        self._drop_sign_options.current(0)
        self._drop_sign_options.grid(row=5, column=2, padx=5, pady=5, ipadx=15, ipady=5)
        value = IntVar()
        self._entry_filters = Entry(self._frame, width=5, textvariable=value)
        self._entry_filters.grid(row=5, column=3, padx=5, ipady=4)

        return self._drop_sign_options, value
