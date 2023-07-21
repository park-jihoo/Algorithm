class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(capacity):
            ships = []
            for c in weights:
                if c > capacity:
                    return False
                elif len(ships) == 0 or ships[-1] + c > capacity:
                    ships.append(c)
                else:
                    ships[-1] += c
                if len(ships) > days:
                    return False
            return True

        left = 0
        right = sum(weights)
        while left <= right:
            center = (left + right) // 2
            if possible(center):
                right = center - 1
            else:
                left = center + 1
        return left
