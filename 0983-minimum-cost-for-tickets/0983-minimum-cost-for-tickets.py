class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last = days[len(days) - 1]
        dp = [0 for x in range(last+1)]
        for i in range(1, last+1):
            if i not in days:
                dp[i] = dp[i-1]
                continue
            else:
                day = dp[i-1] + costs[0]
                week = dp[max(0, i-7)] + costs[1]
                month = dp[max(0, i-30)] + costs[2]
                dp[i] = min(day, week, month)

        return dp[last]