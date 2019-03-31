# MUST BE RUN WITH > PYTHON 3.6 TO PRESERVE DICTIONARY ORDERING

with open("Prob13.in.txt") as input_file:
    lines = [line.strip() for line in input_file.readlines()[1:]]
    idx = 0

    while idx < len(lines):
        data = list(
            zip(
                *map(
                    lambda l: l[1:][:-1].split(","),
                    lines[idx + 1][1:][:-1].replace("],[", "]#[").split("#"),
                )
            )
        )
        idx += 2 + len(data)

        people_data = []
        for i, person in enumerate(data):
            people_data.append({})
            for info in zip(
                ["Name", "Age", "Instagram", "Twitter", "Phone", "Email"], person
            ):
                people_data[i][info[0]] = info[1]

        for key in sorted(people_data, key=lambda k: k["Name"]):
            for key2, value in key.items():
                print("{}: {}".format(key2, value))
