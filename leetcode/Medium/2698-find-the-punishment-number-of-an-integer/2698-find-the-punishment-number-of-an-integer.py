class Solution:
    @cache
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return set([0])
        ans = set()
        for i in range(1, len(s) + 1):
            for f in self.partition(s[i:]):
                ans.add(int(s[:i]) + f)
        return ans

    def punishmentNumber(self, n: int) -> int:
        return sum(i**2 for i in range(1, n+1) if i in self.partition(str(i**2)))
        