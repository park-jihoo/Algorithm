class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = sorted([x for x, y in points])
        ans = 0
        for i in range(len(xs) - 1):
            ans = max(ans, xs[i+1]-xs[i])
        return ans