class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    ans += 4
                    for dx, dy in d:
                        if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
                            if grid[x + dx][y + dy] == 1:
                                ans -= 1
        return ans
