import sys

#read in command line argument, need to be exactly 2
def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        lines = check_file(sys.argv[1])
        print(lines_of_code(lines))


def check_file(filename):
    # check file ends in .py
    if filename.endswith(".py") == False:
        sys.exit("Not a Python file")
    else:
        try:
            with open(filename) as file:
                lines = file.readlines()
                return lines
        except FileNotFoundError:
            sys.exit("File does not exist")


def lines_of_code(lines):
    count = 0
    for line in lines:
        if line.strip() != "" and line.strip().startswith("#") == False:
            count = count + 1
    return count


if __name__ == "__main__":
    main()
