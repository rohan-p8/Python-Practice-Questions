class Programmer:
    company = "Microsoft"

# You can also use any valid variable name in place of 'self' but 
# it is a convention to use 'self' as the first parameter of 
# instance methods in Python. It refers to the instance of the 
# class and allows you to access the attributes and methods of 
# that instance.   

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