# Take three numbers and print the median value (neither maximum nor minimum). 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a > b and a < c) or (a < b and a > c):
    print("Median value is:", a)
elif (b > a and b < c) or (b < a and b > c):
    print("Median value is:", b)
else:
    print("Median value is:", c)