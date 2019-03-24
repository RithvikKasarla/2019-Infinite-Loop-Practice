def echo(line):
    print(line * 2)
with open('Prob1.in.txt') as f:
    lines = f.readlines()[::1]
    for line in lines:
        echo(line.strip())
        