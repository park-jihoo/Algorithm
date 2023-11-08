class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        mx, my = abs(fx - sx), abs(fy - sy)
        if max(mx, my) > t:
            return False
        if mx == 0 and my == 0 and t == 1:
            return False
        return True
