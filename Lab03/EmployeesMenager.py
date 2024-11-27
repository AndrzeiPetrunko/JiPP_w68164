from Employee import Employee


class EmployeesMenager:
    def __init__(self):
        self.employees = []

    def AddEmployee(self):
        print("Pass employee information: ")
        firstName = input("Name: ")
        lastName = input("Surname: ")
        age = int(input("Age: "))
        salary = float(input("Salary: "))
        self.employees.append(Employee(firstName, lastName, age, salary))

    def viewEmployees(self):
        if len(self.employees) > 0:
            for employee in self.employees:
                print(employee)
        else:
            print("There are no employees yet.")
            return

    def deleteEmployeesByAge(self, ageFrom, ageTo):
        for employee in self.employees:
            if employee.age >= ageFrom and employee.age <= ageTo:
                print(f"Employee {employee.firstName} {employee.lastName} deleted.")
                self.employees.remove(employee)

    def findEmployeesByName(self, firstName, lastName):
        for employee in self.employees:
            if employee.firstName == firstName and employee.lastName == lastName:
                return employee
            return None

    def updateSalaryByName(self, firstName, lastName, salary):
        employee = self.findEmployeesByName(firstName, lastName)
        if employee is not None:
            print("There are no employee named", firstName, lastName,".")
        employee.salary = salary