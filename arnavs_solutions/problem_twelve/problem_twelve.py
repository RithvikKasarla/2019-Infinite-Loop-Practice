with open("Prob12.in.txt") as input_file:
    for num in list(map(int, input_file.readlines()[1:])):
        primes = [False, False] + [True] * (num - 1)

        for i, elem in enumerate(primes):
            removed = []
            if not primes[i]:
                continue

            for j in range(i * 2, len(primes), i):
                if primes[j]:
                    removed.append(j)
                primes[j] = False

            if len(removed) > 0:
                 print("Prime {} Composite Set Size: {}".format(i, len(removed)))

        print("{{{}}}".format(",".join(str(i) for i, elem in enumerate(primes) if elem)))
