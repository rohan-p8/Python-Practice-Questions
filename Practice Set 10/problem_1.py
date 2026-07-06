class Programmer:
    company = "Microsoft"

    def __init__(self, name, empid, salary):
        self.name = name
        self.empid = empid
        self.salary = salary

    def getInfo(self):
        print(f"Company: {self.company}")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.empid}")
        print(f"Salary: {self.salary}")

p1 = Programmer("Rohan", 101, 50000)

p2 = Programmer("Sohan", 102, 60000)

p1.getInfo()
print()
p2.getInfo()