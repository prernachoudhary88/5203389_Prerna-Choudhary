def arrayManipulation(n, queries):
    arr = [0] * (n + 2)  

    for a, b, k in queries:
        arr[a] += k
        arr[b + 1] -= k

    m = 0
    curr = 0
    for val in arr:
        curr += val
        if curr > m:
            m = curr

    return m
