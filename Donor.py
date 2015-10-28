from datetime import datetime
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
    def __init__(self,  name, weight, date_of_birth, unique_id, blood_type, expiration_of_id, email_address, mobile_number,last_donation_date, was_sick, gender):
        self.name = name
        self.weight = weight
        self.date_of_birht = date_of_birth
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
            print("Weight value should be an integer!")
            return False
        return True

    def get_weight(self):
        while self.weight == "":
            self.weight = input("Weight(kg):")
            if self.weight == "":
                print("Weight field cannot be empty!")
            elif not (self.check_weight()):
                self.weight = ""

    def check_gender(self):
        if self.gender.lower() not in self.gender_list:
            return False
        return True

    def get_gender(self):
        while self.gender == "":
            self.gender == input("Gender (F/f/M/m):")
            if self.gender == "":
                print("Gender field cannot be empty!")
            elif not self.check_gender():
                self.gender = ""

    def parse_birth_of_date(self):
        return datetime.strptime(self.date_of_birth, '%Y.%m.%d')

    def check_birth_of_date(self):
        date_parts = self.date_of_birht.split(".")
        if len(date_parts) == 3:
            for part in date_parts:
                if not part.isdigit():
                    print("Bad date format! It should be YYYY.MM.DD!")
                    return False
            return True
        print("Bad date format! It should be YYYY.MM.DD!")
        return False

    def check_last_donation_date(self):
        pass

    def valid_last_donation_date(self):
        pass

    def check_was_sick(self):
        pass

    def valid_was_sick(self):
        pass

    def check_unique_id(self):
        pass

    def valid_unique_id(self):
        pass

    def check_blood_type(self):
        pass

    def valid_blood_type(self):
        pass

    def check_expiration_of_id(self):
        pass

    def valid_expiration_of_id(self):
        pass

    def check_email_address(self):
        pass

    def valid_email_address(self):
        pass

    def check_mobile_number(self):
        pass

    def valid_mobile_number(self):
        pass


# don = Donor("","","","","","","","","","","")
# don.get_name()

