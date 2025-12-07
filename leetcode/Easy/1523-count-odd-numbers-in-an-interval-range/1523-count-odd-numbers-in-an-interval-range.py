class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (high % 2 or low % 2)