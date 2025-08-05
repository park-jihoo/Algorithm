class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        placed = set()
        for val in fruits:
            for idx, cap in enumerate(baskets):
                if idx not in placed and cap >= val:
                    placed.add(idx)
                    break
        return len(baskets) - len(placed)
