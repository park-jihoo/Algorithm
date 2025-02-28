class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
        for i, c in enumerate(str1):
            for j, d in enumerate(str2):
                dp[i + 1][j + 1] = (
                    1 + dp[i][j] if c == d else max(dp[i][j + 1], dp[i + 1][j])
                )
        i, j = len(str1), len(str2)
        ans = []

        while i>0 or j>0:
            if i>0 and j>0 and str1[i-1] == str2[j-1]:
                ans.append(str1[i-1])
                i-=1
                j-=1
            elif i>0 and (j==0 or dp[i-1][j] >= dp[i][j-1]):
                ans.append(str1[i-1])
                i-=1
            else:
                ans.append(str2[j-1])
                j-=1

        return "".join(reversed(ans))