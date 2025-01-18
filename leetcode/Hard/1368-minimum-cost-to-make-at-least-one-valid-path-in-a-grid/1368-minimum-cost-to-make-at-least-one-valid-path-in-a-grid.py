class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        graph = defaultdict(dict)
        m, n = len(grid), len(grid[0])
        q = [(0, 0, 0)]
        costs = [[float("inf")] * n for _ in range(m)]
        costs[0][0] = 0
        while q:
            cost, x, y = heapq.heappop(q)
            if costs[x][y] != cost:
                continue
            for idx, (dx, dy) in enumerate(d):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nc = cost + (idx + 1 != grid[x][y])
                    if costs[nx][ny] > nc:
                        costs[nx][ny] = nc
                        heapq.heappush(q, (nc, nx, ny))
        return costs[m - 1][n - 1]
