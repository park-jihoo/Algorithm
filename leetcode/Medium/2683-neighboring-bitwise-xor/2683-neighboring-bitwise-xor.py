class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return reduce(lambda x, y: x ^ y, derived, 0) == 0
