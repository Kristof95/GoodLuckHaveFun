import os
import sys
import csv
import msvcrt
import main
from operator import itemgetter

size=os.get_terminal_size()
donor_listing_order=[1,2,3,4,5,6,7,8,9,10,11,12,13]
donation_listing_order=[1,2,3,4,5,6,7,8,9,10]

def list_donors():
    counter=0
    row_number=-1
    hits=[]
    total=[]
    global size
    rows=size[1]
    with open(os.path.join(os.path.dirname(sys.argv[0]), "Data\donor.csv"), newline='') as csvfile:
        search_file = csv.reader(csvfile, delimiter=',',quotechar='"')
        for row in search_file:
            if row!="":
                row_number+=1
            if row_number>0:
                total.append(row)
        if row_number==0:
            print("There is nothing in the list!")
            msvcrt.getwch()
            main.creat_menu()
        elif row_number>0:
            print("What should be the order:\n"
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
            if int(order_donor) in donor_listing_order:
                for order_int in total:
                    order_int[1]=int(order_int[1])
                    order_int[3]=int(order_int[3])
                    order_int[12]=int(order_int[12])
                total=sorted(total, key=itemgetter(int(order_donor)-1))
                for i in total:
                    counter+=1
                    hits.append('-'*40)
                    name=i[0].split(" ")
                    if len(name)==2:
                        hits.append(str(counter)+"."+"\t "+name[1]+ ", "+ name[0])
                    elif len(name)==3:
                        hits.append(str(counter)+"."+"\t "+name[2]+", "+name[1]+", "+name[0])
                    hits.append("\t "+str(i[1])+"kg")
                    hits.append("\t "+i[2][0:4]+"."+i[2][5:7]+"."+i[2][8:10]+"  -  "+str(i[3])+" years old")
                    hits.append("\t "+i[9])
                    hits.append("\t "+i[10])
                    hits.append("\t "+"ID: "+i[7])
                os.system('cls')
                page_row=(rows-1)//7
                page=0
                length=len(hits)
                while page<length:
                    os.system('cls')
                    for i in range(0+page,page_row*7+page):
                        if i<length:
                            print(hits[i])
                        else:
                            break
                    key=msvcrt.getwch()
                    if key=='s':
                        page+=page_row*7
                    if key=='w':
                        page-=page_row*7
                        if page<0:
                            page=0

        main.creat_menu()

def list_donations():
    row_number=-1
    hits=[]
    total=[]
    counter=0
    global size
    rows=size[1]
    with open(os.path.join(os.path.dirname(sys.argv[0]), "Data\donations.csv"), newline='') as csvfile:
        search_file = csv.reader(csvfile, delimiter=',',quotechar='"')
        for row in search_file:
            if row!="":
                row_number+=1
            if row_number>0:
                total.append(row)

        if row_number==0:
            print("There is nothing in the list!")
            msvcrt.getwch()
            main.creat_menu()
        elif row_number>0:
            print("What should be the order:\n"
                  "1. id\n"
                  "2. date of event\n"
                  "3. start time\n"
                  "4. end time\n"
                  "5. zip_code\n"
                  "6. city\n"
                  "7. address\n"
                  "8. number of available beds\n"
                  "9. planned donor number\n"
                  "10. final_donor_number")
            order_donation=int(input())
            while order_donation not in donation_listing_order:
                print("choose from above")
                order_donation=int(input())
            if int(order_donation) in donor_listing_order:
                for order_int in total:
                    order_int[7]=int(order_int[7])
                    order_int[8]=int(order_int[8])
                    order_int[9]=int(order_int[9])
                total=sorted(total, key=itemgetter(int(order_donation)-1))
                for i in total:
                    counter+=1
                    hits.append('-'*40)
                    hits.append(str(counter)+"."+"\t"+"ID: "+i[0])
                    hits.append("\t "+i[1])
                    hits.append("\t "+i[2]+" - "+i[3])
                    hits.append("\t "+i[4]+' '+ i[5]+' '+i[6])
            os.system('cls')
            page_row=(rows-1)//5
            page=0
            length=len(hits)
            while page<length:
                os.system('cls')
                for i in range(0+page,page_row*5+page):
                    if i<length:
                        print(hits[i])
                    else:
                        break
                key=msvcrt.getwch()
                if key=='s':
                    page+=page_row*5
                if key=='w':
                    page-=page_row*5
                    if page<0:
                        page=0
        main.creat_menu()
