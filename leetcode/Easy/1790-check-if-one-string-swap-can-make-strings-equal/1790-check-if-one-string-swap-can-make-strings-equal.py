class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        return Counter(s1) == Counter(s2) and sum(x!=y for x,y in zip(s1, s2)) in [0, 2]