import os
import pathlib
from unittest import TestCase

from ..CSVReader import CSVReader


class TestCSVReader(TestCase):
    """
    @see https://realpython.com/python-csv/
    """

    def test_read(self):
        parent = pathlib.Path(__file__).parent.resolve()
        reader = CSVReader(
            os.path.join(str(parent), "..", "..", "..", "resources", "2020-01-19-(178)-utf8.csv"),
            ";")
        rows = reader.read()

        self.assertIsNotNone(rows)
        self.assertEqual(4040, len(rows))

        self.assertEqual(rows[1].get("CODIGO CENTRO"), "28063027")
        self.assertEqual(rows[1].get("TITULARIDAD"), "Público")
