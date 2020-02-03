import csv


class CSVWriter:

    def __init__(self, file, delimiter=",", quoting=csv.QUOTE_NONE):
        """
        Write a CSV file from a list of dictionaries
        :param file: CSV file
        :param delimiter: field delimiter. By default ','
        :param quoting: Flag to indicate if the field value must be included between quotes
        SEE  https://realpython.com/python-csv/
        """
        self.file = file
        self.delimiter = delimiter
        self.quoting = quoting

    def write(self, rows):
        num_lines = 0

        if rows is not None:
            with open(self.file, 'w', encoding='utf-8', newline='') as f:

                fieldnames = []
                for key in rows[0].keys():
                    fieldnames.append(key)

                print("----------------------------------------")
                print(fieldnames)
                print("----------------------------------------")

                writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=self.delimiter, quoting=self.quoting)

                writer.writeheader()
                num_lines += 1

                for row in rows:
                    print(row.keys())
                    writer.writerow(row)
                    num_lines += 1

        return num_lines
