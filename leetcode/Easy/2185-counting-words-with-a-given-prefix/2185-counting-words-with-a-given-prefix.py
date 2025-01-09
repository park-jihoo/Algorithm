class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len([x for x in words if x.startswith(pref)])
