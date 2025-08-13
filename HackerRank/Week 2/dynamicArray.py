def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    result = []

    for query in queries:
        t, x, y = query
        idx = (x ^ lastAnswer) % n

        if t == 1:
            arr[idx].append(y)
        elif t == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]
            result.append(lastAnswer)

    return result


if __name__ == '__main__':
    n, q = map(int, input().split())
    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().split())))

    answers = dynamicArray(n, queries)

    for answer in answers:
        print(answer)
