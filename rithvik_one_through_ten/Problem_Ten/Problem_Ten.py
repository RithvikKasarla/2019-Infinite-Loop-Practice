with open("Probinput.txt") as input_file:
    lines = input_file.readlines()[1:]
for line in range(1,len(lines)+1,3):
    x = str(lines[line-1]).split(",")
    z = str(lines[line]).split(",")
    y = str(lines[line+1]).split(",")
    
    if (int(z[0]) - int(z[1])) == (int(y[0]) - int(y[1])):
        print("YES")
    else:
        print("No")