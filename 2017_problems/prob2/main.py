def run(ipt):
    ipt = ipt.split(" ")
    st = list(ipt[0])
    st.pop(int(ipt[1]))
    return "".join(st)


with open("prob2.txt") as input_file:
    for line in input_file.readlines()[1:]:
        print(run(line))