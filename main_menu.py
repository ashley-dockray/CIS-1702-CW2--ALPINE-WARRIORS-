#Max

import csv

def load_inventory(): 
    inventory = []
    try: 
        with open("inventory.csv", newline="") as csvfile: # with statement used to open the csv file 
            redaer = csv.reader(csvfile)
            for row in reader: 
                if not row: 
                    continue #skips empty lines 
                if len(row) != 4: 
                    # if the file malformed rows, skip rather than crashing, and keeps runtime stable 
                    continue
                name_raw, id_raw, price_raw, qty_raw = row 
                try: 
                    item = {
                        "id": int(id_raw), 
                        "name": str(name_raw),
                        "price": float(price_raw),
                        "quantity": int(qty_raw)
                    }
                except ValueError: 
                    # skip rows that cannot be converted cleanly 
                    continue
                inventory.append(item) 
        return inventory 
    except FileNotFoundError
        print("inventory file has not been found. starting with an empty inventory.")
        return[]

def save_inventory_file(inventory): 
    try: 
        with open("inventory.csv", "w", newline="") as csvfile: 
            writer = csv.writer(csvfile) 
            for item in inventory:
                writer.writerow([item["name"], item["id"], item["price"], item["quantity"]])
        print("inventory saved successfully.")
    except exeception as e: 
        print(f"error saving inventory: {e}")

def main():
    inventory = load_inventory_file()
    while True:
        print("\n--- Inventory Management Menu ---")
        print("1. Add item")
        print("2. View stock")
        print("3. Update item")
        print("4. Delete item")
        print("5. Search item")
        print("6. Save inventory")
        print("7. Exit")

        choice = input("Select an option (1–7): ").strip()

        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            view_stock(inventory)
        elif choice == "3":
            update_item(inventory)
        elif choice == "4":
            delete_item(inventory)
        elif choice == "5":
            result = search_item(inventory)
        
            if result is not None:
                print("\nItem details")
                print("------------")
                print("ID:", result["id"])
                print("Name:", result["name"])
                print("Price:", result["price"])
                print("Quantity:", result["quantity"])
            else:
                print("Item not found.")

        elif choice == "6":
            save_inventory_file(inventory)
        elif choice == "7":
            try:
                save_inventory_file(inventory)
                print("Exiting program. Inventory saved.")
            except Exception:
                print("Exiting program. Warning: inventory could not be saved.")
            break

if __name__ == "__main__":
    main()

