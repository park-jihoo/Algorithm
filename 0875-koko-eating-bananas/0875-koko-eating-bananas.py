class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles) * h
        while left < right:            
            mid = (left + right) // 2
            if sum([((x-1) // mid + 1) for x in piles]) <= h:
                right = mid
            else:
                left = mid + 1
        return left