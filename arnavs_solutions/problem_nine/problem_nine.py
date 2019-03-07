with open("Prob09.in.txt") as input_file:
    for line in input_file.readlines()[1:]:
        minuend = -1
        subtrahend, difference = map(int, line.strip().split(","))
        while difference != 0:
            minuend = subtrahend if subtrahend > difference else difference
            subtrahend = difference if minuend == subtrahend else subtrahend
            difference = minuend - subtrahend
            print("{}-{}={}".format(minuend, subtrahend, difference))

        print("COPRIME" if minuend == 1 else "NOT COPRIME")
