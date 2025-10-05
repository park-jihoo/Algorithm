class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights[0]), len(heights)
        pacific, atlantic = set(), set()

        def bfs(i, j, visited):
            q = deque([])
            q.append((i, j))
            visited.add((i, j))
            while q:
                x, y = q.popleft()
                for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                    if (
                        0 <= x + dx < n
                        and 0 <= y + dy < m
                        and (x + dx, y + dy) not in visited
                        and heights[x][y] <= heights[x + dx][y + dy]
                    ):
                        visited.add((x + dx, y + dy))
                        q.append((x + dx, y + dy))

        for i in range(n):
            bfs(i, 0, pacific)
        for i in range(m):
            bfs(0, i, pacific)
        for i in range(n):
            bfs(i, m - 1, atlantic)
        for i in range(m):
            bfs(n - 1, i, atlantic)
        return list(map(list, atlantic & pacific))
