class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row, col = defaultdict(list), defaultdict(list)
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row[i].append(j)
                    col[j].append(i)
        ans = 0
        for i in range(m):
            if len(row[i]) == 1 and len(col[row[i][0]]) == 1:
                continue
            ans += len(row[i])
        return ans