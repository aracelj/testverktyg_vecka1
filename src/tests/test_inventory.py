from inventory import Inventory

def test_inventory_rent():
    inv = Inventory()
    inv.set_item("kayak", 100, 5)
    assert inv.get_amount_left("kayak") == 5
    inv.rent("kayak")
    assert inv.get_amount_left("kayak") == 4
