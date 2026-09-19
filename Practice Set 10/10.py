# Take a number and print “Fizz” if divisible by 3, “Buzz” if divisible by 5, and 
# “FizzBuzz” if divisible by both. 

n = int(input("Enter a number: "))

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")

elif n % 5 == 0:
    print("Buzz")

elif n % 3 == 0:
    print("Fizz")
    