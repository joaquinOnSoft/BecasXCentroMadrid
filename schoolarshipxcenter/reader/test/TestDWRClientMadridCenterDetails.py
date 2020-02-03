from unittest import TestCase

from ..DWRClientMadridCenterDetails import DWRClientMadridCenterDetails


class TestDRWClient(TestCase):

    def test_request_IES(self):
        client = DWRClientMadridCenterDetails(28041512)
        res = client.read()

        self.assertIsNotNone(res)
        self.assertEqual(res['Total 2018-2019'], '728')
        self.assertEqual(res['ESO 2018-2019'], '526')
        self.assertEqual(res['Bachillerato 2018-2019'], '202')
        # Check none existing columns have been added
        self.assertEqual(res['Infantil II Ciclo 2018-2019'], '')


    def test_request_CP_INF_PRI(self):
        client = DWRClientMadridCenterDetails(28006275)
        res = client.read()

        self.assertIsNotNone(res)
        self.assertEqual(res['Total 2018-2019'], '466')
        self.assertEqual(res['Infantil II Ciclo 2018-2019'], '150')
        self.assertEqual(res['Primaria 2018-2019'], '316')


    def test_request_no_data(self):
        client = DWRClientMadridCenterDetails(28078262)
        res = client.read()

        self.assertIsNotNone(res)
        self.assertEqual(res['Total 2018-2019'], '')
        self.assertEqual(res['ESO 2018-2019'], '')
        self.assertEqual(res['Bachillerato 2018-2019'], '')
