import main
import csv
import Donor
import os
import msvcrt


donor_listing_order=[1,2,3,4,5,6,7,8,9,10,11,12,13]

#   itten menu, meg cserelehetoseg, meg letrehozunk egy classtagot a megadott elemekkel feltoltve,
#   meg megkerdezzuk hogy akarja-e, esmeghvijuk a get fuggvenyeket



def donor_data_manager(lista):
    donor_data = Donor.create_class()
    print("What you want to change?: \n"
                      "1. name\n"
                      "2. weight\n"
                      "3. date of birth\n"
                      "4. age\n"
                      "5. last donation date\n"
                      "6. sickness\n"
                      "7. gender\n"
                      "8. unique id\n"
                      "9. expiration of id\n"
                      "10. email address\n"
                      "11. blood type\n"
                      "12. mobile_number\n"
                      "13. hemoglobin_level\n")
    order_donor=int(input())
    while order_donor not in donor_listing_order:
        print("choose from above")
        order_donor=int(input())
        ####NAME####
    if order_donor == 1:
        print("Old name:"+lista[0])
        donor_data.get_name()
        if save_or_not_answer()=="yes":
            lista[0]=donor_data.name
        else:
            return lista

        ####WEIGHT####
    if order_donor == 2:
        print("Old weight:"+lista[1])
        donor_data.get_weight()
        if save_or_not_answer()=="yes":
            lista[1]=donor_data.weight
        return lista


        ####DATE OF BIRTH####
    if order_donor == 3:
        print("Old date of birth:"+lista[2])
        donor_data.get_birth_of_date()
        if save_or_not_answer()=="yes":
            lista[2]=donor_data.birth_of_date
        else:
            return lista

        ####Age####
    if order_donor == 4:
        print("Old age:"+lista[3])
        age=""
        while age=="":
            age=input("new age: ")
            if not age.isdigit():
                age=""
        if save_or_not_answer()=="yes":
            lista[3]=age
        else:
            return lista

       ###LastDonation###
    if order_donor == 5:
        print("Old last donation date:"+lista[4])
        donor_data.get_last_donation_date()
        if save_or_not_answer()=="yes":
            lista[4]=donor_data.last_donation_date
        else:
            return lista

        ####Sickness###
    if order_donor == 6:
        print("Old sickness:"+lista[5])
        donor_data.get_sickness()
        if save_or_not_answer()=="yes":
            lista[5]=donor_data.was_sick
        else:
            return lista

        ###Gender###
    if order_donor == 7:
        print("Old gender:"+lista[6])
        donor_data.get_gender()
        if save_or_not_answer()=="yes":
            lista[6]=donor_data.gender
        else:
            return lista

        ####uniqueID###
    if order_donor == 8:
        print("Old uniqueID:"+lista[7])
        donor_data.get_unique_id()
        if save_or_not_answer()=="yes":
            lista[7]=donor_data.unique_id
        else:
            return lista

        ###expirationofid###
    if order_donor == 9:
        print("Old expiration of ID:"+lista[8])
        donor_data.get_expiration_of_id()
        if save_or_not_answer()=="yes":
            lista[8]=donor_data.expiration_of_id
        else:
            return lista

        ###emailadress#
    if order_donor == 10:
        print("Old email address:"+lista[9])
        donor_data.get_email_adress()
        if save_or_not_answer()=="yes":
            lista[9]=donor_data.email_adress
        else:
            return lista

        ###bloodtype###
    if order_donor == 11:
        print("Old bloody type:"+lista[10])
        donor_data.get_blood_type()
        if save_or_not_answer()=="yes":
            lista[10]=donor_data.blood_type
        else:
            return lista

        ###mobilenumber###
    if order_donor == 12:
        print("Old mobile number:"+lista[11])
        donor_data.get_mobile_number()
        if save_or_not_answer()=="yes":
            lista[11]=donor_data.mobile_number
        else:
            return lista

        ####hemoglobinlevel
    if order_donor == 13:
        print("Old hemoglobin:"+lista[12])
        hemoglobin=""
        while hemoglobin=="":
            hemoglobin=input("new hemoglobin: ")
            if not hemoglobin.isdigit():
                hemoglobin=""
        if save_or_not_answer()=="yes":
            lista[12]=hemoglobin
        else:
            return lista

    return lista

possible_answers=['yes','no']
def save_or_not_answer():
    answer = input("Do you wanna save?(yes/no):")
    while answer not in possible_answers:
        print("Yes or No!")
        answer=input()
    return answer

def donor_data_modifier():
    lista=[]
    found=0
    os.system('cls')
    change_according_ID=input("What ID you search for: ").lower()
    read_line=open("Data/donor.csv", "r+")
    read_the_list=csv.reader(read_line,delimiter=',',quotechar='"')
    for row in read_the_list:
        if row[7]==change_according_ID:
            found+=1
            lista=row
            print('-'*40)
            name=row[0].split(" ")
            if len(name)==2:
                print("\t "+name[1]+ ", "+ name[0])
            elif len(name)==3:
                print("\t "+name[2]+", "+name[1]+", "+name[0])
            print("\t "+str(row[1])+"kg")
            print("\t "+row[2][0:4]+"."+row[2][5:7]+"."+row[2][8:10]+"  -  "+str(row[3])+" years old")
            print("\t "+row[9])
            print("\t "+row[10])
            print("\t "+"ID: "+row[7])
            print('-'*40)
            print('\n')
    read_line.close()
    if found==0:
        print("This ID not found!")
        msvcrt.getwch()
    else:
        delete_from_csv = open("Data/donor.csv", "r+")
        read_csv_line=delete_from_csv.readlines()
        delete_from_csv.seek(0)
        for i in read_csv_line:
            splitted=i.split(',')
            if change_according_ID!=splitted[7]:
                delete_from_csv.write(i)
        delete_from_csv.truncate()
        delete_from_csv.close()
        write_rows=open("Data/donor.csv", 'a', newline='\n')
        writter=csv.writer(write_rows)
        lista=donor_data_manager(lista)
        writter.writerow(lista)
        write_rows.close()
        msvcrt.getwch()
    main.creat_menu()

