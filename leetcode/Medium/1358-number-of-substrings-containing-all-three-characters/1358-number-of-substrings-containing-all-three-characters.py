class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        pos = [-1, -1, -1]
        for i in range(len(s)):
            pos[ord(s[i]) - ord("a")] = i
            ans += 1 + min(pos)
        return ans
