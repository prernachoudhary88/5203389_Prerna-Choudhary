def tower_breakers(n, m):
    if m == 1:
        return 2
    elif n % 2 == 0:
        return 2
    else:
        return 1

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(tower_breakers(n, m))
