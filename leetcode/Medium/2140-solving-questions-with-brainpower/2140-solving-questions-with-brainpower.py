class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * (len(questions) + 1)
        for i in reversed(range(len(questions))):
            point, jump = questions[i]
            idx = min(i + jump + 1, len(questions))
            cur = point + dp[idx]
            dp[i] = max(cur, dp[i + 1])

        return dp[0]
