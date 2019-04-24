def AEIOU(quote):
    count = 0
    vowels = ["a","e","i","o","u"]
    ar = list(quote.strip())
    for x in ar:
        if x in vowels:
            count += 1
    print(count)


with open('input_two.txt') as f:
    for line in f.readlines()[1::]:
        print(line.strip(),AEIOU(line.strip()))
