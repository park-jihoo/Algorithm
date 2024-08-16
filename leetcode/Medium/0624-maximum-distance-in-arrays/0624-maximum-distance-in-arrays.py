class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans, minval, maxval = 0, float('inf'), -float('inf')
        for a in arrays:
            ans = max(ans, max(a[-1]-minval, maxval-a[0]))
            minval, maxval = min(minval, a[0]), max(maxval, a[-1])
        return ans