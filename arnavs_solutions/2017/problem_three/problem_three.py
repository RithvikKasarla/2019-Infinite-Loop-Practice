def addiply(line: str):
    nums = list(map(int, line.split()))

    return f"{nums[0] + nums[1]} {nums[0] * nums[1]}"

with open("Prob03.in.txt") as input_file:
    for line in input_file.readlines()[1:]:
        print(addiply(line.strip()))
