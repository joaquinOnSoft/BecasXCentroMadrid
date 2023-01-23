import csv

from schoolarshipxcenter.reader.CSVReader import CSVReader
from schoolarshipxcenter.writer.CSVWriter import CSVWriter


class MadridGrantByCenterConsolidator:
    FIELD_GRANT_AMOUNT = "CUANTÍA DE LAS BECAS"
    FIELD_CENTER_ID = "CÓDIGO DE CENTRO"

    @staticmethod
    def process(center_file, center_delimiter, grant_file, grant_delimiter, output_file, output_delimiter):
        center_reader = CSVReader(center_file, center_delimiter)
        centers = center_reader.read()

        if centers is not None:

            num_lines = 0
            lines = []

            grant_reader = CSVReader(grant_file, center_delimiter)
            grants = grant_reader.read()

            if grants is not None:
                grant_dict = {}
                for grant in grants:
                    grant_dict[grant[MadridGrantByCenterConsolidator.FIELD_CENTER_ID]] = \
                        grant[MadridGrantByCenterConsolidator.FIELD_GRANT_AMOUNT]

                for center in centers:
                    # Remove column 'None'. Returned by CSVReader. It's a useless column
                    del center[None]

                    amount = grant_dict[grant[MadridGrantByCenterConsolidator.FIELD_CENTER_ID]]
                    if amount is not None:
                        amount = 0
                    else:
                        center[MadridGrantByCenterConsolidator.FIELD_GRANT_AMOUNT] = amount

                reader = CSVWriter(output_file, output_delimiter, csv.QUOTE_ALL)
                reader.write(centers)
