import csv

from schoolarshipxcenter.reader.CSVReader import CSVReader
from schoolarshipxcenter.writer.CSVWriter import CSVWriter


class MadridGrantByCenterConsolidator:
    FIELD_GR_GRANT_AMOUNT = "CUANTÍA DE LAS BECAS"
    FIELD_GR_CENTER_ID = "CÓDIGO DE CENTRO"
    FIELD_CE_CENTER = "CODIGO CENTRO"

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
                    grant_dict[grant[MadridGrantByCenterConsolidator.FIELD_GR_CENTER_ID]] = \
                        grant[MadridGrantByCenterConsolidator.FIELD_GR_GRANT_AMOUNT]

                center_id = None
                for center in centers:
                    # Remove column 'None'. Returned by CSVReader. It's a useless column
                    del center[None]

                    center_id = center[MadridGrantByCenterConsolidator.FIELD_CE_CENTER]
                    if center_id in grant_dict.keys():
                        amount = grant_dict[center_id]
                    else:
                        amount = 0

                    center[MadridGrantByCenterConsolidator.FIELD_GR_GRANT_AMOUNT] = amount

                    amount = None

                reader = CSVWriter(output_file, output_delimiter, csv.QUOTE_ALL)
                reader.write(centers)
