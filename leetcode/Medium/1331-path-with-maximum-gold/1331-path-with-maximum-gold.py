class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r == m or c < 0 or c == n or grid[r][c] == 0:
                return 0
            ans = 0
            org = grid[r][c]
            grid[r][c] = 0
            for dr, dc in d:
                ans = max(ans, dfs(r + dr, c + dc))
            grid[r][c] = org
            return ans + grid[r][c]

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans
