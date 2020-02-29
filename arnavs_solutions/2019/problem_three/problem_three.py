with open("Prob03.txt") as input_file:
    lines = input_file.read().splitlines()[1:]

    for line in lines:
        a, b = line.split(" ")

        if a[0] == "t":
            a = True
        else:
            a = False
        if b[0] == "f":
            b = True
        else:
            b = False

        if a ^ b:
            print("true")
        else:
            print("false")
