#list
# students = ["Hermione", "Harry", "Ron"]
#
# print(students[0])
# print(students[1])
# print(students[2])

#equivalent to
# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i + 1, students[i])

#dict
# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
# }
#
# for student in students:
#     # iterate over all the keys, second parameter is the value
#     print(student, students[student], sep=", ")


#list of dictionaries
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
