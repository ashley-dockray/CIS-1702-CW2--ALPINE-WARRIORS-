# Robbie – Update and Delete items from inventory

def update_item(inventory):

    # Get valid item ID or return to menu
    while True:
        
        user_input = input("Enter item ID to update (or M to return to menu): ").strip()

        if user_input.lower() == "m":
            return

        try:
            item_id = int(user_input)
        except ValueError:
            print("ID must be a whole number.")
            continue

        
        item = None
        for i in inventory:
            if i["id"] == item_id:
                item = i
                break

        if item is not None:
            break

        print("Item not found.")
        choice = input("Enter R to retry or M to return to menu: ").strip().lower()
        if choice == "m":
            return

    # Getting valid name
    while True:
        new_name = input("Enter new name: ").strip()
        if new_name != "":
            break
        print("Name cannot be blank.")

    # Getting valid price
    while True:
        try:
            new_price = float(input("Enter new price: ").strip())
            if new_price >= 0:
                break
            print("Price cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")

    # Getting valid quantity
    while True:
        try:
            new_quantity = int(input("Enter new quantity: ").strip())
            if new_quantity >= 0:
                break
            print("Quantity cannot be negative.")
        except ValueError:
            print("Please enter a whole number.")

    item["name"] = new_name
    item["price"] = new_price
    item["quantity"] = new_quantity

    print("Item updated.")

# Deleting items

def delete_item(inventory):

    while True:
        user_input = input("Enter item ID to delete (or M to return to menu): ").strip()

        if user_input.lower() == "m":
            return

        try:
            item_id = int(user_input)
        except ValueError:
            print("ID must be a whole number.")
            continue
        
        for i in range(len(inventory)):
            if inventory[i]["id"] == item_id:
                del inventory[i]
                print("Item deleted.")
                return

        print("Item not found.")
        choice = input("Enter R to retry or M to return to menu: ").strip().lower()
        if choice == "m":
            return


# ====== Temporary testing code =======

if __name__ == "__main__":
    inventory = [
    {"id": 1, "name": "Apple", "price": 0.50, "quantity": 10},
    {"id": 2, "name": "Milk", "price": 1.20, "quantity": 5}
]
    
    print("Inventory before update:", inventory)
    update_item(inventory)
    print("Inventory after update:", inventory)

    print("\nInventory before delete:", inventory)
    delete_item(inventory)
    print("Inventory after delete:", inventory)