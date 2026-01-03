class Solution:
    def numOfWays(self, n: int) -> int:
        # ABA -> BAB, BCB, CAC, BAC, CAB
        # ABC -> BAB, BCB, CAB, BCA
        color2, color3, mod = 6, 6, 10**9+7
        for i in range(2, n+1):
            color2, color3 = (color2 * 3 + color3 * 2) % mod, (color2 * 2 + color3 * 2) % mod
        return (color2 + color3) % mod