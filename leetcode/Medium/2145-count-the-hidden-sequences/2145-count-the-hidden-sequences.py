class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        lst = [0] + list(accumulate(differences))
        return max(0, 1 + (upper - lower) - (max(lst) - min(lst)))
