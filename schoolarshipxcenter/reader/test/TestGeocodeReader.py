import pathlib
from unittest import TestCase

from ..GeocodeReader import GeocodeReader
from schoolarshipxcenter.util.Properties import Properties


class TestGeocodeReader(TestCase):

    def get_API_key(self):
        prop = Properties(str(pathlib.Path(__file__).parent.absolute()) + "/../../../resources/grant.properties")
        return prop.get("google.geocode.api.key")

    def test_read(self):

        reader = GeocodeReader("Avenida De Isabel De Farnesio, 14, 28660, Boadilla del Monte",
                               self.get_API_key())
        coordinates = reader.read()

        self.assertIsNotNone(coordinates)
        self.assertEqual(40.40437, coordinates['lat'])
        self.assertEqual(-3.88754, coordinates['lng'])

    def test_read_none_existing_address(self):
        reader = GeocodeReader("C/ Inifinite Loop, 7, Madrid",
                               self.get_API_key())
        coordinates = reader.read()

        self.assertIsNone(coordinates)
