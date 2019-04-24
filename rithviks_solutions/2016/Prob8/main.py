def sort(li):
    return sorted(li)
    
def music(li):
    new_li= []
    for x in li:
        y = x.split(" ")
        if y[0] == "The":
            s=""
            for z in range(1,len(x)-4):
                s+= y[z]
            new_li.append(s)
        else:
            new_li.append(y[0])
    s = sort(new_li)
    fin = []
    for z in new_li:
        for u in li:
            print("z",z)
            print('u',u)
            if z in u:
                fin.append(u)
    return fin


with open("input.txt") as f:
    lines = f.readlines()
    t = lines.pop(0)
    for po in range(int(t)):
        pas = []
        x = lines.pop(0)
        for q in range(int(x)):
            pas.append(lines.pop(0).strip())
        fin = music(pas)
        for p in range(len(fin)):
            print(p)
            