class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        values = sorted(list(chain.from_iterable(grid)))
        values = list(map(lambda a: a - values[0], values))
        if any(val % x != 0 for val in values):
            return -1
        values = list(map(lambda a: a // x, values))
        center = values[len(values) // 2]
        return sum(abs(a - center) for a in values)
