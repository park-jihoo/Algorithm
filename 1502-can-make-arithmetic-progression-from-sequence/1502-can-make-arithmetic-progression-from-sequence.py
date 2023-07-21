class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for idx in range(len(arr) - 1):
            if arr[idx + 1] - arr[idx] != diff:
                return False
        return True
