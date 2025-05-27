class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        allsum = n * (n + 1) // 2
        d = n // m
        divsum = d * (d + 1) // 2
        return allsum - 2 * divsum * m