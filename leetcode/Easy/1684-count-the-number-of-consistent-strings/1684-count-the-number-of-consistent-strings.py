class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return len([x for x in words if set(allowed) >= set(x)])
