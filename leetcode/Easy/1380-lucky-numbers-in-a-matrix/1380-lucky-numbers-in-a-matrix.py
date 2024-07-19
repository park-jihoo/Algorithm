class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # minimum in row, maximun in column
        minrow = [min(row) for row in matrix]
        maxcol = [max(matrix[j][i] for j in range(len(matrix))) for i in range(len(matrix[0]))]
        return list(set(minrow) & set(maxcol))