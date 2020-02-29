test_cases = int(input())

for _ in range(test_cases):
    a, b = input().split(" ")
    print("false" if a != b else "true")
