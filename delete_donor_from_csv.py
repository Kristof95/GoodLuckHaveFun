def delete_donations_from_csv_file():
    according_ID = input("Add ID which donation you want to delete:")
    delete_from_csv = open("Data\donations.csv", "r+")
    read_cs_line = delete_from_csv.readlines()
    delete_from_csv.seek(0)
    for i in read_cs_line:
        if according_ID not in i:
            delete_from_csv.write(i)
    delete_from_csv.truncate()
    delete_from_csv.close()
