class Solution:
    def numberOfWays(self, corridor: str) -> int:
        a, b, c = 1, 0, 0
        for ch in corridor:
            if ch == 'S':
                a, b, c = 0, a+c, b
            else:
                a, b, c = a+c, b, c
        return c % (10**9 + 7)