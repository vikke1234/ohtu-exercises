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
        self.assertEqual(len(self.cart), 1)

    def test_after_one_add_the_cart_contains_one_purchase(self):
        self.cart.lisaa_tuote(self.item)
        self.assertEqual(len(self.cart.ostokset()), 1)

    def test_name_is_correct_after_adding_single_item(self):
        self.cart.lisaa_tuote(self.item)
        item = self.cart.ostokset()[0]

        self.assertEqual(item.tuotteen_nimi(), "test")

    def test_cart_contains_two_items_after_adding_two_different_ones(self):
        self.cart.lisaa_tuote(self.item)
        self.cart.lisaa_tuote(self.milk)
        self.assertEqual(len(self.cart.ostokset()), 2)


    def test_name_is_correct_after_adding_two_items(self):
        self.cart.lisaa_tuote(self.item)
        items = self.cart.ostokset()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].tuotteen_nimi(), "test")

    def test_removing_item_with_two_different_items(self):
        self.cart.lisaa_tuote(self.item)
        self.cart.lisaa_tuote(self.milk)

        self.cart.poista_tuote(self.milk)
        self.assertEqual(len(self.cart), 1)

    def test_removing_item_with_two_same_items(self):
        self.cart.lisaa_tuote(self.item)
        self.cart.lisaa_tuote(self.item)

        self.cart.poista_tuote(self.item)
        self.assertEqual(len(self.cart), 1)

