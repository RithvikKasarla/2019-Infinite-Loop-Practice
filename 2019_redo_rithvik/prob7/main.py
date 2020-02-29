with open("input.txt") as f:
    lines = f.readlines()
    for l in range(int(lines[0].strip())):
        lines.pop(0)
        ar = []
        for x in range(int(lines[0].strip())):
            p = lines.pop(0)
            ar.append(float(p.strip()))

        
        for y in ar:
            if  max(ar) == min(ar):
                print("0")
            else:
                print(int(round(  ((y-min(ar))/ (max(ar)-min(ar))) * 255, 0)))