def search_item(name, inventory_data):
    for item in inventory_data:
        if item['name'] == name:
            return item
    return None
