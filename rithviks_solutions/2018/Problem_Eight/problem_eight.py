def apollo(line):
    line = line.strip()
    li = line.split(" ")
    for x in li:
        x = x.split(".")
    for x in range(0,len(li),2):
        if int(x) + (int(x+1) /100) >= 180:
            li[x] = int(x) + (int(x+1) /100) - 180
        else:
            li[x] = int(x) + (int(x+1) /100) + 180
    print(li)
    
    
with open("ProbInput.txt") as input_file:
    lines = input_file.readlines()[1:]
for line in lines:
    apollo(line)
    