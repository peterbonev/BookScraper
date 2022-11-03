import unittest
from book_data_parser.data_parser_mixin import DataParserMixin as dpm
from bs4 import BeautifulSoup

# coverage 100%


class DMPTests(unittest.TestCase):
    def setUp(self):
        file_red = open('mock_files/html_content_example.html', 'r')
        self.html_content = BeautifulSoup(file_red, 'html.parser')
        file_red.close()
        self.dpm_inst = dpm()

    def test_scrape_title(self):
        result = self.dpm_inst.scrape_title(self.html_content)
        expected_res = 'Private Paris (Private #10)'
        self.assertEqual(expected_res, result)

    def test_scrape_genre(self):
        result = self.dpm_inst.scrape_genre(self.html_content)
        expected_res = 'Fiction'
        self.assertEqual(expected_res, result)

    def test_scrape_price_return_type(self):
        self.assertEqual(type(self.dpm_inst.scrape_price(self.html_content)), float)

    def test_scrape_price(self):
        expected_res = 47.61
        result = self.dpm_inst.scrape_price(self.html_content)
        self.assertEqual(expected_res, result)

    def test_scrape_rating_return_type(self):
        self.assertEqual(type(self.dpm_inst.scrape_rating(self.html_content)), int)

    def test_scrape_rating(self):
        expected_res = 5
        result = self.dpm_inst.scrape_rating(self.html_content)
        self.assertEqual(expected_res, result)

    def test_scrape_rate_1(self):
        file_read = open('mock_files/star_rate_1.html', 'r')
        test_html_one_star = BeautifulSoup(file_read, 'html.parser')
        file_read.close()
        expected_res = 1
        result = self.dpm_inst.scrape_rating(test_html_one_star)
        self.assertEqual(expected_res, result)

    def test_scrape_rate_2(self):
        file_read = open('mock_files/star_rate_2.html', 'r')
        test_html_two_star = BeautifulSoup(file_read, 'html.parser')
        file_read.close()
        expected_res = 2
        result = self.dpm_inst.scrape_rating(test_html_two_star)
        self.assertEqual(expected_res, result)

    def test_scrape_rate_3(self):
            file_read = open('mock_files/star_rate_3.html', 'r')
            test_html_three_star = BeautifulSoup(file_read, 'html.parser')
            file_read.close()
            expected_res = 3
            result = self.dpm_inst.scrape_rating(test_html_three_star)
            self.assertEqual(expected_res, result)

    def test_scrape_rate_4(self):
        file_read = open('mock_files/star_rate_4.html', 'r')
        test_html_four_star = BeautifulSoup(file_read, 'html.parser')
        file_read.close()
        expected_res = 4
        result = self.dpm_inst.scrape_rating(test_html_four_star)
        self.assertEqual(expected_res, result)

    def test_scrape_stock_available_return_type(self):
        self.assertEqual(type(self.dpm_inst.scrape_stock_available(self.html_content)), int)

    def test_scrape_stock_available(self):
        expected_res = 17
        result = self.dpm_inst.scrape_stock_available(self.html_content)
        self.assertEqual(expected_res, result)

    def test_scrape_description(self):
        expected_res = "Paris is burning--and only Private's Jack Morgan can put out the fire.When Jack Morgan stops " \
                       "by Private's Paris office, he envisions a quick hello during an otherwise relaxing trip filled" \
                       " with fine food and sightseeing. But Jack is quickly pressed into duty after a call from his " \
                       "client Sherman Wilkerson, asking Jack to track down his young granddaughter who is on the run " \
                       "f Paris is burning--and only Private's Jack Morgan can put out the fire.When Jack Morgan stops " \
                       "by Private's Paris office, he envisions a quick hello during an otherwise relaxing trip filled" \
                       " with fine food and sightseeing. But Jack is quickly pressed into duty after a call from his " \
                       "client Sherman Wilkerson, asking Jack to track down his young granddaughter who is on the run " \
                       "from a brutal drug dealer.Before Jack can locate her, several members of France's cultural " \
                       "elite are found dead--murdered in stunning, symbolic fashion. The only link between the crimes " \
                       "is a mysterious graffiti tag. As religious and ethnic tensions simmer in the City of Lights, " \
                       "only Jack and his Private team can connect the dots before the smoldering powder keg explodes. " \
                       "...more"
        result = self.dpm_inst.scrape_description(self.html_content)
        self.assertEqual(expected_res, result)

    def test_scrape_description_none_description(self):
        file_read = open('mock_files/star_rate_1.html', 'r')
        test_html = BeautifulSoup(file_read, 'html.parser')
        file_read.close()
        expected_res = 'No description'
        result = self.dpm_inst.scrape_description(test_html)
        self.assertEqual(expected_res, result)

    def test_scrape_upc(self):
        expected_res = 'b12b89017878a60d'
        result = self.dpm_inst.scrape_upc(self.html_content)
        self.assertEqual(expected_res, result)


if __name__ == '__main__':
    unittest.main()
