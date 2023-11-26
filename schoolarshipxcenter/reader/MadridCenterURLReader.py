import re

from schoolarshipxcenter.reader.URLReader import URLReader


class MadridCenterURLReader(URLReader):
    URL_BASE = "http://gestiona.comunidad.madrid/wpad_pub/run/j/MostrarFichaCentro.icm?cdCentro="

    LABEL_MAIL = "E-MAIL"
    LABEL_URL = "URL"
    LABEL_OWNER = "TITULAR"
    LABEL_DIFFERENTIATED = "EDUC. DIFERENCIADA"
    LABEL_SEGREGATED = "SEGREGADA"

    VALUE_OWNERSHIP_PRIVATE = "Privado"
    VALUE_OWNERSHIP_PRIVATE_CONCERTED = "Privado Concertado"

    def __init__(self, center_id):
        super().__init__(self.URL_BASE + center_id)

    def read(self):
        html = super().read()

        data = {self.LABEL_URL: self.url,
                self.LABEL_MAIL: "",
                self.LABEL_OWNER: "",
                self.LABEL_SEGREGATED: "NO",
                self.LABEL_DIFFERENTIATED: ""}

        mail_list = re.findall(r"<input TYPE='hidden' name='tlMail' value='(.*)'\/>", html)
        if mail_list is not None and len(mail_list) > 0:
            data[self.LABEL_MAIL] = mail_list[0]

        prev_tag_owner = False

        ownership_list = re.findall(r"<input TYPE='hidden' name='tlTitularidad' value='(.*)'\/>", html)
        if ownership_list is not None and len(ownership_list) > 0:
            ownership = ownership_list[0]

            if ownership == self.VALUE_OWNERSHIP_PRIVATE or ownership == self.VALUE_OWNERSHIP_PRIVATE_CONCERTED:
                strong_tags = re.findall(r"<strong>(.*)<\/strong>", html)

                for tag in strong_tags:
                    if prev_tag_owner:
                        data[self.LABEL_OWNER] = tag
                        break

                    if tag == self.VALUE_OWNERSHIP_PRIVATE or tag == self.VALUE_OWNERSHIP_PRIVATE_CONCERTED:
                        prev_tag_owner = True

        differentiated = re.findall(r"<input type=\"hidden\" name=\"tlEdDiferenciada\" value=\"(.*)\" \/>", html)
        if differentiated is not None and len(differentiated) > 0:
            if differentiated[0] is not None and differentiated[0] != "null":
                data[self.LABEL_DIFFERENTIATED] = differentiated[0]
                data[self.LABEL_SEGREGATED] = "SI"
        else:
            data[self.LABEL_DIFFERENTIATED] = ""

        return data

