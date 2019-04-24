with open("Prob10.in.txt") as input_file:
    lines = [
        list(map(int, line.strip().split(","))) for line in input_file.readlines()[1:]
    ]
    for i in range(0, len(lines), 3):
        (x1, y1), (x2, y2) = lines[i + 1 : i + 3]
        print("Yes" if abs(y2 - y1) / (x2 - x1) == 1 else "No")
