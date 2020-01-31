from unittest import TestCase

from ..URLReader import URLReader


class TestURLReader(TestCase):

    def test_read(self):
        reader = URLReader("http://gestiona.madrid.org/wpad_pub/run/j/MostrarFichaCentro.icm?cdCentro=28041512")
        html = reader.read()

        self.assertIsNotNone(html)
        self.assertTrue(html.find("calle san antonio") > -1)
