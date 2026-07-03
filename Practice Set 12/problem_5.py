n = int(input("Enter a number for multiplication table: "))

list = [n * i for i in range(1, 11)]
print(list)

with open("table.txt", "w") as f:
    f.write(str(list))


with open("table.txt", "r") as f:
    content = f.read()
    print("\nThis is table.txt file:", content)

