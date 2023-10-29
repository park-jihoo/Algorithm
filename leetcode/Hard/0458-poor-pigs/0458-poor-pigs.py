class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        t = minutesToTest // minutesToDie
        x = 0
        while (t+1)**x < buckets:
            x += 1
        return x