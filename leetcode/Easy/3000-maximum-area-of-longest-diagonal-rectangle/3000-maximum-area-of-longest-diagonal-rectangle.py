class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        dimensions.sort(key=lambda x: (-x[0]*x[0] - x[1]*x[1], -x[0]*x[1]))
        return dimensions[0][0] * dimensions[0][1]