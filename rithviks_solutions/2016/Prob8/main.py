def time(dist, rate):
    dist = float(dist) * 1000000
    rate = float(rate)
    hours = dist / rate
    days = int(hours/24)
    hours = hours - 24 * days
    minu = hours % 1
    minu = minu *  60
    sec = minu % 1
    minu = int(minu - sec)
    sec = sec * 60
    if round(sec) == 60:
        sec = 0
        minu += 1
    return [days, hours, round(minu), round(sec)]


with open("input.txt") as f:
    lines = f.readlines()[1:]
    for line in lines:
        l = line.split(" ")
        times = time(l[0],l[1])
        print("Time to Mars: %s days, %d hours, %d minutes, %d seconds"%(times[0],times[1],times[2],times[3]))
        