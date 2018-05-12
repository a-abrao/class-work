def computepay(hours,rate):
    if hours <= 40:
        print(hours * rate)
    else:
        if hours > 41:
           print((hours - 40) * 15 + (40 * rate))