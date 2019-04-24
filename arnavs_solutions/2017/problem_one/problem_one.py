def echo_twice(line: str):
    return f"{line}\n{line}"


with open("Prob01.in.txt") as input_file:
    for line in input_file.readlines()[1:]:
        print(echo_twice(line.strip()))
