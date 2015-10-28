#import donor
#import donation

type_of_register=["Donor","Donation"]
ENTER_DATA_TEXT = "Enter"


def print_separator_line():
    print("* "*32)


def greetings():
    print("Welcome in the donation register center!")
    print_separator_line()
    print("Which type of registration would you like to do?(Donor/Donation) ")


def get_type():
    type=input().lower()
    if type=="":
        print("This can't be empty!")
        print("Which type of registration would you like to do?(Donor/Donation) ")
        get_type()
    elif type==type_of_register[0].lower() or type==type_of_register[1].lower():
        print("You choosed: ",type)
    else:
        print("You must choose from the types of above!")
        print("Which type of registration would you like to do?(Donor/Donation) ")
        get_type()
    pass

if __name__=="__main__":
    greetings()
    get_type()
