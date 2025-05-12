class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt = Counter(digits)
        return [v for v in range(100, 1000, 2) if Counter(map(int, str(v))) <= cnt]
