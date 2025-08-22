def roadsAndLibraries(n, lib, road, c):
    if road >= lib:
        return n * lib

    from collections import defaultdict, deque

    g = defaultdict(list)
    for u, v in c:
        g[u].append(v)
        g[v].append(u)

    visited = [False] * (n + 1)
    total_cost = 0

    def bfs(start):
        q = deque([start])
        visited[start] = True
        count = 1
        while q:
            node = q.popleft()
            for neighbor in g[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
                    count += 1
        return count

    for city in range(1, n + 1):
        if not visited[city]:
            component_size = bfs(city)
            
            total_cost += lib + (component_size - 1) * road

    return total_cost

