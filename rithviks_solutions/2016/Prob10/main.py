def GCAS(line, N):
    
    previousAltitude = 0
    currentAltitude = 0
    futureAltitude = 0
    currentElevation = 0
    futureElevation = 0
    z= ""
    for x in range(N):
        currentAltitude = int(line.split(",")[0])
        futureElevation = int(line.split(",")[1])
        
        altitudeDifference = currentAltitude - previousAltitude
        
        futureAltitude = currentAltitude + altitudeDifference
        if (futureAltitude <= futureElevation):
            return ("PULL UP!")
        elif ((currentAltitude - currentElevation) <= 500):
            return ("Low Altitude!")
        else:
            return ("ok")
            
        previousAltitude = currentAltitude;
        currentElevation = futureElevation;


with open("input.txt") as f:
    lines = f.readlines()[1:]
    N = lines.pop(0)
    for line in lines:
        print( GCAS(line.strip(),int(N.strip())) )