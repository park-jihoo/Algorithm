class Solution:
    def searchInsert(self, matrix: List[List[int]], target: int) -> int:
        start = 0
        end = len(matrix) - 1
        while start <= end:
            center = (start + end) // 2
            if matrix[center][0] > target:
                end = center - 1
            elif matrix[center][0] < target:
                start = center + 1
            else:
                return center
        return start - 1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row = self.searchInsert(matrix, target)
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid
            else:
                left = mid + 1
        return False