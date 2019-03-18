from math import sin, cos, radians

def starpoints(coords):
    xc, yc, num_points, r1, r2 = map(int, coords.split(" "))
    total_vertices = num_points * 2

    angle_increment = 360 / total_vertices

    result = []
    angle = 90
    for i in range(total_vertices):
        next_point = [0, 0]
        if i % 2 == 0:
            next_point = [r1 * cos(radians(angle)) + xc, r1 * sin(radians(angle)) + yc]
        else:
            next_point = [r2 * cos(radians(angle)) + xc, r2 * sin(radians(angle)) + yc]
        angle += angle_increment
        if round(next_point[0]) == 0:
            next_point[0] = "0.00"
            next_point[1] = "{0:.2f}".format(next_point[1])
        elif round(next_point[1]) == 0:
            next_point[1] = "0.00"
            next_point[0] = "{0:.2f}".format(next_point[0])
        else:
            next_point[0] = "{0:.2f}".format(next_point[0])
            next_point[1] = "{0:.2f}".format(next_point[1])
        result.append(next_point)

    result_string = ""
    for point in result:
        result_string += ",".join(point) + " "
    return result_string[:-1]

import os

with open(os.path.join(os.path.dirname(__file__), "Prob16.in.txt")) as inputFile:
    inputs = inputFile.readlines()[1:]
    for x in inputs:
        x = x.strip()
        print(starpoints(x))
    