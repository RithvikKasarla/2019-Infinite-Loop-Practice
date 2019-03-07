from math import sqrt

with open("Prob11.in.txt") as input_file:
    lines = input_file.readlines()[1:]

    for line in lines:
        Cr, Cg, Cb, tolerance, Fr, Fg, Fb, Br, Bg, Bb = map(int, line.strip().split())

        distance_background = sqrt((Br - Cr)**2 + (Bg - Cg)**2 + (Bb - Cb)**2)
        distance_foreground = sqrt((Fr - Cr)**2 + (Fg - Cg)**2 + (Fb - Cb)**2)

        if distance_foreground <= tolerance:
            print(Br, Bg, Bb)
        else:
            print(Fr, Fg, Fb)
