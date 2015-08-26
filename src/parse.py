"""
New Coder Data Visualization Project
Parse Data from CSV/Excel and return JSON output
"""

import csv
import logging

FILENAME = "../data/sample-data.csv"

def parse_csv(input_file, delimiter):
    """
    :param input_file: Data source - csv file
    :param delimiter: Delimiter used in the file
    :return: JSON-line object
    """

    # Open File
    opened_file = open(input_file)

    # Declare an empty list to hold the data
    parsed_data = []

    # Read Data from file
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    # Separate the headers from the data part of the file
    file_headers = csv_data.next()

    # For each row, match the headers to the data
    for row in csv_data:
        parsed_data.append(dict(zip(file_headers, row)))

    # Close File
    opened_file.close()

    return parsed_data

def main():
    json_data = parse_csv(FILENAME, ',')
    print json_data


if __name__ == "__main__":
    main()