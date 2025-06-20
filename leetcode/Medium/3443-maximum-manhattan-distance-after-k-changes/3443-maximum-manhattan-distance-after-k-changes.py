class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        for dirc in 'NE','SE','SW','NW':
            kk, dist = k, 0
            for c in s:
                dist += (c in dirc or kk>0 or -1)
                kk -= (c not in dirc)
                ans = max(ans, dist)
        
        return ans