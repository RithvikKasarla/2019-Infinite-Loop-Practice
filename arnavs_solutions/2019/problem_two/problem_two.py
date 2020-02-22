with open("Prob02.txt") as input_file:
    lines = input_file.read().splitlines()[1:]

    for line in lines:
        a, b = map(int, line.split())
        print(a + b)
