class VerifiedInputData(object):
    """
    Interface class, stores and transfers verified data from CLI to the BookLinksParser
    """

    def __init__(
        self,
        books=None,
        genres=None,
        filter=None,
        keywords=None,
        book_title=None,
        sort=None,
        sort_type=None,
        file_info=None,
        X=None,
    ):
        self.books = books
        self.genres = genres
        self.filter = filter
        self.keywords = keywords
        self.book_title = book_title
        self.sort = sort
        self.sort_type = sort_type
        self.file_info = file_info
        self.run_gui = X

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}".format(
            self.books,
            self.genres,
            self.filter,
            self.keywords,
            self.book_title,
            self.sort,
            self.sort_type,
            self.run_gui,
        )
