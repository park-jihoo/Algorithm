class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if k > sum(candies):
            return 0
        left, right = 0, sum(candies)
        while left < right:
            mid = (left + right + 1) // 2
            c = sum(map(lambda x:x//mid, candies))
            if c >= k:
                left = mid
            else:
                right = mid - 1
        return left