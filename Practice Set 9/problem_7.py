

with open("log.txt", "r") as f:
    line_no = 1

    for line in f:
        if "python" in line.lower():
            print(f"Python is present on line {line_no}")
        
        line_no += 1