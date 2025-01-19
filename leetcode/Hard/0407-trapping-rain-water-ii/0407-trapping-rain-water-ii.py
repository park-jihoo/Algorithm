class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        min_heap = []

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        trapped = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while min_heap:
            height, x, y = heapq.heappop(min_heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    trapped += max(0, height - heightMap[nx][ny])
                    heapq.heappush(min_heap, (max(height, heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True

        return trapped
