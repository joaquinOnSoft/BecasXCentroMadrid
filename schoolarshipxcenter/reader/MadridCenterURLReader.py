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
            print(address_list[0])
            print(address_html)

            address_fragments = re.findall(r"<strong>((.|\n)*?)</strong>", address_html)
            # for address in address_fragments:
            #    print(address)

        return html
