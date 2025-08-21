def icecreamParlor(m, arr):
    p = {}

    for i, price in enumerate(arr):
        comp = m - price
        if comp in p:
           
            return [p[comp] + 1, i + 1]
        p[price] = i
