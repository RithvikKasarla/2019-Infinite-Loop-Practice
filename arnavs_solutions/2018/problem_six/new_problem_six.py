LED_STATES = {0: "off", 1: "red", 2: "green", 3: "blue"}


def determine_led_states(line: str) -> str:
    total = sum(
        (
            v if s == "BROKEN" else 0
            for (s, v) in zip(line.strip().split(), [1, 2, 4, 8])
        )
    )
    return f"{LED_STATES[(total - total % 4) / 4]} {LED_STATES[total % 4]}"


with open("Prob06.in.txt") as input_file:
    for line in input_file.readlines()[1:]:
        print(determine_led_states(line))
