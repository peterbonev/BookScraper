from book_scraper.verified_input_data.verified_input_data import VerifiedInputData


class GUIInputDataSelector(object):
    def __init__(self, search, sort):
        self._search = search
        self._sort = sort

    def select(self, verified_data):
        """
        Selction of the GUI Inputs(from Entries) - only if checkboxes is on
        param: VerifiedInputData object
        """
        if int(self._search[0].get()):
            if int(self._search[1].get() == 0):
                verified_data.keywords = self._search[2].get("1.0", "end-1c")
            else:
                verified_data.book_title = self._search[3].get("1.0", "end-1c")

        if int(self._sort[0].get()):
            verified_data.sort = self._sort[1].get()
            verified_data.sort_type = self._sort[2].get()
