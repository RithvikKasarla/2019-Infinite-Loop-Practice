def pass_or_fail(grade: int) -> bool:
    return "PASS" if int(grade) >= 70 else "FAIL"

with open("Prob01.in.txt") as input_file:
    for line in input_file.readlines()[1:]:
        print(pass_or_fail(int(line)))
