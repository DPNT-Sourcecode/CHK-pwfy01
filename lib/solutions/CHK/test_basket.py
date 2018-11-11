import unittest

from checkout_solution import Basket, checkout


class TestBasket(unittest.TestCase):

    def setUp(self):
        self.valid_basket_1 = u'AAbC'
        self.valid_basket_2 = u''
        self.not_valid_basket_1 = u'%B1'

    def test_is_valid_basket(self):
        basket1 = Basket(self.valid_basket_1)
        self.assertTrue(basket1.is_valid())

        basket2 = Basket(self.valid_basket_2)
        self.assertTrue(basket2.is_valid())

    def test_is_not_valid_basket(self):
        basket1 = Basket(self.not_valid_basket_1)
        self.assertFalse(basket1.is_valid())


class TestCheckout(unittest.TestCase):

    def setUp(self):
        self.valid_basket_1 = u''
        self.valid_basket_2 = u'AAABBB'
        self.valid_basket_3 = u'BABA'
        self.valid_basket_4 = u'AAB'

    def test_checkout(self):
        self.assertEqual(0, checkout(self.valid_basket_1))
        self.assertEqual(205, checkout(self.valid_basket_2))
        self.assertEqual(145, checkout(self.valid_basket_3))
        self.assertEqual(130, checkout(self.valid_basket_4))
