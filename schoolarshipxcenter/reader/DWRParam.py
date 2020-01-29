class DWRParam:

    TYPE_STRING = "string"
    TYPE_OBJECT = "Object"

    def __init__(self, param, value, data_type=None):
        self.param = param
        self.value = value
        self.data_type = data_type

    def __str__(self):
        string = self.param + "="

        if self.data_type == self.TYPE_STRING:
            string += self.TYPE_STRING + ":"
        elif self.data_type == self.TYPE_OBJECT:
            string += self.TYPE_OBJECT + ":"

        string += str(self.value)

        return string
