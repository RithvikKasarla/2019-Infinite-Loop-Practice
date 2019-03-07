import math
with open("probinput.txt") as inputFile:
    lines = int(inputFile.readline().replace("\n", ""))
    for x in range(0,lines):
        line = inputFile.readline().replace("\n", "")
        data = line.split(" ")
        red = (int(data[0]) - int(data[4])) ** 2
        green = (int(data[1]) - int(data[5])) ** 2
        blue = (int(data[2]) - int(data[6])) ** 2
        dist = math.sqrt(red + green + blue)
        if  int(data[3]) >= dist:
            print data[7],data[8],data[9] 
        else:
            print data[4],data[5],data[6] 
