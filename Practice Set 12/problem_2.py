list = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]

for i, num in enumerate(list, start=1):
    if i in [3, 5, 7]:
        print(num)