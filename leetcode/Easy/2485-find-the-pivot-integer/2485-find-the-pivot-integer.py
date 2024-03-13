class Solution:
    def pivotInteger(self, n: int) -> int:
        s = n * (n + 1) // 2
        # (s + pivot) / 2 = pivot * (pivot + 1) /2
        # s = pivot ^ 2
        if float(int(sqrt(s))) == sqrt(s):
            return int(sqrt(s))
        return -1
