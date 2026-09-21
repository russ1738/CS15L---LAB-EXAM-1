class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        for existing in self.items:
            if existing.name.lower() == item.name.lower():
                print(f"Error: An item named '{item.name}' already exists in inventory.")
                return False
        self.items.append(item)
        print(f"Item '{item.name}' added successfully.")
        return True

    def search(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None

    def update_quantity(self, name, qty):
        item = self.search(name)
        if item is None:
            print(f"Error: Item '{name}' not found.")
            return False
        if qty < 0:
            print("Error: Quantity cannot be negative.")
            return False
        item._quantity = qty
        print(f"Stock for '{item.name}' updated to {item._quantity}.")
        return True

    def display_all(self):
        if not self.items:
            print("The inventory is currently empty.")
            return
        print("\n--- Current Inventory List ---")
        for item in self.items:
            item.display()

    def total_inventory_value(self):
        total = 0.0
        for item in self.items:
            total += item.total_value()
        return total