def sort(lis):
    for x in lis:
        x = int(x.strip())
    return sorted(lis)

def create_fib(line):
    x = 0
    y = 1
    z = 0
    dump = 0
    count = 3
    lo = line
    while len(lo) != 0:
        z = x + y
        x = y
        y = z

        if 




with open("input.txt") as file:
    lines = file.readlines()[1:]
    spots = sort(lines)
    print(create_fib(spots))