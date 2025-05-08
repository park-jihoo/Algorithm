class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dist = [[float("inf")] * n for _ in range(m)]
        dist[0][0] = 0
        heap = [(0, 0, 0, 1)]
        visited = set()

        while heap:
            d, x, y, f = heapq.heappop(heap)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if moveTime[nx][ny] > dist[x][y]:
                        dist[nx][ny] = moveTime[nx][ny] + f
                    elif dist[x][y] + f < dist[nx][ny]:
                        dist[nx][ny] = dist[x][y] + f
                    else:
                        continue
                    nf = 1 + f % 2
                    heapq.heappush(heap, (dist[nx][ny], nx, ny, nf))
        return dist[m - 1][n - 1]
