from unittest import TestCase

from ..DWRParam import DWRParam


class TestDRWClient(TestCase):

    def test_str(self):
        param = DWRParam("c0-e1", 28041512, DWRParam.TYPE_STRING)
        self.assertEqual("c0-e1=string:28041512", str(param))


        p2_value = "{cdCentro:reference:c0-e1, cdnivelEducativo:reference:c0-e2, cdGrafica:reference:c0-e3, " \
                   "tipoGrafica:reference:c0-e4}"
        param2 = DWRParam("c0-param0", p2_value, DWRParam.TYPE_OBJECT)

        p2_expected_value = "c0-param0=Object:{cdCentro:reference:c0-e1, cdnivelEducativo:reference:c0-e2, " \
                            "cdGrafica:reference:c0-e3, tipoGrafica:reference:c0-e4}"

        self.assertEqual(p2_expected_value, str(param2))

