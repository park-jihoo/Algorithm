class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # array greedy sorting
        ans, arrow = 0, 0
        points.sort(key=lambda x:x[1])
        for s, e in points:
            if ans == 0 or s > arrow:
                ans, arrow = ans+1, e
        return ans