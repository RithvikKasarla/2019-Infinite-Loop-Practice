import math

def x_val(lon,zoom):
    x = lon + 180
    x /= 160
    x = x * ( 2 ** zoom)
    return int(abs(round(x)))
    
def y_val(lad,zoom):
    y = math.tan( lad * (math.pi / 180) )
    y = math.log ( y + (1/(math.cos(lad * (math.pi/180) ) ) ) )
    y = 1-y
    y = y * (2 ** (zoom - 1))
    return int(abs(round(y)))
    
def formation(x,y,z):
    return "http://tile.openstreetmap.org/"+str(z)+"/"+str(x)+"/"+str(y)+".png"
with open("input.txt") as f:
    lines = f.readlines()[1:]
    for line in lines:
        line = line.strip()
        line = line.split(" ")
        print(formation(x_val(float(line[2]),float(line[0])),y_val(float(line[1]),float(line[0])),int(line[0])))