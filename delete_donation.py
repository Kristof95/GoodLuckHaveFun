import msvcrt
import main

def delete_donor_from_csv_file():
    del_according_ID = input('Add ID which you want to delete:')
    del_according_ID = del_according_ID.lower()
    delete_from_csv = open("Data/donor.csv", "r+")
    read_csv_line = delete_from_csv.readlines()
    delete_from_csv.seek(0)
    for i in read_csv_line:
        splited=i.split(',')
        if del_according_ID!=splited[7]:
            delete_from_csv.write(i)
        else:
            sure_about_delete(delete_from_csv,i)
    delete_from_csv.truncate()
    delete_from_csv.close()
    print('1. New delete')
    print('2. Back')
    end_of_delete('donor')


def delete_donations_from_csv_file():
    according_ID = input("Add ID which donation you want to delete:")
    according_ID = according_ID.upper()
    delete_from_csv = open("Data/donations.csv", "r+")
    read_cs_line = delete_from_csv.readlines()
    delete_from_csv.seek(0)
    for i in read_cs_line:
        splited=i.split(',')
        if according_ID!=splited[0]:
            delete_from_csv.write(i)
        else:
            sure_about_delete(delete_from_csv,i)
    delete_from_csv.truncate()
    delete_from_csv.close()
    print('1. New delete')
    print('2. Back')
    end_of_delete('donation_event')

def sure_about_delete(delete_from_csv,i):
    want_to_delete_ans = input('Are sure to delete it?(yes/no):')
    if want_to_delete_ans.lower()=="yes":
        pass
    elif want_to_delete_ans.lower()=="no":
        delete_from_csv.write(i)
    else:
        print("Yes or no!")
        sure_about_delete(delete_from_csv,i)

def end_of_delete(kind):
    get=msvcrt.getwch()
    if get=='1':
        if kind=='donor':
            delete_donor_from_csv_file()
        elif kind=='donation_event':
            delete_donations_from_csv_file()
    elif get=='2':
        main.creat_menu()
    else:
        print("Choose one!")
        end_of_delete(kind)
