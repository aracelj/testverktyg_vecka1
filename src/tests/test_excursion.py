import pytest
from excursion import Excursion


@pytest.fixture
def excursion():
    excursion = Excursion()
    excursion.add_member("Maria")
    excursion.add_member("Joseph")
    excursion.add_member("Maja")
    return excursion

@pytest.fixture
def members(excursion):
    # Returns current members list dynamically
    return lambda: excursion.get_members()

def test_add_get_members(excursion):
    members = excursion.get_members()
    assert "Maria" in members
    assert "Joseph" in members
    assert "Maja" in members
    assert len(members) == 3

def test_remove_members(excursion):
    # Remove a member
    excursion.remove_member("Maja")
    members = excursion.get_members()
    assert "Maria" in members
    assert "Joseph" in members
    assert "Maja" not in members

def test_register_item_rented_and_returned(excursion):
    # Rent items
    excursion.register_item_rented("Maria", "camping stove")
    excursion.register_item_rented("Joseph", "kayak")
    excursion.register_item_rented("Maja", "sleeping mat")

    # Return items
    excursion.register_item_returned("Maria", "camping stove")
    excursion.register_item_returned("Joseph", "kayak")
    excursion.register_item_returned("Maja", "sleeping mat")

    assert excursion.get_all_who_has_not_returned_items() == []

def test_get_all_who_has_not_returned_items(excursion):
    excursion.register_item_rented("Maria", "camping stove")
    excursion.register_item_rented("Joseph", "kayak")
    excursion.register_item_rented("Maja", "sleeping mat")

    # Maria & Joseph returns the item
    excursion.register_item_returned("Maria", "camping stove")
    excursion.register_item_returned("Joseph", "kayak")

    not_returned = excursion.get_all_who_has_not_returned_items()
    assert set(not_returned) == {"Maja"}  # Maja still has sleeping mat



