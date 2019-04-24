def collatz(n):
    t = 0
    while n != 1:
        t += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
    
    return t + 1

with open("Prob05.in.txt") as input_file:
    lines = input_file.readlines()[1:]
    
    for line in lines:
        l = int(line.strip())
        print("{}:{}".format(l, collatz(l)))
