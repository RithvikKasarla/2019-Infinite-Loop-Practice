def time_to_mars(line: str):
    distance, rate = map(float, line.split())

    time = distance * 1_000_000 / rate
    days = time // 24
    time -= 24 * days
    hours = int(time)
    time -= hours
    minutes = 0
    seconds = 0

    time = round(time, 2)
    if int(time * 60) != round(time * 60):
        print(time)
        minutes = int(time * 60)
        time -= minutes
        print(time)
        seconds = time * 60
    else:
        minutes = time * 60

    return f"Time to Mars: {int(round(days))} days, {int(round(hours))} hours, {int(round(minutes))} minutes, {int(round(seconds))} seconds"


with open("Prob08.in.txt") as input_file:
    for line in input_file.readlines()[1:]:
        print(time_to_mars(line))
