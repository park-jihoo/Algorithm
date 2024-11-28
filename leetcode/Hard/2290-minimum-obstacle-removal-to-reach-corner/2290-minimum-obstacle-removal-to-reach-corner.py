class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)
        queue = deque([(0, 0, 0)])
        d = [[float("inf")] * m for _ in range(n)]
        d[0][0] = 0
        while queue:
            brk, x, y = queue.popleft()
            if d[x][y] < brk:
                continue
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] == 1:
                        if d[nx][ny] > brk + 1:
                            d[nx][ny] = brk + 1
                            queue.append([brk + 1, nx, ny])
                    elif d[nx][ny] > brk:
                        d[nx][ny] = brk
                        queue.appendleft([brk, nx, ny])
        return d[-1][-1]
