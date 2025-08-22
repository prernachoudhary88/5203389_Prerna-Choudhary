def highestValuePalindrome(s, n, k):
    s = list(s)
    changes = [0] * n

    l = 0
    r = n - 1
    while l < r:
        if s[l] != s[r]:
            higher = max(s[l], s[r])
            s[l] = s[r] = higher
            changes[l] = changes[r] = 1
            k -= 1
        l += 1
        r -= 1

    if k < 0:
        return '-1'  
        
    l = 0
    r = n - 1
    while l <= r:
        if l == r:
            if k > 0 and s[l] != '9':
                s[l] = '9'
                k -= 1
        else:
            if s[l] != '9':
                
                if changes[l] or changes[r]:
                    if k >= 1:
                        s[l] = s[r] = '9'
                        k -= 1
                        
                elif k >= 2:
                    s[l] = s[r] = '9'
                    k -= 2
        l += 1
        r -= 1

    return ''.join(s)
