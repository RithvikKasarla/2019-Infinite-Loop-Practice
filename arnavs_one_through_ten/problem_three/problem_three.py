with open("Prob03.in.txt") as input_file:
    lines = input_file.readlines()[1:]

    for line in lines:
        num = line.strip()[:-2]

        if num[-1] == "1" and num != "11":
            suffix = "st"
        elif num[-1] == "2" and num != "12":
            suffix = "nd"
        elif num[-1] == "3" and num != "13":
            suffix = "rd"
        else:
            suffix = "th"
        print(num + suffix)
