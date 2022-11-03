# coding=utf-8
import unittest

from request_par_content_example import expected_res_async, expected_content_str
from request_parser.request_parser import RequestsParser as rp


class RequestParserTest(unittest.TestCase):
    def setUp(self):
        self.single_url = 'http://books.toscrape.com/catalogue/private-paris-private-10_958/index.html'
        self.list_url = ['http://books.toscrape.com/catalogue/private-paris-private-10_958/index.html',
                         'http://books.toscrape.com/catalogue/the-three-searches-meaning-and-the-story_649/index.html',
                         'http://books.toscrape.com/catalogue/the-art-of-not-breathing_58/index.html']
        self.single_url_broken = 'http://books.toscrape.com/catalogue/private-paris-pri-10_958/index.html'
        self.list_url_broken = ['hp://books.toscape.com/catalogue/private-paris-private-10_958/index.html',
                         'http://books.toscrape.com/catalogue/the-three-searches-meaning-and-the-story_6dex.html',
                         'http://books.toscrape.com/cataloue/the-art-of-not-breathing_58/index.html']
        self.sing_req_par = rp(self.single_url)
        self.multi_req_par = rp(self.list_url)

    def test_content_response(self):
        expected_res = '<Response [200]>'
        self.assertEqual(expected_res, str(self.sing_req_par.content()))

    def test_async_requests_return_type(self):
        self.assertEqual(list, type(self.multi_req_par.content()))

    def test_async_requests(self):
        self.assertEqual(expected_res_async, self.multi_req_par.content())

    def test_action_decision(self):
        self.assertEqual(type(self.multi_req_par.content()), list)

    def test_exceptions_sync_requests(self):
        with self.assertRaises(Exception) as context:
            rp(self.single_url_broken)
        self.assertTrue('Invalid URL' in context.exception)

    def test_exceptions_async_requests(self):
        with self.assertRaises(Exception) as context:
            rp(self.list_url_broken)
        self.assertTrue('Invalid URL' in context.exception)

    def test_str_method_pars(self):
        result = self.sing_req_par.__str__(), 'html.parser'
        self.assertEqual(result, expected_content_str)


if __name__ == '__main__':
    unittest.main()

