from Tkinter import LabelFrame


class BookScraperApplicationGenresFrame(object):

    # def __init__(self):
    #     self._frame = None

    def _frame(self, frame):

        self.__label_frame_genres = LabelFrame(frame, text="Genres")
        self.__label_frame_genres.grid(row=2, column=0, padx=5, pady=5, ipadx=7)

        return self.__label_frame_genres
