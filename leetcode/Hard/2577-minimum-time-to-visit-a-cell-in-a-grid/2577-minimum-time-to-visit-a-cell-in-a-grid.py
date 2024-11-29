class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        while q:
            time, x, y = heapq.heappop(q)
            if x == m - 1 and y == n - 1:
                return time
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    if grid[nx][ny] <= time + 1:
                        heapq.heappush(q, [time + 1, nx, ny])
                    else:
                        if (grid[nx][ny] - time) % 2 == 0:
                            heapq.heappush(q, [grid[nx][ny] + 1, nx, ny])
                        else:
                            heapq.heappush(q, [grid[nx][ny], nx, ny])
        return -1