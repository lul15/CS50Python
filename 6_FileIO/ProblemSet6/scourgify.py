import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        write_files(sys.argv[1], sys.argv[2])


def write_files(file1, file2):
    students = []
    try:
        with open(file1) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name": row["name"], "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {file1}")

    # write to file
    with open(file2, "w") as file2:
        writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            name = student['name'].split(",")
            first_name = name[1].strip()
            last_name = name[0].strip()
            writer.writerow({"first": first_name, "last": last_name, "house": student["house"]})


if __name__ == "__main__":
    main()
