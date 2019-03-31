def batter(line):
    L = line.split(":")
    name = L[0]
    hits = L[1]
    hits = hits.split(",")
    bb = hits.count("BB")
    k = hits.count("K")
    b1 = hits.count("1B")
    b2 = hits.count("2B")
    b3 = hits.count("3B")
    hr = hits.count("HR")
    if (k + b1 + b2 + b3 + hr) != 0:    
        slg = (  ( (1 * b1) + (2 * b2) + (3*b3) + (4*hr) ) / (k + b1 + b2 + b3 + hr) ) 

    return name + "=" + str("%.3f" % (round(slg,3)))


with open("input.txt") as file:
    lines = file.readlines()[1:]
    for line in lines:
        print(batter(line.strip()))