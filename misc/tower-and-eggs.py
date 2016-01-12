N = 100  # floors

step = 2  # start: first egg step between drops
min_drops = N  # min drops for two eggs

while True:
    drops = 0  # drops for current step
    n = 0  # current floor

    # calculate drops for current N
    while True:
        n += step
        if n > N:  # over floors
            n -= step  # correct for debug
            break
        drops += 1

    # second egg drops first egg step minus one drop
    # additionaly we can skip last drop of second egg
    drops += step - 1 - 1

    print drops, step

    # next drops will increase
    # graph will like this:
    # \       /
    #  \     /
    #    -.-
    # step: 0 -> N
    if drops > min_drops:
        break

    min_drops = min(drops, min_drops)  # collect min drops between attempts

    step += 1  # increase first egg step one by one for each attempt

    if step >= N:  # overload
        break

print min_drops
