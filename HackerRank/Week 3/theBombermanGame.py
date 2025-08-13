def bomberMan(n, grid):
    if n == 1:
        return grid
    
    R, C = len(grid), len(grid[0])
    
    def full_bombs():
        return ['O' * C for _ in range(R)]
    
    def explode(grid):
        exploded = [['O'] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 'O':
                    exploded[r][c] = '.'
                    for nr, nc in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
                        if 0 <= nr < R and 0 <= nc < C:
                            exploded[nr][nc] = '.'
        return [''.join(row) for row in exploded]
    
    if n % 2 == 0:
        return full_bombs()
    
    grid_3 = explode(grid)    
    grid_5 = explode(grid_3)
    
    if n % 4 == 3:
        return grid_3
    else:  
        return grid_5

initial_grid = [
    "...",
    ".O.",
    "..."
]

print("\n".join(bomberMan(3, initial_grid)))

