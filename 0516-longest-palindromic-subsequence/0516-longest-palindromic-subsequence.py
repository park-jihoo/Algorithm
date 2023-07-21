class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        table = [[0] * n for _ in range(n)]
        for i in range(n):  # string length equals to 1
            table[i][i] = 1
        for i in range(n - 1):  # string length equals to 2
            table[i][i + 1] = 2 if s[i] == s[i + 1] else 1
        for l in range(2, n + 1):  # string length more than 3
            for i in range(n - l):
                j = l + i
                if s[i] == s[j]:
                    table[i][j] = table[i + 1][j - 1] + 2
                else:
                    table[i][j] = max(table[i + 1][j], table[i][j - 1])
        return table[0][n - 1]
