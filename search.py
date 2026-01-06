def search_item(inventory_data):
    name = input('Enter product name: ').strip()
    for item in inventory_data:
        if item['name'].lower() == name.lower():
            return item
    return None
