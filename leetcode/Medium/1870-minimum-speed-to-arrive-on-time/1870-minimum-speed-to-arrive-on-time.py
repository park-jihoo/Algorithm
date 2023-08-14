class Solution:
    def calTime(self, dist, speed):
        ans = 0.0
        for idx, val in enumerate(dist):
            if idx != len(dist) - 1:
                ans += math.ceil(val / speed)
            else:
                ans += val / speed
        return ans

    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left, right, minSpeed = 1, 10**7, -1
        while left <= right:
            mid = (left + right) // 2
            if self.calTime(dist, mid) <= hour:
                minSpeed = mid
                right = mid - 1
            else:
                left = mid + 1
        return minSpeed
