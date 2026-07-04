
age = int(input("Enter your age: "))

if age < 18:
    raise ValueError("You must be at least 18 years old to proceed.")

else:
    print("Welcome! You are old enough to proceed.")

print("This line will not be executed if an exception is raised.")