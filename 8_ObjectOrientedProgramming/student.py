class Student:  #OOP, custom data type Student
    def __init__(self, name, house): # initialization method, method is just a function inside a class
        self.name = name    # self needs to come first, gives you access to the current object
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)  # Constructor call
    return student



if __name__ == "__main__":
    main()

