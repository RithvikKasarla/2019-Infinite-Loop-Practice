led_states = {
    0: "off",
    1: "red",
    2: "green",
    3: "blue"
}

with open("Prob06.in.txt") as input_file:
    for line in input_file.readlines()[1:]:
        total = sum((v if s == "BROKEN" else 0 for (s, v) in zip(line.strip().split(), [1, 2, 4, 8])))
        print("{} {}".format(led_states[(total - total % 4) / 4], led_states[total % 4]))
