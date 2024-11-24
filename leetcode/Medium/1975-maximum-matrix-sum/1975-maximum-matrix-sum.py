class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        minval = float("inf")
        total = 0
        negs = 0

        for row in matrix:
            for value in row:
                if value < 0:
                    negs += 1
                absval = abs(value)
                minval = min(minval, absval)
                total += absval
        if negs % 2 == 0:
            return total
        return total - 2 * minval
