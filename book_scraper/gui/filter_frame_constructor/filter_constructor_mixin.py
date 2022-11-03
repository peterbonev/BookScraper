from filter_args import BookScraperApplicationExclusionFilterFirstArg
from filter_combobox import BookScraperApplicationExclusionFilterCombobox
from filter_frame import BookScraperApplicationExclusionFilterFrame


class BookScraperApplicationExclusionFiltersMixin(BookScraperApplicationExclusionFilterCombobox,
                                                  BookScraperApplicationExclusionFilterFrame,
                                                  BookScraperApplicationExclusionFilterFirstArg):

    def construct(self, frame):
        """
            Main method of mixin constructor class of Exclusion Filters Dialog(as builder of exclusion filters GUI dialog,
             from following prpducts: frame, categories as ['price', 'rating', 'available'] and [">", "<", "="]
             and input number
             If checkbox is checked arguments will be taken as valid input, otherwise they will be discarded
        """
        main_frame, state = self._filter_frame(frame)
        result_categories = self._args(main_frame)
        limit, value = self._combo(main_frame)

        return result_categories, limit, value, state



