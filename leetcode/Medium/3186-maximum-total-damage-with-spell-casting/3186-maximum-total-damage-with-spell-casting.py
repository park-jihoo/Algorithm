class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        v = [(-(10**9), 0)]
        for k in sorted(cnt.keys()):
            v.append((k, cnt[k]))
        n = len(v)
        dp, x, j = [0] * n, 0, 1
        for i in range(1, n):
            while j < i and v[j][0] < v[i][0] - 2:
                x = max(x, dp[j])
                j += 1
            dp[i] = x + v[i][0] * v[i][1]
        return max(dp)
