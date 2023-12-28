class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def f(start, pre, last_count, left):
            if left < 0:
                return float("inf") 
            if start >= len(s):
                return 0
            if s[start]==pre:
                incr = 1 if last_count in (1,9,99) else 0 
                return incr + f(start+1, pre, last_count+1, left) 
            else:
                keep = 1  + f(start+1, s[start], 1, left) 
                delete = f(start+1, pre, last_count, left-1) 
                return min(keep, delete)
        return f(0,"", 0,k)