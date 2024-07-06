class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time == 1:
            return 2
        x = time % ((n - 1) * 2)
        return min(2 * n - 1 - x, x + 1)
