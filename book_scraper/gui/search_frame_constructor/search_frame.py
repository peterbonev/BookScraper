from Tkinter import LabelFrame


class BookScraperApplicationSearchFrame(object):

    def _frame(self, frame):
        """
            Search dialog frame
        """
        self.__keywords_frame = LabelFrame(frame, text="Search by criteria", padx=5, pady=5)
        self.__keywords_frame.grid(row=6, column=0)

        return self.__keywords_frame
