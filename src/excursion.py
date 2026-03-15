class Excursion:
    def __init__(self):
        # Internal storage
        self.members = {}  # member_name -> list of rented items

    def get_members(self):
        return list(self.members.keys())

    def add_member(self, name):
        if name not in self.members:
            self.members[name] = []

    def remove_member(self, name):
        if name in self.members:
            del self.members[name]

    def register_item_rented(self, member_name, item_name):
        if member_name in self.members:
            self.members[member_name].append(item_name)

    def register_item_returned(self, member_name, item_name):
        if member_name in self.members and item_name in self.members[member_name]:
            self.members[member_name].remove(item_name)

    def get_all_who_has_not_returned_items(self):
        return [member for member, items in self.members.items() if items]