from collections import Counter

def slugging_percentage(line: str):
    player_name, at_bats = line.split(":")
    at_bats = at_bats.split(",")

    result = f"{player_name}="

    num_at_bats = 0
    
    counted_at_bats = Counter(at_bats)
    num_at_bats = sum(counted_at_bats.values()) - counted_at_bats["BB"]
    numerator = counted_at_bats["1B"] + 2 * counted_at_bats["2B"] + 3 * counted_at_bats["3B"] + 4 * counted_at_bats["HR"]

    if num_at_bats == 0:
        return f"{result}0.000"
    
    return f"{result}{round(numerator / num_at_bats, 3):.3f}"

with open("Prob07.in.txt") as input_file:
    for line in input_file.readlines()[1:]:
        print(slugging_percentage(line.strip()))