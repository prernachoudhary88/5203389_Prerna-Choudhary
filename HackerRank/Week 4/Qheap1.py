def process(q):
    m = []
    e = set()
    o = []

    for q in q:
        if q[0] == 1:
            v = q[1]
            heapq.heappush(m, v)
            e.add(v)
        elif q[0] == 2:
            v = q[1]
            e.discard(v)  
        elif q[0] == 3:
            
            while m[0] not in e:
                heapq.heappop(m)
            o.append(m[0])
    
    return o
