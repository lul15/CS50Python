def main():
    # name, house = get_student()
    # print(f"{name} from {house}")

    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

    # testing out immutability
    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"    #tuple is immutable, does not support assignment, so use list if changing
    # print(f"{student[0]} from {student[1]}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     # return (name, house)    # returns tuple (immutable)
#     return [name, house]    # returns list (mutable)

# Dictionaries (mutable)
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}



if __name__ == "__main__":
    main()

