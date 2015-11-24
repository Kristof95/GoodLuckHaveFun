import os
import sys
import csv
import msvcrt
import main


size=os.get_terminal_size()

def search_donor():
    print("You want to search in Donors")
    searching_string=input("What are you looking for?")
    hit=0
    counter=0
    row_number=0
    hits=[]
    global size
    rows=size[1]
    with open(os.path.join(os.path.dirname(sys.argv[0]), "Data\donor.csv"), newline='') as csvfile:
        search_file = csv.reader(csvfile, delimiter=',',quotechar='"')
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
                    hits.append('-'*40)
                    name=row[0].split(" ")
                    if len(name)==2:
                        hits.append(str(counter)+"."+"\t "+name[1]+ ", "+ name[0])
                    elif len(name)==3:
                        hits.append(str(counter)+"."+"\t "+name[2]+", "+name[1]+", "+name[0])
                    hits.append("\t "+row[1]+"kg")
                    hits.append("\t "+row[2][0:4]+"."+row[2][5:7]+"."+row[2][8:10]+"  -  "+row[3]+" years old")
                    hits.append("\t "+row[9])
                    hits.append("\t "+row[10])
                    hits.append("\t "+"ID: "+row[7])
        if hit==0:
            print("There is no things like this!")
        elif hit!=0:
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

    end_of_search()


def search_donation_event():
    print("You want to search in Donation events")
    searching_string=input("What are you looking for?")
    hit=0
    counter=0
    row_number=0
    hits=[]
    global size
    rows=size[1]
    with open(os.path.join(os.path.dirname(sys.argv[0]), "Data\donations.csv"), newline='') as csvfile:
        search_file = csv.reader(csvfile, delimiter=',', quotechar='"')
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
                    hits.append('-'*40)
                    hits.append(str(counter)+"."+"\t"+"ID: "+row[0])
                    hits.append("\t "+row[1])
                    hits.append("\t "+row[2]+" - "+row[3])
                    hits.append("\t "+row[4]+' '+ row[5]+' '+row[6])

        if hit==0:
            print("There is no things like this!")
        elif hit!=0:
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

    end_of_search()

def end_of_search():
    print('1. New search')
    print('2. Back')
    get=msvcrt.getwch()
    if get=='1':
        main.search_menu()
    elif get=='2':
        main.creat_menu()
    else:
        print('Choose one!')
        end_of_search()



