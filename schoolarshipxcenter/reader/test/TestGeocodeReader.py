from unittest import TestCase

from ..GeocodeReader import GeocodeReader


class TestGeocodeReader(TestCase):

    def test_read(self):

        reader = GeocodeReader("Avenida De Isabel De Farnesio, 14, 28660, Boadilla del Monte")
        coordinates = reader.read()

        self.assertIsNotNone(coordinates)
        self.assertEqual(40.40437, coordinates['lat'])
        self.assertEqual(-3.88754, coordinates['lng'])

    def test_read_none_existing_address(self):
        reader = GeocodeReader("C/ Inifinite Loop, 7, Madrid")
        coordinates = reader.read()

        self.assertIsNone(coordinates)

    def test_read_no_coordinates(self):
        reader = GeocodeReader("Avenida De Viña Grande, 2 , 28925, Alcorcón")
        coordinates = reader.read()

        self.assertIsNotNone(coordinates)
        self.assertEqual(40.3496458, coordinates['lat'])
        self.assertEqual(-3.806678899999999, coordinates['lng'])
