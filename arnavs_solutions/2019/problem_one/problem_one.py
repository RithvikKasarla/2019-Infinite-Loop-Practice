with open("Prob01.txt") as input_file:
    for line in input_file.read().splitlines()[1:]:
        print(line.lower())
