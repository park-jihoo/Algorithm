class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = list(map(int, str(n)))
        return n % (sum(digits) + math.prod(digits)) == 0