class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return len(max(s.split('0'),key=len)) > 1