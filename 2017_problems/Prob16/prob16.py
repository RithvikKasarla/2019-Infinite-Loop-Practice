import itertools as it


def dele(inp,ops, out):
    x = it.permutations(inp)
    print(x)
    for x in range(len(inp)):
        c = {"*":out/int(inp[x]), "/":out*int(inp[x]), "-":out+int(inp[x]), "-":out+int(inp[x]) } [ops]

dele([1,2,3],["*","/"],1)