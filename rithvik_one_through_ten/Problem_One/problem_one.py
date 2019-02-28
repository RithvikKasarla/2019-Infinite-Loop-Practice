

def Pass_Fail(x):
    if x >= 70:
        return "PASS"
    return "FAIL"

with open('input_one.txt') as f:
    for line in f.readlines()[1::]:
        print(Pass_Fail(int(line.strip())))
