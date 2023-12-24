class Solution:
    def minOperations(self, s: str) -> int:
        diff = 0
        for i in range(len(s)):
            if i % 2 == 0 and s[i] == '1':
                diff += 1
            elif i % 2 == 1 and s[i] == '0':
                diff += 1
        return min(diff, len(s) - diff)