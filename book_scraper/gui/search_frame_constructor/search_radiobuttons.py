from Tkconstants import W
from Tkinter import IntVar, Radiobutton, Text


class BookScraperApplicationSearchRadiobuttons(object):
    def _radiobuttons(self, frame):
        """
        Search dialog radiobuttons and Text boxes
        """
        option_keyword_title = IntVar()
        self.keywords_radio = Radiobutton(
            frame, text="Keywords", variable=option_keyword_title, value=0
        )
        self.keywords_radio.grid(row=8, column=0, sticky=W)
        self.keywords_text = Text(frame, width=35, height=3)
        self.keywords_text.grid(row=9, column=0, padx=5)

        self.titles_radio = Radiobutton(
            frame, text="Titles", variable=option_keyword_title, value=1
        )
        self.titles_radio.grid(row=8, column=1, sticky=W)
        self.titles_text = Text(frame, width=35, height=3)
        self.titles_text.grid(row=9, column=1, padx=5, pady=5)

        return option_keyword_title, self.keywords_text, self.titles_text
