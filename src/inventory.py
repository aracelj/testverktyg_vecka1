class Inventory:
    def __init__(self, db):
        self.db = db

    def set_item(self, name, rent_price, amount):
        self.db[name] = {"rent_price": rent_price, "quantity": amount}

    def get_quantity_left(self, name):
        return self.db.get(name, {}).get("quantity", 0)

    def rent(self, item_name):
        if self.db[item_name]["quantity"] > 0:
            self.db[item_name]["quantity"] -= 1
        else:
            raise ValueError(f"Item {name} is not available to rent")


