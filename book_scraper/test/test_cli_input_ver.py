import argparse
import unittest
from cli_input_arguments.cli_input_verificator.cli_input_verificatior \
    import CLIInputVerificatior as climix


class CliMixTests(unittest.TestCase):
    def setUp(self):
        self.climix = climix()

    def test_verify_books(self):
        self.assertEqual(self.climix._verify_books(2), 2)

    def test_verify_books_fail(self):
        with self.assertRaises(argparse.ArgumentTypeError) as context:
            self.climix._verify_books(-2)
        self.assertTrue('Expected positive integer, got value = -2' in context.exception)

    def test_verify_filters_wrong_filter(self):
        with self.assertRaises(argparse.ArgumentTypeError) as context:
            self.climix._verify_filters('published')
        self.assertTrue("Expected input in ['price', 'rating', 'available'], got value = published" in context.exception)

    def test_verify_filters_multiple_wrong_filters(self):
        with self.assertRaises(argparse.ArgumentTypeError) as context:
            self.climix._verify_filters(['rating', '!2'])
        self.assertTrue(
            "Expected input in ['>', '<', '='], got value = 2" in context.exception)

    def test_verify_filters(self):
        expected_res = ['rating', '=2']
        result = self. climix._verify_filters(['rating', '=2'])
        self.assertEqual(expected_res, result)

    def test_verify_genres(self):
        expected_res = ['Travel']
        result = self.climix._verify_genres(['Travel'], ['Travel', 'Mystery', 'Historical Fiction'])
        self.assertEqual(expected_res, result)

    def test_verify_genres_wrong(self):
        with self.assertRaises(argparse.ArgumentTypeError) as context:
            self.climix._verify_genres(['Cooking'], ['Travel', 'Mystery', 'Historical Fiction'])
        self.assertTrue(
            "Expected input in ['Travel', 'Mystery', 'Historical Fiction'], got value = Cooking" in context.exception)


if __name__ == '__main__':
    unittest.main()
