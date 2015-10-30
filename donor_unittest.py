__author__ = 'Vas Richard Roland'

import unittest
from Donor import Donor_class


class MyTestCase(unittest.TestCase):
    global test
    test=Donor_class("", "", "", "", "", "", "", "", "", "", "")

    def test_name_one(self):
        test.name="Szekely Peter"
        self.assertTrue(test.valid_name())
    def test_name_two(self):
        test.name="ab"
        self.assertFalse(test.valid_name())
    def test_name_three(self):
        test.name=" "
        self.assertFalse(test.valid_name())
    def test_name_four(self):
        test.name="ab "
        self.assertFalse(test.valid_name())
    def test_name_five(self):
        test.name="12345 123"
        self.assertFalse(test.valid_name())



    def test_weight_one(self):
        test.weight="50"
        self.assertTrue(test.valid_weight() and test.check_weight())
    def test_weight_two(self):
        test.weight="20"
        self.assertFalse(test.valid_weight() and test.check_weight())
    def test_weight_three(self):
        test.weight=" "
        self.assertFalse(test.valid_weight() and test.check_weight())
    def test_weight_four(self):
        test.weight="sfrgg"
        self.assertFalse(test.valid_weight() and test.check_weight())



    def test_gender_one(self):
        test.gender="f"
        self.assertTrue(test.check_gender())
    def test_gender_two(self):
        test.gender="M"
        self.assertTrue(test.check_gender())
    def test_gender_three(self):
        test.gender="akg74"
        self.assertFalse(test.check_gender())



    def test_was_sick_one(self):
        test.was_sick="y"
        self.assertTrue(test.check_was_sick())
    def test_was_sick_two(self):
        test.was_sick="N"
        self.assertTrue(test.check_was_sick())
    def test_was_sick_three(self):
        test.was_sick="afd567"
        self.assertFalse(test.check_was_sick())



    def test_unique_id_one(self):
        test.unique_id="asdfgh12"
        self.assertTrue(test.check_unique_id())
    def test_unique_id_two(self):
        test.unique_id="123456ab"
        self.assertTrue(test.check_unique_id())
    def test_unique_id_three(self):
        test.unique_id="123456abc"
        self.assertFalse(test.check_unique_id())
    def test_unique_id_three(self):
        test.unique_id="123456abc"
        self.assertFalse(test.check_unique_id())
    def test_unique_id_four(self):
        test.unique_id="asdfgh123"
        self.assertFalse(test.check_unique_id())



    def test_blood_type_one(self):
        test.blood_type="+a"
        self.assertTrue(test.check_blood_type())
    def test_blood_type_two(self):
        test.blood_type="b"
        self.assertFalse(test.check_blood_type())
    def test_blood_type_three(self):
        test.blood_type="123"
        self.assertFalse(test.check_blood_type())



    def test_expiration_id_one(self):
        test.expiration_of_id="2015.11.01"
        self.assertTrue(test.valid_expiration_of_id())
    def test_expiration_id_two(self):
        test.expiration_of_id="2015.10.30"
        self.assertFalse(test.valid_expiration_of_id())



    def test_email_address_one(self):
        test.email_address="btthtaba@bltta.hu"
        self.assertTrue(test.valid_email_address())
    def test_email_address_two(self):
        test.email_address="btthtababltta.hu"
        self.assertFalse(test.valid_email_address())
    def test_email_address_three(self):
        test.email_address="@btthtababltta.hu"
        self.assertFalse(test.valid_email_address())



    def test_mobile_number_one(self):
        test.mobile_number="+36202105552"
        self.assertTrue(test.valid_mobile_number())
    def test_mobile_number_two(self):
        test.mobile_number="06702105552"
        self.assertTrue(test.valid_mobile_number())
    def test_mobile_number_three(self):
        test.mobile_number="+36202105552"
        self.assertTrue(test.valid_mobile_number())
    def test_mobile_number_four(self):
        test.mobile_number="+362021055522"
        self.assertFalse(test.valid_mobile_number())
    def test_mobile_number_five(self):
        test.mobile_number="+3620210552"
        self.assertFalse(test.valid_mobile_number())
    def test_mobile_number_six(self):
        test.mobile_number="+362021055a2"
        self.assertFalse(test.valid_mobile_number())



    def test_birth_date_one(self):
        test.date_of_birth="2007.11.01"
        self.assertFalse(test.check_birth_date())
    def test_birth_date_one(self):
        test.date_of_birth="2015.10.31"
        self.assertFalse(test.check_birth_date())
    def test_birth_date_one(self):
        test.date_of_birth="1995.06.29"
        self.assertTrue(test.check_birth_date())


if __name__ == '__main__':
    unittest.main()
