def encoder(key, line):
    key = list(key)
    l = len(key)
    li = list(line)
    line = ""
    keyplace = 0
    for ch in range(len(li)):
        if li[ch] == " ":
            line += " "
        else:
            c= ord( key[keyplace%l].lower() ) - 96
            if (ord(li[ch].lower()) + c-1) > 122:
                z = ord(li[ch].lower()) + c-1
                z = z-122
                z +=  96
                line += chr(z)
                keyplace += 1
            else:
                line += chr( ord(li[ch].lower()) + c-1 )
                keyplace += 1
    return line
    
    
with open("input.txt") as f:
    lines = f.readlines()[1:]
    
    for line in range(0 , len(lines), 2):
        print(encoder(lines[line+1].lower().strip(),lines[line].lower().strip()))