with open("Prob07.txt") as input_file:
    lines = input_file.read().splitlines()

    i = 0
    while i < len(lines):
        i += 1
        print(i)
        in_list = int(lines[i])
        values = []

        for _ in range(in_list):
            i += 1
            values.append(float(lines[i]))

        maxNum = max(values)
        minNum = max(values)

        for value in values:
            if minNum == maxNum:
                print(0)
            else:
                print(round((value - minNum) / (maxNum - minNum) * 255))
