class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        cnt = Counter((s1 + " " + s2).split())
        return [key for key, val in cnt.items() if val == 1]
