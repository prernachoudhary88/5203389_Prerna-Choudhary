def cookies(k, A):
    heapq.heapify(A)  
    o = 0

    while len(A) >= 2 and A[0] < k:
        least = heapq.heappop(A)
        s = heapq.heappop(A)
        n = least + 2 * s
        heapq.heappush(A, n)
        o += 1

    if A and A[0] >= k:
        return o
    else:
        return -1
