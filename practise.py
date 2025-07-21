class Employee:
    compName = "gfg"  # Class attribute

    def __init__(self, id):
        self.id = id  # Instance attribute

e = Employee(1001)

print(e.compName)
print(e.id)
print(Employee.compName)