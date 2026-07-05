

try:
    num = int(input("Enter a number :"))
    result = 10 / num
    print("The result is:", result)

except ZeroDivisionError:
    print("You cannot divide by zero")

except ValueError:
    print("Invalid input. Please enter a valid number.")

else:
    print("Division successful.")

finally:
    print("This block will always execute.")
