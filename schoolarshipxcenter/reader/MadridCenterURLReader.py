from schoolarshipxcenter.reader.URLReader import URLReader
import re


class MadridCenterURLReader(URLReader):
    URL_BASE = "http://gestiona.madrid.org/wpad_pub/run/j/MostrarFichaCentro.icm?cdCentro="

    LABEL_MAIL = "E-MAIL"
    LABEL_URL = "URL"

    def __init__(self, center_id):
        super().__init__(self.URL_BASE + center_id)

    def read(self):
        html = super().read()

        data = {self.LABEL_URL: self.url}

        mail_list = re.findall(r"<input TYPE='hidden' name='tlMail' value='(.*)'\/>", html)
        if mail_list is not None and len(mail_list) > 0:
            data[self.LABEL_MAIL] = mail_list[0]
        else:
            data[self.LABEL_MAIL] = ""

        return data
