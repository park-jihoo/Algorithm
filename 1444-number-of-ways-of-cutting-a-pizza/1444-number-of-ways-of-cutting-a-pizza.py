from functools import lru_cache

class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.prefix = []

    def hasApple(self, row1, row2, col1, col2):
        return (self.prefix[row1][col1] + self.prefix[row2][col2] - self.prefix[row1][col2] - self.prefix[row2][col1]) > 0
    
    @lru_cache(None)
    def dp(self, m, n, k):
        if k == 0:
            return 1
        ans = 0
        for i in range(m+1, self.m):
            if self.hasApple(m, i, n, self.n) and self.hasApple(i, self.m, n, self.n):
                ans += self.dp(i, n, k - 1)
        for j in range(n+1, self.n):
            if self.hasApple(m, self.m, n, j) and self.hasApple(m, self.m, j, self.n):
                ans += self.dp(m, j, k - 1)
        return ans

    
    def ways(self, pizza: List[str], k: int) -> int:
        self.m, self.n = len(pizza), len(pizza[0])
        self.prefix = [[0]*(self.n+1) for _ in range(self.m+1)]
        for i in range(self.m):
            for j in range(self.n):
                self.prefix[i+1][j+1] = (pizza[i][j] == 'A') - self.prefix[i][j] + self.prefix[i+1][j] + self.prefix[i][j+1]
        return self.dp(0, 0, k-1) % (10**9+7)