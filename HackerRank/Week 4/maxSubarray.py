def maxSubarray(arr):
    
    curr = a = arr[0]
    for n in arr[1:]:
        curr = max(n, curr + n)
        a = max(a, curr)
    
    seq = sum(x for x in arr if x > 0) or max(arr)
    
    return [a, seq]
