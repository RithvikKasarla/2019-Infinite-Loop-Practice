with open("input.txt") as f:
    lines = f.readlines()[1:]
    for line in lines:
        line = line.strip()
        l = line.split(" ")
        if not(("t" in l[0]) ^ ("t" in l[1])):
            print ("true")
        else:
            print ("false")