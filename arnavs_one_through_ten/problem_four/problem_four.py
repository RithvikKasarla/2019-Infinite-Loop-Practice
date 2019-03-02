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
        moves = line.strip().split()

        output = ""
        while len(moves) != 1:
            if len(set(moves)) == 3:
                output = "NO WINNER"
                break
            for i in range(0, len(moves) - 1):
                if moves[i] == moves[i + 1]:
                    if len(moves) == 2:
                        output = "NO WINNER"
                    else:
                        del moves[i]
                elif beats[moves[i]] == moves[i + 1]:
                    del moves[i + 1]
                elif beats[moves[i + 1]] == moves[i]:
                    del moves[i]
                break
            if len(output) > 0:
                break

        if len(output) == 0:
            print(letter_to_name[moves[0]])
        else:
            print(output)
