import unittest
import StringIO
import sys
from create_read_json.read_json import ReadJson


class ReadJTest(unittest.TestCase):
    def setUp(self):
        self.read = ReadJson()

    def test_init(self):
        self.assertIsInstance(self.read, ReadJson)

    def test_check_title(self):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        self.read.check_title_json_file(['Objects', 'e00eb4fd7b871a48', 'description'], 'list_of_items.json')
        expected_res = "{u'available': 10, u'rating': 1, u'description': u'description', u'title': u'Objects', u'price': 40.0, u'upc': u'e00eb4fd7b871a48', u'genre': u'smt'}\n"
        result = captured_output.getvalue()
        self.assertEqual(expected_res, result)


if __name__ == '__main__':
    unittest.main()
