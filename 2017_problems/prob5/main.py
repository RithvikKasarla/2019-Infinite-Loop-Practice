def run(a, b):
    a = a.split(",")
    b = b.split(",")
    out1 = []
    out2 = []
    out3 = []
    for i in a:
        if i not in b:
            out1.append(i)
    for i in a:
        if i in b:
            out2.append(i)
    for i in b:
        if i not in a:
            out3.append(i)
    return (",".join(sorted(out1)), ",".join(sorted(out2)), ",".join(sorted(out3)))

if __name__ == '__main__':
    print(run("Bob,Joe,Steve,Mary,Ann", "Bob,Steve,Ann,Paula,Chris"))