from excursion import Excursion

def test_excursion_rentals():
    excursion = Excursion()

    # Add members
    excursion.add_member("Maria")
    excursion.add_member("Joseph")
    excursion.add_member("Maja")

    assert set(excursion.get_members()) == {"Maria", "Joseph", "Maja"}

    # Remove a member
    excursion.remove_member("Maja")
    assert set(excursion.get_members()) == {"Maria", "Joseph"}

    # Rent items
    excursion.register_item_rented("Maria", "camping stove")
    excursion.register_item_rented("Joseph", "kayak")
    excursion.register_item_rented("Joseph", "sleeping  mat")

    # Check members who have not returned items
    not_returned = excursion.get_list_not_returned_items()
    assert set(not_returned) == {"Maria", "Joseph"}

    # Return items
    excursion.register_item_returned("Maria", "camping stove")
    excursion.register_item_returned("Joseph", "kayak")

    not_returned = excursion.get_list_not_returned_items()
    assert set(not_returned) == {"Joseph"}  # Joseph still has sleeping  mat

    # Return remaining items
    excursion.register_item_returned("Joseph", "sleeping  mat")
    assert excursion.get_list_not_returned_items() == []