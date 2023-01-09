import requests

from schoolarshipxcenter.reader.DWRParam import DWRParam


class DWRClient:
    """
    Direct Web Remoting, or DWR, is a Java open-source library that helps developers
    write web sites that include Ajax technology.
    """
    PARAM_SCRIPT_NAME = "c0-scriptName"
    PARAM_METHOD_NAME = "c0-methodName"

    def __init__(self, url=None):
        self.url = url

        self.params = []

    def set_script_name(self, value):
        self.params.append(DWRParam(self.PARAM_SCRIPT_NAME, value))

    def set_method_name(self, value):
        self.params.append(DWRParam(self.PARAM_METHOD_NAME, value))

    def add_param(self, name, value):
        self.params.append(DWRParam(name, value))

    def add_object_param(self, name, value):
        self.params.append(DWRParam(name, value, DWRParam.TYPE_OBJECT))

    def add_string_param(self, name, value):
        self.params.append(DWRParam(name, value, DWRParam.TYPE_STRING))

    def read(self):
        content = None

        post_data = self.get_body_params()

        res = requests.post(self.url, data=post_data)

        if res is not None and res.status_code == 200:
            content = res.content

        return content

    def get_body_params(self):
        post_data = ""

        for param in self.params:
            post_data += str(param) + "\n"

        return post_data
