def time_mars(ipt):
    ipt = ipt.split(" ")
    distance = float(ipt[0]) * 1000000
    rate = float(ipt[1])
    seconds = distance / rate
    seconds *= 3600
    seconds = round(seconds)
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minutes = minutes % 60
    days = hours // 24
    hours = hours % 24
    
    days = int(days)
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    
    return "Time to Mars: {0} days, {1} hours, {2} minutes, {3} seconds".format(days, hours, minutes, seconds)

if __name__ == "__main__":
    print(time_mars("34.8 36000"))