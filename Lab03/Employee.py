class Employee:
    def __init__(self, firstName, lastName, age, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.salary = salary

    def getInfo(self):
        return (f"Employee: {self.firstName} {self.lastName}"
                f"\tAge: {self.age} "
                f"\tSalary: {self.salary}")

    def __str__(self):
        return (f"Employee: {self.firstName} {self.lastName}"
                f"\tAge: {self.age} "
                f"\tSalary: {self.salary}")

    def __repr__(self):
        return self.__str__()