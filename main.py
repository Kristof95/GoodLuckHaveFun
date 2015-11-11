import Donor
import donation_location
from os import system
import msvcrt



def creat_menu():
    system('cls')
#    print('lol')
#    system('color a')
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

def menu_choose(choosen):
    if choosen=='1':
        system('cls')
        print("New Donor")
        Donor.main()
    elif choosen=='2':
        system('cls')
        print("New Donation event")
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
        system('cls')
        print("Search")
    elif choosen=='7':
        system('cls')
        print("Exit")
    else:
        print("You must choose one!")



if __name__=="__main__":
    creat_menu()
    choosen=msvcrt.getwch()
    menu_choose(choosen)