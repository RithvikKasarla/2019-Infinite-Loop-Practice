def remove_letter_at_index(line: str):
    word, index = line.split()

    return f"{word[:int(index)]}{word[int(index) + 1:]}"

with open("Prob02.in.txt") as input_file:
    for line in input_file.readlines()[1:]:
        print(remove_letter_at_index(line.strip()))
