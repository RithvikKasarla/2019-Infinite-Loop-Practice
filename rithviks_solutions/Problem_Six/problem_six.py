def machine(line):
    statuses = line.split(" ")
    value = 8
    code = 0
    errorCode = {0:"off", 1:"red", 2:"green", 3:"blue"}
    for status in statuses:
        if status == "BROKEN":
            code = code + value
        value = value / 2
    left = "off"
    right = "off"
    lval = code // 4
    rval = code % 4
    right = errorCode[rval]
    left = errorCode[lval]
    print(left + " " + right)
    
with open("probinput.txt") as inputFile:
    lines = inputFile.readline().strip()
    for line in lines:
        line = inputFile.readline().strip()
        machine(line)