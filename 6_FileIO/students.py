import csv

# with open("students.csv") as file:
#     for line in file:
#         # row = line.rstrip().split(",")
#         # print(f"{row[0]} is in {row[1]}")
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")

students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         # student = {}
#         # student["name"] = name
#         # student["house"] = house
#         student = {"name": name, "house": house}
#         students.append(student)


# def get_name(student):
#     return student["name"]
#
#
# def get_house(student):
#     return student["house"]


# # characteristic of python, can pass in a function as a parameter of another function
# # see key function
# # Key function only takes in the function name, not (), bc sorted will be calling it on my behalf
# for student in sorted(students, key=get_name):
#     print(f"{student['name']} is in {student['house']}")


# read csv
# with open("students.csv") as file:
#     reader = csv.DictReader(file)   # Read each row in as a dictionary
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})
#
# # lambda function == get_name(), this is an anonymous function
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

# # write to csv
# name = input("What's your name? ")
# home = input("Where's your home? ")
#
# with open("students.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])
#

# write to csv using DictWriter
name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
