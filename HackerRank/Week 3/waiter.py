def waiter(n):
    root = int(n**(0.5))
    s = list(range(n+1))
    s[1] = 0
    
    for i in range(2, root+1):
        if s[i] != 0:
            m = n//i - i
            s[i*i: n+1:i] = [0] * (m+1)
    
    return [x for x in s if x !=0]
