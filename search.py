def search_item(inventory_data):
    name = input('Enter product name: ').strip() # saves the product name as an input, removing unnecisary spacings
    for item in inventory_data: #iterates through the data in search for item with that name 
        if item['name'].lower() == name.lower(): #compares each item with the name 
            return item #returnes the correct item
    return None
