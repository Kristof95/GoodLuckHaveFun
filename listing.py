import os
import sys
import csv
import msvcrt
import main

size=os.get_terminal_size()

def list_donors():
    hit=0
    counter=0
    row_number=-1
    hits=[]
    global size
    rows=size[1]
    with open(os.path.join(os.path.dirname(sys.argv[0]), "Data\donor.csv"), newline='') as csvfile:
        search_file = csv.reader(csvfile, delimiter=',')
        for row in search_file:
            if row!="":
                row_number+=1
            if row_number>0:
                hits.append('-'*40)
                name=row[0].split(" ")
                if len(name)==2:
                    hits.append(str(row_number)+"."+"\t "+name[1]+ ", "+ name[0])
                elif len(name)==3:
                    hits.append(str(row_number)+"."+"\t "+name[2]+", "+name[1]+", "+name[0])
                hits.append("\t "+row[1]+"kg")
                hits.append("\t "+row[2][0:4]+"."+row[2][5:7]+"."+row[2][8:10]+"  -  "+row[3]+" years old")
                hits.append("\t "+row[9])
                hits.append("\t "+row[10])
                hits.append("\t "+"ID: "+row[7])
        if row_number==0:
            print("There is nothing in the list!")
            msvcrt.getwch()
            main.creat_menu()

        elif row_number>0:
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
    global size
    rows=size[1]
    with open(os.path.join(os.path.dirname(sys.argv[0]), "Data\donor.csv"), newline='') as csvfile:
        search_file = csv.reader(csvfile, delimiter=',')
        for row in search_file:
            if row!="":
                row_number+=1
            if row_number>0:
                hits.append('-'*40)
                hits.append(str(row_number)+"."+"\t"+"ID: "+row[0])
                hits.append("\t "+row[1])
                hits.append("\t "+row[2]+" - "+row[3])
                hits.append("\t "+row[4]+' '+ row[5]+' '+row[6])
        if row_number==0:
            print("There is nothing in the list!")
            msvcrt.getwch()
            main.creat_menu()
        elif row_number>0:
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
