class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        res, R, C = 0, len(grid1), len(grid1[0])

        def dfs(x, y):
            isSubIsland = True
            if 0 <= x < R and 0 <= y < C and grid2[x][y] == 1:
                if grid1[x][y] != 1: return False
                grid2[x][y] = -1
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    isSubIsland &= dfs(x + dx, y + dy)
            return isSubIsland

        for x, y in itertools.product(range(R), range(C)):
            if grid2[x][y] == 1:
                res += dfs(x, y)

        return res