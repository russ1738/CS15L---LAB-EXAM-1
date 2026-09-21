from items import Item, PerishableItem, ElectronicItem
from inventory import Inventory

def main():
    store_inventory = Inventory()

    while True:
        print("       INVENTORY SYSTEM       ")
        print("1. Add Item")
        print("2. Restock")
        print("3. Sell")
        print("4. Search")
        print("5. Display All Items")
        print("6. Show Total Inventory Value")
        print("7. Exit")

        choice = input("Enter choice (1-7): ").strip()

        if choice == "1":
            print("\nSelect Item Category:")
            print("1. Standard Item")
            print("2. Perishable Item")
            print("3. Electronic Item")
            cat_choice = input("Enter choice (1-3): ").strip()

            name = input("Enter item name: ").strip()
            if not name:
                print("Error: Item name cannot be blank.")
                continue

            try:
                qty = int(input("Enter quantity: "))
                price = float(input("Enter price per unit: "))
                if qty < 0 or price < 0:
                    print("Error: Quantity and price cannot be negative.")
                    continue

                if cat_choice == "1":
                    new_item = Item(name, qty, price)
                    store_inventory.add_item(new_item)
                elif cat_choice == "2":
                    days = int(input("Enter days until expiry: "))
                    new_item = PerishableItem(name, qty, price, days)
                    store_inventory.add_item(new_item)
                elif cat_choice == "3":
                    warranty = int(input("Enter warranty period (in months): "))
                    new_item = ElectronicItem(name, qty, price, warranty)
                    store_inventory.add_item(new_item)
                else:
                    print("Invalid category selected.")
            except ValueError:
                print("Error: Please enter valid numbers for quantity, price, and attributes.")

        elif choice == "2":
            name = input("Enter item name to restock: ").strip()
            item = store_inventory.search(name)
            if item is None:
                print("Item not found.")
            else:
                try:
                    qty = int(input("Enter quantity to add: "))
                    item.restock(qty)
                except ValueError:
                    print("Error: Quantity must be a whole number.")

        elif choice == "3":
            name = input("Enter item name to sell: ").strip()
            item = store_inventory.search(name)
            if item is None:
                print("Item not found.")
            else:
                try:
                    qty = int(input("Enter quantity to sell: "))
                    item.sell(qty)
                except ValueError:
                    print("Error: Quantity must be a whole number.")

        elif choice == "4":
            name = input("Enter item name to search: ").strip()
            item = store_inventory.search(name)
            if item:
                print("\nItem Found:")
                item.display()
            else:
                print(f"No item matching '{name}' found.")

        elif choice == "5":
            store_inventory.display_all()

        elif choice == "6":
            total = store_inventory.total_inventory_value()
            print(f"\nTotal Inventory Value: ₱{total:.2f}")

        elif choice == "7":
            print("Exiting Inventory System. Goodbye!")
            break

        else:
            print("Invalid input. Please choose an option from 1 to 7.")

if __name__ == "__main__":
    main()