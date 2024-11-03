class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if (s + s)[i : i + len(s)] == goal:
                return True
        return False
