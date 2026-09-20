class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((idx+1) * (1 + ord('z') - ord(ch)) for idx, ch in enumerate(s))