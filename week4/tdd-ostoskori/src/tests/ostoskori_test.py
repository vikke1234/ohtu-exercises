import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.cart = Ostoskori()
        self.item = Tuote("test", 5)
        self.milk = Tuote("milk", 1)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.cart.hinta(), 0)

    def test_add_single_item(self):
        self.cart.lisaa_tuote(self.item)
        self.assertEqual(len(self.cart), 1)

    def test_add_different_items(self):
        self.cart.lisaa_tuote(self.item)
        self.cart.lisaa_tuote(self.milk)
        self.assertEqual(len(self.cart), 2)

    def test_add_different_items_price_correct(self):
        self.cart.lisaa_tuote(self.item)
        self.cart.lisaa_tuote(self.milk)
        self.assertEqual(self.cart.hinta(), 6)

    def test_add_same_item_twice(self):
        self.cart.lisaa_tuote(self.item)
        self.cart.lisaa_tuote(self.item)
        self.assertEqual(len(self.cart), 2)


