class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        max_left = max(left) if left else 0
        max_right = max(n - num for num in right) if right else 0
        return max(max_left, max_right)
