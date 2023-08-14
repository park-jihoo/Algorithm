from collections import deque


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        score = [[-1 for x in range(n)] for y in range(m)]
        score[0][0] = grid[0][0]
        for i in range(1, m):
            score[i][0] = score[i - 1][0] + grid[i][0]
        for j in range(1, n):
            score[0][j] = score[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                score[i][j] = min(score[i - 1][j], score[i][j - 1]) + grid[i][j]
        return score[m - 1][n - 1]
