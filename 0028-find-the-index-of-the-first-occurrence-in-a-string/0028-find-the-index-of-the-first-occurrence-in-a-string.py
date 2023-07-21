class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        for idx, char in enumerate(haystack):
            if idx > len(haystack) - len(needle):
                return -1
            if haystack[idx : idx + len(needle)] == needle:
                return idx
        return -1
