import unittest
from links.links import Links


class LinksTests(unittest.TestCase):
    def setUp(self):
        self.linksb = Links()
        self.linksb.add('Travel', 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html')
        self.expected_res = {'Travel': 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'}

    def test_init(self):
        self.assertIsInstance(self.linksb, Links)

    def test_add_content(self):
        self.assertEqual(self.expected_res, self.linksb.content())

    def test_reset(self):
        self.linksb.reset()
        self.assertEqual({}, self.linksb.content())

    def test_dict(self):
        self.assertEqual(self.expected_res, self.linksb.__dict__())


if __name__ == '__main__':
    unittest.main()
 