num = int(input())
for x in range(num):
    sub = int(input())
    line = input().strip().split(" ")
    un = ""
    for l in line:
        l = list(l)
        for char in l:
            new = ord(char) - 97
            new -= sub
            new %= 26
            un += chr(new+97)
        un += " "
    print(un)