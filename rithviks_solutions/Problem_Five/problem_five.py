def linear(line):
    li = []
    num = int(line)
    st = num
    li.append(num)
    while num != 1:
        if num % 2 == 1 and num != 1:
            num = num * 3 + 1
        else:
            num /= 2
    
        li.append(num)
    print(str(st) + ":" + str(len(li)))
    
with open("ProbInput.txt") as input_file:
    lines = input_file.readlines()[1:]
    
    for line in lines:
        line = line.strip()
        linear(line)
 