test_cases = int(input())

for _ in range(test_cases):
    a, b = map(int, input().split())
    print(a + b if a != b else (a + b) * 2)
