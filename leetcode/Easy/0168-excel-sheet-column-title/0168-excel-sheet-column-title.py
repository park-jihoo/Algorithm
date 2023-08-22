class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = ""
        while columnNumber > 0:
            columnNumber -= 1
            answer = answer + chr(ord("A") + columnNumber % 26)
            columnNumber //= 26
        return "".join(reversed(list(answer)))
