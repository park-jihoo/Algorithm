class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        for i in range(1+n//2):
            if target in (words[(startIndex-i)%n], words[(startIndex+i)%n]):
                return i
        return -1