import unittest
from date_time import DateTime, DateFormatInvalid


class TestDateTime(unittest.TestCase):

    def test_date_time_invalid_format_are_refuse(self):
        self.assertRaises(DateFormatInvalid, DateTime, "2020-14-31")

    def test_date_time_accepte_str_partiel(self):
        date_time = DateTime("2020-12-31")
        assert date_time.est_coherent()

    def test_date_time_accepte_str_complet(self):
        date_time = DateTime("2020-12-31:23:59:59")
        assert date_time.est_coherent()
