class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self._quantity = int(quantity)  #protected/private attribute
        self._price = float(price)     #protected/private attribute

    def restock(self, qty):
        if qty <= 0:
            print("Error: Restock quantity must be greater than zero.")
            return False
        self._quantity += qty
        print(f"Successfully added {qty} units. Current stock: {self._quantity}")
        return True

    def sell(self, qty):
        if qty <= 0:
            print("Error: Sell quantity must be greater than zero.")
            return False
        if qty > self._quantity:
            print(f"Error: Not enough stock. Only {self._quantity} available.")
            return False
        self._quantity -= qty
        print(f"Sold {qty} units. Remaining stock: {self._quantity}")
        return True

    def total_value(self):
        return self._quantity * self._price

    def display(self):
        print(f"Item: {self.name} | Qty: {self._quantity} | Price: ₱{self._price:.2f} | Total Value: ₱{self.total_value():.2f}")


class PerishableItem(Item):
    def __init__(self, name, quantity, price, days_until_expiry):
        super().__init__(name, quantity, price)
        self.days_until_expiry = int(days_until_expiry)

    def is_expiring_soon(self):
        return self.days_until_expiry <= 3

    def total_value(self):
        base_value = self._quantity * self._price
        if self.is_expiring_soon():
            return base_value * 0.5  
        return base_value

    def display(self):
        status = "EXPIRING SOON (50% Off Applied)" if self.is_expiring_soon() else "Fresh"
        print(f"Perishable: {self.name} | Qty: {self._quantity} | Price: ₱{self._price:.2f} | Expiry in: {self.days_until_expiry} days ({status}) | Total Value: ₱{self.total_value():.2f}")


class ElectronicItem(Item):
    def __init__(self, name, quantity, price, warranty_months):
        super().__init__(name, quantity, price)
        self.warranty_months = int(warranty_months)

    def display(self):
        print(f"Electronic: {self.name} | Qty: {self._quantity} | Price: ₱{self._price:.2f} | Warranty: {self.warranty_months} months | Total Value: ₱{self.total_value():.2f}")