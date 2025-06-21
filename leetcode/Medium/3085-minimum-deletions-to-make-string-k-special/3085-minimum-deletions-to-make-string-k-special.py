class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = Counter(word)
        ans = len(word)
        for a in cnt.values():
            deleted = 0
            for b in cnt.values():
                if a > b:
                    deleted += b
                elif b > a + k:
                    deleted += b - (a + k)
            ans = min(ans, deleted)
        return ans