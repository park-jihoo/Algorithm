class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opens, closes = 0, 0
        for ch in s:
            if ch == "(":
                opens += 1
            elif ch == ")" and opens > 0:
                opens -= 1
            else:
                closes += 1
        return opens + closes
