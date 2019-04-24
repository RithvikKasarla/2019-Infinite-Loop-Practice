with open("Prob14.in.txt") as input_file:
    lines = [line.strip() for line in input_file.readlines()[1:]]

    data = "".join(lines[4:])

    data = [
        (
            [int(l) for l in lines[1].split()],
            "".join(c for c in data if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ-").replace(
                "-", " "
            ),
        ),
        (
            [int(l) for l in lines[3].split()],
            "".join(c for c in data if c in "abcdefghijklmnopqrstuvwxyz=\n").replace(
                "=", " "
            ),
        ),
    ]

    idx = 0
    for length in data[0][0]:
        print(data[0][1][idx : idx + length])
        idx += length
    idx = 0
    print()
    for length in data[1][0]:
        print(data[1][1][idx : idx + length])
        idx += length
