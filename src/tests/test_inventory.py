import pytest
from inventory import Inventory


@pytest.fixture
def inventory():
    return Inventory()


def test_set_item(inventory):
    inventory.set_item("kayak", 100, 5)
    assert inventory.get_amount_left("kayak") == 5


def test_rent(inventory):
    inventory.set_item("kayak", 100, 5)
    inventory.rent("kayak")
    assert inventory.get_amount_left("kayak") == 4