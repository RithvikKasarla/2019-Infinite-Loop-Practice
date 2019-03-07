import math
with open("probinput.txt") as inputFile:
    lines = int(inputFile.readline().replace("\n", ""))
    for x in range(0,lines):
        line = inputFile.readline().replace("\n", "")
        data = line.split(" ")
        redDist = (int(data[0]) - int(data[4])) ** 2
        greenDist = (int(data[1]) - int(data[5])) ** 2
        blueDist = (int(data[2]) - int(data[6])) ** 2
        distance = math.sqrt(redDist + greenDist + blueDist)
        if  int(data[3]) >= distance:
            print data[7],data[8],data[9] 
        else:
            print data[4],data[5],data[6] 