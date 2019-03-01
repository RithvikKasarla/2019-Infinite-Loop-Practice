# TODO: Fix (this fails on third from last test case)

beats = {
    "R": "S",
    "S": "P",
    "P": "R"
}

letter_to_name = {
    "R": "ROCK",
    "P": "PAPER",
    "S": "SCISSORS"
}

with open("Prob04.in.txt") as input_file:
    lines = input_file.readlines()[1:]

    for line in lines:
        moves = list({*line.strip().split()})

        print(moves, end=' ')

        if len(moves) == 1:
            print("NO WINNER")
        if len(moves) == 2:
            if moves[0] == moves[1]:
                print("NO WINNER")
            else:
                if beats[moves[0]] == moves[1]:
                    print(letter_to_name[moves[0]])
                else:
                    print(letter_to_name[moves[1]])
        if len(moves) == 3:
            print("NO WINNER")