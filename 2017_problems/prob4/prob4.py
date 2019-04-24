def sort(lis):
    for x in range(len(lis)):
        lis[x] = int(lis[x].strip())
    return sorted(lis)

def create_fib(line):
    x = 0
    y = 1
    z = 0
    dump = 0
    count = 3
    lo = line
    lin = []
    if lo[0] == 1:
        lin.append("1 = 0")
        lo.pop(0)
    if lo[0] == 2:
        lin.append("2 = 1")
        lo.pop(0)

    while len(lo) != 0:
        z = x + y
        x = y
        y = z
        print(z, "=",  count)
        if count in line:
            lin.append(str(lo.pop(0))+ " = "+ str(z))
        count += 1
    return(lin)




with open("input.txt") as file:
    lines = file.readlines()[1:]
    spots = sort(lines)
    l = create_fib(spots)
    for x in l:
        print(x)