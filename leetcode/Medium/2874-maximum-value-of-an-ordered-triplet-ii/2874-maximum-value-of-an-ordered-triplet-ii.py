class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans, ix, dx = 0, 0, 0
        for x in nums:
            ans = max(ans, dx * x)
            dx = max(dx, ix - x)
            ix = max(ix, x)
        return ans
