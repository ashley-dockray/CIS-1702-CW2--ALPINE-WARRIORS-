#Ben
import csv

#view file in a formatted table
def view():
    #reads inventory csv and converts it into a list of lists
    with open("inventory.csv", newline="") as csvfile:
        csv_reader = csv.reader(csvfile) 
        rows = list(csv_reader)
    
    column_widths = []
    #for each column, finds the length of the longest string and stores it in column_widths
    for i in range(len(rows[0])): #loops through each column in the csv
        max_width = 0
        for row in rows: #loops through rows in the csv         
            width = len(row[i])
            if width > max_width:
                max_width = width
        column_widths.append(max_width)

    for row in rows: #loops through rows in the csv
        for i, item in enumerate(row): #gives both the index and the value of each column in the row
            print(item.ljust(column_widths[i] + 2), end="") #pads the string with spaces on the right so its total length is column_widths + 2 for a more neat look
        print()  #new line after each row

#add item to csvfile
def add(item, productid, price, quantity):
    with open("inventory.csv", "a", newline="") as csvfile: #opens csv in append mode
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([item, productid, price, quantity]) #writes the new inputted data into the csv

#asks for what new item the user wants to add and its details
def userinput():
    item = str(input("name of item: "))
    productid = int(input("product ID of item: "))
    price = str(input("price of item: "))
    quantity = int(input("quantity of item: "))
    add(item, productid, price, quantity)


view()



