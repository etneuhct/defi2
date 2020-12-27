import unittest
from date_time import DateTime, DateFormatInvalid


class TestDateTime(unittest.TestCase):

    def test_dateTimeInvalidFormatAreRefuse(self):
        self.assertRaises(DateFormatInvalid, DateTime, "2020-14-31")

    def test_dateTimeAccepteStrPartiel(self):
        date_time = DateTime("2020-12-31")
        assert date_time.est_coherent()

    def test_dateTimeAccepteStrComplet(self):
        date_time = DateTime("2020-12-31:23:59:59")
        assert date_time.est_coherent()
