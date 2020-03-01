test_cases = int(input())

for _ in range(test_cases):
    small, large, target = map(int, input().split())

    while target > 4 and large > 0:
        target -= 5
        large -= 1

    if small >= target:
        print("true")
    else:
        print("false")
