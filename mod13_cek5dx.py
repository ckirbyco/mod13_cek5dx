import unittest
from datetime import datetime
from user_input import UserInput


class UserInputTest(unittest.TestCase):

    # symbol: capitalized, 1-7 alpha characters
    def test_symbol(self):
        test_symbols = ["loca", "GOOGL", "HELP", "hi", "AMZN"]
        test_result = [False, True, True, False, True]

        for symbol, expected_result in zip(test_symbols, test_result):
            result = symbol.isupper() and len(symbol) <= 7 and symbol.isalpha()
            self.assertEqual(result, expected_result)

    # chart type: 1 numeric character, 1 or 2
    def test_chart(self):
        test_chart = ["1", "2", "0", ""]
        test_result = [True, True, False, False]

        for chart_type, expected_result in zip(test_chart, test_result):
            result = chart_type in ["1", "2"]
            self.assertEqual(result, expected_result)

    # time series: 1 numeric character, 1 - 4
    def test_time_series(self):
        test_time_series = ["1", "2", "3", "4", "5", ""]
        test_result = [True, True, True, True, False, False]

        for time_series, expected_result in zip(test_time_series, test_result):
            result = 1 <= int(time_series) <= 4
            self.assertEqual(result, expected_result)

    # start date: date type YYYY-MM-DD 
    def test_date_format_constraints(self):
        user_input = UserInput()
        user_date = user_input.get_date('Start')
        self.assertIsInstance(user_date, datetime)
        

    # end date: date type YYYY-MM-DD
    def test_date_range_constraints(self):
        user_input = UserInput()
        start_date = datetime(2024, 1, 1)
        end_date = datetime(2024, 12, 31)

        self.assertTrue(user_input.valid_date_range(start_date, end_date))

if __name__ == "__main__":
    unittest.main()