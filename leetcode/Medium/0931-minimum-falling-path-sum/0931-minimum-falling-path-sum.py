class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] += min(matrix[i-1][k] for k in (j-1, j, j+1) if 0 <= k < len(matrix))
        return min(matrix[-1])