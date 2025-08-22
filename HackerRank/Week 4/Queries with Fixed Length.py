
def solve(arr, qu):
    def subarrays(k):
        m = []
        dq = deque()
        
        for i in range(len(arr)):
            
            while dq and dq[0] <= i - k:
                dq.popleft()
           
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            dq.append(i)
            
            if i >= k - 1:
                m.append(arr[dq[0]])
        
        return min(m)
    
    return [subarrays(q) for q in qu]
