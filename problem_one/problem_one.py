with open("Prob01.in.txt") as input_file:
    lines = input_file.readlines()[1:]
    
    for line in lines:
        print("PASS" if int(line) >= 70 else "FAIL")
