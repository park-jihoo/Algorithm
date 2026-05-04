class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose
        transposed = list([list(x) for x in zip(*matrix)])
        # reverse row
        for idx, row in enumerate(transposed):
            matrix[idx] = row[::-1]
