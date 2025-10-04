class Solution:
    def maxArea(self, height: List[int]) -> int:
        lo, hi = 0, len(height) - 1
        ans = 0
        while lo < hi:
            ans = max(ans, (hi - lo) * min(height[hi], height[lo]))
            if height[lo] < height[hi]:
                lo += 1
            elif height[hi] < height[lo]:
                hi -= 1
            else:
                lo += 1
                hi -= 1
        return ans
