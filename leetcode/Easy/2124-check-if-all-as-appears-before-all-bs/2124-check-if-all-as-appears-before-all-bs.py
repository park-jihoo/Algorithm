class Solution:
    def checkString(self, s: str) -> bool:
        b = False
        for c in s:
            if c == 'b':
                b = True
            if c == 'a' and b:
                return False
        return True