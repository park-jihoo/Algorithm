class Solution:
    def split(self, intervals):
        intervals.sort()
        cuts = 0
        cur = intervals[0][1]
        for s, e in intervals[1:]:
            if s >= cur:
                cuts += 1
                if cuts >= 2:
                    return True
            cur = max(cur, e)
        return False

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        xs, ys = [], []
        for sx, sy, ex, ey in rectangles:
            xs.append((sx, ex))
            ys.append((sy, ey))
        return self.split(xs) or self.split(ys)
