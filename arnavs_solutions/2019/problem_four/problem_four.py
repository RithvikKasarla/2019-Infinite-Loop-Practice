test_cases = int(input())

for _ in range(test_cases):
    speed, birthday = input().split(" ")

    speed = int(speed)
    if birthday == "true":
        speed -= 5

    if speed <= 60:
        print("no ticket")
    elif 60 < speed <= 80:
        print("small ticket")
    else:
        print("big ticket")
