import string
with open("input.txt") as inputFile:
    cases = int(inputFile.readline().replace("\n", ""))
    letters = "0" + string.ascii_uppercase
    a = ""
    for caseNum in range(cases):
        plaintext = inputFile.readline().replace("\n", "")
        for i in range(len(plaintext)):
            original = plaintext[i]
            value = letters.index(original)
            if value <= 5:
                value = value + 6
            elif value <= 10:
                value = value ** 2
            elif value <= 15:
                value = ((value % 3) * 5) + 1
            elif value <= 20:
                value = ((value // 10) + (value % 10)) * 8
            else:
                factor = 1
                for i in range(value // 2, 1, -1):
                    if value % i == 0:
                        factor = i
                        break
                value = factor * 2
            while value > 26:
                value = value - 26
            # Convert back
            newLetter = letters[value]
            if newLetter == '0':
                newLetter = original
            a += newLetter
        a+="\n"
    print(a)