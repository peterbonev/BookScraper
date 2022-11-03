import argparse
import unittest
from cli_input_arguments.cli_input_verificator.cli_input_verification_mixin \
    import CLIInputVerificationCriteriaMixin as climix


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
            self.climix.verify_filters('published')
        self.assertTrue("Expected input in ['price', 'rating', 'available'], got value = published" in context.exception)

    def test_verify_filters_no_filter(self):
        with self.assertRaises(TypeError) as context:
            self.climix.verify_filters()
        self.assertTrue("verify_filters() takes exactly 2 arguments (1 given)" in context.exception)

    def test_verify_filters_multiple_wrong_filters(self):
        with self.assertRaises(argparse.ArgumentTypeError) as context:
            self.climix.verify_filters(['rice', 'raing', 'published'])
        self.assertTrue(
            "Expected input in ['price', 'rating', 'available'], got value = ['rice', 'raing', 'published']" in context.exception)

    def test_verify_filters(self):
        expected_res = ['rating', '=2']
        result = self. climix.verify_filters(['rating', '=2'])
        self.assertEqual(expected_res, result)

    def test_verify_genres(self):
        expected_res = ['Travel']
        result = self.climix.verify_genres(['Travel'], ['Travel', 'Mystery', 'Historical Fiction'])
        self.assertEqual(expected_res, result)


if __name__ == '__main__':
    unittest.main()
