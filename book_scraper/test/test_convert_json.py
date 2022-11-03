import re
import unittest

from create_read_json.convert_json import ConvertToJson


class ConvJTest(unittest.TestCase):
    def setUp(self):
        self.conv = ConvertToJson()

    def test_init(self):
        self.assertIsInstance(self.conv, ConvertToJson)

    def test_convert(self):
        items = [{'upc': 'e00eb4fd7b871a48',
                  'available': 10,
                  'rating': 1,
                  'description': 'description',
                  'title': 'Objects',
                  'genre': 'smt',
                  'price': 40.0}]
        expected_result = '[{"available":10,"rating":1,"description":"description","title":"Objects","price":40.0,"upc":"e00eb4fd7b871a48","genre":"smt"}]'
        self.conv.convert(items)
        tmplist = []
        with open('list_of_items.json', 'r') as source:
            tmp = source.read()
            tmplist.append(tmp)
        result = ''.join(tmplist)
        result = re.sub(r'\s+', '', result)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
