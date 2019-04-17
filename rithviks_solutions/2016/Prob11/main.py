def en_de(lines):
    t = lines.pop(0).strip()
    print("t",t)
    code = lines.pop(0).strip()
    ans = []
    if t == "ENCRYPT":
        code = list(code)
        for line in lines:
            z = ""
            l = list(line)
            for c in l:
                ascii = ord(c.lower()) - 97
                if c.islower():
                    z += code[ascii]
                elif c.isupper():
                    z+= code[ascii].upper()
                else:
                    z+= " "
            ans.append(z)
                
    else:
        code = list(code)
        for line in lines:
            z = ""
            l = list(line)
            for c in line:
                z = code.index(c.lower())
                ascii = 97 + z
                if c.isupper():
                    z+= chr(ascii).upper()
                elif c.islower():
                    z += chr(ascii)
                else:
                    z += " "
            ans.append(z)
    return(ans)


with open("input.txt") as l:
    f = l.readlines()
    tasks = f.pop(0)
    for p in range(int(tasks.strip())):
        line = []
        line.append(f.pop(0).strip())
        line.append(f.pop(0).strip())
        for x in range(int(tasks[0])):
            line.append(f.pop(0).strip())
        print(en_de(line))