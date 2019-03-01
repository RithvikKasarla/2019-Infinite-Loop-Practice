def collatz(num):
    ct = 0
    while num != 1:
        num = num / 2 if num % 2 == 0 else num * 3 + 1
        ct += 1
    return ct + 1

with open("Prob05.in.txt") as input_file:
    lines = [line.strip() for line in input_file.readlines()[1:]]

    for line in lines:
        print("{}:{}".format(line, collatz(int(line))))
