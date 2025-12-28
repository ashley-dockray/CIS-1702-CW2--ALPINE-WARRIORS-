inventory_json= [{"id": 101, "name": "Wireless Mouse", "price": 25.50, "stock": 15},
{"id": 102, "name": "Mechanical Keyboard", "price": 120.00, "stock":
8},
{"id": 103, "name": "USB-C Hub", "price": 45.99, "stock": 0},
{"id": 104, "name": "Monitor Stand", "price": 29.99, "stock": 12}]


def search_item(Name, inventory_data):
    for items in inventory_data:
        if items['name'] == Name:
            print (items)
        else:
            None


if __name__=="__main__":
    search_item('USB-C Hub', inventory_json)
