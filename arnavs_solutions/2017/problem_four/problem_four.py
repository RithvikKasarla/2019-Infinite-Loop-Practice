import os


def fibonacci(n: int):
    previous = 0
    current = 1

    for i in range(n - 2):
        previous, current = current, previous + current

    return current


with open(os.path.join(os.path.dirname(__file__), "Prob04.in.txt")) as input_file:
    for num in input_file.read().splitlines()[1:]:
        print(f"{num} = {fibonacci(int(num))}")
