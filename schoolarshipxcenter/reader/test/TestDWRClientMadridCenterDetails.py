from unittest import TestCase

from ..DWRClientMadridCenterDetails import DWRClientMadridCenterDetails


class TestDRWClient(TestCase):

    def test_request(self):
        client = DWRClientMadridCenterDetails(28041512)
        res = client.read()

        self.assertIsNotNone(res)
        self.assertEqual(res['# total alumnos 2017-2018'], '728')
        self.assertEqual(res['# alumnos ESO 2017-2018'], '526')
        self.assertEqual(res['# alumnos Bachillerato 2017-2018'], '202')

        client = DWRClientMadridCenterDetails(28047551)
        res = client.read()

        self.assertIsNotNone(res)
        #self.assertEqual(res['# total alumnos 2017-2018'], '728')
        #self.assertEqual(res['# alumnos ESO 2017-2018'], '526')
        #self.assertEqual(res['# alumnos Bachillerato 2017-2018'], '202')