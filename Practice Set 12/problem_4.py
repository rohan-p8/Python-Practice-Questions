
try:
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))

    result = a / b
    print("The result of division is:", result)


except ZeroDivisionError:
    print("Infinite by handling the 'ZeroDivisionError' exception")

else:
    print("This block is executed only if no exception occurs.")

finally:
    print("This block is always executed, regardless of whether an exception occurred or not.")