def game():
    return 95

score = game()

with open("Hi_score.txt", "r") as f:
    hi_score = f.read()

if hi_score == "":
    hi_score = 0
else:
    hi_score = int(hi_score)

if score > hi_score:
    with open("Hi_score.txt", "w") as f:
        f.write(str(score))

with open("Hi_score.txt", "r") as f:
    content = f.read()

print(content)

game()