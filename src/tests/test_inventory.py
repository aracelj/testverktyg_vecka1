import pytest
from inventory import Inventory

class DummyDB:
    def __init__(self):
        self.data = {}


# Fixture for db
@pytest.fixture
def db():
    return {}

@pytest.fixture
def inventory(db):
    return Inventory(db)


def test_set_item(inventory):
    inventory.set_item("kayak", 100, 5)
    assert inventory.get_quantity_left("kayak") == 5


def test_rent(inventory):
    inventory.set_item("kayak", 100, 5)
    inventory.rent("kayak")
    assert inventory.get_quantity_left("kayak") == 4