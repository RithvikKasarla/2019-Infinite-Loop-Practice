ICAO_MAPPINGS = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliet",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "Xray",
    "Y": "Yankee",
    "Z": "Zulu",
}


def icao_version(line: str):
    result = []
    for word in line.split():
        new_word = []
        for char in word:
            new_word.append(ICAO_MAPPINGS[char[0].upper()])
        result.append("-".join(new_word))

    return " ".join(result)


with open("Prob06.in.txt") as input_file:
    lines = input_file.readlines()

    num_cases = int(lines[0])

    i = 1
    current = 0
    while current < num_cases:
        num_current = int(lines[i])

        for j in range(i + 1, i + num_current + 1):
            print(icao_version(lines[j]))

        i += i + num_current
        current += 1
