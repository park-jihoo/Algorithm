class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int, dp={}
    ) -> int:
        mod = 10**9 + 7
        if maxMove < 0:
            return 0
        if not (0 <= startRow < m and 0 <= startColumn < n):
            return 1
        if (m, n, maxMove, startRow, startColumn) not in dp:
            dp[(m, n, maxMove, startRow, startColumn)] = (
                self.findPaths(m, n, maxMove - 1, startRow - 1, startColumn)
                + self.findPaths(m, n, maxMove - 1, startRow + 1, startColumn)
                + self.findPaths(m, n, maxMove - 1, startRow, startColumn - 1)
                + self.findPaths(m, n, maxMove - 1, startRow, startColumn + 1)
            ) % mod
        return dp[(m, n, maxMove, startRow, startColumn)]
