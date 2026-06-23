class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        dp = [1] * (r - l + 1)
        for i in range(1, n):
            dp = list(accumulate(dp, initial = 0))[-2::-1]
        return sum(dp) * 2 % (10 ** 9 + 7)