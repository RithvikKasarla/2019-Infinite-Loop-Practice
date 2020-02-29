from math import pi

with open("Prob06.txt") as input_file:
    lines = input_file.read().splitlines()

    earth_radius = 40075 / (2 * pi)
    for line in lines[1:]:
        altitude = int(line)
        circumference = (earth_radius + altitude) * 2 * pi

        print(round(circumference, 1))
