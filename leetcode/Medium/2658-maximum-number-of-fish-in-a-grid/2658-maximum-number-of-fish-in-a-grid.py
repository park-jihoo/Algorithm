class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n, ans = len(grid[0]), len(grid), 0
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[grid[i][j] == 0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    q = deque([(i, j)])
                    visited[i][j] = True
                    a = grid[i][j]
                    while q:
                        x, y = q.pop()
                        for dx, dy in d:
                            if (
                                0 <= x + dx < n
                                and 0 <= y + dy < m
                                and not visited[x + dx][y + dy]
                            ):
                                visited[x + dx][y + dy] = True
                                a += grid[x + dx][y + dy]
                                q.append((x + dx, y + dy))
                    ans = max(ans, a)
        return ans
