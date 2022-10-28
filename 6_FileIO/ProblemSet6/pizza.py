import csv
import sys

from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        check_file(sys.argv[1])


def check_file(filename):
    if filename.endswith(".csv"):
        try:
            with open(filename) as file:
                reader = csv.DictReader(file)
                print(tabulate(reader, headers="keys", tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
