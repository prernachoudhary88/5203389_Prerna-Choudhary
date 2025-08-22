def hackerlandRadioTransmitters(x, k):
    x.sort()
    n = len(x)
    i = 0
    t = 0

    while i < n:
        t += 1

        loc = x[i] + k
        while i < n and x[i] <= loc:
            i += 1

        i -= 1
        loc = x[i] + k

        while i < n and x[i] <= loc:
            i += 1

    return t
