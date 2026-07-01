class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * self.increment / 100

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary / self.salary) - 1) * 100


e = Employee(50000, 10)

print("Salary:", e.salary)
print("Increment:", e.increment)
print("Salary After Increment:", e.salaryAfterIncrement)

e.salaryAfterIncrement = 60000

print("\nAfter changing salaryAfterIncrement to 60000")
print("New Increment:", e.increment)

