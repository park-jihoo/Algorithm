class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key = lambda v:v[1])
        dp = [[0, 0]]
        for start, end, p in jobs:
            i = bisect.bisect(dp, [start+1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([end, dp[i][1]+p])
        return dp[-1][1]