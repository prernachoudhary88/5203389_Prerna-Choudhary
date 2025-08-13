def maxMin(k, arr):
    arr.sort()
    min_unfairness = float('inf')

    for i in range(len(arr) - k + 1):
        unfairness = arr[i + k - 1] - arr[i]
        min_unfairness = min(min_unfairness, unfairness)

    return min_unfairness

if __name__ == '__main__':
    n = int(input())  
    k = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))

    result = maxMin(k, arr)
    print(result)
