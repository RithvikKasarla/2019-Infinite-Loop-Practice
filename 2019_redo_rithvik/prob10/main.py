num = int(input())
for x in range(num):
    sub = int(input())
    line = input().strip().split(" ")
    un = ""
    for l in line:
        l = list(l)
        for char in l:
            new = ord(char) - (sub%26)
            if new < 97:
                new = 122 + (97-new)
            un += chr(new)
        un += " "
    print(un)