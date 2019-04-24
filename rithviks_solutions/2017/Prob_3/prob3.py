def addiply(num1, num2):
    return  str(num1 + num2) + " " + str(num1 *  num2)


with open("prob3.txt") as f:
    lines = f.readlines()[1:]
    for line in lines:
        l = line.split()
        num1 = int(l[0])
        num2 = int(l[1])
        print addiply(num1, num2)