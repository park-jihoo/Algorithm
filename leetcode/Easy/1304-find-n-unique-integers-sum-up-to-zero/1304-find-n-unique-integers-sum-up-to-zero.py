class Solution:
    def sumZero(self, n: int) -> List[int]:
        return list(range(1, n//2 + 1)) + list(range(-(n//2), 0)) + ([0] if n % 2 == 1 else [])