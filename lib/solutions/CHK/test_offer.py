import unittest

from checkout_solution import Offer


class TestOffer(unittest.TestCase):

    def setUp(self):
        self.offers_list = [
            {
                "offer_id": 1,
                "quantity": 3,
                "price": 130
            },
            {
                "offer_id": 2,
                "quantity": 2,
                "price": 45
            }
        ]

    def test_offer_is_available(self):
        offer = Offer(1)
        self.assertTrue(offer.is_available())

    def test_offer_not_available(self):
        offer = Offer(100)
        self.assertFalse(offer.is_available())

    def test_get_available_offer(self):
        offer = Offer(1)
        self.assertEqual(1, len(offer.get_offer()))

    def test_get_not_available_offer(self):
        offer = Offer(100)
        self.assertEqual(0, len(offer.get_offer()))
