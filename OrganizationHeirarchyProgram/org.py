import json

class Employee:
    def __init__(self, empId, name, designation, reportsTo, dateOfBirth, salary, someData, someMoreData) -> None:
        self.empId = empId
        self.name = name
        self.designation = designation
        self.reportsTo = reportsTo
        self.dateOfBirth = dateOfBirth
        self.salary = salary
        self.someData = someData
        self.someMoreData = someMoreData
        self.subordinates = []

    @staticmethod
    def createEmployee(empDetails):
        empId, name, designation, reportsTo, dateOfBirth, salary, someData, someMoreData = [i for i in empDetails]
        return Employee(empId, name, designation, reportsTo, dateOfBirth, salary, someData, someMoreData)

    @staticmethod
    def spacing(level):
        spaces = level
        while spaces > 0:
            print("       ", end="")
            spaces -= 1

    def displayEmployee(self, level):
        if level == 0:        
            print(self.name + ' (' + self.designation + ')')
        else:
            Employee.spacing(level)
            print("|--" + self.name + ' (' + self.designation + ')')
        for subordinate in self.subordinates:
            subordinate.displayEmployee(level+1)


lines = []
with open("emp.txt") as file_in:
    lines = file_in.read().splitlines()
    withoutDuplicates = [*set(lines)]
    lines = withoutDuplicates

listOfEmployees = []

for str in lines:
    listOfAttributes = [item for item in str.split(",")]
    listOfEmployees.append(Employee.createEmployee(listOfAttributes))

ceo = None

for emp in listOfEmployees:
    boss = emp.reportsTo
    if boss == 'NULL':
        ceo = emp
    for e in listOfEmployees:
        if e.empId == boss:
            (e.subordinates).append(emp)


# ceoDict = ceo.__dict__
# ceoJsonObj = json.dumps(ceo, default= lambda em : em.__dict__, spacing=5)
# print(ceoJsonObj)

ceo.displayEmployee(0)