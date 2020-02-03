import time
from schoolarshipxcenter.reader.CSVReader import CSVReader
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
                        center = MadridCenterURLReader(center_id)
                        res = center.read()

                        if res is not None:
                            row.update(res)
                            lines.append(row)
                            print(num_lines, row)

                        retry = False
                    except ConnectionResetError:
                        # An error 'ConnectionResetError' happens when you try a
                        # few hundreds of consecutive calls to the server.
                        print("Sleeping 5 seconds")
                        time.sleep(5)

                #client = DWRClientMadridCenterDetails(center_id)
                #res = client.read()

                #if res is not None:
                #    row.update(res)
                #    print(row)

            reader = CSVWriter(output_file, delimiter)
            reader.write(lines)