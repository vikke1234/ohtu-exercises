import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self) -> None:
        self.bank = Mock()
        self.id_generator = Mock()
        self.warehouse_mock = Mock()
        self.transaction_defaults = ("test", 42, "123", "33333-44455")
        self.transaction_short_defaults = ("test", "123")
        self.shop = Kauppa(self.warehouse_mock, self.bank, self.id_generator)

        self.id_generator.uusi.return_value = 42


        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 1
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "butter", 3)
            if tuote_id == 3:
                return Tuote(3, "chicken", 50)

        self.warehouse_mock.saldo.side_effect = varasto_saldo
        self.warehouse_mock.hae_tuote.side_effect = varasto_hae_tuote
        self.shop.aloita_asiointi()

    def test_shopping_same_item_not_in_stock(self):
        self.shop.lisaa_koriin(1)
        self.shop.lisaa_koriin(3)
        self.shop.tilimaksu(*self.transaction_short_defaults)
        self.bank.tilisiirto.assert_called_with(*self.transaction_defaults, 5)

    def test_shopping_same_item_in_stock(self):
        self.shop.lisaa_koriin(1)
        self.shop.lisaa_koriin(1)
        self.shop.tilimaksu(*self.transaction_short_defaults)
        self.bank.tilisiirto.assert_called_with(*self.transaction_defaults, 10)

    def test_shopping_works(self):
        self.shop.lisaa_koriin(1)
        self.shop.lisaa_koriin(2)
        self.shop.tilimaksu(*self.transaction_short_defaults)
        self.bank.tilisiirto.assert_called_with(*self.transaction_defaults, 8)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        bank_mock = Mock()
        id_generator = Mock()

        # palautetaan aina arvo 42
        id_generator.uusi.return_value = 42

        warehouse_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        warehouse_mock.saldo.side_effect = varasto_saldo
        warehouse_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        shop = Kauppa(warehouse_mock, bank_mock, id_generator)

        # tehdään ostokset
        shop.aloita_asiointi()
        shop.lisaa_koriin(1)
        shop.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        bank_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_starting_shopping_zeroes(self):

        self.shop.aloita_asiointi()
        self.shop.lisaa_koriin(1)
        self.assertNotEqual(self.shop._ostoskori.hinta(), 0)
        self.shop.aloita_asiointi()
        self.assertEqual(self.shop._ostoskori.hinta(), 0)

    def test_transaction_correct(self):
        self.shop.lisaa_koriin(1)
        self.shop.tilimaksu(*self.transaction_short_defaults)
        self.bank.tilisiirto.assert_called_with(*self.transaction_defaults, 5)

    def test_new_id_each_transaction(self):
        self.shop.tilimaksu(*self.transaction_short_defaults)
        self.shop.aloita_asiointi()
        self.shop.tilimaksu(*self.transaction_short_defaults)
        self.assertEqual(self.id_generator.uusi.call_count, 2)
