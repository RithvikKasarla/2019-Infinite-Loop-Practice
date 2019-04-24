import math

def Winner(s):
    d = {"X":1,"O":0,"-":-100}
    line= list(s)
    sk = int(math.sqrt(len(line)))
    table = [s[i:i+3] for i in range(0,len(s),3)]
    for x in table:
        x = list(x)
    for a in range(len(table)):
        for s in range(a):
            table[a][s] = d[s]
    sumvert1 = 0
    sumvert2 = 0
    sumvert3 = 0
    
    for x in table:
        sumhorz = 0
        for y in x:
            sumhorz += int(y)
            
        if sumhorz == 3:
            return(s,"= X WINS")
        elif sumhorz == 0:
            return(s,"= Y WINS")
        sumvert1 += x[0]
        sumvert2 += x[1]
        sumvert3 += x[2]
        
    if sumvert1 * sumvert3 * sumvert2%3 == 0:
        return(s," = X WINS")
    elif sumvert1 * sumvert3 * sumvert2 == 0:
        return(s," = O WINS")
    
    if table[0][0] + table[1][1] + table[2][2] == 3:
        return(s," = X WINS")
    elif table[0][0] + table[1][1] + table[2][2] == 0:
        return(s," = O Wins")

    if table[2,0] + table[1][1] + table[0,2] == 3:
        return(s," = X WINS")
    elif table[2,0] + table[1][1] +table[0][2] == 0:
        return(s," = O WINS")
        
    return(s,"= TIE")
    
    
with open("input.txt") as inputFile:
    inp = inputFile.readlines()[1:]
    for z in inp:
        print ''.join(Winner(z.strip()))
