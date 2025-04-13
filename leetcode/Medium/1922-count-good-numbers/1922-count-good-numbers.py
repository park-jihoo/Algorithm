class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return (pow(20, n//2, 10**9+7) * pow(5, n%2)) % (10**9+7)