class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1
        
    def numberOfMatches2(self, n: int) -> int:
        ans = 0
        while n > 1:
            ans += (n // 2)
            n -= n // 2
        return ans
        