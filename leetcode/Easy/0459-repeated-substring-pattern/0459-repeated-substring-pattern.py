class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                sub = s[:i] * (n // i)
                if s == sub:
                    return True
        return False
