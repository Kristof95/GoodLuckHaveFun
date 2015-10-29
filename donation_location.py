from datetime import datetime
class Donation_class:
    available_cities = ("miskolc", "szerencs", "sarospatak", "kazincbarcika")


    date_and_time_of_event = ""
    start_time_text = ""
    end_time_text = ""
    zip_code = ""
    city = ""
    address = ""
    number_of_successful_donation = ""
    available_beds = ""
    planned_donor_number = ""
    preparation_time = 30
    donation_time = 30

    def __init__ (self, date_and_time_of_event, start_time_text, end_time_text, zip_code, city, address, number_of_successful_donation, available_beds, planned_donor_number, available_cities):
        self.date_and_time_of_event = date_and_time_of_event
        self.start_time_text = start_time_text
        self.end_time_text = end_time_text
        self.zip_code = zip_code
        self.city = city
        self.address = address
        self.number_of_successful_donation = number_of_successful_donation
        self.available_beds = available_beds
        self.planned_donor_number = planned_donor_number
        self.available_cities = available_cities


    def calculate_duration_in_minutes(start, end):
        return (end - start).seconds // 60

    def max_donor_number(duration_in_minutes, preparation_time, donation_time, available_beds):
        print(((duration_in_minutes - preparation_time) / donation_time) * int(available_beds))
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
       return True

    def check_number_of_successful_donation(self):
        if self.number_of_successful_donation == "":
            print("Success donation number can't be empty")
        if not self.number_of_successful_donation.isdigit():
            print("Success donation number should be digits!")
            return False
        return True


    def validate_date_and_time_of_event(self):
        date_event = self.parse_date()
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
            print("Not good city")
            return False
        return True

    def get_donation_success_rate(planned_donor_number, number_of_successful_donation_string):
        rate = number_of_successful_donation_string / planned_donor_number

        if rate < 0.2:
            print ("Unsuccessful, not worth to organise there again.")
        elif rate <= 0.75:
            print ("Normal event.")
        elif rate <= 1.1:
            print ("Successful.")
        else:
            print ("Outstanding.")



    def get_date_and_time_of_event(self):
        while self.date_and_time_of_event == "":
            self.date_and_time_of_event = input("Event day:")
            if not (self.check_date_and_time_of_event()and self.validate_date_and_time_of_event()):
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
            if not (self.check_number_of_successful_donation()):
                self.number_of_successful_donation = ""

    def get_planned_donor_number(self):
        while self.planned_donor_number == "":
            self.planned_donor_number = input("Planned number:")
            if not (self.check_planned_donor_number()):
                self.planned_donor_number = ""

    def get_start_time_text(self):
        while self.start_time_text == "":
            self.start_time_text = input("Start time:")
            if not (self.check_time_text()):
                self.start_time_text = ""

    def get_end_time(self):
        while self.end_time_text == "":
            self.end_time_text = input("End time:")
            if not (self.check_time_text()):
                self.end_time_text = ""


    #duration = calculate_duration_in_minutes(start_time, end_time)


    #max_donor_number(duration, preparation_time, donation_time, available_beds)
    #get_donation_success_rate(int(planned_donor_number), int(number_of_successful_donation))




don = Donation_class("","","","","","","","","","")
don.get_date_and_time_of_event()
don.get_start_time_text()
start_time_string=don.start_time_text
don.start_time=don.parse_time_text(start_time_string)
