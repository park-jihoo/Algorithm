class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        start, end = 1, max(quantities)
        while start < end:
            mid = (start + end) // 2
            if sum(ceil(q/mid) for q in quantities) <= n:
                end = mid
            else:
                start = mid + 1
        return start