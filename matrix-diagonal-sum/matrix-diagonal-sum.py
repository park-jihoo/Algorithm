class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagonal = [mat[i][i] for i in range(len(mat))]
        sec_diagonal = [mat[i][len(mat) - 1 - i] for i in range(len(mat))]
        if len(mat) % 2 == 1:
            return sum(diagonal) + sum(sec_diagonal) - mat[len(mat)//2][len(mat)//2]
        else:
            return sum(diagonal) + sum(sec_diagonal)