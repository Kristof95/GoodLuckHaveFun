import unittest
from date_handle import *


class MyTestCase(unittest.TestCase):

    def test_date_one(self):
        self.assertTrue(check_date("1993.03.29"))

    def test_date_two(self):
        self.assertFalse(check_date("1993.03.29."))

    def test_date_three(self):
        self.assertFalse(check_date("19933.03.29"))

    def test_date_four(self):
        self.assertFalse(check_date("asdf.03.29"))

    def test_date_five(self):
        self.assertFalse(check_date("1993.13.29"))

    def test_date_six(self):
        self.assertFalse(check_date("1993.00.29"))

    def test_date_seven(self):
        self.assertFalse(check_date("1993.04.31"))




    def test_time_one(self):
        self.assertTrue(check_time_text("12:00"))

    def test_time_two(self):
        self.assertFalse(check_time_text("24:00"))

    def test_time_three(self):
        self.assertFalse(check_time_text("12:67"))

    def test_time_four(self):
        self.assertFalse(check_time_text(" :00"))

    def test_time_five(self):
        self.assertFalse(check_time_text("23:sdf"))

    def test_time_six(self):
        self.assertFalse(check_time_text("23:00:00"))

    def test_time_seven(self):
        self.assertFalse(check_time_text(" "))


if __name__ == '__main__':
    unittest.main()
