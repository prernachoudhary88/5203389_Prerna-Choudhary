def legoBlocks(n, m):
    MOD = 10**9 + 7

    a = [0] * (m + 1)
    a[0] = 1  
    for i in range(1, m + 1):
        for b in range(1, 5):  
            if i - b >= 0:
               a[i] = (a[i] + a[i - b]) % MOD

    t = [pow(a[i], n, MOD) for i in range(m + 1)]

    s = [0] * (m + 1)
    s[0] = 1  

    for i in range(1, m + 1):
        s[i] = t[i]
        for j in range(1, i):
            s[i] = (s[i] - s[j] * t[i - j]) % MOD

    return s[m]
