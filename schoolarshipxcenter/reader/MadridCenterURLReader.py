from schoolarshipxcenter.reader.URLReader import URLReader
import re


class MadridCenterURLReader(URLReader):
    URL_BASE = "http://gestiona.madrid.org/wpad_pub/run/j/MostrarFichaCentro.icm?cdCentro="

    def __init__(self, id):
        super().__init__(self.URL_BASE + id)
        print(self.url)

    def read(self):
        html = super().read()

        print("Evaluating...")

        address_list = re.findall(r"Direcci&oacute;n:((.|\n)*?)<\/td>", html)\

        if len(address_list) > 0:
            address_html = "".join(str(v) for v in address_list)

            address_fragments = re.findall(r"<strong>((.|\n)*?)</strong>", address_html)
            address = ""
            for fragment in address_fragments:
                address += fragment[0]

        print(address)

        return address
