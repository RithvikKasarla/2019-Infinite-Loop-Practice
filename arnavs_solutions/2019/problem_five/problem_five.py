with open("Prob05.txt") as input_file:
    lines = input_file.read().splitlines()

    for line in lines[1:]:
        small, large, target = map(int, line.split(" "))

        target -= small

        if target <= 0:
            print("true")
            continue

        if small :


        if target % 5 == 0:
            print("true")
        else:
            print("false")
