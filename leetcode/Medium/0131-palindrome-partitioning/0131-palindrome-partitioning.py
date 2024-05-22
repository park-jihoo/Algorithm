class Solution:
    @cache
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                for f in self.partition(s[i:]):
                    ans.append([s[:i]] + f)
        return ans