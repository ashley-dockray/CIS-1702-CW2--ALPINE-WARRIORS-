def search_item( inventory_data): # imports the inventory data
    while True: 
        name = input('enter product name') # allows user to enter the name of the product
        for item in inventory_data: # itterates through the data in search for the name
            if item['name'] == name:
                return item  # retruns the item of matching name 
        print('sorry item not found, Please try again')
