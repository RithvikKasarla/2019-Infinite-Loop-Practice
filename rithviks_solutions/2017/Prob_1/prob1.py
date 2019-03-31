def echo(line):
    print(line + line)

with open('Prob1.txt') as f:
    lines = f.readlines()[::1]
    for line in lines:
        echo(line.strip())