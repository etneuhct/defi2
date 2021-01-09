import unittest
from gestionTemps import decompositionDate, decompositionDateComplete, verifieBissextile, rectifieJour, rectifieHeure, \
    rectifieMinute, calculAdditionTemps, formatDateHeure, verifieJourAnneeBissextile, verifieJourAnneeNonBissextile


class GestionTempsTestCase(unittest.TestCase):

    def test_decompositionDate(self):

        assert decompositionDate("2021-12-08") == (2021, 12, 8, 0, 0, 0)
        assert decompositionDate("2022-10-18") == (2022, 10, 18, 0, 0, 0)
        assert decompositionDate("2026-05-26") == (2026, 5, 26, 0, 0, 0)

    def test_decompositionDateComplete(self):

        assert decompositionDateComplete("2021-12-08:23:43:23") == (2021, 12, 8, 23, 43, 23)
        assert decompositionDateComplete("2022-10-18:02:43:21") == (2022, 10, 18, 2, 43, 21)
        assert decompositionDateComplete("2026-05-26:08:30:34") == (2026, 5, 26, 8, 30, 34)

    def test_verifieBissextile(self):

        self.assertTrue(verifieBissextile(2020))
        self.assertTrue(verifieBissextile(2024))
        self.assertFalse(verifieBissextile(2021))
        self.assertFalse(verifieBissextile(2023))

    def test_rectifieJour(self):

        self.assertEqual(rectifieJour(2024, 2, 30), (2024, 3, 1))
        self.assertEqual(rectifieJour(2023, 2, 29), (2023, 3, 1))
        self.assertEqual(rectifieJour(2024, 4, 31), (2024, 5, 1))
        self.assertEqual(rectifieJour(2023, 5, 32), (2023, 6, 1))
        self.assertEqual(rectifieJour(2024, 8, 32), (2024, 9, 1))

    def test_rectifieHeure(self):

        self.assertEqual(rectifieHeure(2024, 2, 29, 25), (2024, 3, 1, 1))
        self.assertEqual(rectifieHeure(2023, 2, 28, 24), (2023, 3, 1, 0))
        self.assertEqual(rectifieHeure(2024, 4, 30, 25), (2024, 5, 1, 1))
        self.assertEqual(rectifieHeure(2023, 5, 31, 24), (2023, 6, 1, 0))
        self.assertEqual(rectifieHeure(2024, 8, 31, 25), (2024, 9, 1, 1))

    def test_rectifieMinute(self):

        self.assertEqual(rectifieMinute(2028, 2, 29, 24, 60), (2028, 3, 1, 1, 0))
        self.assertEqual(rectifieMinute(2025, 2, 28, 23, 61), (2025, 3, 1, 0, 1))
        self.assertEqual(rectifieMinute(2028, 4, 30, 24, 62), (2028, 5, 1, 1, 2))
        self.assertEqual(rectifieMinute(2023, 5, 31, 23, 60), (2023, 6, 1, 0, 0))
        self.assertEqual(rectifieMinute(2024, 8, 31, 24, 63), (2024, 9, 1, 1, 3))

    def test_calculAdditionTemps(self):

        self.assertEqual(calculAdditionTemps("2021-02-28", 1200), (2024, 6, 12, 0, 0, 0))
        self.assertEqual(calculAdditionTemps("2019-12-13", 900), (2021, 6, 1, 0, 0, 0))
        self.assertEqual(calculAdditionTemps("2018-11-14:06:32:21", 74, 5, 45), (2018, 1, 27, 12, 17, 21))
        self.assertEqual(calculAdditionTemps("2023-07-27", 0, 3, 43, 15), (2023, 7, 27, 3, 43, 15))
        self.assertEqual(calculAdditionTemps("2020-12-27:13:30:00", 0, 0, 30), (2020, 12, 27, 14, 0, 0))
        self.assertEqual(calculAdditionTemps("2025-06-15:12:23:34", 5, 3, 7, 6), (2025, 6, 20, 15, 30, 40))



    def test_formatDateHeure(self):

        assert formatDateHeure(2020, 12, 27, 14, 30, 0) == ("La date recherchée est : 2020 - 12 - 27 : 14 : 30 : 0 ")
        
        
    def test_verifieJourAnneeNonBissextile(self):
        
        self.assertEqual(verifieJourAnneeNonBissextile(2019, 2, 45), (2019,3, 17))
        self.assertEqual(verifieJourAnneeNonBissextile(2023, 7, 50), (2023 ,8, 19))
        self.assertEqual(verifieJourAnneeNonBissextile(2021, 8, 32), (2021,9, 1))
        
    def test_verifieJourAnneeBissextile(self):
        
        self.assertEqual(verifieJourAnneeBissextile(2020, 2, 56), (2020 ,3, 27))
        self.assertEqual(verifieJourAnneeBissextile(2024, 9, 78), (2024 ,11, 17))
        self.assertEqual(verifieJourAnneeBissextile(2028, 5, 89), (2028 ,7, 28))



if __name__ == '__main__':

    unittest.main()



