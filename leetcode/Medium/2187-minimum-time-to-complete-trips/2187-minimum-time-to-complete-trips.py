class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, max(time) * totalTrips
        while left <= right:
            mid = (left + right) // 2
            if sum([mid // x for x in time]) >= totalTrips:
                right = mid - 1
            else:
                left = mid + 1
        return left
