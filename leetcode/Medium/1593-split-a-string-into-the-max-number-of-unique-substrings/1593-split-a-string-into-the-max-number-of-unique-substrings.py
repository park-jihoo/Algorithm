class Solution:
    def dfs(self, s, seen=set()):
        ans = 0
        if s:
            for i in range(1, len(s)+1):
                cand = s[:i]
                if cand not in seen:
                    seen.add(cand)
                    ans = max(ans, 1+self.dfs(s[i:], seen))
                    seen.remove(cand)
        return ans
    def maxUniqueSplit(self, s: str) -> int:
        return self.dfs(s)