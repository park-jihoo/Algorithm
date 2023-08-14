class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dirs = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, 2), (-1, -2)]
        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        dp[0][row][column] = 1

        for m in range(1, k + 1):
            for x in range(n):
                for y in range(n):
                    for dx, dy in dirs:
                        if 0 <= x + dx < n and 0 <= y + dy < n:
                            dp[m][x][y] += dp[m - 1][x + dx][y + dy]
                    dp[m][x][y] /= 8

        answer = sum(sum(dp[k][i]) for i in range(n))
        return answer
