import argparse
import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):
    def test_calculate_should_work_for_29_february_for_leap_years(self):
        weekday = calculate(2016, 2, 29)
        self.assertEqual(weekday, 0)

    def test_calculate_should_return_none_for_non_existing_day(self):
        weekday = calculate(2017, 2, 29)
        self.assertIsNone(weekday)

    def test_calculate_should_return_none_for_invalid_date(self):
        weekday = calculate(1234, 1234, 1234)
        self.assertIsNone(weekday)

    def test_calculate_should_work_for_first_day_of_a_year(self):
        weekday = calculate(2017, 1, 1)
        self.assertEqual(weekday, 6)

    def test_calculate_should_return_a_whole_week(self):
        weekdays = [calculate(2020, 1, day) for day in range(1, 7)]
        self.assertEqual(sorted(weekdays), [0, 1, 2, 3, 4, 5, 6])

    def test_calculate_should_work_for_the_last_day_of_a_year(self):
        weekday = calculate(2017, 12, 31)
        self.assertEqual(weekday, 6)

    def test_main_should_return_0_for_legal_arguments(self):
        res = main('--year 2000 --month 10 --day 10')
        self.assertEqual(res, 0)

    def test_main_should_raise_an_error_for_illegal_arguments(self):
        self.assertRaises(
            argparse.ArgumentError,
            main('--year 2000 --month 10 --da 1')
        )

    def test_main_should_raise_an_error_when_provided_not_enough_args(self):
        self.assertRaises(
            argparse.ArgumentError,
            main('--year 2000 --month 10')
        )

    def test_main_should_raise_an_error_for_empty_arguments(self):
        self.assertRaises(
            argparse.ArgumentError,
            main('--year --month --day')
        )

    def test_main_should_raise_an_error_for_non_integer_arguments(self):
        self.assertRaises(
            argparse.ArgumentError,
            main('--year 2015 --month 8 --day hello')
        )


if __name__ == '__main__':
    unittest.main()
