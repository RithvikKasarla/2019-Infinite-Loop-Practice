from math import sqrt

with open("Prob11.in.txt") as input_file:
    for line in input_file.readlines()[1:]:
        Cr, Cg, Cb, tolerance, Fr, Fg, Fb, Br, Bg, Bb = map(int, line.strip().split())
        print(Br, Bg, Bb) if sqrt((Fr - Cr)**2 + (Fg - Cg)**2 + (Fb - Cb)**2) <= tolerance else print(Fr, Fg, Fb)
