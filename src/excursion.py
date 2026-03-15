class Excursion:
    def __init__(self):
        self.members = set()  # store member names
        self.rented_items = {}  # {member_name: set of items rented}

    def get_members(self):
        return list(self.members)

    def add_member(self, name):
        self.members.add(name)
        if name not in self.rented_items:
            self.rented_items[name] = set()

    def remove_member(self, name):
        self.members.discard(name)
        self.rented_items.pop(name, None)

    def register_item_rented(self, member_name, item_name):
        if member_name in self.members:
            self.rented_items.setdefault(member_name, set()).add(item_name)

    def register_item_returned(self, member_name, item_name):
        if member_name in self.members:
            self.rented_items.get(member_name, set()).discard(item_name)

    def get_list_not_returned_items(self):
        # members with non-return rented item sets
        return [member for member, items in self.rented_items.items() if items]