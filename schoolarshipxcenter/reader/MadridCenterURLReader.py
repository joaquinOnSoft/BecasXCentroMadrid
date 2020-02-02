from schoolarshipxcenter.reader.URLReader import URLReader
import re


class MadridCenterURLReader(URLReader):
    URL_BASE = "http://gestiona.madrid.org/wpad_pub/run/j/MostrarFichaCentro.icm?cdCentro="

    LABEL_MAIL = "e-mail"

    def __init__(self, id):
        super().__init__(self.URL_BASE + id)

    def read(self):
        html = super().read()

        data = {}

        mail_list = re.findall(r"<input TYPE='hidden' name='tlMail' value='(.*)'\/>", html)
        if mail_list is not None:
            data[self.LABEL_MAIL] = mail_list[0]

        return data
