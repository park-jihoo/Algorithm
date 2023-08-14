class Solution:
    def countPaths(self, grid):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def memoization(grid, i, j, lookup):
            if not lookup[i][j]:
                lookup[i][j] = 1
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if (
                        0 <= ni < len(grid)
                        and 0 <= nj < len(grid[0])
                        and grid[i][j] < grid[ni][nj]
                    ):
                        lookup[i][j] = (
                            lookup[i][j] + memoization(grid, ni, nj, lookup)
                        ) % (10**9 + 7)
            return lookup[i][j]

        lookup = [[0] * len(grid[0]) for _ in range(len(grid))]
        return sum(
            memoization(grid, i, j, lookup)
            for i in range(len(grid))
            for j in range(len(grid[0]))
        ) % (10**9 + 7)
