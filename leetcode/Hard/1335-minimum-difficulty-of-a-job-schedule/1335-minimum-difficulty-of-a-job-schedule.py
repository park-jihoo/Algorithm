class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        if len(jobDifficulty) == d:
            return sum(jobDifficulty)
        dp = [int(1e9)]*len(jobDifficulty)
        dp[0] = jobDifficulty[0]
        for i in range(1, len(jobDifficulty)):
            dp[i] = max(dp[i-1] , jobDifficulty[i])
        dp_prev = dp.copy()

        for i in range(1, d):
            dp = [int(1e9)]*len(jobDifficulty)
            for j in range(1, len(jobDifficulty)):
                last_diff = jobDifficulty[j]
                tmp_min = last_diff + dp_prev[j-1]
                for t in range(j-1, i-1, -1):
                    last_diff = max(last_diff, jobDifficulty[t])
                    tmp_min = min(tmp_min, last_diff + dp_prev[t-1])
                dp[j] = tmp_min
            dp_prev = dp.copy()
        return dp[-1]