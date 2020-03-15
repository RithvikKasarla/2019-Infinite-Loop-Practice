num_tests = int(input())

for x in range(num_tests):
    l1 = input()
    l1= l1.strip().split(" ")
    walls = []
    for x in range( int(l1[len(l1)-1]) ):
        walls.append( list(map(int, input().strip().split(" ")))) 
    
    person = (int(l1[0]),int(l1[1]))
    camera = (int(l1[2]),int(l1[3]))
    denom  = (camera[0]-person[0])
    if denom == 0:
        PC_Slope = "UNDEFINED"
        PC_B = camera[0]

    else:
        PC_Slope = float(camera[1]-person[1])/(camera[0]-person[0])
        PC_B = person[1] - float(PC_Slope * person[0])

    WallEq = []
    for wall in walls:
        w = wall
        wallS = (int(w[0]),int(w[1]))
        WallE = (int(w[2]),int(w[3]))
        denomWall = (WallE[0]-wallS[0])
        if denomWall == 0:
            Wall_Slope = "UNDEFINED"
            Wall_B = WallE[1]-wallS[1]
            WallEq.append([Wall_Slope,Wall_B])
        else:
            Wall_Slope = float(WallE[1]-wallS[1])/(WallE[0]-wallS[0])
            Wall_B = wallS[1] - float(Wall_Slope * wallS[0])
            WallEq.append([Wall_Slope,Wall_B])

    interestionpoints = []
    intersects = False
    for idx, wall in enumerate(WallEq):
        if PC_Slope != "UNDEFINED" and wall[0] != "UNDEFINED":
            x = float(wall[1]- PC_B)/(PC_Slope - wall[0])
            y = x * PC_Slope + PC_B
            interestionpoints.append([x,y])
        elif PC_Slope == "UNDEFINED" and wall[0] == "UNDEFINED":
            interestionpoints.append([None, None])
        elif PC_Slope != "UNDEFINED" and wall[0] == "UNDEFINED":
            interestionpoints.append([wall[1], (PC_Slope * wall[1] + PC_B) ])
        elif PC_Slope == "UNDEFINED" and wall[0] != "UNDEFINED":
            interestionpoints.append([PC_B, (wall[0] * PC_B + wall[1])])
    
    for idx, point in enumerate(interestionpoints):
        
        if point == [None,None]:
            continue
        else:
            wall_points = walls[idx]

            if ((point[0] > wall_points[0] and point[0] < wall_points[2]) or (point[0] <= wall_points[0] and point[0] >= wall_points[2])) and ((point[1] > wall_points[1] and point[1] < wall_points[3]) or (point[1] <= wall_points[1] and point[1] >= wall_points[3])):
                print("NO")
                intersects = True
            else:
                continue

    if not intersects:
        print("YES")