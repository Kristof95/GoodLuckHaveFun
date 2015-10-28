class Donor:

# variables
    get_name = ""
    get_weight = ""
    get_gender = ""
    get_date_of_birht = ""
    get_last_donation_date = ""
    get_was_sick = ""
    get_unique_id = ""
    get_blood_type = ""
    get_expiration_of_id = ""
    get_email_address = ""
    get_mobile_number = ""


# lists
    was_sick = ('y', 'n')
    gender = ('f', 'm')
    blood_type = ('a', 'b', 'ab', '0')


# functions
    def __init__(self):
        pass

    def parse_name(self):
        splitted = self.get_name.split(",")
        full_name = {}
        if len(splitted) > 0:
            full_name['first_name'] = splitted[0]
        if len(splitted) > 1:
            full_name['last_name'] = splitted[1]
        return full_name

    def valid_name(self):
        name_parts = self.get_name.split(" ")
        if not name_parts == 2:
            return False
        return True

    def check_name(self):
        if not self.get_name.isalpha():
            return False
        return True

    def check_weight(self):
        pass

    def valid_weight(self):
        pass

    def check_gender(self):
        pass

    def valid_gender(self):
        pass

    def check_birth_of_date(self):
        pass

    def valid_check_of_date(self):
        pass

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

    while get_name == "":
        get_name = input("Your name:")
        if get_name == "":
            print("Name field cannot be empty!")
        elif not valid_name(get_name) and check_name(get_name):
            get_name = ""
