class Programmer:
    company = "Microsoft"


# You can also use any valid variable name in place of 'self' but it is a convention to use 'self' as the first parameter of instance methods in Python. It refers to the instance of the class and allows you to access the attributes and methods of that instance.   
    def __init__(slf, name, empid, salary):
        slf.name = name
        slf.empid = empid
        slf.salary = salary


    def getInfo(slf):
        print(f"Company: {slf.company}")
        print(f"Name: {slf.name}")
        print(f"Employee ID: {slf.empid}")
        print(f"Salary: {slf.salary}")


p1 = Programmer("Rohan", 101, 50000)

p2 = Programmer("Sohan", 102, 60000)

p1.getInfo()
print()
p2.getInfo()
