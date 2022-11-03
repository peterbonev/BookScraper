"""
GENERAL PURPOSE CONSTANTS
"""
STARTING_PAGE = 1
FIRST_PAGE = 1
INCREASE_ONE = 1
DEFAULT_NUMBER_BOOKS_TO_SCRAPE = 10
FROM_START = 26
TO_END = -15
FROM_END = -10
MAX_VALUE = 100
MAX_URLS = 1000

VALIDATION_ARG_RANGE = ['price', 'rating', 'available']
"""
HTTP AND DOMAIN NAME SPECIFIC CONSTANTS
"""
CLIENT_ERROR_RESPONSE = 400
DEFAULT_SERVER_TIMEOUT = 3
PAGE_SUFFIX = '.html'
DOMAIN_NAME = 'http://books.toscrape.com/'
DOMAIN_URL_PREFIX = 'http://books.toscrape.com/catalogue/page-'
DOMAIN_NAME_STRING = 'http://books.toscrape.com/catalogue/'
HEADER_BOOK_TAG = 'h3'
A_TAG = 'a'
HREF_TAG = 'href'
HTML_TAG = 'html'
NEXT_TAG = 'next'
TAG_ = 'index.html'
HTML_BOOK_CLASS = 'col-xs-6 col-sm-4 col-md-3 col-lg-3'
HTML_LIST_TAG = 'li'
PAGER_TAG = 'pager'
DOMAIN_ALL_GENRES = "side_categories"
BOOK_TITLE_CLASS_NAME =  'active'
BOOK_PRICE_CLASS_NAME = 'price_color'
BOOK_PRODUCT_DESCRIPTION_ID_NAME = 'product_description'
BOOK_NUM_AVAILABILITY = 'instock availability'
BOOK_STAR_RATE = r"(?<=\bstar-rating\s)(\w+)"
NO_DESCRIPTION = 'No description'

HEADER_GET={'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Linux; {Android Version}', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate'}
