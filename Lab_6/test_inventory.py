
import unittest

from product import Product
from inventory import Inventory


class TestInventory(unittest.TestCase):

    def setUp(self):
        # Create a fresh inventory before each test
        self.inventory = Inventory()
        self.product1 = Product("P001", "Laptop", 1200.00, 15)
        self.product2 = Product("P002", "Mouse", 25.50, 40)

    def test_add_product(self):
        self.inventory.add_product(self.product1)

        self.assertEqual(len(self.inventory.get_all_products()), 1)

    def test_search_existing_product(self):
        self.inventory.add_product(self.product1)

        result = self.inventory.search_product("P001")

        self.assertIsNotNone(result)
        self.assertEqual(result.get_name(), "Laptop")

    def test_search_non_existing_product(self):
        result = self.inventory.search_product("P999")

        self.assertIsNone(result)

    def test_get_all_products(self):
        self.inventory.add_product(self.product1)
        self.inventory.add_product(self.product2)

        result = self.inventory.get_all_products()

        self.assertEqual(len(result), 2)
        self.assertIn(self.product1, result)
        self.assertIn(self.product2, result)


if __name__ == "__main__":
    unittest.main()
