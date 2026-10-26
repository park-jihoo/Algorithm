class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        ans = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0 and (i, j) not in visited:
                    s = grid[i][j]
                    visited.add((i, j))
                    queue = deque([(i, j)])
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in d:
                            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
                                if (
                                    grid[x + dx][y + dy] >= 1
                                    and (x + dx, y + dy) not in visited
                                ):
                                    visited.add((x + dx, y + dy))
                                    s += grid[x + dx][y + dy]
                                    queue.append((x + dx, y + dy))
                    ans += (s % k) == 0
        return ans
