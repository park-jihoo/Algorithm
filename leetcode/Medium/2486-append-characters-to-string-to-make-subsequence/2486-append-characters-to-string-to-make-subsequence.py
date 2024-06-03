class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        end = 0
        for idx in range(len(s)):
            if end == len(t):
                return 0
            elif s[idx] == t[end]:
                end += 1
        if end == len(t):
            return 0
        return len(t) - end
