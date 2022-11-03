# Book Scraper Tool

* ## Project Summary
*A tool to collect the book data asynchronously from a bookstore website, then to sort this data based on given 
keys, dedicated to http://books.toscrape.com/. Used and developped technologies are aplicable for scrapping to most conteporary websites with certain updates*

* ## Requirements
Python 2.7+ (This script is written for Python 2.7, but could be run on all newer versions of Python)*

*Packages used:*

*bs4 BeautifulSoup 4.9.3- (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)*

*grequests - (requests + gevent, including urllib3 - https://github.com/spyoungtech/grequests)*

* ### All packages should be installed for the proper Python version
* 
* ## Usage

*The script is used to gather data from http://books.toscrape.com/.
You can write the following command in your terminal:

 -b - number of books (as -b 50 - 50 books will be scraped from the site). If option will be used must provide a positive intefer, as number of books

 -g - list of genres to search through (-g Scence, Travel - books from those genres will be scraped)

 -s - list of sortings (provide sort of the output, ascending or descending). The default order is descending

 -f - list of priority filters for which books to exclude from the scrape ( -f rating ">2" will be excluded from scrape all books with rating higher of 2 stars). Input string with format "criteria" "ComparatorNumber" will be accepted

 -d - list of keywords to be searched from the description (-d genre, book, etc). Only existing genre categories will be allowed

 -t - title of a book to search for (-t Whole-book-title)

 -F - list of book titles to search for (from given json) (-F name-of-file)
 
 -X - to start app with GUI


* ## Technical Details

*To get data from http://books.toscrape.com/, the script uses class RequestHandler,
which uses request response functions from urlparse package.RequestsHandler is used by the
LinkParser class to obtain each page URL.LinkParser is used by BookLinkParser class
to obtain each book URL, traversing through every page URL.The books URLs are then used to extract the
data for the books title, price, in stock availability, description, star rating and genre. 
A full list of the genres is obtained from the main page URL by search in 'div', class_="side_categories"
All the books ing\formation is stored in DataBase class in a dictionary format*

  
### Workflow:

*When and how is an input and output expected? When and how is data transfered or saved? When and how are any alghoritms used?*

The script works from command-line interface and has a graphic user interface also. The default interface is a command-line interface
The script can be run with options to scrape a selecton(as mentioned the above). If no option argument is given, script will scrape all books.
Starting from command-line interface
1. You can start the script with one or more of the options, already descriped)
2. Once the script is started, BookGenreParser module will push the RequestParser(communication module with web-server, working synchronously, if only one URL is provided or asynchronously, with list of URLs) to get all genres(as category) from the site. 
3. CLI_input_verificator module will check, if input parameters meet following requirements:
 - number of books - positive integer
 - genre of book - if this genre or selection of genres are existing ones in the site
 - exclusion filter - books, could be excluded upon rating, price and availability. No other options will be allowed
3. Once the input will be verified, the script will works, as follow:
4. With no prompt script accesses http://books.toscrape.com/ and scrape all links of every book's internal page, through genre categories(if provided) or through the main DOM tree, by BoolLinkParser module. The module passes output, through Links container (as links) to the next module BookContentParser
5. BookContentParser module will scrape all info (through the RequestParser to get the HTML content of every book's page) of every book in book name(as string), genre(as string), price(as float), availabitlity(as integer), rating(as integer), description(as unicode string) and UPC(as string). BookContentParser module, will check if exclusion filter (-f option) is provided and will discard all books upon given range. Once the information is get, BookContentParser push it to Content object(an interface between BookContentParser and Database module). 
6. Content, transfer all scraped data into the Database
7. Database organizes it as main dictionary(UPC of the book is the key), containing dictionaries for book's title, genre, price, rating, available number of books and description.
8. If search filter is set (-d words_to_search), Items modelude will access Database and the following algorithm will be performed: after the request Database will generate content from the values of the main dictionary and will be passed to the Item module(as return value of the Database internal method). Items will perform a search into the given selection into the 'description' for one or more keywords. All the selected books will be printed as output in the console.
9. If sort is selected the scraped and filtered books will be presented (print into the console) sorted in selected order ascending/descending. If no order is chosen ascending order is default. If no sort option is provided, the selection of books will be presented in sorted ascending order by book's title
10. The output will be presented in json-format style for visibility.
11. If -X is chosen, all other options (if given) will be discarded and GUI (graphic user interface) will be run
12. The same steps will be performed in book scraping process, through the GUI - the input will be verified only for the entry options, so only positive integers will be accepted for numbers. Text or string inputs for keywords and titles to search will be taken as is. All other options are pre-set by comboboxes or list.
13. Once the input is given, BookLinkParser will be requested, BookLinkParser will push the RequestParser - links of the books will be scraped. Through Links object will be passed to BookContentParser. BookContentParser will push RequestParser and raw HTML data for every book's page will be scraped. BookContentPaerser will select the needed information, by category and through Content, will be stored into the Database module. Through the Items module will be performed search and sort of the scraped information.
14. All selected information will be presented into the console (as output)

