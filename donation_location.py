from datetime import datetime
import date_handle
import csv
import os
import sys
import string
import random
import uuid
class Donation_class:

    available_cities = ["miskolc", "szerencs", "sarospatak", "kazincbarcika"]


    date_and_time_of_event = ""
    start_time_text = ""
    end_time_text = ""
    zip_code = ""
    address = ""
    number_of_successful_donation = ""
    available_beds = ""
    planned_donor_number = ""
    duration=0
    preparation_time = 30
    donation_time = 30
    maximum_donor_number=0

    def __init__(self, date_and_time_of_event, start_time_text, end_time_text, zip_code, city, address, number_of_successful_donation, available_beds, planned_donor_number, available_cities):
        self.date_and_time_of_event = date_and_time_of_event
        self.start_time_text = start_time_text
        self.end_time_text = end_time_text
        self.zip_code = zip_code
        self.city = city
        self.address = address
        self.number_of_successful_donation = number_of_successful_donation
        self.available_beds = available_beds
        self.planned_donor_number = planned_donor_number


    def calculate_duration_in_minutes(start, end):
        return (end - start).seconds // 60

    def calculate_max_donor_number(self):
       print (((self.duration - self.preparation_time) // self.donation_time) * int(self.available_beds), "is the maximum donor number")
       self.maximum_donor_number=((self.duration - self.preparation_time) // self.donation_time) * int(self.available_beds)
       return True


    def check_zip_code(self):
       if not self.zip_code.isdigit():
            print("Zip code should be digits !")
            return False
       return True


    def check_available_beds(self):
        if self.available_beds == "":
            print("Beds number can't be empty")
        if not self.available_beds.isdigit():
            print("Beds number should be digits!")
            return False
        return True


    def check_planned_donor_number(self):
       if self.planned_donor_number == "":
           print("Donors number can't be empty")
           return False
       if self.planned_donor_number == " ":
           print("Space is not a number!")
           return False
       if not (int(self.planned_donor_number) > 0):
           print("Planned donor number must be positive integer!")
           return False
       if not self.planned_donor_number.isdigit():
           print("Planned donor number must be integer!")
           return False

       return True

    def check_number_of_successful_donation(self):
        if self.number_of_successful_donation == "":
            print("Success donation number can't be empty")
        if not self.number_of_successful_donation.isdigit():
            print("Success donation number should be digits!")
            return False
        return True


    def validate_date_and_time_of_event(self):
        date_event = date_handle.parse_date(self.date_and_time_of_event)
        date_and_time_of_event = date_event - datetime.now()
        if date_and_time_of_event.days < 10:
            print("The event should be kept after 10 days")
            return False
        if date_event.isoweekday() == 6 or date_event.isoweekday() == 7:
            print("Datetime can be only on weekdays")
            return False
        return True

    def validate_zip_code(self):
      if (self.zip_code.startswith("0")):
        print("Zip code can't start with 0")
        return False
      if len(self.zip_code) != 4:
        print("Zip code should be exactly 4 characters long !")
        return False
      return True


    def validate_address(self):
        if not len(self.address) <= 25:
            print("Too long")
            return False
        return True

    def validate_city(self):
        if self.city.lower() not in self.available_cities:
            print("The city is not in the list")
            return False
        return True

    def valid_number_of_successful_donation(self):
        if int(self.number_of_successful_donation) > self.maximum_donor_number:
            print("Successful cannot exceed maximum donor number!")
            return False
        return True


    def get_donation_success_rate(self):
        rate = int(self.number_of_successful_donation)/ int(self.planned_donor_number)
        if rate < 0.2:
            print("Unsuccessful, not worth to organise there again.")
        elif rate <= 0.75:
            print("Normal event.")
        elif rate <= 1.1:
            print("Successful.")
        else:
            print("Outstanding.")
        return rate



    def get_date_and_time_of_event(self):
        while self.date_and_time_of_event == "":
            self.date_and_time_of_event = input("Event day:")
            if not (date_handle.check_date(self.date_and_time_of_event)and self.validate_date_and_time_of_event()):
                self.date_and_time_of_event = ""


    def get_zip_code(self):
        while self.zip_code == "":
            self.zip_code = input("Code:")
            if not (self.check_zip_code() and self.validate_zip_code()):
                self.zip_code = ""


    def get_city(self):
        while self.city == "":
            self.city = input("City:")
            if not (self.validate_city()):
                self.city = ""


    def get_address(self):
        while self.address == "":
            self.address = input("Address:")
            if not (self.validate_address()):
                self.address = ""

    def get_available_beds(self):
        while self.available_beds == "":
            self.available_beds = input("Beds number:")
            if not (self.check_available_beds()):
                self.available_beds = ""

    def get_number_of_successful_donation(self):
        while self.number_of_successful_donation == "":
            self.number_of_successful_donation = input("Success donation number:")
            if not (self.check_number_of_successful_donation() and self.valid_number_of_successful_donation()):
                self.number_of_successful_donation = ""

    def get_planned_donor_number(self):
        while self.planned_donor_number == "":
            self.planned_donor_number = input("Planned number:")
            if not (self.check_planned_donor_number()):
                self.planned_donor_number = ""

    def calculate_duration(self):
        self.get_start_time_text()
        self.get_end_time_text()
        start_time=self.start_time_text.split(":")
        end_time=self.end_time_text.split(":")
        duration=(int(end_time[0])-int(start_time[0]))*60+int(end_time[1])-int(start_time[1])
        if duration<0:
            print("The end time must be later than start time!")
            self.start_time_text=""
            self.end_time_text=""
            self.calculate_duration()
        elif duration==0:
            print("There must be some time!")
            self.start_time_text=""
            self.end_time_text=""
            self.calculate_duration()
        elif duration>0:
            print(duration, "minutes the duration of the event.")
            self.duration=duration


    def get_start_time_text(self):
        while self.start_time_text == "":
            self.start_time_text = input("Start time:")
            if not (date_handle.check_time_text(self.start_time_text)):
                self.start_time_text = ""

    def get_end_time_text(self):
        while self.end_time_text == "":
            self.end_time_text = input("End time:")
            if not (date_handle.check_time_text(self.end_time_text)):
                self.end_time_text = ""


    def csv_writer(self):
        def my_random_string(string_length=10):
            random = str(uuid.uuid4())
            random = random.upper()
            random = random.replace("-","")
            return random[0:string_length]
        data = [my_random_string(6),
                self.date_and_time_of_event,
                self.zip_code,
                self.city,
                self.address,
                self.available_beds,
                self.planned_donor_number,
                self.number_of_successful_donation
                ]
        with open(os.path.join(os.path.dirname(sys.argv[0]),"Data\donations.csv"), "a") as csv_file:

            writer = csv.writer(csv_file)
            writer.writerow(data)





def main():
    don = Donation_class("","","","","","","","","","")
    don.get_date_and_time_of_event()
    don.calculate_duration()
    don.get_zip_code()
    don.get_city()
    don.get_address()
    don.get_available_beds()
    don.get_planned_donor_number()
    don.calculate_max_donor_number()
    don.get_number_of_successful_donation()
    don.get_donation_success_rate()
    don.csv_writer()
