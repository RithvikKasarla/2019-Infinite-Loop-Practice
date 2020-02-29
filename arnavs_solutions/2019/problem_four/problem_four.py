with open("Prob04.txt") as input_file:
    lines = input_file.read().splitlines()

    for line in lines[1:]:
        speed, birthday = line.split(" ")

        speed = int(speed)
        if birthday == "true":
            speed -= 5

        if speed <= 60:
            print("no ticket")
        elif 60 < speed <= 80:
            print("small ticket")
        else:
            print("big ticket")
