def counts(x ,f):
    count = 0
    for z in f:
        if z == x:
            count += 1
    return count
    

def poker(line):
    f = line
    line = sorted(list(line))
    l = []
    for x in range(1,10):
        l.append(counts(str(x) ,f))
    print(l)
    if(any(x>=5 for x in l)):
        return("FIVE OF A KIND")

    elif(any(x==4 for x in l)):
        return("FOUR OF A KIND")
        
    if(any(x>=3 for x in l)):
        z=l
        e = -1
        for p in range(len(l)):
            if l[p]>=3:
                e = p
        if e > -1:
            z.pop(e)
            if(any(x>=2 for x in z)):
                return "FULL HOUSE"
    for x in range(0, len(line),5):
        if int(line[x]) + 4 == int(line[x+1]) + 3 == int(line[x+2]) + 2 == int(line[x+3]) + 1 == int(line[x+4]):
            return "STRAIGHT"
  
    if(any(x>=2 for x in l)):
        z=l
        for p in range(len(l)):
            if l[p]>3:
                e = p
                
        if x>-1:
            z.pop(x)
            if(any(x>=2 for x in z)):
                return "TWO PAIR"
    if(any(x==2 for x in l)):
        return "PAIR"
    else:
        return max(l)
        
with open("prob15.txt") as f:
    lines = f.readlines()[1:]
    for line in lines:
        line = line.strip()
        print(poker(line))

