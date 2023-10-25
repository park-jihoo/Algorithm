class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        elems = 2 ** (n - 1)
        half = 2 ** (n - 2)
        if k > half:
            return 1 - self.kthGrammar(n, k - half)
        return self.kthGrammar(n - 1, k)
