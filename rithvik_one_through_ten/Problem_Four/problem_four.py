with open("ProbInput.txt") as input_file:
    lines = input_file.readlines()[1:]
    
    for line in lines:
        line=line.strip()
        data = line
        dic = dict((letter,data.count(letter)) for letter in set(data))
        input_data = set(data.strip().split())
        if "P" in input_data and "S" in input_data and "R" in input_data:
            print("NO WINNER")
        elif "P" in input_data and "S" in input_data and "R" not in input_data:
            if (dic["S"] != 1):
                print("NO WINNER")
            else:
                print("SCISSORS")
        elif "P" in input_data and "S" not in input_data and "R"  in input_data:
            if (dic["P"] != 1):
                print("NO WINNER")
            else:
                print("PAPER")
        elif "P" not in input_data and "S"  in input_data and "R"  in input_data:
            if (dic["R"] != 1):
                print("NO WINNER")
            else:
                print("ROCK")
        else:
            print("NO WINNER")