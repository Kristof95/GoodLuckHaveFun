def delete_donor_from_csv_file():
    del_according_ID = input('Add id which you want to delete:')
    want_to_delete_ans = input('Are sure to delete it?(y/n):')
    delete_from_csv = open("donor.csv", "r+")
    read_csv_line = delete_from_csv.readlines()
    delete_from_csv.seek(0)
    for i in read_csv_line:
        if del_according_ID not in i:
            if want_to_delete_ans.lower() == "y":
                delete_from_csv.write(i)
            elif want_to_delete_ans.lower() == "n":
                pass
            else:
                print("You must choose(y/n)!")
        delete_from_csv.truncate()
        delete_from_csv.close()