import json
import pathlib
import urllib

from schoolarshipxcenter.reader.URLReader import URLReader
from schoolarshipxcenter.util.Properties import Properties


class GeocodeReader(URLReader):
    """
    Get Latitude & Longitude from a given address
    SEE: https://stackoverflow.com/questions/25888396/how-to-get-latitude-longitude-with-python
    """
    URL_BASE = "https://maps.googleapis.com/maps/api/geocode/json?"

    PARAM_ADDRESS = "address"
    PARAM_KEY = "key"

    def __init__(self, address, key=None):
        """
        Get Latitude & Longitude from a given address
        :param address: Address, following this format:
            street name, street number, zip, location
        Example:
            Avenida De Isabel De Farnesio, 14, 28660, Boadilla del Monte
        :param key: Google Geocoding API key
        """
        if key is None:
            prop = Properties(str(pathlib.Path(__file__).parent.absolute()) + "/../../resources/grant.properties")
            key = prop.get("google.geocode.api.key")

        params = {self.PARAM_ADDRESS: address, self.PARAM_KEY: key}
        str_params = urllib.parse.urlencode(params)

        super().__init__(self.URL_BASE + str_params)

    def read(self):
        coordinates = None
        html = super().read()

        jsonObj = json.loads(html)

        if jsonObj is not None and jsonObj["results"] is not None and len(jsonObj["results"]) > 0:
            # if "partial_match" not in jsonObj["results"][0].keys():
            coordinates = jsonObj["results"][0]["geometry"]["location"]

        return coordinates
