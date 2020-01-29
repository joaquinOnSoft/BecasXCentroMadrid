from unittest import TestCase

from ..DWRClient import DWRClient


class TestDRWClient(TestCase):
    """
    @see https://github.com/push0ebp/dwr-client
    """

    def test_request(self):
        url = "http://gestiona.madrid.org/wpad_pub/dwr/exec/GraficasDWRAccion.obtenerGrafica.dwr"

        dwr_client = DWRClient(url)

        dwr_client.add_param("callCount", 1)
        dwr_client.set_script_name("GraficasDWRAccion")
        dwr_client.set_method_name("obtenerGrafica")
        dwr_client.add_param("c0-id", "8195_1580332252722")
        dwr_client.add_string_param("c0-e1", "28041512")
        dwr_client.add_string_param("c0-e2", "TODO")
        dwr_client.add_string_param("c0-e3", 1)
        dwr_client.add_string_param("c0-e4", 1)
        param0 = "{cdCentro:reference:c0-e1, cdnivelEducativo:reference:c0-e2, cdGrafica:reference:c0-e3, " \
                 "tipoGrafica:reference:c0-e4}"
        dwr_client.add_object_param("c0-param0", param0)
        dwr_client.add_param("xml", "true")

        res = dwr_client.read()

        self.assertIsNotNone(res)
