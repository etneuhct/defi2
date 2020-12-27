import unittest
from gestionTemps import decompositionDate, decompositionDateComplete, checkBissextile, checkJour, checkHeure, \
    checkMinute, calculTemps, formatDateHeure


class GestionTempsTestCase(unittest.TestCase):

    def test_decompositionDate(self):

        assert decompositionDate("2021-12-08") == (2021, 12, 8, 0, 0, 0)
        assert decompositionDate("2022-10-18") == (2022, 10, 18, 0, 0, 0)
        assert decompositionDate("2026-05-26") == (2026, 5, 26, 0, 0, 0)

    def test_decompositionDateComplete(self):

        assert decompositionDateComplete("2021-12-08:23:43:23") == (2021, 12, 8, 23, 43, 23)
        assert decompositionDateComplete("2022-10-18:02:43:21") == (2022, 10, 18, 2, 43, 21)
        assert decompositionDateComplete("2026-05-26:08:30:34") == (2026, 5, 26, 8, 30, 34)

    def test_checkBissextile(self):

        self.assertTrue(checkBissextile(2020))
        self.assertTrue(checkBissextile(2024))
        self.assertFalse(checkBissextile(2021))
        self.assertFalse(checkBissextile(2023))

    def test_checkJour(self):

        self.assertEqual(checkJour(2024, 2, 30), (2024, 3, 1))
        self.assertEqual(checkJour(2023, 2, 29), (2023, 3, 1))
        self.assertEqual(checkJour(2024, 4, 31), (2024, 5, 1))
        self.assertEqual(checkJour(2023, 5, 32), (2023, 6, 1))
        self.assertEqual(checkJour(2024, 8, 32), (2024, 9, 1))

    def test_checkHeure(self):

        self.assertEqual(checkHeure(2024, 2, 29, 25), (2024, 3, 1, 1))
        self.assertEqual(checkHeure(2023, 2, 28, 24), (2023, 3, 1, 0))
        self.assertEqual(checkHeure(2024, 4, 30, 25), (2024, 5, 1, 1))
        self.assertEqual(checkHeure(2023, 5, 31, 24), (2023, 6, 1, 0))
        self.assertEqual(checkHeure(2024, 8, 31, 25), (2024, 9, 1, 1))

    def test_checkMinute(self):

        self.assertEqual(checkMinute(2028, 2, 29, 24, 60), (2028, 3, 1, 1, 0))
        self.assertEqual(checkMinute(2025, 2, 28, 23, 61), (2025, 3, 1, 0, 1))
        self.assertEqual(checkMinute(2028, 4, 30, 24, 62), (2028, 5, 1, 1, 2))
        self.assertEqual(checkMinute(2023, 5, 31, 23, 60), (2023, 6, 1, 0, 0))
        self.assertEqual(checkMinute(2024, 8, 31, 24, 63), (2024, 9, 1, 1, 3))

    def test_calculTemps(self):

        self.assertEqual(calculTemps("2020-12-27", 5), (2021, 1, 1, 0, 0, 0))
        self.assertEqual(calculTemps("2021-12-27", 5), (2022, 1, 1, 0, 0, 0))
        self.assertEqual(calculTemps("2022-05-19:16:30:00", 7), (2022, 5, 26, 16, 30, 0))
        self.assertEqual(calculTemps("2023-07-27", 0, 3, 43, 15), (2023, 7, 27, 3, 43, 15))
        self.assertEqual(calculTemps("2020-12-27:13:30:00", 0, 0, 30), (2020, 12, 27, 14, 0, 0))
        self.assertEqual(calculTemps("2025-06-15:12:23:34", 5, 3, 7, 6), (2025, 6, 20, 15, 30, 40))

    def test_formatDateHeure(self):

        assert formatDateHeure(2020, 12, 27, 14, 30, 0) == ("La date recherchée est : 2020 - 12 - 27 : 14 : 30 : 0 ")
