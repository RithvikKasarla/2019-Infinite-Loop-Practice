def winner(dic):
    Rock = data.count("R")
    Paper = data.count("P")
    Scissors = data.count("S")
    dic = {"R":Rock,"P":Paper,"S":Scissors}
    if dic["R"] == 1 and dic["P"] == 0:
        return "ROCK"
    elif dic["P"] == 1 and dic["S"] == 0:
        return "PAPER"
    elif dic["S"] == 1 and dic["R"] == 0:
        return "SCISSORS"
    return "NO WINNER"

with open("ProbInput.txt") as input_file:
    lines = input_file.readlines()[1:]
    
    for line in lines:
        line=line.strip()
        data = line
        print(winner(data))