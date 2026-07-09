word = ["donkey", "bad"]

with open("sample.txt", "r") as f:
    content = f.read()

    for w in word:
        contentnew = content.replace(w, "####")

with open("sample.txt", "w")as f:
    f.write(contentnew)

    print(contentnew)