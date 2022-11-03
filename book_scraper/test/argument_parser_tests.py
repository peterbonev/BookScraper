import unittest
from cli_input_arguments.cli_argument_parser_module.cli_argument_parser import CLIInputParser as ap


class ArgPars(unittest.TestCase):
    def setUp(self):
        self.parser = ap()

    def test_parse_instance(self):
        self.assertTrue(isinstance(self.parser, ap))

    def test_arg(self):
        self.parser = ['-b', '-g', '-s', 'sort_type', '-f', '-d', '-t', '-F', '-X']
        self.assertEqual(type(self.parser), list)

    def test_parse(self):
        result = str(self.parser.parse())
        expected_res = "Namespace(X=None, book_title=None, books=1000, file_info=None, filter=None, genres=None, " \
                       "keywords=None, sort=None, sort_type=None)"
        self.assertEqual(expected_res, result)


if __name__ == '__main__':
    unittest.main()
