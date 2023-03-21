class Student:  # OOP, the class is the custom data type Student
    def __init__(self, name, house):  # initialization method / instance method, method is just a function inside a class
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Ravenclaw", "Slytherin", "Hufflepuff"]:
            raise ValueError("Invalid house")
        self.name = name  # self needs to come first, gives you access to the current object
        self.house = house  # name and house are attributes (aka instance variables)
        #self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    #by convention, if it is a method (function within a class)
    # needs at least one parameter - "self" to have access to current object
    # def charm(self):
    #     match self.patronus:
    #         case "Stag":
    #             return "🦌"
    #         case "Otter":
    #             return "🦦"
    #         case "Jack Russell terrier":
    #             return "🐶"
    #         case _:
    #             return "🪄"


def main():
    student = get_student()

    # example of where you can still edit the attribute post-initialization
    # circumvents error checking
    student.house = "Number Four, Privet Drive"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    #patronus = input("Patronus: ")
    # student = Student(name, house)  # Constructor call - instantiates a Student object
    # return student
    return Student(name, house)


if __name__ == "__main__":
    main()
