from schoolarshipxcenter.reader.CSVReader import CSVReader
from schoolarshipxcenter.reader.DWRClientMadridCenterDetails import DWRClientMadridCenterDetails
from schoolarshipxcenter.reader.MadridCenterURLReader import MadridCenterURLReader


class MadridCenterConsolidator:

    FIELD_CENTER_ID = "CODIGO CENTRO"

    @staticmethod
    def process(input_file, delimiter):
        reader = CSVReader(input_file, delimiter)
        rows = reader.read()

        if rows is not None:
            for row in rows:
                # Remove column 'None'. Returned by CSVReader. It's a useless column
                del row[None]

                # Recover center Id
                center_id = row[MadridCenterConsolidator.FIELD_CENTER_ID]

                # Recover Center extra information not included in the CSV file (e-mail)
                center = MadridCenterURLReader(center_id)
                res = center.read()

                if res is not None:
                    row.update(res)
                    print(row)

                #client = DWRClientMadridCenterDetails(center_id)
                #res = client.read()

                #if res is not None:
                #    row.update(res)
                #    print(row)
