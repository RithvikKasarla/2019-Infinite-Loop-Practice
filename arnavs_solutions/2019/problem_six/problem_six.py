from math import pi

test_cases = int(input())

EARTH_RADIUS = 40075 / (2 * pi)

for _ in range(test_cases):
    altitude = int(input())
    circumference = (EARTH_RADIUS + altitude) * 2 * pi

    print(round(circumference, 1))
