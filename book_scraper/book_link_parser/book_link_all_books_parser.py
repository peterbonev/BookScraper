from bs4 import BeautifulSoup

from book_scraper.book_link_parser.book_link_parser_defines import A_TAG, HREF_TAG, HTML_LIST_TAG, DOMAIN_URL_PREFIX, \
    PAGE_SUFFIX, MAX_VALUE, HTML_BOOK_CLASS, DOMAIN_NAME_STRING

from book_scraper.request_parser.request_parser import RequestsParser
from book_scraper.links.links import Links

class BookLinkAllBooksParser(object):
    """
       Link parsing class for all books in site
    """
    def _parse_all_urls(self, target_amount = None):
        """
        Parse all books' URLs from the given site
        :return: All books URL, parsed from the site, data type: list od str
        """
        all_links = Links()
        generate_url_guess_list = ['{}{}{}'.format(DOMAIN_URL_PREFIX,index,PAGE_SUFFIX) for index in range(1,MAX_VALUE)]
        requests = RequestsParser(generate_url_guess_list)
        if len(requests.content()) == MAX_VALUE:
            generate_url_guess_list = ['{}{}{}'.format(DOMAIN_URL_PREFIX, index, PAGE_SUFFIX) for index in
                                       range(1, MAX_VALUE * 2)]
            requests = RequestsParser(generate_url_guess_list)
        index = 0
        for request in requests.content():
            index += 1
            soup = BeautifulSoup(request, 'lxml')
            input_tag = soup.find_all(HTML_LIST_TAG, class_=HTML_BOOK_CLASS)
            quit_flag = False

            for url in input_tag:
                all_links.add(index,'{}{}'.format(DOMAIN_NAME_STRING,url.find(A_TAG).get(HREF_TAG)))
                index += 1
                if target_amount:
                    if len(all_links.content()) >= target_amount:
                        quit_flag = True
                        break
            if quit_flag:
                break

        return all_links


