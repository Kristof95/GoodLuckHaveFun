import Donor
import donation_location
import search
import delete_donation
#from os import system
import msvcrt
import os
import sys
import csv
import listing

menu_choosen=['1','2','3','4','5','6','7']

def first_init():
    if os.path.isfile(os.path.join(os.path.dirname(os.sys.argv[0]), "Data\donor.csv")):
        return 0
    else:
        os.system('mkdir Data')
        os.system('fsutil file createnew Data\donor.csv 0')
        os.system('fsutil file createnew Data\donations.csv 0')
        with open(os.path.join(os.path.dirname(sys.argv[0]), "Data\donor.csv"), 'a', newline='\n') as csvfile:
            write_to_donor_csv = csv.writer(csvfile)
            write_to_donor_csv.writerow(["name","weight","date_of_birth","age","last_donation_date","sickness",
                                         "gender","unique_id","expiration_of_id","email_address","blood_type",
                                         "mobile_number","hemoglobin_level"])
        with open(os.path.join(os.path.dirname(sys.argv[0]), "Data\donations.csv"), 'a', newline='\n') as csvfile:
            write_to_donor_csv = csv.writer(csvfile)
            write_to_donor_csv.writerow(["unique_ID","date_and_time_of_event","start_time","end_time","zip_code",
                                         "city","adress","avalaible_beds","planned_donor_number"])
    return 0

def creat_menu():
    os.system('cls')
    print('-'*101)
    print('-'*18+" Welcome to the coolest donor and donation event managing system "+'-'*18)
    print('-'*101)
    print("MAIN MENU")
    print("\t1. Add new Donor")
    print("\t2. Add new Donation event")
    print("\t3. Delete Donor")
    print("\t4. Delete Donation event")
    print("\t5. List Donors or Donation events")
    print("\t6. Search")
    print("\t7. Exit")
    print("Choose one!")
    choosen=msvcrt.getwch()
    if choosen not in menu_choosen:
        creat_menu()
    else:
        menu_choose(choosen)

def menu_choose(choosen):
    if choosen=='1':
        os.system('cls')
        print("New Donor")
        Donor.donor_main()
        print('1. New add donor')
        print('2. Back')
        add_end('donor')
    elif choosen=='2':
        os.system('cls')
        print("New Donation event")
        donation_location.main()
        print('1. New add donation event')
        print('2. Back')
        add_end('donation')
    elif choosen=='3':
        os.system('cls')
        print("Delete Donor")
        delete_donation.delete_donor_from_csv_file()
        print("1. Delete another one")
        print("2. Back")
        choosen=msvcrt.getwch()
        if choosen=='1':
            menu_choose(3)
        elif choosen=='2':
            creat_menu()
    elif choosen=='4':
        os.system('cls')
        print("Delete Donation event")
        delete_donation.delete_donations_from_csv_file()
        print("1. Delete another one")
        print("2. Back")
        choosen=msvcrt.getwch()
        if choosen=='1':
            menu_choose(4)
        elif choosen=='2':
            creat_menu()
    elif choosen=='5':
        os.system('cls')
        print("List Donors or Donation events")
        print("\t1. Donors")
        print("\t2. Donation events")
        print("Choose one!")
        get=msvcrt.getwch()
        if get=="1":
            listing.list_donors()
        elif get=="2":
            listing.list_donations()
        else:
            menu_choose('5')
    elif choosen=='6':
        search_menu()
    elif choosen=='7':
        os.system('exit')
    else:
        print("You must choose one!")

def search_menu():
    os.system('cls')
    print("SEARCH MENU")
    print("\t1. Donor search")
    print("\t2. Donation event search")
    print("\t3. Back")
    search_type=msvcrt.getwch()
    if search_type=="1":
        search.search_donor()
    elif search_type=="2":
        search.search_donation_event()
    elif search_type=="3":
        creat_menu()
    else:
        search_menu()

def add_end(kind):
    get=msvcrt.getwch()
    if get=='1':
        if kind=='donor':
            menu_choose('1')
        elif kind=='donation':
            menu_choose('2')
    elif get=='2':
        creat_menu()
    else:
        print('Choose one!')
        add_end(kind)





if __name__=="__main__":
    first_init()
    creat_menu()
