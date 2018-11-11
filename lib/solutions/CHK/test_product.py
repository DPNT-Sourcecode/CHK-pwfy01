import unittest

from checkout_solution import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        self.products_list = [
            {
                "sku": "A",
                "price": 50,
                "offer_id": [1]
            },
            {
                "sku": "B",
                "price": 50,
                "offer_id": [2]
            }
        ]

    def test_product_is_available(self):
        product = Product('A')
        self.assertTrue(product.is_available())

    def test_product_is_not_available(self):
        product = Product('X')
        self.assertFalse(product.is_available())

    def test_get_available_product_from_list(self):
        product = Product('A')
        self.assertEqual(1, len(product.get_product()))

    def test_get_not_available_product_from_list(self):
        product = Product('X')
        self.assertEqual(0, len(product.get_product()))
