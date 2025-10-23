class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        n1, n2 = 0, 0
        for i in range(n - 1):
            print(math.comb(n - 2, i), s[i], s[i + 1])
            n1 += math.comb(n - 2, i) * int(s[i])
            n2 += math.comb(n - 2, i) * int(s[i + 1])
        return n1 % 10 == n2 % 10
