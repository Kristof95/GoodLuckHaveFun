import main
import csv
import donation_location
import os
import msvcrt


donation_listing_order=[1,2,3,4,5,6,7,8,9,10]

#   itten menu, meg cserelehetoseg, meg letrehozunk egy classtagot a megadott elemekkel feltoltve,
#   meg megkerdezzuk hogy akarja-e, esmeghvijuk a get fuggvenyeket



def donation_data_manager(lista):
    #kerd be hogy akar-e
    don = donation_location.Donation_class("","","","","","","","","","")
    print("Old date of event: "+lista[1])
    don.get_date_and_time_of_event()
    print("Old start time of event: "+lista[2])
    print("Old end time of event: "+lista[3])
    don.calculate_duration()
    print("Old zip code: "+lista[4])
    don.get_zip_code()
    print("Old city: "+lista[5])
    don.get_city()
    print("Old address: "+lista[6])
    don.get_address()
    print("Old numbr of available beds: "+lista[7])
    don.get_available_beds()
    don.calculate_max_donor_number()
    print("Old planned donor number: "+lista[8])
    don.get_planned_donor_number()
    print("Old successful donation number: "+lista[9])
    don.get_number_of_successful_donation()
    don.get_donation_success_rate()
##kérdezd meg, hogy biztos-e a modositas
    if save_or_not_answer()=='yes':

        lista[1]=don.date_and_time_of_event
        lista[2]=don.start_time_text
        lista[3]=don.end_time_text
        lista[4]=don.zip_code
        lista[5]=don.city
        lista[6]=don.address
        lista[7]=don.available_beds
        lista[8]=don.planned_donor_number
        lista[9]=don.number_of_successful_donation



    return lista


possible_answers=['yes','no']
def save_or_not_answer():
    answer = input("Do you wanna save?(yes/no):")
    while answer not in possible_answers:
        print("Yes or No!")
        answer=input()
    return answer

def donation_data_modifier():
    lista=[]
    found=0
    os.system('cls')
    change_according_ID=input("What ID you search for: ").upper()
    read_line=open("Data/donations.csv", "r+")
    read_the_list=csv.reader(read_line,delimiter=',',quotechar='"')
    for row in read_the_list:
        if row[0]==change_according_ID:
            found+=1
            lista=row
            print('-'*40)
            print("\t"+"ID: "+row[0])
            print("\t "+row[1])
            print("\t "+row[2]+" - "+row[3])
            print("\t "+row[4]+' '+ row[5]+' '+row[6])
            print('-'*40)
            print('\n')
    read_line.close()
    if found==0:
        print("This ID not found!")
        msvcrt.getwch()
    else:
        delete_from_csv = open("Data/donations.csv", "r+")
        read_csv_line=delete_from_csv.readlines()
        delete_from_csv.seek(0)
        for i in read_csv_line:
            splitted=i.split(',')
            if change_according_ID!=splitted[0]:
                delete_from_csv.write(i)
        delete_from_csv.truncate()
        delete_from_csv.close()
        write_rows=open("Data/donations.csv", 'a', newline='\n')
        writter=csv.writer(write_rows)
        lista=donation_data_manager(lista)
        writter.writerow(lista)
        write_rows.close()
        msvcrt.getwch()
    main.creat_menu()