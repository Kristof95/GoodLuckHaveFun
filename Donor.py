from datetime import datetime
import time
from random import randint
import date_handle
import csv
import os
import sys

class Donor_class:

# variables
    name = ""
    weight = ""
    gender = ""
    date_of_birth = ""
    last_donation_date = ""
    was_sick = ""
    unique_id = ""
    blood_type = ""
    expiration_of_id = ""
    email_address = ""
    mobile_number = ""
    date_format = ""
    age=0
    birth_date_string=""
    hemoglobin=0


# lists
    was_sick_list = ('yes', 'no')
    gender_list = ('f', 'm')
    blood_type_list = ('+a','-a','+b','-b','+ab','-ab','+0','-0')


# functions
    def __init__(self,  name, weight, date_of_birth, unique_id, blood_type, expiration_of_id, email_address, mobile_number, last_donation_date, was_sick, gender):
        self.name = name
        self.weight = weight
        self.date_of_birth = date_of_birth
        self.unique_id = unique_id
        self.blood_type = blood_type
        self.expiration_of_id = expiration_of_id
        self.email_address = email_address
        self.mobile_number = mobile_number
        self.last_donation_date = last_donation_date
        self.was_sick = was_sick
        self.gender = gender

    def parse_name(self):
        splitted = self.name.split(" ")
        return splitted

    def valid_name(self):
        name_parts = self.name.split(" ")
        if not (len(name_parts) >= 2):
            print("Your name is too short!")
            return False
        for i in name_parts:
            if not (i.isalpha()):
                print("Name should contains only letters!")
                return False
        return True

    def get_name(self):
        while self.name == "":
            self.name = input("Name:")
            if self.name == "":
                print("Name field cannot be empty!")
            elif not (self.valid_name()):
                self.name = ""

    def check_weight(self):
        if not self.weight.isdigit():
            print("Weight should be number!")
            return False
        return True

    def valid_weight(self):
        if not self.check_weight():
            return False
        elif int(self.weight) < 0:
            print("Weight should be a positive integer!")
            return False
        elif int(self.weight)<50:
            self.not_suitable("You are too light!")
            return True
            #exit()
        return True


    def get_weight(self):
        while self.weight == "":
            self.weight = input("Weight(kg):")
            if self.weight == "":
                print("Weight field cannot be empty!")
            elif not (self.check_weight()):
                self.weight = ""
            elif not (self.valid_weight()):
                self.weight = ""

    def check_gender(self):
        if self.gender.lower() not in self.gender_list:
            print ("Only F or M")
            return False
        return True

    def get_gender(self):
        while self.gender == "":
            self.gender = input("Gender (f/m):")
            if self.gender == "":
                print("Gender field cannot be empty!")
            elif not self.check_gender():
                self.gender = ""

    def check_birth_date(self):
        self.birth_date_string=datetime.strptime(self.date_of_birth, '%Y.%m.%d')
        self.age=(datetime.now()-self.birth_date_string).days//365
        if self.birth_date_string>datetime.now():
            print("I think you was born before now!")
            return False
        elif self.age<18:
            self.not_suitable("You are too young, you need to be at least 18 years old.")
            return True
            #exit()
        else:
            return True



    def get_birth_of_date(self):
        while self.date_of_birth == "":
            self.date_of_birth = input("Date of birth(YYYY.MM.DD):")
            if self.date_of_birth == "":
                print("Date of birth field cannot be empty!")
            elif not (date_handle.check_date(self.date_of_birth)and self.check_birth_date()):
                self.date_of_birth = ""



    def valid_last_donation_date(self): #Peter
        donationdate=datetime.strptime(self.last_donation_date, '%Y.%m.%d')
        if donationdate>datetime.now():
            print("The donation must be earlier than the today date!")
            return False
        time_from_last_donation=(datetime.now()-donationdate).days
        if time_from_last_donation<90:
            self.not_suitable("You need at least 90 days from your last donation")
            return True
        return True

    def get_last_donation_date(self):
        while self.last_donation_date == "":
            self.last_donation_date = input("Last donation date:")
            if self.last_donation_date == "":
                print("Last donation field cannot be empty!")
            elif not (date_handle.check_date(self.last_donation_date) and self.valid_last_donation_date()):
                self.last_donation_date = ""

    def check_was_sick(self):
        if self.was_sick.lower() not in self.was_sick_list:
            print("You can choose between: yes/no")
            return False
        return True

    def get_was_sick(self):
        while self.was_sick == "":
            self.was_sick = input("Was he/she sick in the last month?(yes/no):")
            if self.was_sick == "":
                print("Was he/she sick in the last month' cannot be empty!")
            elif not (self.check_was_sick()):
                self.was_sick = ""
            if self.was_sick == "yes":
                self.not_suitable("Sorry, you cannot be a donor!")
                return True
                #quit()
            return True

    def check_unique_id(self):
        if (len(self.unique_id)) < 8:
            print("Unique id is too short!")
            return False
        elif len(self.unique_id) > 8:
            print("Unique id is too long!")
            return False
        elif self.unique_id[:6].isdigit() and  self.unique_id[6:].isalpha():
            #print("Identity card should be 6 digits and 2 letters!")
            print("This is identity card!")
            return True
        elif self.unique_id[:6].isalpha() and self.unique_id[6:].isdigit():
            print("This is passport!")
            #print("Passport card should be 6 letters and 2 digits!")
            return True
        return False

    def get_unique_id(self):
        while self.unique_id == "":
            self.unique_id = input("Identity card(6 digit + 2 letter) or passport card(6 letter + 2 digit):")
            if self.unique_id == "":
                print("ID field cannot be empty!")
            elif not(self.check_unique_id()):
                self.unique_id = ""

    def check_blood_type(self):
        if self.blood_type.lower() not in self.blood_type_list:
            print("You can choose: +a,-a,+b,-b,+ab,-ab,+0,-0!")
            return False
        return True

    def get_blood_type(self):
        while self.blood_type == "":
            self.blood_type = input("Blood type(a, b, ab, 0):")
            if self.blood_type == "":
                print("Blood type field cannot be empty!")
            elif not self.check_blood_type():
                self.blood_type = ""


    def valid_expiration_of_id(self):
        expiration=datetime.strptime(self.expiration_of_id, '%Y.%m.%d')
        if expiration<datetime.now():
            self.not_suitable("Your ID has expired!")
            return True
            #exit()
        return True


    def get_expiration_of_id(self):  # ide is majd hivd meg a valid_expiration_of_id-t
        while self.expiration_of_id == "":
            self.expiration_of_id = input("Expiration of id:")
            if self.expiration_of_id == "":
                print("Expiration of id filed cannot be empty!")
            elif not (date_handle.check_date(self.expiration_of_id)and self.valid_expiration_of_id()):
                self.expiration_of_id = ""

    def valid_email_address(self):
        if not (self.email_address.endswith('.hu') or self.email_address.endswith('.com')):
            print("Email address must ends with .hu or .com!")
            return False
        if '@' not in self.email_address:
            print("Email must contain a @!")
            return False
        if self.email_address[0]=="@":
            print("This is not a valid e-mail address!")
            return False
        return True

    def get_email_address(self):
        while self.email_address == "":
            self.email_address = input("Email address:")
            if self.email_address == "":
                print("Email address field cannot be empty!")
            elif not self.valid_email_address():
                self.email_address = ""

    def valid_mobile_number(self):
        if not (self.mobile_number.startswith("+36") or self.mobile_number.startswith("06")):
            print("Mobile number must start with +36 or 06!")
            return False
        check_digit = 0
        if self.mobile_number.startswith("+"):
            check_digit = 1
        mobile_nr_check = self.mobile_number[check_digit:]
        if not mobile_nr_check.isdigit():
            print("Mobile number should be integer!")
            return False
        if len(mobile_nr_check) < 11:
            print("Mobile number is too short!")
            return False
        if len(mobile_nr_check) > 11:
            print("Mobile number is too long!")
            return False
        if not (mobile_nr_check[2:4] == "30" or mobile_nr_check[2:4] == "20" or mobile_nr_check[2:4] == "70"):
            print("Region number should be 30, 20, 70")
            return False
        return True

    def get_mobile_number(self):
        while self.mobile_number == "":
            self.mobile_number = input("Mobile number (e.g 06301234567):")
            if self.mobile_number == "":
                print("Mobile number field cannot be empty!")
            elif not self.valid_mobile_number():
                self.mobile_number = ""

    def get_hemoglobin(self):
        self.hemoglobin=randint(80,201)
        if self.hemoglobin > 110:
            print("Cool ! You're ready for donation.")
        else:
            self.not_suitable("Your hemoglobin level is too low!")
            return True
        return True
            #quit()
 #   def write_out_of_donor_datas(self):
  #      name=self.parse_name()
  #      if len(name)==2:
  #          print(name[1], ",", name[0])
  #      elif len(name)==3:
  #          print(name[2],",",name[1],",",name[0])
  #      print(str(self.weight),"kg")
  #      print(self.date_of_birth[0:4],".",self.date_of_birth[5:7],".",self.date_of_birth[8:10],"-",self.age,"years old")
  #      print(self.email_address)

    def write_to_csv_file(self):
        with open(os.path.join(os.path.dirname(sys.argv[0]), "Data\donor.csv"), 'a', newline='\n') as csvfile:
            write_to_donor_csv = csv.writer(csvfile)
            write_to_donor_csv.writerow([self.name,self.weight,
                                         self.date_of_birth[0:4]+"."+self.date_of_birth[5:7]+"."+self.date_of_birth[8:10],
                                         self.age,self.last_donation_date,self.was_sick,self.gender,self.unique_id,
                                         self.expiration_of_id,self.email_address,self.blood_type,self.mobile_number,
                                         self.hemoglobin])

    def not_suitable(self,string):
        print(string)
        pass



def main():
    don = Donor_class("", "", "", "", "", "", "", "", "", "", "")
    don.get_name()
    don.get_weight()
    don.get_birth_of_date()
    don.get_last_donation_date()
    don.get_was_sick()
    don.get_gender()
    don.get_unique_id()
    don.get_expiration_of_id()
    don.get_blood_type()
    don.get_hemoglobin()
    don.get_email_address()
    don.get_mobile_number()
#   don.write_out_of_donor_datas()
    don.write_to_csv_file()

