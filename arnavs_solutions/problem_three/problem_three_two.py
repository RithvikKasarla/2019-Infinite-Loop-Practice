def correct_suffixes(inp):
    result = ""

    inp = int(inp[:-2])

    put_negative_sign = inp < 0
    
    inp = abs(inp)

    number_reduced = inp % 100

    if number_reduced % 10 == 1 and (number_reduced < 9 or number_reduced > 13):
        result = f"{inp}st"
    elif number_reduced % 10 == 2 and (number_reduced < 9 or number_reduced > 13):
        result = f"{inp}nd"
    elif number_reduced % 10 == 3 and (number_reduced < 9 or number_reduced > 13):
        result = f"{inp}rd"
    else:
        result = f"{inp}th"

    return f"-{result}" if put_negative_sign else result


with open("Prob03.in.txt") as input_file:
    lines = input_file.readlines()[1:]

    for line in lines:
        print(correct_suffixes(line.strip()))