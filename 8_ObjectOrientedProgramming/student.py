
# Property - an attribute that engineers have more control over
# @property - function in Python.
# Decorators - functions that modify the behavior of other functions

class Student:  # OOP, the class is the custom data type Student
    # double underscore (aka dunder)
    def __init__(self, name, house):  # initialization method / instance method, method is just a function inside a class
        self.name = name  # self needs to come first, gives you access to the current object
        self.house = house  # name and house are attributes (aka instance variables), calls the setter method (with .house)

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getters and setters allow Python to detect when programmer is trying to manually set a value.
    # Enables control over the object and ability to trust.
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name


    # Getter - function in a class gets some value
    @property
    def house(self):
        return self._house  # _house (instance variable) to differentiate from property name house
        #underscore signals "private", but in Python this is on the honor system (unlike Java which strictly enforces visiblity - private/protected/public)

    # Setter - function in a class that sets some value
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
