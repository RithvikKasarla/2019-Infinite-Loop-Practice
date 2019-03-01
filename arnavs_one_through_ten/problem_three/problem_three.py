with open("Prob03.in.txt") as input_file:
    for line in input_file.readlines()[1:]:
        num, suffix = line.strip()[:-2], "th"
        if num[-1] == "1" and num != "11":
            suffix = "st"
        elif num[-1] == "2" and num != "12":
            suffix = "nd"
        elif num[-1] == "3" and num != "13":
            suffix = "rd"
        print(num + suffix)
