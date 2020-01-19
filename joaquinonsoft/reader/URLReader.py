import urllib.request


class URLReader:
    def __init__(self, url):
        self.url = url

    def read(self):
        resource = urllib.request.urlopen(self.url)
        response = resource .read()

        html = response.decode(resource.headers.get_content_charset())
        resource .close()

        return html


reader = URLReader("http://www.google.com")
reader.read()
