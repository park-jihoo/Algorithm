class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        memo = {}

        def dp(i, k):
            if k == 0 or i == len(events):
                return 0
            if (i, k) in memo:
                return memo[(i, k)]
            j = bisect.bisect(events, [events[i][1], math.inf, math.inf], i + 1)
            memo[(i, k)] = max(dp(i + 1, k), events[i][2] + dp(j, k - 1))
            return memo[(i, k)]

        return dp(0, k)
