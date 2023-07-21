from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        d = [(0, 0), (-1, 0), (0, -1), (1, 0), (0, 1)]
        island1 = deque()

        def dfs(x, y):
            for dx, dy in d:
                if 0 <= x + dx < m and 0 <= y + dy < n and grid[x + dx][y + dy] == 1:
                    grid[x + dx][y + dy] = 2
                    island1.append([x + dx, y + dy])
                    dfs(x + dx, y + dy)

        flag = False
        for x in range(m):
            for y in range(n):
                if grid[x][y]:
                    dfs(x, y)
                    flag = True
                    break
            if flag:
                break

        answer = 0

        while island1:
            for i in range(len(island1)):
                x, y = island1.popleft()
                for dx, dy in d:
                    if (
                        0 <= x + dx < m
                        and 0 <= y + dy < n
                        and grid[x + dx][y + dy] != 2
                    ):
                        if grid[x + dx][y + dy] == 0:
                            grid[x + dx][y + dy] = 2
                            island1.append([x + dx, y + dy])
                        elif grid[x + dx][y + dy] == 1:
                            return answer
            answer += 1
        return answer
