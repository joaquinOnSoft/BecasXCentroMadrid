from unittest import TestCase

from ..MadridCenterURLReader import MadridCenterURLReader


class TestMadridCenterURLReader(TestCase):
    def test_read(self):
        reader = MadridCenterURLReader("28041512")
        data = reader.read()

        self.assertIsNotNone(data)
        self.assertEqual("ies.calatalifa.villaviciosa@educa.madrid.org", data[MadridCenterURLReader.LABEL_MAIL])

    def test_read_non_existing_center(self):
        reader = MadridCenterURLReader("28022220")
        data = reader.read()

        self.assertIsNotNone(data)
        self.assertEqual("", data[MadridCenterURLReader.LABEL_MAIL])

    def test_read_private_owner(self):
        reader = MadridCenterURLReader("28020077")
        data = reader.read()

        self.assertIsNotNone(data)
        self.assertEqual("COLEGIO BRISTOL, S.A.", data[MadridCenterURLReader.LABEL_OWNER])

    def test_read_private_concerted_owner(self):
        reader = MadridCenterURLReader("28028507")
        data = reader.read()

        self.assertIsNotNone(data)
        self.assertEqual("FUNDACION OBRA SOCIAL Y MONTE DE PIEDAD DE MADRID", data[MadridCenterURLReader.LABEL_OWNER])
