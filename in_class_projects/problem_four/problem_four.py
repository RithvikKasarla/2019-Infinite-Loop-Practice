beats = {
    "P": "R",
    "R": "S",
    "S": "P"
}

with open("Prob04.in.txt") as input_file:
    lines = input_file.readlines()[1:]
    
    for line in lines:
        input_data = line.strip().split()
        
        previous_move = input_data[0]
        winner = None
        for move in input_data[1:]:
            if beats[previous_move] == move:
                print("{} beat {}".format(previous_move, move))
                winner = previous_move
                print(winner)
            elif beats[move] == previous_move:
                winner = move
            previous_move = move
        
        if winner == None:
            print("NO WINNER")
        elif winner == "P":
            print("PAPER")
        elif winner == "R":
            print("ROCK")
        else:
            print("SCISSORS")