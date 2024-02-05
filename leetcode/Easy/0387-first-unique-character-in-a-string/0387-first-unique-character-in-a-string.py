class Solution:
    def firstUniqChar(self, s: str) -> int:
        for idx, char in enumerate(s):
            if s.index(char) == s.rindex(char):
                return idx
        return -1