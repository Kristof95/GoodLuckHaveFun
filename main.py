import Donor
import donation_location
import search
from os import system
import msvcrt




def creat_menu():
    system('cls')
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
        system('cls')
        print("New Donor")
        Donor.main()
    elif choosen=='2':
        system('cls')
        print("New Donation event")
        donation_location.main()
    elif choosen=='3':
        system('cls')
        print("Delete Donor")
    elif choosen=='4':
        system('cls')
        print("Delete Donation event")
    elif choosen=='5':
        system('cls')
        print("List Donors or Donation events")
    elif choosen=='6':
        search_menu()
    elif choosen=='7':
        system('exit')
    else:
        print("You must choose one!")

def search_menu():
    system('cls')
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
    creat_menu()
