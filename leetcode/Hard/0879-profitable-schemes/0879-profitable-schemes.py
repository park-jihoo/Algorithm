class Solution:
    def profitableSchemes(
        self, n: int, minProfit: int, group: List[int], profit: List[int]
    ) -> int:
        # Hard, Array, DP
        # n : 최대의 scheme
        dp = [
            [[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(len(group) + 1)
        ]
        dp[0][0][0] = 1
        for k in range(1, len(group) + 1):
            for i in range(n + 1):
                for j in range(minProfit + 1):
                    dp[k][i][j] = dp[k - 1][i][j]
                    if i >= group[k - 1]:
                        dp[k][i][j] += dp[k - 1][i - group[k - 1]][
                            max(0, j - profit[k - 1])
                        ]
        answer = sum([dp[len(group)][i][minProfit] for i in range(n + 1)]) % (10**9 + 7)
        return answer
