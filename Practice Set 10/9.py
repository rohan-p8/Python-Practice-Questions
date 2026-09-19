# Take a character and check if it is a letter, a digit, or neither.

char = input("Enter character: ")

if char.isalpha():
    print("Letter")

elif char.isdigit():
    print("Digit")

else:
    print("Neither letter or digit.")
