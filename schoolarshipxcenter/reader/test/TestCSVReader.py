from unittest import TestCase

from ..CSVReader import CSVReader


class TestCSVReader(TestCase):
    """
    @see https://realpython.com/python-csv/
    """

    def test_read(self):
        reader = CSVReader("..\\resources\\19-01-2020-(178)-utf8.csv", ";")
        rows = reader.read()

        self.assertIsNotNone(rows)
        self.assertEqual(4040, len(rows))

        self.assertEqual(rows[1].get("CODIGO CENTRO"), "28063027")
        self.assertEqual(rows[1].get("TITULARIDAD"), "Público")
