def donor_sort(l1, l2):
    last = []
    both = []
    this = []
    l1 = l1.split(",")
    l2 = l2.split(",")
    for person in l1:
        if person in l2:
            last.append(person)
        else:
            both.append(person)
    for person in l2:
        if person not in l1:
            this.append(person)
    return [' '.join(both) , ' '.join(last), ' '.join(this)]

with open("prob5.txt") as f:
    lines = f.readlines()
    z = lines.pop(0).strip()
    for x in range(0,len(lines), int(z)):
        x= donor_sort(lines[x].strip(),lines[x+1].strip())
        print(x[0] + "\n" + x[1] + "\n" + x[2])
        