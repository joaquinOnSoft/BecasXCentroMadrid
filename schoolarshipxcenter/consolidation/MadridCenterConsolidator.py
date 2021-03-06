import csv
import time

from urllib.error import HTTPError, URLError
from urllib3.exceptions import IncompleteRead

from schoolarshipxcenter.reader.CSVReader import CSVReader
from schoolarshipxcenter.reader.DWRClientMadridCenterDetails import DWRClientMadridCenterDetails
from schoolarshipxcenter.reader.GeocodeReader import GeocodeReader
from schoolarshipxcenter.reader.MadridCenterURLReader import MadridCenterURLReader
from schoolarshipxcenter.writer.CSVWriter import CSVWriter


class MadridCenterConsolidator:
    FIELD_CENTER_ID = "CODIGO CENTRO"

    @staticmethod
    def process(input_file, output_file, delimiter):
        reader = CSVReader(input_file, delimiter)
        rows = reader.read()

        if rows is not None:

            lines = []
            num_lines = 0

            for row in rows:
                # Remove column 'None'. Returned by CSVReader. It's a useless column
                del row[None]

                # Recover center Id
                center_id = row[MadridCenterConsolidator.FIELD_CENTER_ID]

                num_lines += 1
                retry = True

                while retry:
                    try:
                        # Recover Center extra information not included in the CSV file (e-mail)
                        center_basic_inf = MadridCenterURLReader(center_id)
                        res = center_basic_inf.read()

                        if res is not None:
                            row.update(res)

                            # Recover statistic information about the center (students by year)
                            center_statistics = DWRClientMadridCenterDetails(center_id)
                            res = center_statistics.read()

                            if res is not None:
                                row.update(res)

                            # Recover coordinates from the Center address
                            address = MadridCenterConsolidator.__get_address(row)
                            geo = GeocodeReader(address)
                            coordinates = geo.read()
                            if coordinates is None:
                                coordinates = {'lat': '', 'lng': ''}

                            row.update(coordinates)

                            lines.append(row)
                            print(f"{num_lines} - {row['CODIGO CENTRO']} ({row['lat']}, {row['lng']}) {address} - {row['TITULAR']}")

                        retry = False
                    except ConnectionError:
                        MadridCenterConsolidator.__sleep(5)
                    except ConnectionResetError:
                        MadridCenterConsolidator.__sleep(5)
                    except IncompleteRead:
                        MadridCenterConsolidator.__sleep(5)
                    except HTTPError:
                        MadridCenterConsolidator.__sleep(5)
                    except URLError:
                        MadridCenterConsolidator.__sleep(5)
                    except TimeoutError:
                        MadridCenterConsolidator.__sleep(5)

            reader = CSVWriter(output_file, delimiter, csv.QUOTE_ALL)
            reader.write(lines)

    @staticmethod
    def __get_address(center):
        address = f"{center['DOMICILIO']}, {center['COD. POSTAL']}, {center['MUNICIPIO']}"
        return address

    @staticmethod
    def __sleep(secs):
        # An error 'ConnectionResetError' happens when you try a
        # few hundreds of consecutive calls to the server.
        print(f"Sleeping {secs} seconds")
        time.sleep(secs)
