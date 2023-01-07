from schoolarshipxcenter.reader.CSVReader import CSVReader


class MadridGrantByCenterConsolidator:
    FIELD_GRANT_AMOUNT = "CUANTÍA DE LAS BECAS"
    FIELD_CENTER_ID = "CÓDIGO DE CENTRO"

    @staticmethod
    def process(center_file, center_delimiter, grant_file, grant_delimiter, output_file):
        center_reader = CSVReader(center_file, center_delimiter)
        rows = center_reader.read()

        if rows is not None:

            lines = []
            num_lines = 0

            for row in rows:
                # Remove column 'None'. Returned by CSVReader. It's a useless column
                del row[None]
