def starpoints(coords):
    pass

with open("Prob16.in.txt") as inputFile:
    inputs = inputFile.readlines()
    for x in inputs:
        x = x.strip()
        starpoints(x)
    