import os
import sys
import csv

def search_donor():
    print("You want to search in Donors")
    searching_string=input("What are you looking for?")
    hit=0
    counter=0
    row_number=0
    with open(os.path.join(os.path.dirname(sys.argv[0]), "Data\donor.csv"), newline='') as csvfile:
        search_file = csv.reader(csvfile, delimiter=',')
        for row in search_file:
            row_number+=1
            found=0
            for coll in row:
                if searching_string in coll:
                    found=1
                    hit=1
            if found ==1:
                if row_number==1:
                    hit=0
                else:
                    counter+=1
                    print('-'*40)
                    name=row[0].split(" ")
                    if len(name)==2:
                        print(str(counter)+"."+"\t",name[1]+ ",", name[0])
                    elif len(name)==3:
                        print(str(counter),"."+"\t",name[2]+",",name[1]+",",name[0])
                    print("\t",row[1]+"kg")
                    print("\t",row[2][0:4]+"."+row[2][5:7]+"."+row[2][8:10]," - ",row[3],"years old")
                    print("\t",row[9])
                    print("\t",row[10])
                    print("\t","ID: "+row[7])
        if hit==0:
            print("There is no things like this!")

def search_donation_event():
    print("You want to search in Donation events")
    searching_string=input("What are you looking for?")
    hit=0
    counter=0
    row_number=0
    with open(os.path.join(os.path.dirname(sys.argv[0]), "Data\donations.csv"), newline='') as csvfile:
        search_file = csv.reader(csvfile, delimiter=',')
        for row in search_file:
            row_number+=1
            found=0
            for coll in row:
                if searching_string in coll:
                    found=1
                    hit=1
            if found ==1:
                if row_number==1:
                    hit=0
                else:
                    counter+=1
                    print('-'*40)
                    print(str(counter)+"."+"\t"+"ID: "+row[0])
                    print("\t",row[1])
                    print("\t",row[2]+" - "+row[3])
                    print("\t",row[4], row[5], row[6])
        if hit==0:
            print("There is no things like this!")


