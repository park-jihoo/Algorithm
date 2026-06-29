class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return len([x for x in patterns if x in word])
