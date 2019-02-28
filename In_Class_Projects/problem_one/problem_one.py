with open("Prob01.in.txt") as input_file:
    for line in input_file.readlines()[1:]:
        print("PASS" if int(line) >= 70 else "FAIL")
