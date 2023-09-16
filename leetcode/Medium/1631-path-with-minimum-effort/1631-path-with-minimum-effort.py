from collections import deque


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        def bfs(heights, a):
            visited = [[False] * len(heights[0]) for _ in range(len(heights))]
            q = deque([(0, 0)])
            while q:
                x, y = q.popleft()
                if (x, y) == (len(heights) - 1, len(heights[0]) - 1):
                    return True
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if not (
                        0 <= nx < len(heights)
                        and 0 <= ny < len(heights[0])
                        and abs(heights[nx][ny] - heights[x][y]) <= a
                        and not visited[nx][ny]
                    ):
                        continue
                    visited[nx][ny] = True
                    q.append((nx, ny))
            return False

        left, right = 0, int(1e9)
        while left <= right:
            mid = (left + right) // 2
            if bfs(heights, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
