with open("this.txt", "r") as f:
    content = f.read()


with open("copy.txt", "r") as f:
    content_c = f.read()

    if content == content_c:
        print("The content of both files is the same.")
    else:
        print("The content of both files is different.")