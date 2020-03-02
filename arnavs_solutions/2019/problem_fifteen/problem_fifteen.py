def numeric_value(string: str) -> int:
    total = 0
    for char in string:
        total += ord(char) - 96  # Gets alphabetical positioon from ascii code

    return total


def main():
    test_cases = int(input())

    for _ in range(test_cases):
        data_values = input().split()
        timestamps = list(map(int, input().split()))

        current_hash = 0
        for i in range(1, 11):
            current_hash = (
                (
                    timestamps[i - 1]
                    + numeric_value(data_values[i - 1])
                    + i
                    + current_hash  # Using previous value
                )
                * 50
                / 147
            )

        print(round(current_hash))


if __name__ == "__main__":
    main()
