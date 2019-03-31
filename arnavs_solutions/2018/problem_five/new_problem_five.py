def collatz_conjecture(num: int):
    num_copy = num
    ct = 0
    while num != 1:
        num = num / 2 if num % 2 == 0 else num * 3 + 1
        ct += 1

    return f"{num_copy}:{ct + 1}"


with open("Prob05.in.txt") as input_file:
    for line in [line.strip() for line in input_file.readlines()[1:]]:
        print(collatz_conjecture(int(line)))
