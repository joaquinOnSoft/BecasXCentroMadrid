import unittest
from unittest import TestCase
from ..MadridCenterURLReader import MadridCenterURLReader


class TestMadridCenterURLReader(TestCase):
    def test_read(self):
        reader = MadridCenterURLReader("28041512")
        data = reader.read()

        self.assertIsNotNone(data)
        self.assertEqual("ies.calatalifa.villaviciosa@educa.madrid.org", data[MadridCenterURLReader.LABEL_MAIL])
