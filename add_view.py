import csv

with open("inventory.csv", "r") as csvfile:
    data = csv.reader(csvfile)
    for lines in data:
        print(lines)
