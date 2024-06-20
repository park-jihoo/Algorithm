class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # m balls to basket
        # magnetic force == distance
        # pick m in position and get min distance
        position.sort()
        left, right = 1, position[-1] - position[0]
        while left <= right:
            mid = (left + right) // 2
            balls, prev = 1, position[0]
            for i in range(1, len(position)):
                if position[i] - prev >= mid:
                    balls += 1
                    prev = position[i]
            if balls >= m:
                left = mid + 1
                force = mid
            else:
                right = mid - 1
        return force
