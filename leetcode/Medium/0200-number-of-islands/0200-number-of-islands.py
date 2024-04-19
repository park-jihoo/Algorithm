class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ans += 1
                    queue = deque([(i, j)])
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in d:
                            if 0<=x+dx<len(grid) and 0<=y+dy<len(grid[0]):
                                if grid[x+dx][y+dy]== "1":
                                    grid[x+dx][y+dy] = "0"
                                    queue.append((x+dx, y+dy))
        return ans