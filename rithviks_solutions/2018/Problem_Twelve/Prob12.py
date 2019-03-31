with open("input.txt") as inputFile:
    lines = int(inputFile.readline().replace("\n", ""))
    for x in range(lines):
        lim = int(inputFile.readline().replace("\n", "")) + 1
        ppri = [True for x in range(lim)]
        primes = []
        for i in range(2, lim):
            if ppri[i]:
                primes.append(i)
                elim = 0
                for j in range(i * 2, lim, i):
                    if ppri[j]:
                        ppri[j] = False
                        elim += 1
                if elim >= 1:
                    print "Prime" , str(i) , "Composite Set Size:" , str(elim)
        a = "{"
        for prime in primes:
            a+= str(prime)
            a+= ","
        a = a [:-1]
        a+= "}"
        print a