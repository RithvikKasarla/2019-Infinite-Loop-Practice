with open("Prob08.in.txt") as input_file:
    lines = [map(float, line.strip().split()) for line in input_file.readlines()[1:]]
    for line in lines:
        outputs = []
        for angle in line:
            new_angle = str(round((angle - 180) % 360, 2)).zfill(5)
            outputs.append(new_angle + '0' if len(new_angle) == 5 else new_angle)

        print(*outputs, sep=' ')
