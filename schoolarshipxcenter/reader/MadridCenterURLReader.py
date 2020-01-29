from schoolarshipxcenter.reader.URLReader import URLReader
import re


class MadridCenterURLReader(URLReader):
    URL_BASE = "http://gestiona.madrid.org/wpad_pub/run/j/MostrarFichaCentro.icm?cdCentro="

    INDEX_ADDRESS = 0
    INDEX_NUMBER = 1
    INDEX_ZIP = 2
    INDEX_POPULATION = 3

    LABEL_ADDRESS = "Dirección"
    LABEL_NUMBER = "Número"
    LABEL_ZIP = "Código Postal"
    LABEL_POPULATION = "Población"

    def __init__(self, id):
        super().__init__(self.URL_BASE + id)

    def read(self):
        html = super().read()

        address_list = re.findall(r"Direcci&oacute;n:((.|\n)*?)<\/td>", html)\

        if len(address_list) > 0:
            address_html = "".join(str(v) for v in address_list)

            address_fragments = re.findall(r"<strong>((.|\n)*?)<\/strong>", address_html)
            address = {}

            counter = 0
            for fragment in address_fragments:
                if counter == self.INDEX_ADDRESS:
                    address[self.LABEL_ADDRESS] = fragment[0]
                elif counter == self.INDEX_NUMBER:
                    address[self.LABEL_NUMBER] = fragment[0].replace(",", "")
                elif counter == self.INDEX_ZIP:
                    address[self.LABEL_ZIP] = fragment[0].replace(",", "")
                elif counter == self.INDEX_POPULATION:
                    address[self.LABEL_POPULATION] = fragment[0]

                counter += 1

        return address
