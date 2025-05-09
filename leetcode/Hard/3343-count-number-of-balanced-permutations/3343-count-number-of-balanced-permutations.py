class Solution:
    def __init__(self):
        self.mod = 10**9 + 7

    def countBalancedPermutations(self, num: str) -> int:
        self.nums = list(map(int, num))
        self.s = sum(self.nums)
        self.n = len(self.nums)
        self.cnt = Counter(self.nums)

        if self.s % 2:
            return 0

        return self._dfs(0, self.s // 2, self.n // 2, (self.n + 1) // 2)

    @cache
    def _dfs(self, i: int, j: int, a: int, b: int) -> int:
        if i > 9:
            return int((j | a | b) == 0)

        if a == 0 and j:
            return 0

        ans = 0
        for l in range(min(self.cnt[i], a) + 1):
            r = self.cnt[i] - l
            if 0 <= r <= b and l * i <= j:
                t = comb(a, l) * comb(b, r) * self._dfs(i + 1, j - l * i, a - l, b - r)
                ans = (ans + t) % self.mod

        return ans
