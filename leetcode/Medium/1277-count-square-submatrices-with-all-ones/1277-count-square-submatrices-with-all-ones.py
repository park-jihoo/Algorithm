class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1 and i*j == 0:
                    dp[i][j] = 1
        
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        
        return sum(sum(x) for x in dp)