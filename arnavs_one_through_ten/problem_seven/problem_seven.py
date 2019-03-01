def palindrome(a):
    return a == a[::-1]


with open("Prob07.in.txt") as input_file:
    lines = [line.strip() for line in input_file.readlines()]
    total_count = int(lines[0])
    lines = lines[1:]

    i, j = 0, 0
    while j != 2:
        sub_count = int(lines[i])

        palindromes = []
        for k in range(i, i + sub_count + 1):
            if not palindrome(lines[k].lower()):
                palindromes.append(k - i)

        print("False - {}".format(", ".join(map(str, palindromes))) if palindromes else "True")

        i += sub_count + 1
        j += 1
