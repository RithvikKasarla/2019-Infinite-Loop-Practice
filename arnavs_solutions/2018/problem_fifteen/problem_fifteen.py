with open("Prob15.in.txt") as input_file:
    for line in input_file.readlines()[1:]:
        res = ""
        for letter in line.strip():
            t = ord(letter) - 64
            if letter in "ABCDE":
                calculation = t + 6
            elif letter in "FGHIJ":
                calculation = t ** 2
            elif letter in "KLMNO":
                calculation = t % 3 * 5 + 1
            elif letter in "PQRST":
                calculation = sum(map(int, str(t))) * 8
            elif letter in "UVWXYZ":
                r = 1
                for i in range(2, t):
                    if t % i == 0:
                        r = i
                calculation = r * 2

            calculation %= 26
            res += letter if calculation == 0 else chr(calculation + 64)
        print(res)
