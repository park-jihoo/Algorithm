class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        EMPTY, WALL, GUARD, GUARDED = 0, -1, -2, -3
        grid = [[EMPTY]*n for _ in range(m)]
        
        for row, col in walls:
            grid[row][col] = WALL
        for row, col in guards:
            grid[row][col] = GUARD
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for row, col in guards:
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while 0 <= r < m and 0 <= c < n and grid[r][c] not in (WALL, GUARD):
                    if grid[r][c] == EMPTY:
                        grid[r][c] = GUARDED
                    r += dr
                    c += dc
        
        return sum(cell == EMPTY for row in grid for cell in row)