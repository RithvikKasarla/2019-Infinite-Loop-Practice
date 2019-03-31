def count_vowels(line: str) -> int:
    return len(list(filter(lambda c: c in ['a', 'e', 'i', 'o', 'u'], line.strip())))

with open("Prob02.in.txt") as input_file:
    for line in input_file.readlines()[1:]:
        print(count_vowels(line))
