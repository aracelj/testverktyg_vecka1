class Inventory:
    def __init__(self, db):
        self.db = db

    def set_item(self, name, rent_price, amount):
        self.db[name] = {"rent_price": rent_price, "amount": amount}

    def rent(self, item_name):
        if self.db[item_name]["amount"] > 0:
            self.db[item_name]["amount"] -= 1

    def get_amount_left(self, name):
        return self.db.get(name, {}).get("amount", 0)
