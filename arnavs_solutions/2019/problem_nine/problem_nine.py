test_cases = int(input())

for _ in range(test_cases):
    string = input()

    found_digit = False
    current_num = ""
    hours = 0
    minutes = 0
    seconds = 0

    for i, character in enumerate(string):
        if found_digit:
            if character.isdigit():
                current_num += character
            else:
                if character == "h":
                    hours = int(current_num)
                elif character == "m":
                    minutes = int(current_num)
                elif character == "s":
                    seconds = int(current_num)
                found_digit = False
                current_num = ""

        elif character.isdigit():
            current_num += character
            found_digit = True

    print(f"{hours:0>2}:{minutes:0>2}:{seconds:0>2}")
