with open("input.txt") as f:
    lines = f.readlines()[1:]
    for line in lines:
        l = line.strip()
        print(l.lower())
