

def pass_fail(x):
    if x >= 70:
        return "PASS"
    return "FAIL"


with open('input_one.txt') as f:
    for line in f.readlines()[1::]:
        print(line.strip(), pass_fail(int(line.strip())))
