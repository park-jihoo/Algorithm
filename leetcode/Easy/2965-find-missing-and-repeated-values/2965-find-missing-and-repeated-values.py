class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        flat = list(reduce(operator.add, grid, []))
        twice = Counter(flat).most_common()[0][0]
        miss = set(range(1, len(grid) * len(grid) + 1)) - set(flat)
        return [twice, miss.pop()]