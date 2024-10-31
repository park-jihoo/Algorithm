class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        n, m = len(robot), len(factory)
        dp = [float('inf')] * (n + 1)
        dp[n] = 0
        robot.sort()
        factory.sort()
        for j in range(m-1, -1, -1):
            for i in range(n):
                cur = 0
                for k in range(1, min(factory[j][1], n - i) + 1):
                    cur += abs(robot[i+k-1]-factory[j][0])
                    dp[i] = min(dp[i], dp[i+k] +cur)
        return dp[0]