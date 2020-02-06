class Properties:
    def __init__(self, file_name):
        separator = "="
        self.properties = {}

        # I named your file conf and stored it
        # in the same directory as the script

        with open(file_name) as f:

            for line in f:
                if separator in line:
                    # Find the name and value by splitting the string
                    name, value = line.split(separator, 1)

                    # Assign key value pair to dict
                    # strip() removes white space from the ends of strings
                    self.properties[name.strip()] = value.strip()

    def get(self, name):
        if name in self.properties.keys():
            return self.properties[name]
        else:
            return None
