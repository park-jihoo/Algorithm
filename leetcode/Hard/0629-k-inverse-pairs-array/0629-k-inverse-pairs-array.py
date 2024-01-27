class Solution:
    def __init__(self):
        self.mod = 10**9 + 7

    @cache
    def kInversePairs(self, n: int, k: int) -> int:
        max_pairs = (n * (n - 1)) // 2
        if n == 0 or k < 0 or k > max_pairs:
            return 0
        elif k == 0 or k == max_pairs:
            return 1
        else:
            return (
                self.kInversePairs(n - 1, k)
                + self.kInversePairs(n, k - 1)
                - self.kInversePairs(n - 1, k - n)
            ) % self.mod
