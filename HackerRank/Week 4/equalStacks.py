def equalStacks(h1, h2, h3):
    def d(stack):
        h = []
        total = 0
        for height in reversed(stack):  
            total += height
            h.append(total)
        return set(h)  

    a = d(h1)
    b = d(h2)
    c = d(h3)

    e = a & b & c

    return max(e) if e else 0
