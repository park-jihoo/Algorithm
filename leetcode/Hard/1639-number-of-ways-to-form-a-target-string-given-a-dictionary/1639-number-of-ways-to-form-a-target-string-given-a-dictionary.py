class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # 어떻게 이틀 연속으로 Hard가 나오냐 이 문제가 또 나오다니(241229)
        m, n = len(words[0]), len(target) + 1
        dp = [0] * n
        dp[0] = 1
        for i in range(m):
            counter = Counter([w[i] for w in words])
            for j in reversed(range(n - 1)):
                dp[j + 1] += dp[j] * counter[target[j]] % (10**9 + 7)
        return dp[-1] % (10**9 + 7)
