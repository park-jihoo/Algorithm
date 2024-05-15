class Solution:
    def isValid(self, grid, value):
        n = len(grid)
        if grid[0][0] < value:
            return False
        d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set([(0, 0)])
        q = deque([(0, 0)])

        while q:
            x, y = q.popleft()
            if x == n-1 and y == n-1:
                return True
            for dx, dy in d:
                nx , ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<n and (nx, ny) not in visited and grid[nx][ny] >= value:
                    q.append((nx, ny))
                    visited.add((nx, ny))
        return False

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0

        # Multi-source BFS to compute distance from any thief
        thieves = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
        distance = [[float('inf')] * n for _ in range(n)]
        queue = deque(thieves)
        
        for x, y in thieves:
            distance[x][y] = 0

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and distance[nx][ny] == float('inf'):
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))

        # Binary search for the maximum safeness factor
        left, right = 0, max(max(row) for row in distance)
        while left < right:
            mid = (left + right + 1) // 2
            if self.isValid(distance, mid):
                left = mid
            else:
                right = mid - 1

        return left