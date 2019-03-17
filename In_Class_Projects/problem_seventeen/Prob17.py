import math

def Winner(s):
    d = {"X":1,"O":0,"-":-100}
    fline= s.split()
    line = fline[0]
    sk = int(math.sqrt(len(line)))
    table = [[d[line[i]]] * sk for i in range(sk)]
    sumvert1 = 0
    sumvert2 = 0
    sumvert3 = 0
    for x in table:
        sumhorz = 0
        for y in x:
            sumhorz += int(y)
            
        if sumhorz == 3:
            return(s,"= X Wins")
        elif sumhorz == 0:
            return(s,"= Y Wins")
        sumvert1 += x[0]
        sumvert2 += x[1]
        sumvert3 += x[2]
        
    if sumvert1 * sumvert3 * sumvert2%3 == 0:
        return(s,"= X Wins")
    elif sumvert1 * sumvert3 * sumvert2 == 0:
        return(s,"= O Wins")
    
    if table[0][0] + table[1][1] + table[2][2] == 3:
        return(s,"= X Wins")
    elif table[0][0] + table[1][1] + table[2][2] == 0:
        return(s,"= O Wins")

    if table[2,0] + table[1][1] + table[0,2] == 3:
        return(s,"= X Wins")
    elif table[2,0] + table[1][1] +table[0][2] == 0:
        return(s,"= O Wins")
        
    return(s,"= Tie")
    
    
with open("input.txt") as inputFile:
    inp = inputFile.readlines()[1:]
    for z in inp:
        print(Winner(z.strip()))
