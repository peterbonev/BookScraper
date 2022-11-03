from Tkconstants import W
from Tkinter import Checkbutton, IntVar


class BookScraperApplicationSearchFrameCheckbutton(object):

    def _checkbutton(self, frame):
        """
           Search dialog checkbutton
        """
        selection = IntVar(value=0)
        self__option = Checkbutton(frame, text="Search", variable=selection)
        self__option.grid(row=7, column=0, sticky=W)

        return selection