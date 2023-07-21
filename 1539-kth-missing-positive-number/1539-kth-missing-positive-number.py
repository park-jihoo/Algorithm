class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        answer = 0
        for idx, val in enumerate(arr):
            if idx + k < val:
                return idx + k
        return len(arr) + k
