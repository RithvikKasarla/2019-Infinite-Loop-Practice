def remove(s,p):
    return(s[0:int(p)] + s[int(p)+1:])
    


with open("prob2.txt") as f:
    lines = f.readlines()[1:]
    for line in lines:
        line= line.strip()
        l = line.split(" ")
        s = l[0]
        p = l[1]
        print(remove(s,p))