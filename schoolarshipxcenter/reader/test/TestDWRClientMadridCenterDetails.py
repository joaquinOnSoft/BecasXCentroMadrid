from unittest import TestCase

from ..DWRClientMadridCenterDetails import DWRClientMadridCenterDetails


class TestDRWClient(TestCase):

    def test_request(self):
        client = DWRClientMadridCenterDetails(28041512)
        res = client.read()

        self.assertIsNotNone(res)
