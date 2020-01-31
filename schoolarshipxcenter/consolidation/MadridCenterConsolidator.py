from schoolarshipxcenter.reader.CSVReader import CSVReader
from schoolarshipxcenter.reader.DWRClientMadridCenterDetails import DWRClientMadridCenterDetails


class MadridCenterConsolidator:

    FIELD_CENTER_ID = "CODIGO CENTRO"

    @staticmethod
    def process(input_file, delimiter):
        reader = CSVReader(input_file, delimiter)
        rows = reader.read()

        if rows is not None:
            for row in rows:
                center_id = row[MadridCenterConsolidator.FIELD_CENTER_ID]

                client = DWRClientMadridCenterDetails(center_id)
                res = client.read()

                if res is not None:
                    row.update(res)
                    print(row)
