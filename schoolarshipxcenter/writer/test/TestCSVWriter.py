import csv
from unittest import TestCase
from ..CSVWriter import CSVWriter


class TestCSVReader(TestCase):
    """
    @see https://realpython.com/python-csv/
    """

    def test_write(self):
        row1 = {"Name": "Michael Jordan", "Number": "23"}
        row2 = {"Name": "Dennis Rodman", "Number": "91"}
        rows = [row1, row2]

        reader = CSVWriter("..\\resources\\out_example.csv", ";", csv.QUOTE_ALL)
        num_lines = reader.write(rows)

        self.assertEqual(3, num_lines)

