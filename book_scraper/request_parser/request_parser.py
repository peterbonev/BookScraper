import grequests
import requests

from book_scraper.request_parser.request_parser_defines import (
    DEFAULT_SERVER_TIMEOUT,
    HEADER_GET,
)


class RequestsParser(object):
    """
    Request-response parser class. Pass payload, if Server response = 200OK
    """

    def __init__(self, url):
        self._response_code = 0
        self._response_data = self.__action(url)

    @staticmethod
    def __request_server_sync(page_url):
        """
            Safely returns data content from input URL, as result of GET request to HTTP Server
        :param page_url: input URL, as string
        :return: parsed HTML data from GET Request response payload
        """
        try:
            response = requests.get(
                page_url, headers=HEADER_GET, timeout=DEFAULT_SERVER_TIMEOUT
            )
            response.raise_for_status()
        except:
            raise ValueError("Invalid URL")
        response.close()
        return response

    @staticmethod
    def __request_server_async(list_url):
        """
             Safely returns data content from input list of URLs, as result of multiple GET requests to HTTP Server
        :param list_url: List of URLs to resolve
        :return: Map with the valid received content
        """
        server_response = (grequests.get(url) for url in list_url)
        try:
            map_url = grequests.map(server_response, size=10, exception_handler=True)
        except:
            raise ValueError("Invalid URL")

        return [url.content for url in map_url if url]

    def content(self):
        """
            Getter for parsed content from server responses
        :return: HTML data
        """
        return self._response_data

    def __action(self, item):
        """
            Setter for content, based on variative behaviour - a single request will be resolved synchronously,
            (requests.get) and list of URLs will be resolved asynchronously (grequests.get)
        :param item: single or list URLS
        :return: Function object
        """
        if isinstance(item, str):
            return self.__request_server_sync(item)
        elif isinstance(item, list):
            return self.__request_server_async(item)

    def __str__(self):
        return ", ".join(self._response_data)
