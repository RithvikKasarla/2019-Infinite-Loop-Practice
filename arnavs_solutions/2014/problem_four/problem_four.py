with open("Prob04.in.txt") as input_file:
    lines = input_file.readlines()

    for line in lines:
        line = line.strip()

        for word in line.split(" "):
            prefix = word[0]
            rest = word[1:]

            print(f"{rest}{prefix}ay", end=" ")
        print()
