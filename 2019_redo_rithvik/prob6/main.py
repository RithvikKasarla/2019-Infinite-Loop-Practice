from math import pi
with open("input.txt") as f:
    lines = f.readlines()[1:]
    for line in lines:
        l = int(line.strip())
        r = 40075 / (2*pi)
        print( round( (l + r) * 2 * pi ,1))
