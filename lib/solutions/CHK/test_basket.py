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
        self.valid_basket_0 = u'a'
        self.valid_basket_1 = u''
        self.valid_basket_2 = u'AAABBB'
        self.valid_basket_3 = u'BABA'
        self.valid_basket_4 = u'AAB'
        self.valid_basket_5 = u'A'
        self.valid_basket_6 = u'B'
        self.valid_basket_7 = u'C'
        self.valid_basket_8 = u'AAAAAA'
        self.valid_basket_9 = u'BBBB'
        self.valid_basket_10 = u'ABCDCBAABCABBAAA'
        self.valid_basket_11 = u'EEB'
        self.valid_basket_12 = u'EEBB'
        self.valid_basket_13 = u'AAAAA'
        self.valid_basket_14 = u'AAAAAAAA'
        self.valid_basket_15 = u'AxA'
        self.valid_basket_16 = u'ABCa'
        self.valid_basket_17 = u'FFF'
        self.valid_basket_18 = u'FFFF'
        self.valid_basket_19 = u'FFFE'
        self.valid_basket_20 = u'FF'
        self.valid_basket_21 = u'FFFF'
        self.valid_basket_22 = u'FFFFFF'

    def test_checkout(self):
        # self.assertEqual(-1, checkout(self.valid_basket_0))
        # self.assertEqual(0, checkout(self.valid_basket_1))
        # self.assertEqual(205, checkout(self.valid_basket_2))
        # self.assertEqual(145, checkout(self.valid_basket_3))
        # self.assertEqual(130, checkout(self.valid_basket_4))
        # self.assertEqual(50, checkout(self.valid_basket_5))
        # self.assertEqual(30, checkout(self.valid_basket_6))
        # self.assertEqual(20, checkout(self.valid_basket_7))
        # self.assertEqual(250, checkout(self.valid_basket_8))
        # self.assertEqual(90, checkout(self.valid_basket_9))
        # self.assertEqual(495, checkout(self.valid_basket_10))
        # self.assertEqual(80, checkout(self.valid_basket_11))
        # self.assertEqual(110, checkout(self.valid_basket_12))
        # self.assertEqual(200, checkout(self.valid_basket_13))
        # self.assertEqual(330, checkout(self.valid_basket_14))
        # self.assertEqual(-1, checkout(self.valid_basket_15))
        # self.assertEqual(-1, checkout(self.valid_basket_16))
        # self.assertEqual(20, checkout(self.valid_basket_17))
        # self.assertEqual(30, checkout(self.valid_basket_18))
        # self.assertEqual(60, checkout(self.valid_basket_19))
        # self.assertEqual(20, checkout(self.valid_basket_20))
        # self.assertEqual(30, checkout(self.valid_basket_21))
        self.assertEqual(40, checkout(self.valid_basket_22))
