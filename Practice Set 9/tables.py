for i in range(2, 21):
    with open(f"tables/table_{i}.txt", "w") as file:
        for j in range(1, 11):
            file.write(f"{i} x {j} = {i * j}\n")     