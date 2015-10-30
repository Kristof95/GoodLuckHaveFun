import unittest
from donation_location import Donation_class


class DonationLocation(unittest.TestCase):
    global test
    test=Donation_class("","","","","","","","","","")

    ############
    ##zip_code##
    ############
    def test_zip_code_one(self):
        test.zip_code = "3530"
        self.assertTrue(test.check_zip_code() and test.validate_zip_code())

    def test_zip_code_two(self):
        test.zip_code="35302"
        self.assertFalse(test.check_zip_code() and test.validate_zip_code())

    def test_zip_code_three(self):
        test.zip_code="353"
        self.assertFalse(test.check_zip_code() and test.validate_zip_code())

    def test_zip_code_four(self):
        test.zip_code="353e"
        self.assertFalse(test.check_zip_code() and test.validate_zip_code())

    def test_zip_code_five(self):
        test.zip_code="353 "
        self.assertFalse(test.check_zip_code() and test.validate_zip_code())

    ############
    ##  city  ##
    ############
    def test_city_one(self):
        test.city = "miskolc"
        self.assertTrue(test.validate_city())

    def test_city_two(self):
        test.city = "debrecen"
        self.assertFalse(test.validate_city())

    def test_city_three(self):
        test.city = "kolc"
        self.assertFalse(test.validate_city())

    def test_city_four(self):
        test.city = "MISKOLC"
        self.assertTrue(test.validate_city())

    def test_city_five(self):
        test.city = "Mis kolc"
        self.assertFalse(test.validate_city())

    def test_city_six(self):
        test.city = " Miskolc"
        self.assertFalse(test.validate_city())

    def test_city_seven(self):
        test.city = "SzErEnCs"
        self.assertTrue(test.validate_city())


    #############
    ## Address ##
    #############
    def test_address_one(self):
        test.address = "Miskolc 12312312"
        self.assertTrue(test.validate_address())

    def test_address_two(self):
        test.address = "123145756463551231457564635512314575646355"
        self.assertTrue(test.validate_address())

    def test_address_three(self):
        test.address = " "*50
        self.assertTrue(test.validate_address())

    def test_address_four(self):
        test.address = "a"*50
        self.assertTrue(test.validate_address())

    ###################################
    ## number of successful donation ##
    ###################################
    def test_number_of_successful_donation_one(self):
        test.number_of_successful_donation = "100"
        test.max_donor_number = "50"
        self.assertTrue(test.check_number_of_successful_donation() and test.valid_number_of_successful_donation())

    def test_number_of_successful_donation_two(self):
        test.number_of_successful_donation = "asd"
        test.max_donor_number = "50"
        self.assertFalse(test.check_number_of_successful_donation() and test.valid_number_of_successful_donation())

    def test_number_of_successful_donation_three(self):
        test.number_of_successful_donation = "asd"
        test.max_donor_number = "lol"
        self.assertFalse(test.check_number_of_successful_donation() and test.valid_number_of_successful_donation())

    def test_number_of_successful_donation_four(self):
        test.number_of_successful_donation = "1000"
        test.max_donor_number = "feri"
        self.assertFalse(test.check_number_of_successful_donation() and test.valid_number_of_successful_donation())

    def test_number_of_successful_donation_five(self):
        test.number_of_successful_donation = "10"
        test.max_donor_number = "-2"
        self.assertFalse(test.check_number_of_successful_donation() and test.valid_number_of_successful_donation())

    def test_number_of_successful_donation_six(self):
        test.number_of_successful_donation = "-5"
        test.max_donor_number = "2"
        self.assertFalse(test.check_number_of_successful_donation() and test.valid_number_of_successful_donation())

    def test_number_of_successful_donation_seven(self):
        test.number_of_successful_donation = "-5"
        test.max_donor_number = "-2"
        self.assertFalse(test.check_number_of_successful_donation() and test.valid_number_of_successful_donation())

    def test_number_of_successful_donation_eight(self):
        test.number_of_successful_donation = " "
        test.max_donor_number = " "
        self.assertFalse(test.check_number_of_successful_donation() and test.valid_number_of_successful_donation())

    ####################
    ## available_beds ##
    ####################
    def test_available_beds_one(self):
        test.available_beds = "50"
        self.assertTrue(test.check_available_beds())

    def test_available_beds_two(self):
        test.available_beds = "0"
        self.assertTrue(test.check_available_beds())

    def test_available_beds_three(self):
        test.available_beds = "-1"
        self.assertFalse(test.check_available_beds())

    def test_available_beds_four(self):
        test.available_beds = " "
        self.assertFalse(test.check_available_beds())

    def test_available_beds_five(self):
        test.available_beds = "asd"
        self.assertFalse(test.check_available_beds())

    ##########################
    ## planned_donor_number ##
    ##########################
    def test_planned_donor_number_one(self):
        test.planned_donor_number = "50"
        self.assertTrue(test.check_planned_donor_number())

    def test_planned_donor_number_two(self):
        test.planned_donor_number = "-50"
        self.assertFalse(test.check_planned_donor_number())

    def test_planned_donor_number_three(self):
        test.planned_donor_number = ""
        self.assertFalse(test.check_planned_donor_number())

    def test_planned_donor_number_four(self):
        test.planned_donor_number = "asdfgh"
        self.assertFalse(test.check_planned_donor_number())

    def test_planned_donor_number_five(self):
        test.planned_donor_number = " "
        self.assertFalse(test.check_planned_donor_number())

    ############################
    ## date_and_time_of_event ##
    ############################
    def test_date_and_time_of_event_one(self):
        test.date_and_time_of_event = "2015.12.11"
        self.assertTrue(test.validate_date_and_time_of_event())

    def test_date_and_time_of_event_two(self):
        test.date_and_time_of_event = "2015.12.12"
        self.assertFalse(test.validate_date_and_time_of_event())

    def test_date_and_time_of_event_three(self):
        test.date_and_time_of_event = "2015.06.01"
        self.assertFalse(test.validate_date_and_time_of_event())

if __name__ == '__main__':
    unittest.main()
