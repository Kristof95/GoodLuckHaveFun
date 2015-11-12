import Donor
import donation_location
import search
#from os import system
import msvcrt
import os
import sys
import csv


def first_init():
    if os.path.isfile(os.path.join(os.path.dirname(os.sys.argv[0]), "Data\donor.csv")):
        return 0
    else:
        os.system('mkdir Data')
        os.system('fsutil file createnew Data\donor.csv 0')
        os.system('fsutil file createnew Data\donotions.csv 0')
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
    choosen=msvcrt.getwch()
    menu_choose(choosen)

def menu_choose(choosen):
    if choosen=='1':
        os.system('cls')
        print("New Donor")
        Donor.main()
    elif choosen=='2':
        os.system('cls')
        print("New Donation event")
        donation_location.main()
    elif choosen=='3':
        os.system('cls')
        print("Delete Donor")
    elif choosen=='4':
        os.system('cls')
        print("Delete Donation event")
    elif choosen=='5':
        os.system('cls')
        print("List Donors or Donation events")
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




if __name__=="__main__":
    first_init()
    creat_menu()
