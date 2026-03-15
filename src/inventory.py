class Inventory:
    def __init__(self):
        self.items = {}

    def set_item(self, name, rent_price, amount):
        """Add or update an item in the inventory"""
        self.items[name] = {
            "price": rent_price,
            "amount": amount
        }

    def rent(self, item_name):
        """Rent one unit of the item if available"""
        if item_name in self.items and self.items[item_name]["amount"] > 0:
            self.items[item_name]["amount"] -= 1

    def get_amount_left(self, name):
        """Return the remaining amount of the item"""
        return self.items.get(name, {}).get("amount", 0)