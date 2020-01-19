import unittest
from unittest import TestCase
from ..MadridCenterURLReader import MadridCenterURLReader


class TestMadridCenterURLReader(TestCase):
    def test_read(self):
        reader = MadridCenterURLReader("28041512")
        rows = reader.read()
