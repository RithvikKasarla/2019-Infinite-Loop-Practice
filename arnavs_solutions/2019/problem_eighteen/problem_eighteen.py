from math import sqrt

# def mandlebrot_impl(previous_value, c):

def absolute_complex(a, b):
    return sqrt(a**2 + b**2)

def mandlebrot(a, b):
    c = (a, b)
    n = 1
    z_n = c # Z_1 = c_1
    z_n_mag = absolute_complex(a, b)
    while z_n_mag < 100 and n < 52:
        n += 1
        z_n = (z_n[0]**2 - z_n[1]**2 + c[0], 2 * z_n[0] * z_n[1] + c[1])
        z_n_mag = absolute_complex(*z_n)

    return n


def main():
    test_cases = int(input())

    for _ in range(test_cases):
        a, b = input().split()
        result = mandlebrot(float(a), float(b))

        if result <= 10:
            print(f"{a}+{b}i RED")
        elif 11 <= result <= 20:
            print(f"{a}+{b}i ORANGE")
        elif 21 <= result <= 30:
            print(f"{a}+{b}i YELLOW")
        elif 31 <=result <= 40:
            print(f"{a}+{b}i GREEN")
        elif 41 <=result <= 50:
            print(f"{a}+{b}i BLUE")
        else:
            print(f"{a}+{b}i BLACK")

if __name__ == "__main__":
    main()
