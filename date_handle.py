from datetime import datetime


def parse_date(date_string):
    return datetime.strptime(date_string, '%Y.%m.%d')


def check_date(date):
    date_parts = date.split(".")
    if len(date_parts) == 3:
        for part in date_parts:
            if not part.isdigit():
                print("Bad date format! It should be YYYY.MM.DD!")
                return False
            if int(date_parts[1]) > 12:
                print("Date incorrect: month cannot be bigger than 12!")
                return False
            if int(date_parts[1]) < 0:
                print("Month is incorrect: it cannot be minus!\nIt must be a positive integer!")
                return False
            if int(date_parts[1]) == 2 and int(date_parts[2]) > 29:
                print("Month is incorrect: february has 29 days. ")
                return False
        return True
    print("Bad date format! It should be YYYY.MM.DD!")
    return False


def parse_time_text(time_string):
    return datetime.strptime(time_string,'%H:%M')


def check_time_text(time_text):
    text_parts = time_text.split(".")
    if len(text_parts) == 2:
        for part in text_parts:
            if not part.isdigit():
                print("Bad time format ! It should be HH:MM !")
                return False
        return True
    print("Bad date format ! It should be HH:MM !")
    return False