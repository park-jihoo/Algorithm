class Solution:
    def checkRecord(self, n: int) -> int:
        @lru_cache
        def f(i, a, l):
            if a < 2 and l < 3:
                if i == n:
                    return 1
                return (f(i+1, a, 0) + f(i+1, a+1, 0) + f(i+1, a, l+1))%(10**9+7)

            return 0
        
        return f(0, 0, 0)