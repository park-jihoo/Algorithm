class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ans = 0
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j == 0:
                    dp[i][j] = mat[i][j]
                else:
                    dp[i][j] = 0 if mat[i][j] == 0 else dp[i][j-1]+1
                cur = dp[i][j]
                for k in range(i, -1, -1):
                    cur = min(cur, dp[k][j])
                    if cur == 0:
                        break
                    ans += cur
        return ans