def minimumBribes(q):
    bribes = 0
    for i in range(len(q)):
        
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        
        for j in range(max(q[i] - 2, 0), i):
            if q[j] > q[i]:
                bribes += 1
    
    print(bribes)
