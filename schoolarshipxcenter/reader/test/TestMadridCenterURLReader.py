import unittest
from unittest import TestCase
from ..MadridCenterURLReader import MadridCenterURLReader


class TestMadridCenterURLReader(TestCase):
    def test_read(self):
        reader = MadridCenterURLReader("28041512")
        address = reader.read()

        self.assertEqual(address, "calle san antonio2,28670,Villaviciosa de Odón.")
