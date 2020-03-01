test_cases = int(input())

for _ in range(test_cases):
    num_bits = int(input())

    for i in range(2 ** num_bits):
        print(f"{bin(i)[2:]:0>{num_bits}}")
