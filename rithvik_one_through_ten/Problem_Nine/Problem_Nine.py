with open("ProbInput.txt") as input_file:
    lines = input_file.readlines()[1:]
for line in lines:
    line.strip()
    line  = line.split(",")
    if int(line[0]>line[1]):
        x = int(line[0])
        y = int(line[1])
        z = 1000
    else:
        x = int(line[1])
        y = int(line[0])
        z= 10000
    while (z != 0):
        z = abs(x - y)
        if x > y:
            print x,"-",y,"=",z 
            x = y
            y = z
        else:
            print y,"-",x,"=",z 
            y = x
            x = z
            
    if z == 1:
        print("COPRIME")
    else:
        print("NOT COPRIME")
    