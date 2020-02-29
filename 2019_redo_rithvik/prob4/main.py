with open("input.txt") as f:
    lines = f.readlines()[1:]
    for line in lines:
        l = line.strip().split(" ")
        speed = int(l[0])
        birthday = l[1]
        if "t" in birthday:
            speed -= 5
        if speed <= 60:
            print("no ticket")
        elif speed >= 81:
            print("big ticket")
        else:
            print("small ticket")