def rewrite(line):
    DICTION = {"A":"Alpha", "N":"November", "B":"Bravo", "O":"Oscar", "C":"Charlie", "P":"Papa", "D":"Delta", "Q":"Quebec", "E":"Echo", "R":"Romeo","F":"Foxtrot", "S":"Sierra", "G":"Golf", "T":"Tango", "H":"Hotel", "U":"Uniform", "I":"India", "V":"Victor", "J":"Juliet", "W":"Whiskey", "K":"Kilo", "X":"Xray", "L":"Lima", "Y":"Yankee", "M":"Mike", "Z":"Zulu"," ":" "}
    line += " "
    l = list(line)
    s = ""
    for x in range(len(l)):
        s += DICTION[l[x].upper]
        try:
            if  l[x + 1]  !=  " ":
                s+= "-"
        except:
            pass
    return(s)
    

with open("prob6.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        try:
            print(rewrite(line))
        except:
            pass
