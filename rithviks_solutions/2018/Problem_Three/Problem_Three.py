def suf(x):
    li = list(x)
    nums = ["1","2","3","4","5","6","7","8","9","0"]
    numbers = ""
    for n in li:
        if n in nums:
            numbers+= n

    if int(numbers) > 9 and int(numbers) < 21:
        print(numbers + "th")
    elif int(numbers) % 10 == 1:
        print(numbers + "st")
    elif int(numbers) % 10 == 2:
        print(numbers + "nd")
    elif int(numbers) % 10 == 3:
        print(numbers + "rd")
    else:
        print(numbers + "th")

with open('problem_three.txt') as f:
    for line in f.readlines()[1::]:
        suf(line.strip())
