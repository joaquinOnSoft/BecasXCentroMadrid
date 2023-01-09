from unittest import TestCase

from ..GeocodeReader import GeocodeReader


class TestGeocodeReader(TestCase):

    def test_read(self):

        reader = GeocodeReader("Avenida De Isabel De Farnesio, 14, 28660, Boadilla del Monte")
        coordinates = reader.read()

        self.assertIsNotNone(coordinates)
        self.assertEqual(40.403947, coordinates['lat'])
        self.assertEqual(-3.8875135, coordinates['lng'])

    def test_read_none_existing_address(self):
        reader = GeocodeReader("abc xyz 123 987")
        coordinates = reader.read()

        self.assertIsNone(coordinates)

    def test_read_no_coordinates(self):
        reader = GeocodeReader("Avenida De Viña Grande, 2 , 28925, Alcorcón")
        coordinates = reader.read()

        self.assertIsNotNone(coordinates)
        self.assertEqual(40.349476, coordinates['lat'])
        self.assertEqual(-3.8067598, coordinates['lng'])
