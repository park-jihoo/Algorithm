class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        nines, rest = divmod(sum, 9)
        return ("9" * nines + str(rest) + "0" * num)[:num] 