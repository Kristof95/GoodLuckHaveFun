from datetime import datetime


def parse_date(date_string):
    return datetime.strptime(date_string, '%Y.%m.%d')


def check_date(date):
    date_parts = date.split(".")
    if len(date_parts) == 3:
        if len(date_parts[0])!=4:
            print("The year is 4 char!")
            return False
        for part in date_parts:
            if not part.isdigit():
                print("Bad date format! It should be YYYY.MM.DD!")
                return False
            if int(date_parts[1]) > 12:
                print("Date incorrect: month cannot be bigger than 12!")
                return False
            if int(date_parts[1])==0:
                print("There is no 0 month")
                return False
            if int(date_parts[1]) < 0:
                print("Month is incorrect: it cannot be minus!\nIt must be a positive integer!")
                return False
            if int(date_parts[2])>31:
                print("There is maximum 31 days")
                return False
            if int(date_parts[1]) == 2 and int(date_parts[2]) > 28:
                print("Month is incorrect: february has 28 days. ")
                return False
            if int(date_parts[0])%4==0 and  int(date_parts[1]) == 2 and int(date_parts[2]) > 29:
                print("In that year february is only 29 days long! (28 in other years)")
                return False
            if (int(date_parts[1])==4 or int(date_parts[1])==6 or int(date_parts[1])==9 or
                        int(date_parts[1])==11) and int(date_parts[2])>30:
                print("This month is only 30 days long!")
                return False
        return True
    print("Bad date format! It should be YYYY.MM.DD!")
    return False


def parse_time_text(time_string):
    return datetime.strptime(time_string,'%H:%M')


def check_time_text(time_text):
    text_parts = time_text.split(":")
    if len(text_parts) == 2:
        for part in text_parts:
            if not part.isdigit():
                print("Bad time format ! It should be HH:MM !")
                return False
        if int(text_parts[0])>23 or int(text_parts[0])<0:
            print("The hour must be between 0 and 23")
            return False
        if int(text_parts[1])>59 or int(text_parts[1])<0:
            print("The minutes must be between 0 and 59")
            return False
        return True
    print("Bad date format ! It should be HH:MM !")
    return False