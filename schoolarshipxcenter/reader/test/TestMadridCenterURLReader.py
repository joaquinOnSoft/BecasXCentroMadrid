import unittest
from unittest import TestCase
from ..MadridCenterURLReader import MadridCenterURLReader


class TestMadridCenterURLReader(TestCase):
    def test_read(self):
        reader = MadridCenterURLReader("28041512")
        address = reader.read()

        self.assertIsNotNone(address)
        self.assertEqual("calle san antonio", address[MadridCenterURLReader.LABEL_ADDRESS])
        self.assertEqual("2", address[MadridCenterURLReader.LABEL_NUMBER])
        self.assertEqual("28670", address[MadridCenterURLReader.LABEL_ZIP])
        self.assertEqual("Villaviciosa de Odón.", address[MadridCenterURLReader.LABEL_POPULATION])