from datetime import datetime
import time
from random import randint

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


# lists
    was_sick_list = ('y', 'n')
    gender_list = ('f', 'm')
    blood_type_list = ('a', 'b', 'ab', '0')


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
        splitted = self.name.split(",")
        full_name = {}
        if len(splitted) > 0:
            full_name['first_name'] = splitted[0]
        if len(splitted) > 1:
            full_name['last_name'] = splitted[1]
        return full_name

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
        if int(self.weight) < 0:
            print("Weight should be a positive integer!")
            return False
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
            return False
        return True

    def get_gender(self):
        while self.gender == "":
            self.gender = input("Gender (f/m):")
            if self.gender == "":
                print("Gender field cannot be empty!")
            elif not self.check_gender():
                self.gender = ""

    def parse_birth_of_date(self):
        return datetime.strptime(self.date_of_birth, '%Y.%m.%d')

    def check_date(self):
        date_parts = self.date_of_birth.split(".")
        if len(date_parts) == 3:
            for part in date_parts:
                if not part.isdigit():
                    print("Bad date format! It should be YYYY.MM.DD!")
                    return False
                if int(date_parts[0]) > int(datetime.now().year):
                    print("Year is incorrect year cannot be bigger than present year!")
                    return False
                if int(date_parts[1]) > 12:
                    print("Date incorrect month cannot be bigger than 12!")
                    return False
                if int(date_parts[1]) < 0:
                    print("Month is incorrect it cannot be minus!\nIt must be a positive integer!")
                    return False
                if int(date_parts[1]) == 2 and int(date_parts[2]) > 29:
                    print("Month is incorrect february month has 29 days. ")
                    return False
                if int(date_parts[2]) > 31:
                    print("Day is incorrect cannot be bigger than 31!")
                    return False
            return True
        print("Bad date format! It should be YYYY.MM.DD!")
        return False

    def get_birth_of_date(self):
        while self.date_of_birth == "":
            self.date_of_birth = input("Date of birth(YYYY.MM.DD):")
            if self.date_of_birth == "":
                print("Date of birth field cannot be empty!")
            elif not (self.check_date()):
                self.date_of_birth = ""

    def check_last_donation_date(self):
        return self.check_date()

    def valid_last_donation_date(self): #Peter
        pass

    def get_last_donation_date(self):  #A cikluson belul meg hivd meg majd a valid_last_donation_date-t
        while self.last_donation_date == "":
            self.last_donation_date = input("Last donation date:")
        if self.last_donation_date == "":
            print("Last donation field cannot be empty!")
        elif not self.check_last_donation_date():
            self.last_donation_date = ""

    def check_was_sick(self):
        if self.was_sick.lower() not in self.was_sick_list:
            print("You can choose between: y/n")
            return False
        return True

    def get_was_sick(self):
        while self.was_sick == "":
            self.was_sick = input("Was he/she sick in the last month?(y/n):")
            if self.was_sick == "":
                print("Was he/she sick in the last month' cannot be empty!")
            elif not (self.check_was_sick()):
                self.was_sick = ""
            if self.was_sick == "y":
                print("Sorry, you cannot be a donor!")
                quit()
            return True

    def check_unique_id(self):
        if (len(self.unique_id)) < 8:
            print("Unique id is too short!")
            return False
        if len(self.unique_id) > 8:
            print("Unique id is too long!")
            return False
        if not (self.unique_id[:6].isdigit()) and not (self.unique_id[6:].isalpha()):
            print("Identity card should be 6 digits and 2 letters!")
            return False
        if not (self.unique_id[:6].isalpha()) and not (self.unique_id[6:].isdigit()):
            print("Passport card should be 6 letters and 2 digits!")
            return False
        return True

    def get_unique_id(self):
        while self.unique_id == "":
            self.unique_id = input("Identity card(6 digit + 2 letter) or passport card(6 letter + 2 digit):")
        if self.unique_id == "":
            print("ID field cannot be empty!")
        elif self.check_unique_id():
            self.unique_id = ""

    def check_blood_type(self):
        if self.blood_type.lower() not in self.blood_type_list:
            print("You can choose: a, b, ab, 0!")
            return False
        return True

    def get_blood_type(self):
        while self.blood_type == "":
            self.blood_type = input("Blood type(a, b, ab, 0):")
        if self.blood_type == "":
            print("Blood type field cannot be empty!")
        elif not self.check_blood_type():
            self.blood_type = ""

    def check_expiration_of_id(self):
        return self.check_date()

    def valid_expiration_of_id(self): #Peter
        pass

    def get_expiration_of_id(self):  # ide is majd hivd meg a valid_expiration_of_id-t
        while self.expiration_of_id == "":
            self.expiration_of_id = input("Expiration of id:")
            if self.expiration_of_id == "":
                print("Expiration of id filed cannot be empty!")
            elif not self.check_expiration_of_id():
                self.expiration_of_id = ""

    def valid_email_address(self):
        if not (self.email_address.endswith('.com')) or not (self.email_address.endswith('.com')):
            print("Email address must ends with .hu or .com!")
            return False
        if '@' not in self.email_address:
            print("Email must contain a @!")
            return False
        if len(self.email_address) < 6:
            print("Email address is too short!")
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
        if not mobile_nr_check[2:4] == "30" or mobile_nr_check[2:4] == "20" or mobile_nr_check[2:4] == "70":
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
        if randint(80, 201) > 110:
            print("Cool ! You're ready for donation.")
        else:
            print("Your hemoglobin level is too low!")
            time.sleep(2)
            quit()

don = Donor_class("", "", "", "", "", "", "", "", "", "", "")
# don.get_name()
# don.get_weight()
# don.get_birth_of_date()
# don.get_was_sick()
# don.get_gender()
# don.get_unique_id()
# don.get_hemoglobin()
# don.get_email_address()
# don.get_mobile_number()

