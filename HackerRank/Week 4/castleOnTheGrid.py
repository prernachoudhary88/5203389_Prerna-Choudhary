def minimumMoves(grid, startX, startY, goalX, goalY):
    n = len(grid)
    v = [[False]*n for _ in range(n)]
    q = deque()
    q.append((startX, startY, 0))  
    v[startX][startY] = True

    while q:
        x, y, m = q.popleft()

        if x == goalX and y == goalY:
            return m

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy

            while 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != 'X':
                if not v[nx][ny]:
                    v[nx][ny] = True
                    q.append((nx, ny, m + 1))
                nx += dx
                ny += dy
