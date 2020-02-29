with open("input.txt") as f:
    lines = f.readlines()[1:]
    for line in lines:
        l = line.strip().split(" ")
        n1 = int(l[0])
        n2 = int(l[1])
        if n1 == n2:
            print( 2 * (n1 + n2))
        else:
            print(n1 + n2)