class Solution:
    def __init__(self):
        self.serve = [(100, 0), (75, 25), (50, 50), (25, 75)]
        self.dp = []

    def dfs(self, a, b):
        if a <= 0 and b <= 0:
            return 0.5
        elif a <= 0 and b > 0:
            return 1.0
        elif a > 0 and b <= 0:
            return 0.0
        if self.dp[a][b] != -1.0:
            return self.dp[a][b]
        total = 0.0
        for dira, dirb in self.serve:
            total += self.dfs(a - dira, b - dirb)
        self.dp[a][b] = total / 4
        return self.dp[a][b]

    def soupServings(self, n: int) -> float:
        # DP Math Probability
        if n >= 4800:
            return 1
        self.dp = [[-1] * (n + 1) for _ in range(n + 1)]
        return self.dfs(n, n)
