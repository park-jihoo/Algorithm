class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([st[::-1] for st in s.split()])