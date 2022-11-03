import unittest

from cli_input_arguments.cli_input_arguments import InputArguments as ia
from cli_input_arguments.cli_input_verificator.cli_input_verificatior \
    import CLIInputVerificatior as climix


class IATests(unittest.TestCase):
    def setUp(self):
        self.inargs = ia()

    def test_init(self):
        self.assertIsInstance(self.inargs, ia)

    def test_get(self):
        ver_inp = climix()
        result = str(self.inargs.get(ver_inp))
        defult_res = "1000, None, None, None, None, None, None, False"
        self.assertEqual(defult_res, result)


if __name__ == '__main__':
    unittest.main()
