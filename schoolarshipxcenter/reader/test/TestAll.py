import unittest
from unittest import TestSuite

from schoolarshipxcenter.reader.test.TestCSVReader import TestCSVReader
from schoolarshipxcenter.reader.test.TestDWRClient import TestDRWClient
from schoolarshipxcenter.reader.test.TestDWRClientMadridCenterDetails import TestDWRClientMadridCenterDetails
from schoolarshipxcenter.reader.test.TestDWRParam import TestDRWCParam
from schoolarshipxcenter.reader.test.TestGeocodeReader import TestGeocodeReader
from schoolarshipxcenter.reader.test.TestMadridCenterURLReader import TestMadridCenterURLReader


def suite():
    test_suite: TestSuite = unittest.TestSuite()

    test_suite.addTest(TestCSVReader('test_read'))

    test_suite.addTest(TestDRWClient('test_request'))

    test_suite.addTest(TestDWRClientMadridCenterDetails('testRequestIES'))
    test_suite.addTest(TestDWRClientMadridCenterDetails('testRequestCP_INF_PRI'))
    test_suite.addTest(TestDWRClientMadridCenterDetails('testRequestNoData'))
    test_suite.addTest(TestDWRClientMadridCenterDetails('testRequestBugEncoding'))
    test_suite.addTest(TestDWRClientMadridCenterDetails('testRequestFP'))
    test_suite.addTest(TestDWRClientMadridCenterDetails('testRequestPCPI'))
    test_suite.addTest(TestDWRClientMadridCenterDetails('testRequestPCPIEspecial'))

    test_suite.addTest(TestDRWCParam('test_str'))

    test_suite.addTest(TestGeocodeReader('test_read'))
    test_suite.addTest(TestGeocodeReader('test_read_none_existing_address'))
    test_suite.addTest(TestGeocodeReader('test_read_no_coordinates'))

    test_suite.addTest(TestMadridCenterURLReader('test_read'))
    test_suite.addTest(TestMadridCenterURLReader('test_read_non_existing_center'))
    test_suite.addTest(TestMadridCenterURLReader('test_read_private_owner'))
    test_suite.addTest(TestMadridCenterURLReader('test_read_private_concerted_owner'))

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
