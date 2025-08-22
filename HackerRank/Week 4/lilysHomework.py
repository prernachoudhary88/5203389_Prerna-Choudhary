
def lilysHomework(arr):
    def count(arr):
        s = 0
        n = len(arr)
        v = [False] * n
        pos = list(enumerate(arr))
        pos.sort(key=lambda x: x[1])

        for i in range(n):
            if v[i] or pos[i][0] == i:
                continue

            c = 0
            j = i
            while not v[j]:
                v[j] = True
                j = pos[j][0]
                c += 1

            if c > 0:
                s += (c - 1)

        return s

    asc = count(arr[:])
    desc = count(arr[::-1])
    return min(asc, desc)
