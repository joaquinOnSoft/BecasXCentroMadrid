import csv


class CSVReader:

    def __init__(self, file, delimiter=",", quoting=csv.QUOTE_NONE):
        """
        Read a CSV file
        :param file: CSV file
        :param delimiter: field delimiter. By default ','
        :param quoting: Flag to indicate if the field value must be included between quotes
        SEE  https://realpython.com/python-csv/
        """
        self.file = file
        self.delimiter = delimiter
        self.quoting = quoting

    def read(self):
        rows = {}

        with open(self.file, 'r', encoding='utf-8') as f:
            rows = []

            csv_reader = csv.DictReader(f, delimiter=self.delimiter, quoting=self.quoting)
            for row in csv_reader:
                rows.append(row)

            return rows
