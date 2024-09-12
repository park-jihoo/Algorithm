class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return len([x for x in words if not set(x) - set(allowed)])