class Solution:
    def product(self, n):
        ans = 1
        while n:
            ans *= n % 10
            n //= 10
        return ans

    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, n + 10):
            if self.product(i) % t == 0:
                return i
        return n + 10
