class Solution:
    def minSteps(self, s: str, t: str) -> int:
        intersect = Counter(s) & Counter(t)
        return len(s) - intersect.total()
