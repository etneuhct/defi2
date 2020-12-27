import unittest
from date_time import ConversionDateTime


class TestConversionDateTime(unittest.TestCase):

    def test_convertirEnSecondesRetourneLaValeurExacte(self):
        secondes = ConversionDateTime(2000, 1, 2).convertir_en_secondes()
        self.assertEqual(86400, secondes)

    def test_convertirAnneeEnSecondesRetourneLaValeurExacte(self):
        secondes = ConversionDateTime(2001, 1, 1).retourne_annee_en_secondes()
        self.assertEqual(secondes//(24*60*60), 366)

    def test_convertirMoisEnSecondesRetourneLaValeurExacte(self):
        secondes = ConversionDateTime(2001, 2, 1).retourne_mois_en_secondes()
        self.assertEqual(secondes//(24*60*60), 31)

    def test_convertirJourEnSecondesRetourneLaValeurExacte(self):
        secondes = ConversionDateTime.retourne_jour_en_secondes(1)
        self.assertEqual(secondes//(24*60*60), 1)
