class Solution:
    def minSteps(self, n: int) -> int:
        factors = 0
        i = 2
        while i <= n:
            if n % i == 0:
                factors += i
                n /= i
                i = 2
            else:
                i += 1
        return factors