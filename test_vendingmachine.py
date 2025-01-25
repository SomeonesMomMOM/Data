import unittest
from product import Product
from vending_machine import VendingMachine

class TestVendingMachine(unittest.TestCase):
    def setUp(self):
        products = [
            Product("Premium Cola", 1.5, 10),
            Product("Makava", 1.4, 3),
            Product("Wostok", 0.8, 5),
            Product("Club Mate", 1.0, 1)
        ]
        self.vm = VendingMachine(products, 5.0)

    def test_purchase_success(self):
        self.vm.process_purchase(1, 2.0)
        self.assertEqual(self.vm.products[0].stock, 9)

    def test_out_of_stock(self):
        self.vm.process_purchase(4, 1.0)
        self.vm.process_purchase(4, 1.0)
        self.assertEqual(self.vm.products[3].stock, 0)

    def test_insufficient_funds(self):
        with self.assertRaises(AssertionError):
            self.vm.process_purchase(1, 1.0)

if __name__ == "__main__":
    unittest.main()
