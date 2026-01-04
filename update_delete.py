#Robbie
# This script updates and deletes records in a CSV file.

import csv 

with open("inventory.csv", "w") as csvfile:
    data = csv.writer(csvfile)
