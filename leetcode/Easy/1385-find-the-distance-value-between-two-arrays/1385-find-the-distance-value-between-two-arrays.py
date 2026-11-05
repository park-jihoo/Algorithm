class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        ans = 0
        for i in arr1:
            if min(abs(i - j) for j in arr2) > d:
                ans += 1
        return ans