with open("input.txt") as f:
    lines = f.readlines()[1:]
    for line in lines:
        l = line.strip().split(" ")
        s = int(l[0])
        b = int(l[1])
        size = int(l[2])

        while size > 4 and b != 0:
            size -= 5
            b -= 1
        
        if size <= s:
            print("true")
        else:
            print("false")